from compare_functions import compare_functions

def sum_with_list_comprehension():
    sum([i for i in range(10_000)])

def sum_with_loop():
    total = 0
    for i in range(10_000):
        total += i

if __name__ == "__main__":
    compare_functions(sum_with_list_comprehension, sum_with_loop)
