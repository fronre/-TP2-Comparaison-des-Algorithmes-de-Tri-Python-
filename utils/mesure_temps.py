import time

def nano_timer(func):
    start = time.time_ns()
    func()
    end = time.time_ns()
    duration = end - start
    print(f"time: {duration} ns")
    return duration
