try:
    import numpy as np
except ImportError:  # pragma: no cover
    print("Warning: numpy not installed. Install with: pip install numpy")
    raise


# ============================================================
# METODE TOPSIS
# NPM: 2315061091 -> X=1, Y=9
# ============================================================

print("=" * 60)
print("     METODE TOPSIS")
print("     NPM: 2315061091 | X=1, Y=9")
print("=" * 60)

alternatif = ['Kandidat A', 'Kandidat B', 'Kandidat C', 'Kandidat D']

data = np.array([
    [85,  3,  12.0, 80],
    [70,  5,  15.0, 90],
    [90,  2,  10.0, 75],
    [76,  9,  12.5, 85],
])

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

# ---- Normalisasi vektor ----
denom = np.sqrt((data ** 2).sum(axis=0))
norm  = data / denom

print("\n[2] MATRIKS NORMALISASI VEKTOR")
print(f"{'Alternatif':<14}", end="")
for k in kriteria:
    print(f"{k:>15}", end="")
print()
for i, alt in enumerate(alternatif):
    print(f"{alt:<14}", end="")
    for j in range(4):
        print(f"{norm[i, j]:>15.4f}", end="")
    print()

# ---- Normalisasi terbobot ----
v = norm * bobot

print("\n[3] MATRIKS NORMALISASI TERBOBOT")
print(f"{'Alternatif':<14}", end="")
for k in kriteria:
    print(f"{k:>15}", end="")
print()
for i, alt in enumerate(alternatif):
    print(f"{alt:<14}", end="")
    for j in range(4):
        print(f"{v[i, j]:>15.4f}", end="")
    print()

# ---- Solusi ideal ----
ideal_pos = np.zeros(4)
ideal_neg = np.zeros(4)
for j in range(4):
    if sifat[j] == 'benefit':
        ideal_pos[j] = v[:, j].max()
        ideal_neg[j] = v[:, j].min()
    else:
        ideal_pos[j] = v[:, j].min()
        ideal_neg[j] = v[:, j].max()

print("\n[4] SOLUSI IDEAL")
print(f"{'Kriteria':<14}", end="")
for k in kriteria:
    print(f"{k:>15}", end="")
print()
print(f"{'A+ (positif)':<14}", end="")
for j in range(4):
    print(f"{ideal_pos[j]:>15.4f}", end="")
print()
print(f"{'A- (negatif)':<14}", end="")
for j in range(4):
    print(f"{ideal_neg[j]:>15.4f}", end="")
print()

# ---- Jarak ----
D_pos = np.sqrt(((v - ideal_pos) ** 2).sum(axis=1))
D_neg = np.sqrt(((v - ideal_neg) ** 2).sum(axis=1))

print("\n[5] JARAK KE SOLUSI IDEAL")
print(f"{'Alternatif':<14} {'D+ (pos)':>12} {'D- (neg)':>12}")
for i, alt in enumerate(alternatif):
    print(f"{alt:<14} {D_pos[i]:>12.4f} {D_neg[i]:>12.4f}")

# ---- Nilai preferensi ----
skor = D_neg / (D_pos + D_neg)

print("\n[6] NILAI PREFERENSI (Ci)")
print(f"{'Alternatif':<14} {'Ci':>12} {'Rangking':>10}")
ranking = np.argsort(skor)[::-1]
rank_dict = {idx: r + 1 for r, idx in enumerate(ranking)}

for i, alt in enumerate(alternatif):
    print(f"{alt:<14} {skor[i]:>12.4f} {rank_dict[i]:>10}")

print("\n[7] HASIL RANGKING")
for rank, idx in enumerate(ranking, 1):
    print(f"  Rank {rank}: {alternatif[idx]}  (Ci = {skor[idx]:.4f})")

print(f"\n>> REKOMENDASI TOPSIS: {alternatif[ranking[0]]}")
print("=" * 60)
