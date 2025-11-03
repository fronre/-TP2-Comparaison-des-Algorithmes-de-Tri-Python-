from typing import List

def tri_insertion_echange(arr: List[int]) -> tuple[list[int], int, int]:
    a = arr.copy()
    comparaisons = 0
    deplacements = 0

    for i in range(1, len(a)):
        j = i
        while j > 0:
            comparaisons += 1
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                deplacements += 1
                j -= 1
            else:
                break
    return a, comparaisons, deplacements
