import random

def generer_table(n: int, dis: str) -> list[int]:
    if dis == 'c':
        return list(range(1, n + 1))
    elif dis == 'd':
        return list(range(n, 0, -1))
    elif dis == 'a':
        return random.sample(range(1, n + 1), n)
    else:
        raise ValueError("dis doit être 'c', 'd' ou 'a'")
