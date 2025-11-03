from typing import List

def tri_bulles(arr: List[int]) -> tuple[list[int], int, int]:
    a = arr.copy()
    n = len(a)
    comparaisons = 0
    deplacements = 0

    for i in range(n - 1):
        for j in range(n - i - 1):
            comparaisons += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                deplacements += 1
    return a, comparaisons, deplacements
