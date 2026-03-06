import concurrent.futures
import threading
import json

class SecurityEngine:
    def __init__(self, threshold=1000.0):
        self.threshold = threshold
        self.user_risk_scores = {}
        self.processed_event_ids = set()
        self._lock = threading.Lock()

    def process_batch(self, batch):
        flagged_events = []
        for event in batch:
            event_id = event['event_id']
            user_id = event['user_id']
            data_usage = event['data_usage_mb']
            
            location = event.get('location')
            ip_address = event.get('ip_address')

            with self._lock:
                if event_id in self.processed_event_ids:
                    continue
                self.processed_event_ids.add(event_id)

            if data_usage > self.threshold:
                flagged_events.append(event)
                with self._lock:
                    if user_id in self.user_risk_scores:
                        self.user_risk_scores[user_id] += 1
                    else:
                        self.user_risk_scores[user_id] = 1
        return flagged_events

class SecuritySimulator:
    def __init__(self, batches):
        self.batches = batches
        self.engine = SecurityEngine()

    def run(self):
        all_flagged = []
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(self.engine.process_batch, b) for b in self.batches]
            for future in concurrent.futures.as_completed(futures):
                all_flagged.extend(future.result())

        self.generate_report(all_flagged)

    def generate_report(self, flagged_events):
        if not self.engine.user_risk_scores:
            print("No security threats detected.")
            return

        flagged_users_count = len(self.engine.user_risk_scores)
        highest_risk_user = max(self.engine.user_risk_scores, key=self.engine.user_risk_scores.get)

        print("--- Security Detection Report ---")
        print("Users Flagged:", flagged_users_count)
        print("Suspicious Events:", len(flagged_events))
        print("Highest Risk User:", highest_risk_user)

if __name__ == "__main__":
    try:
        with open('security_logs.json', 'r') as file:
            data = json.load(file)
            
        simulator = SecuritySimulator(data)
        simulator.run()
        
    except FileNotFoundError:
        print("Error: 'security_logs.json' not found.")
    except json.JSONDecodeError:
        print("Error: 'security_logs.json' contains invalid formatting.")
