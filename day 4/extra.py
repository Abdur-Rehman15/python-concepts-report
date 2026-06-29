# ==========task queues============

import threading
import time
import queue

task_queue = queue.Queue()


def worker():
    while True:
        task = task_queue.get()
        if task is None:
            break
        print("worker processing", task)
        time.sleep(2)

        task_queue.task_done()


worker_thread = threading.Thread(target=worker, daemon=True)
worker_thread.start()

task_queue.put("task 1 hello")
task_queue.put("task 2 generate email reports")
task_queue.put("task 3 send emails")
print("i can print regardless of above tasks")
time.sleep(8)

task_queue.put("new task 2 generate email reports")
task_queue.put("new task 3 send emails")
print("em here again")

task_queue.join()


# ===========race conditions prevent============

balance = 0
balance_lock = threading.Lock()


def deposit(amount):
    global balance
    with balance_lock:
        curr_balance = balance
        balance = curr_balance + amount


import threading
import time

# Target outcome for both tests: 100 threads * $10 = $1000
EXPECTED = 1000

balance_no_lock = 0

def deposit_no_lock(amount):
    global balance_no_lock
    current_balance = balance_no_lock
    time.sleep(0.0001)  # Forces the OS to switch threads mid-calculation
    balance_no_lock = current_balance + amount

print("Running TEST 1 (Without Lock)...")
threads_no_lock = []
for _ in range(100):
    t = threading.Thread(target=deposit_no_lock, args=(10,))
    threads_no_lock.append(t)
    t.start()

for t in threads_no_lock:
    t.join()


balance_with_lock = 0
balance_lock = threading.Lock()

def deposit_with_lock(amount):
    global balance_with_lock
    with balance_lock:  # Only one thread can enter this block at a time
        current_balance = balance_with_lock
        time.sleep(0.001)
        balance_with_lock = current_balance + amount

print("Running TEST 2 (With Lock)...")
threads_with_lock = []
for _ in range(100):
    t = threading.Thread(target=deposit_with_lock, args=(10,))
    threads_with_lock.append(t)
    t.start()

for t in threads_with_lock:
    t.join()


print("\n=== FINAL RESULTS ===")
print(f"Expected Balance:  ${EXPECTED}")
print(f"Without Lock:      ${balance_no_lock}")
print(f"With Lock:         ${balance_with_lock}")
