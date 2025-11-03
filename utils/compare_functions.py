from nano_timer import measure_time_ns

def compare_functions(func_a, func_b, *args, **kwargs) -> None:

    time_a = measure_time_ns(func_a, *args, **kwargs)
    time_b = measure_time_ns(func_b, *args, **kwargs)

    print(f" Function A time: {time_a} ns")
    print(f" Function B time: {time_b} ns")

    if time_a < time_b:
        print(" Function A is faster.")
    elif time_b < time_a:
        print(" Function B is faster.")
    else:
        print(" Both functions took the same time.")
