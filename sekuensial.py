
import os
import csv
import time
from PIL import Image
import imagehash

# ==========================================
# KONFIGURASI
# ==========================================

FOLDER_DATASET = "dataset"
FOLDER_HASIL = "hasil"

os.makedirs(FOLDER_HASIL, exist_ok=True)

# ==========================================
# FUNGSI DETEKSI FOTO
# ==========================================

def hitung_hash(nama_file):
    lokasi = os.path.join(FOLDER_DATASET, nama_file)

    try:
        with Image.open(lokasi) as gambar:
            nilai_hash = str(imagehash.phash(gambar))

        return nilai_hash

    except Exception as error:
        print("Gagal memproses:", nama_file, error)
        return None


# ==========================================
# PROGRAM UTAMA
# ==========================================

def main():

    print("========================================")
    print(" DETEKSI FOTO DUPLIKAT - SEKUENSIAL")
    print("========================================")

    daftar_foto = sorted([
        file for file in os.listdir(FOLDER_DATASET)
        if file.lower().endswith((".jpg", ".jpeg", ".png"))
    ])

    hasil_hash = {}
    gagal = []

    # Mulai pengukuran waktu
    mulai = time.perf_counter()

    # Memproses gambar satu per satu
    for nama_file in daftar_foto:

        nilai_hash = hitung_hash(nama_file)

        if nilai_hash is not None:
            if nilai_hash not in hasil_hash:
                hasil_hash[nilai_hash] = []

            hasil_hash[nilai_hash].append(nama_file)

        else:
            gagal.append(nama_file)

    # Menghentikan pengukuran waktu
    selesai = time.perf_counter()

    waktu_eksekusi = selesai - mulai

    # ======================================
    # MENGHITUNG HASIL
    # ======================================

    kelompok_duplikat = [
        daftar for daftar in hasil_hash.values()
        if len(daftar) > 1
    ]

    jumlah_berhasil = sum(
        len(daftar) for daftar in hasil_hash.values()
    )

    print("\nHASIL DETEKSI FOTO DUPLIKAT")
    print("----------------------------------------")

    for nomor, daftar in enumerate(kelompok_duplikat, 1):
        print(f"Kelompok {nomor}: {', '.join(daftar)}")

    print("\n========================================")
    print(" RINGKASAN HASIL")
    print("========================================")

    print("Jumlah gambar ditemukan :", len(daftar_foto))
    print("Gambar berhasil diproses:", jumlah_berhasil)
    print("Gambar gagal diproses   :", len(gagal))
    print("Kelompok duplikat       :", len(kelompok_duplikat))
    print(f"Waktu eksekusi          : {waktu_eksekusi:.4f} detik")

    # ======================================
    # MENYIMPAN FILE CSV
    # ======================================

    lokasi_csv = os.path.join(
        FOLDER_HASIL, "duplikat.csv"
    )

    with open(
        lokasi_csv, "w", newline="", encoding="utf-8-sig"
    ) as file:

        penulis = csv.writer(file)

        penulis.writerow([
            "Kelompok",
            "Foto Referensi",
            "Foto Duplikat",
            "Status"
        ])

        for nomor, daftar in enumerate(
            kelompok_duplikat, 1
        ):
            foto_referensi = daftar[0]

            for foto_duplikat in daftar[1:]:
                penulis.writerow([
                    nomor,
                    foto_referensi,
                    foto_duplikat,
                    "pHash identik"
                ])

    # ======================================
    # MENYIMPAN HASIL KE TXT
    # ======================================

    lokasi_txt = os.path.join(
        FOLDER_HASIL, "hasil_sekuensial.txt"
    )

    with open(
        lokasi_txt, "w", encoding="utf-8"
    ) as file:

        file.write(
            "HASIL PRAKTIKUM KOMPUTASI SEKUENSIAL\n"
        )
        file.write("=" * 45 + "\n\n")

        file.write(
            f"Jumlah gambar ditemukan : {len(daftar_foto)}\n"
        )
        file.write(
            f"Gambar berhasil diproses: {jumlah_berhasil}\n"
        )
        file.write(
            f"Gambar gagal diproses   : {len(gagal)}\n"
        )
        file.write(
            f"Kelompok duplikat       : {len(kelompok_duplikat)}\n"
        )
        file.write(
            f"Waktu eksekusi          : {waktu_eksekusi:.4f} detik\n"
        )

        file.write("\nDAFTAR KELOMPOK DUPLIKAT\n")
        file.write("-" * 45 + "\n")

        for nomor, daftar in enumerate(
            kelompok_duplikat, 1
        ):
            file.write(
                f"Kelompok {nomor}: {', '.join(daftar)}\n"
            )

        if gagal:
            file.write("\nGAMBAR GAGAL DIPROSES\n")
            for nama_file in gagal:
                file.write(nama_file + "\n")

    # ======================================
    # INFORMASI PENYIMPANAN
    # ======================================

    print("\nFILE HASIL BERHASIL DISIMPAN")
    print("----------------------------------------")
    print("CSV :", lokasi_csv)
    print("TXT :", lokasi_txt)
    print("========================================")


if __name__ == "__main__":
    main()
