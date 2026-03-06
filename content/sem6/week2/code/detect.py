import threading
import concurrent.futures

def process_batch(batch, threshold, user_scores, processed_ids, lock):
    flagged =[]
    for tx in batch:
        tx_id = tx[0]
        user_id = tx[1]
        amount = tx[2]

        with lock:
            if tx_id in processed_ids:
                continue
            processed_ids.add(tx_id)

        if amount > threshold:
            flagged.append(tx)
            with lock:
                if user_id in user_scores:
                    user_scores[user_id] = user_scores[user_id] +1
                else:
                    user_scores[user_id] = 1
    return flagged

def run_sim():
    data = [
        [["t1", "user_27", 1500], ["t2", "user_10", 200]],
        [["t1", "user_27", 1500], ["t3", "user_27", 5000]],
        [["t4", "user_5", 2000], ["t2", "user_27", 3000]]
    ]
    
    threshold = 1000.0
    user_scores = {}
    processed_ids = set()
    lock = threading.Lock()
    all_flagged = []

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for batch in data:
            f = executor.submit(process_batch, batch, threshold, user_scores, processed_ids, lock)
            futures.append(f)

        for f in concurrent.futures.as_completed(futures):
            result = f.result()
            for item in result:
                all_flagged.append(item)

    flagged_users_count = len(user_scores)
    suspicious_count = len(all_flagged)

    highest_risk_user = "None"
    highest_score = 0 
    
    for user in user_scores:
        if user_scores[user] > highest_score:
            highest_score = user_scores[user]
            highest_risk_user = user

    print("---Fraud Detection Report---")
    print("users flagged:", flagged_users_count)
    print("Highest risk user:", highest_risk_user)
    print("Suspicious transactions:", suspicious_count)

run_sim()
