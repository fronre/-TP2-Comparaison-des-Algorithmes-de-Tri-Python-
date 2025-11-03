import matplotlib.pyplot as plt
from nano_timer import measure_time_ns
from generate_table import generer_table
from tri_bulles import tri_bulles
from tri_insertion_deplacement import tri_insertion_deplacement
from tri_insertion_echange import tri_insertion_echange
from tri_selection import tri_selection

data_c = generer_table(500, 'c')
data_d = generer_table(500, 'd')
data_a = generer_table(500, 'a')

times = {
    "Tri à bulles": measure_time_ns(lambda: tri_bulles(data_a.copy())),
    "Insertion (déplacement)": measure_time_ns(lambda: tri_insertion_deplacement(data_a.copy())),
    "Insertion (échange)": measure_time_ns(lambda: tri_insertion_echange(data_a.copy())),
    "Sélection": measure_time_ns(lambda: tri_selection(data_a.copy()))
}

# 🔹 نرسم النتائج
plt.bar(times.keys(), times.values())
plt.ylabel("Temps (nanosecondes)")
plt.title("Comparaison du temps d’exécution (tableau aléatoire)")
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()
