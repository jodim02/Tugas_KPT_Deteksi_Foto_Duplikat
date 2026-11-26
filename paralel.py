
import os
import time
import multiprocessing
from concurrent.futures import ProcessPoolExecutor
from PIL import Image
import imagehash

FOLDER = "dataset"

def hitung_hash(nama_file):
    lokasi = os.path.join(FOLDER, nama_file)

    try:
        with Image.open(lokasi) as gambar:
            nilai_hash = str(imagehash.phash(gambar))
        return nama_file, nilai_hash

    except Exception as error:
        print("Gagal:", nama_file, error)
        return nama_file, None


def main():
    daftar_foto = sorted(
        f for f in os.listdir(FOLDER)
        if f.lower().endswith((".jpg", ".jpeg", ".png"))
    )

    print("Jumlah gambar:", len(daftar_foto))

    for jumlah_proses in [1, 2, 4, 8]:
        mulai = time.perf_counter()

        with ProcessPoolExecutor(max_workers=jumlah_proses) as executor:
            data_hash = list(executor.map(
                hitung_hash, daftar_foto, chunksize=10
            ))

        hasil_hash = {}

        for nama_file, nilai_hash in data_hash:
            if nilai_hash is not None:
                hasil_hash.setdefault(
                    nilai_hash, []
                ).append(nama_file)

        kelompok_duplikat = [
            daftar for daftar in hasil_hash.values()
            if len(daftar) > 1
        ]

        waktu = time.perf_counter() - mulai

        print("\n==========================")
        print("Jumlah proses:", jumlah_proses)
        print("Gambar berhasil:", sum(
            len(x) for x in hasil_hash.values()
        ))
        print("Kelompok duplikat:", len(kelompok_duplikat))
        print(f"Waktu eksekusi: {waktu:.4f} detik")

if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()
