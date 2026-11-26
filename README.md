
# Deteksi Foto Duplikat Menggunakan Komputasi Paralel

## Identitas
- **Nama:** Jodim Robertus
- **NIM:** D0224312
- **Kelas:** 2024B
- **Mata Kuliah:** Komputasi Paralel

## Deskripsi
Program deteksi foto duplikat menggunakan Python dan algoritma Perceptual Hashing (pHash). Praktikum ini membandingkan kinerja metode sekuensial dan paralel menggunakan 500 gambar digital.

## Teknologi
- Python
- Pillow dan ImageHash
- ProcessPoolExecutor
- Matplotlib

## Cara Menjalankan
Instal library:
`pip install pillow imagehash matplotlib`

Jalankan program:
- Sekuensial: `python sekuensial.py`
- Paralel: `python paralel.py`

Pastikan gambar tersedia dalam folder `dataset/`.

## Hasil Pengujian

| Metode | Waktu Eksekusi |
|---|---:|
| Sekuensial | 5,0608 detik |
| Paralel (1 proses) | 5,9123 detik |
| Paralel (2 proses) | 3,9528 detik |
| Paralel (4 proses) | 3,6020 detik |
| Paralel (8 proses) | 4,8997 detik |

**Hasil:** 500 gambar diproses dan ditemukan 232 kelompok dengan pHash identik.

**Kesimpulan:** Konfigurasi 4 proses memberikan waktu tercepat dengan speedup sekitar 1,41 kali dibandingkan metode sekuensial pada pengujian awal.
