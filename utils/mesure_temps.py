import time

def measure_time_ns(func, *args, **kwargs):

    start = time.time_ns()
    func(*args, **kwargs)
    end = time.time_ns()
    duration = end - start
    return duration
