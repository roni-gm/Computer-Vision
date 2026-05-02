# P2 — Color Space & Conversion

## Deskripsi

Praktikum ini membahas cara merepresentasikan warna dalam format berbeda dan mengonversi antar format menggunakan OpenCV. Program mengimplementasikan fungsi konversi color space dari BGR ke Grayscale dan HSV, serta mengambil nilai channel pada koordinat pixel tertentu.

---

## Tujuan

- Memahami konsep color space dan perbedaan antar format warna
- Mengimplementasikan konversi gambar BGR ke Grayscale dan HSV menggunakan OpenCV
- Mengambil nilai channel warna pada pixel tertentu dari berbagai color space

---

## Konsep Utama

### Color Space

Color space adalah sistem koordinat untuk merepresentasikan warna. Setiap format memiliki cara berbeda dalam menyimpan informasi warna yang sama.

| Color Space | Channel | Deskripsi |
|---|---|---|
| **BGR** | Blue, Green, Red | Format default OpenCV. Setiap channel bernilai 0–255. |
| **Grayscale** | Kecerahan | 1 channel saja. 0 = hitam, 255 = putih. |
| **HSV** | Hue, Saturation, Value | Hue = jenis warna (0–179), Saturation = kepekatan (0–255), Value = kecerahan (0–255). |
| **HLS** | Hue, Lightness, Saturation | Mirip HSV, namun menggunakan Lightness sebagai pengganti Value. |

### Mengapa Perlu Konversi?

- **Grayscale** → komputasi lebih ringan, tidak memerlukan informasi warna
- **HSV/HLS** → deteksi warna tertentu lebih mudah dibandingkan BGR

---

## Alur Kerja Program

```
Gambar BGR (input)
      │
      ├─── load_image(path)              → array BGR shape (H, W, 3)
      │
      ├─── convert_to_grayscale(image)   → array Grayscale shape (H, W)
      │
      └─── convert_to_hsv(image)         → array HSV shape (H, W, 3)
```

### Fungsi Nilai Pixel (exercise_2.py)

Fungsi-fungsi berikut mengembalikan nilai channel tertentu pada koordinat pixel `(x, y)`:

| Fungsi | Color Space | Channel yang Diambil |
|---|---|---|
| `gray_at_pixel(img, x, y)` | Grayscale | Kecerahan |
| `hue_at_pixel(img, x, y)` | HSV | Hue (jenis warna) |
| `saturation_at_pixel(img, x, y)` | HSV | Saturation (kepekatan) |
| `brightness_at_pixel(img, x, y)` | HSV | Value (kecerahan) |
| `lightness_at_pixel(img, x, y)` | HLS | Lightness |

---

## Output yang Diharapkan

| Fungsi | Tipe Output | Shape |
|---|---|---|
| `load_image` | `numpy.ndarray` | `(H, W, 3)` — BGR |
| `convert_to_grayscale` | `numpy.ndarray` | `(H, W)` — 2D |
| `convert_to_hsv` | `numpy.ndarray` | `(H, W, 3)` — HSV |
| `*_at_pixel` | `int` / `numpy scalar` | nilai tunggal |

---

## Struktur Project

```
p2-color-space-and-conversion/
├── conftest.py
├── exercise_2.py
├── images/
│   └── cat-image.jpg
├── src/
│   ├── __init__.py
│   └── main.py
└── tests/
    ├── sample_image.jpg
    └── test_main.py
```