import time

def nano_timer(func):
    start = time.time_ns()
    func()
    end = time.time_ns()
    duration = end - start
    print(f"المدة بالنانوسيكند: {duration} ns")
    return duration
