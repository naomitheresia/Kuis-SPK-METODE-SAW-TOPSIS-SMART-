try:

    import numpy as np
except ImportError:  # pragma: no cover
    print("Warning: numpy not installed. Install with: pip install numpy")
    raise

except ImportError:
    print("Warning: numpy not installed. Install with: pip install numpy")
    import sys
    sys.exit(1)

# ============================================================
# METODE SMART (Simple Multi-Attribute Rating Technique)
# NPM: 2315061091 -> X=1, Y=9
# ============================================================

print("=" * 60)
print("     METODE SMART")
print("     NPM: 2315061091 | X=1, Y=9")
print("=" * 60)

alternatif = ['Kandidat A', 'Kandidat B', 'Kandidat C', 'Kandidat D']

data = np.array([
    [85,  3,  12.0, 80],
    [70,  5,  15.0, 90],
    [90,  2,  10.0, 75],
    [76,  9,  12.5, 85],
], dtype=float)

kriteria = ['C1-Logika', 'C2-Pengalaman', 'C3-Gaji', 'C4-Psikotes']
sifat    = ['benefit', 'benefit', 'cost', 'benefit']
bobot    = np.array([16, 19, 20, 45]) / 100

print("\n[1] DATA AWAL")
print(f"{'Alternatif':<14}", end="")
for k in kriteria:
    print(f"{k:>15}", end="")
print()
for i, alt in enumerate(alternatif):
    print(f"{alt:<14}", end="")
    for j in range(4):
        print(f"{data[i, j]:>15.1f}", end="")
    print()

# ---- Konversi ke utility value (0-100) ----
# Benefit: u = (x - min) / (max - min) * 100
# Cost   : u = (max - x) / (max - min) * 100
utility = np.zeros_like(data)
for j in range(data.shape[1]):
    col_max = data[:, j].max()
    col_min = data[:, j].min()
    if sifat[j] == 'benefit':
        utility[:, j] = (data[:, j] - col_min) / (col_max - col_min) * 100
    else:
        utility[:, j] = (col_max - data[:, j]) / (col_max - col_min) * 100

print("\n[2] UTILITY VALUE (skala 0-100)")
print(f"{'Alternatif':<14}", end="")
for k in kriteria:
    print(f"{k:>15}", end="")
print()
for i, alt in enumerate(alternatif):
    print(f"{alt:<14}", end="")
    for j in range(4):
        print(f"{utility[i, j]:>15.2f}", end="")
    print()

# ---- Skor SMART ----
skor = utility @ bobot

print("\n[3] NILAI AKHIR SMART (U = sum(wj * uj))")
print(f"{'Alternatif':<14} {'Skor SMART':>12} {'Rangking':>10}")
ranking = np.argsort(skor)[::-1]
rank_dict = {idx: r + 1 for r, idx in enumerate(ranking)}

for i, alt in enumerate(alternatif):
    print(f"{alt:<14} {skor[i]:>12.4f} {rank_dict[i]:>10}")

print("\n[4] HASIL RANGKING")
for rank, idx in enumerate(ranking, 1):
    print(f"  Rank {rank}: {alternatif[idx]}  (Skor = {skor[idx]:.4f})")

print(f"\n>> REKOMENDASI SMART: {alternatif[ranking[0]]}")
print("=" * 60)
