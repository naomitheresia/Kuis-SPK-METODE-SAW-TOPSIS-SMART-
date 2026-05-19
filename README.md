# Kuis Sistem Penunjang Keputusan

### Seleksi Karyawan Menggunakan Metode SAW, TOPSIS, dan SMART

---

## Deskripsi Singkat

Proyek ini merupakan implementasi **Sistem Penunjang Keputusan (SPK)** untuk kasus **seleksi karyawan** menggunakan tiga metode MADM (_Multi-Attribute Decision Making_):

| Metode     | Kepanjangan                                                    | Pendekatan                              |
| ---------- | -------------------------------------------------------------- | --------------------------------------- |
| **SAW**    | Simple Additive Weighting                                      | Normalisasi + penjumlahan terbobot      |
| **TOPSIS** | Technique for Order Preference by Similarity to Ideal Solution | Jarak ke solusi ideal positif & negatif |
| **SMART**  | Simple Multi-Attribute Rating Technique                        | Utility value skala 0–100               |

Setiap mahasiswa memiliki konfigurasi unik berdasarkan **NPM masing-masing** (variabel X dan Y), sehingga data dan bobot tiap mahasiswa berbeda.

---

## Konfigurasi NPM (2315061091)

```
NPM  : 2315061091
X    = digit terakhir       = 1
Y    = digit kedua terakhir = 9
```

### Bobot Kriteria

| Kode | Kriteria         | Sifat   | Bobot            |
| ---- | ---------------- | ------- | ---------------- |
| C1   | Tes Logika       | Benefit | 15 + X = **16%** |
| C2   | Pengalaman Kerja | Benefit | 10 + Y = **19%** |
| C3   | Ekspektasi Gaji  | Cost    | **20%**          |
| C4   | Tes Kepribadian  | Benefit | **45%** (sisa)   |

### Data Alternatif

| Alternatif     | C1 (Logika)   | C2 (Exp-thn) | C3 (Gaji-juta)    | C4 (Psikotes) |
| -------------- | ------------- | ------------ | ----------------- | ------------- |
| Kandidat A     | 85            | 3            | 12.0              | 80            |
| Kandidat B     | 70            | 5            | 15.0              | 90            |
| Kandidat C     | 90            | 2            | 10.0              | 75            |
| **Kandidat D** | **76** (75+X) | **9** (Y)    | **12.5** (12+X/2) | **85**        |

---

## 📁 Struktur File

```
📦 Kuis-SPK/
├── 📄 README.md                    ← File ini
├── 🐍 saw.py                       ← Implementasi metode SAW
├── 🐍 topsis.py                    ← Implementasi metode TOPSIS
├── 🐍 smart.py                     ← Implementasi metode SMART
```

---

## Cara Menjalankan

### Prasyarat

Pastikan Python sudah terinstall, lalu install library yang dibutuhkan:

```bash
pip install numpy
```

### Menjalankan Tiap Metode

Jalankan masing-masing file secara terpisah sesuai metode yang ingin dilihat:

```bash
# Metode SAW
python saw.py

# Metode TOPSIS
python topsis.py

# Metode SMART
python smart.py
```

### Contoh Output (SAW)

```
============================================================
     METODE SAW (Simple Additive Weighting)
     NPM: 2315061091 | X=1, Y=9
============================================================

[1] DATA AWAL
...

[4] HASIL RANGKING
  Rank 1: Kandidat D  (Skor = 0.9101)
  Rank 2: Kandidat B  (Skor = 0.8133)
  Rank 3: Kandidat A  (Skor = 0.7811)
  Rank 4: Kandidat C  (Skor = 0.7772)

>> REKOMENDASI SAW: Kandidat D
============================================================
```

---

## Ringkasan Hasil

Ketiga metode menghasilkan **ranking yang konsisten**:

| Rank | Kandidat       | SAW    | TOPSIS (Ci) | SMART |
| ---- | -------------- | ------ | ----------- | ----- |
| 1    | **Kandidat D** | 0.9101 | 0.8195      | 63.80 |
| 2    | Kandidat B     | 0.8133 | 0.4448      | 53.14 |
| 3    | Kandidat A     | 0.7811 | 0.2471      | 41.71 |
| 4    | Kandidat C     | 0.7772 | 0.2577      | 36.00 |

> ✅ **Rekomendasi Final: Kandidat D** — unggul konsisten di ketiga metode berkat pengalaman kerja tertinggi (9 tahun) dan nilai psikotes yang kompetitif (85).

---

## Catatan Penting

- Nilai **X** dan **Y** dari NPM langsung memengaruhi **data Kandidat D** sekaligus **bobot kriteria**, sehingga posisi Kandidat D bisa berubah drastis antar mahasiswa.
- Penjelasan lengkap analisis, perbandingan metode, dan rekomendasi tersedia di file **`Naomi Theresia_2315061091_Kuis_SPK.docx`**.
- Deadline pengumpulan: **22 Mei 2026 pukul 10.00 WIB**

<br>

---

> _Dibuat untuk memenuhi tugas Kuis Mata Kuliah Sistem Penunjang Keputusan_

|                 |                            |
| --------------- | -------------------------- |
| **Nama**        | Naomi Theresia             |
| **NPM**         | 2315061091                 |
| **Mata Kuliah** | Sistem Penunjang Keputusan |
