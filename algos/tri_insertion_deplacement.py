from typing import List

def tri_insertion_deplacement(arr: List[int]) -> tuple[list[int], int, int]:
    a = arr.copy()
    comparaisons = 0
    deplacements = 0

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            comparaisons += 1
            a[j + 1] = a[j]
            j -= 1
            deplacements += 1
        comparaisons += 1
        a[j + 1] = key
    return a, comparaisons, deplacements
