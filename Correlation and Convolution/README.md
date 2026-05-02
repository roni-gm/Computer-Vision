# P3 — Correlation & Convolution

## Deskripsi

Praktikum ini membahas dua operasi fundamental dalam image processing: correlation dan convolution. Keduanya bekerja dengan cara menggeser kernel (filter) di atas gambar untuk menghasilkan efek tertentu seperti deteksi tepi, blur, dan sharpening.

---

## Tujuan

- Memahami perbedaan konseptual antara correlation dan convolution
- Mengimplementasikan kedua operasi menggunakan `scipy.signal`
- Menerapkan Sobel filter untuk deteksi tepi pada gambar

---

## Konsep Utama

### Kernel

Kernel adalah matriks kecil (misalnya 3×3) yang digeser di atas gambar. Di setiap posisi, nilai kernel dikalikan dengan nilai pixel yang tertutup, lalu dijumlahkan menjadi satu nilai output.

```
Contoh Sobel X (deteksi tepi vertikal):
[[ 1,  0, -1],
 [ 2,  0, -2],
 [ 1,  0, -1]]
```

### Correlation

Kernel digeser di atas gambar **tanpa dibalik**. Setiap posisi menghasilkan satu nilai dari perkalian elemen kernel dengan pixel yang bersesuaian.

- **Mode:** `full` → output lebih besar dari gambar asli karena padding penuh di semua sisi
- **Output shape:** `(H + kH - 1, W + kW - 1)`

### Convolution

Proses sama dengan correlation, namun kernel **dibalik 180°** terlebih dahulu sebelum digeser.

- **Mode:** `same` → output sama besar dengan gambar asli
- **Output shape:** `(H, W)`

### Perbandingan

| | Correlation | Convolution |
|---|---|---|
| Kernel | Tidak dibalik | Dibalik 180° |
| Padding | `full` | `same` |
| Output shape | Lebih besar dari input | Sama dengan input |
| Penggunaan umum | Template matching | CNN, filtering standar |

> **Catatan:** Untuk kernel yang simetris (seperti Gaussian blur), hasil correlation dan convolution identik karena membalik kernel tidak mengubah nilainya.

---

## Alur Kerja Program

```
Gambar BGR (input)
      │
      ▼
Konversi ke Grayscale (1 channel)
      │
      ├─── correlate(img, kernel)
      │         └── correlate2d(gray, kernel, mode='full')
      │         └── output shape: (H+kH-1, W+kW-1), dtype int64
      │
      └─── convolve(img, kernel)
                └── convolve2d(gray, kernel, mode='same')
                └── output shape: (H, W), dtype int64
```

### Contoh Penggunaan — Deteksi Tepi Sobel

```python
sobel_x = np.array([[ 1,  0, -1],
                     [ 2,  0, -2],
                     [ 1,  0, -1]])

sobel_y = np.array([[ 1,  2,  1],
                     [ 0,  0,  0],
                     [-1, -2, -1]])

output_x   = convolve(image, sobel_x)        # tepi arah vertikal
output_y   = convolve(image, sobel_y)        # tepi arah horizontal
sobel_full = np.sqrt(output_x**2 + output_y**2)  # gabungan
```

---

## Output yang Diharapkan

| Fungsi | Mode | Output Shape | dtype |
|---|---|---|---|
| `correlate(img, kernel)` | `full` | `(H+kH-1, W+kW-1)` | `int64` |
| `convolve(img, kernel)` | `same` | `(H, W)` | `int64` |

Output diverifikasi secara pixel-per-pixel terhadap file referensi `.npy` yang sudah disediakan di folder `tests/`.

---

## Struktur Project

```
p3-correlation-and-convolution/
├── conftest.py
├── src/
│   └── main.py
└── tests/
    ├── sample_image.png
    ├── output_correlate.npy
    ├── output_convolve.npy
    └── test_main.py
```
