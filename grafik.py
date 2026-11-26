
import os
import matplotlib.pyplot as plt

metode = [
    "Sekuensial",
    "Pool 1",
    "Paralel 2",
    "Paralel 4",
    "Paralel 8"
]

# Data dari pengujian awal
waktu = [5.0608, 5.9123, 3.9528, 3.6020, 4.8997]

os.makedirs("hasil", exist_ok=True)

plt.figure(figsize=(9, 5))
plt.bar(metode, waktu)

plt.title("Perbandingan Waktu Eksekusi CPU")
plt.xlabel("Metode Pemrosesan")
plt.ylabel("Waktu Eksekusi (detik)")

for i, nilai in enumerate(waktu):
    plt.text(i, nilai + 0.08, f"{nilai:.4f}", ha="center")

plt.ylim(0, max(waktu) + 1)
plt.tight_layout()

plt.savefig("hasil/grafik_perbandingan.png", dpi=300)
plt.show()

print("Grafik berhasil disimpan!")
