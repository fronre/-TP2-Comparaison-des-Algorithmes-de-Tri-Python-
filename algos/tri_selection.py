
from typing import List

def tri_selection(arr: List[int]) -> List[int]:
    a = arr.copy()
    n = len(a)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
    return a

if __name__ == "__main__":
    print(tri_selection([3,1,4,1,5,9,2,6]))



