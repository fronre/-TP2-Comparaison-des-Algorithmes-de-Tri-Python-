from compare_functions import compare_functions
from tri_bulles import tri_bulles
from tri_selection import tri_selection
from tri_insertion_echange import tri_insertion_echange
from tri_insertion_deplacement import tri_insertion_deplacement

data = [5, 3, 8, 4, 2]

def func_bulles():
    tri_bulles(data.copy())

def func_selection():
    tri_selection(data.copy())

def func_insert_echange():
    tri_insertion_echange(data.copy())

def func_insert_deplacement():
    tri_insertion_deplacement(data.copy())

print("🔹 Comparing Bubble vs Selection")
compare_functions(func_bulles, func_selection)

print("🔹 Comparing Insertion (échange) vs Insertion (déplacement)")
compare_functions(func_insert_echange, func_insert_deplacement)
