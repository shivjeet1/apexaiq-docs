""" Parallel Fraud Detection Simulator """
import concurrent.futures
import json
import logging
from collections import Counter
from dataclasses import dataclass
from typing import List, Dict, Set, Optional

# Configure logging for production-level observability
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)

@dataclass(frozen=True)
class SecurityEvent:
    """Representing the event as a frozen dataclass for immutability."""
    event_id: str
    user_id: str
    data_usage_mb: float
    location: Optional[str] = None
    ip_address: Optional[str] = None

class SecurityEngine:
    def __init__(self, threshold: float = 1000.0):
        self.threshold = threshold
        # Using a Counter for cleaner score tracking
        self.user_risk_scores: Counter = Counter()
        self.processed_event_ids: Set[str] = set()
        self._lock = threading.Lock()

    def process_batch(self, batch: List[dict]) -> List[SecurityEvent]:
        """Processes a batch of logs and returns flagged SecurityEvent objects."""
        flagged_events = []
        
        for event_data in batch:
            try:
                event = SecurityEvent(
                    event_id=event_data['event_id'],
                    user_id=event_data['user_id'],
                    data_usage_mb=event_data['data_usage_mb'],
                    location=event_data.get('location'),
                    ip_address=event_data.get('ip_address')
                )

                # Deduplication check
                with self._lock:
                    if event.event_id in self.processed_event_ids:
                        continue
                    self.processed_event_ids.add(event.event_id)

                # Analysis logic
                if event.data_usage_mb > self.threshold:
                    flagged_events.append(event)
                    with self._lock:
                        self.user_risk_scores[event.user_id] += 1
                        
            except KeyError as e:
                logging.error(f"Missing required field in event: {e}")
                continue

        return flagged_events

class SecuritySimulator:
    def __init__(self, batches: List[List[dict]], threshold: float = 1000.0):
        self.batches = batches
        self.engine = SecurityEngine(threshold)

    def run(self) -> None:
        """Executes batch processing using a ThreadPoolExecutor."""
        all_flagged: List[SecurityEvent] = []
        
        # Using 'with' ensures the executor shuts down resources properly
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future_to_batch = {
                executor.submit(self.engine.process_batch, batch): batch 
                for batch in self.batches
            }
            
            for future in concurrent.futures.as_completed(future_to_batch):
                try:
                    all_flagged.extend(future.result())
                except Exception as exc:
                    logging.error(f"Batch generated an exception: {exc}")

        self._generate_report(all_flagged)

    def _generate_report(self, flagged_events: List[SecurityEvent]) -> None:
        """Internal method to format and output results."""
        if not self.engine.user_risk_scores:
            logging.info("No security threats detected.")
            return

        # industry standard: extract stats without modifying state
        highest_risk_user, top_score = self.engine.user_risk_scores.most_common(1)[0]

        report = (
            f"\n{'='*30}\n"
            f"Security Detection Report\n"
            f"{'-'*30}\n"
            f"Users Flagged:     {len(self.engine.user_risk_scores)}\n"
            f"Suspicious Events: {len(flagged_events)}\n"
            f"Highest Risk User: {highest_risk_user} ({top_score} flags)\n"
            f"{'='*30}"
        )
        print(report)

def main():
    """Entry point for the script."""
    try:
        with open('security_logs.json', 'r') as file:
            data = json.load(file)
            
        simulator = SecuritySimulator(data)
        simulator.run()
        
    except FileNotFoundError:
        logging.error("Critical: 'security_logs.json' not found.")
    except json.JSONDecodeError:
        logging.error("Critical: 'security_logs.json' contains invalid JSON formatting.")
    except Exception as e:
        logging.exception(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

