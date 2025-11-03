from nano_timer import measure_time_ns

def compare_functions(func_a, func_b) -> None:
    time_a = measure_time_ns(func_a)
    time_b = measure_time_ns(func_b)

    if time_a < time_b:
        print("Function A is faster.")
    elif time_b < time_a:
        print("Function B is faster.")
    else:
        print("Both functions took the same time.")
