try:
    import numpy as np
except ImportError:  # pragma: no cover
    print("Warning: numpy not installed. Install with: pip install numpy")
    raise


# ============================================================
# METODE SAW (Simple Additive Weighting)
# NPM: 2315061091 -> X=1, Y=9
# ============================================================

print("=" * 60)
print("     METODE SAW (Simple Additive Weighting)")
print("     NPM: 2315061091 | X=1, Y=9")
print("=" * 60)

# Data kandidat
alternatif = ['Kandidat A', 'Kandidat B', 'Kandidat C', 'Kandidat D']

# C1=Logika, C2=Pengalaman, C3=Gaji, C4=Psikotes
data = np.array([
    [85,  3,  12.0, 80],   # Kandidat A
    [70,  5,  15.0, 90],   # Kandidat B
    [90,  2,  10.0, 75],   # Kandidat C
    [76,  9,  12.5, 85],   # Kandidat D  (X=1, Y=9)
])

kriteria  = ['C1-Logika', 'C2-Pengalaman', 'C3-Gaji', 'C4-Psikotes']
sifat     = ['benefit', 'benefit', 'cost', 'benefit']
bobot     = np.array([16, 19, 20, 45]) / 100  # bobot dalam desimal

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

print(f"\nBobot  : C1={bobot[0]:.2f}, C2={bobot[1]:.2f}, C3={bobot[2]:.2f}, C4={bobot[3]:.2f}")
print(f"Sifat  : {sifat}")

# ---- Normalisasi ----
norm = np.zeros_like(data)
for j in range(data.shape[1]):
    if sifat[j] == 'benefit':
        norm[:, j] = data[:, j] / data[:, j].max()
    else:  # cost
        norm[:, j] = data[:, j].min() / data[:, j]

print("\n[2] MATRIKS NORMALISASI")
print(f"{'Alternatif':<14}", end="")
for k in kriteria:
    print(f"{k:>15}", end="")
print()
for i, alt in enumerate(alternatif):
    print(f"{alt:<14}", end="")
    for j in range(4):
        print(f"{norm[i, j]:>15.4f}", end="")
    print()

# ---- Nilai SAW ----
skor = norm @ bobot

print("\n[3] NILAI AKHIR SAW (V = sum(wj * rij))")
print(f"{'Alternatif':<14} {'Skor SAW':>12} {'Rangking':>10}")
ranking = np.argsort(skor)[::-1]
rank_dict = {}
for rank, idx in enumerate(ranking, 1):
    rank_dict[idx] = rank

for i, alt in enumerate(alternatif):
    print(f"{alt:<14} {skor[i]:>12.4f} {rank_dict[i]:>10}")

print("\n[4] HASIL RANGKING")
for rank, idx in enumerate(ranking, 1):
    print(f"  Rank {rank}: {alternatif[idx]}  (Skor = {skor[idx]:.4f})")

print(f"\n>> REKOMENDASI SAW: {alternatif[ranking[0]]}")
print("=" * 60)
