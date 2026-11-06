import numpy as np

np.random.seed(42)
nilai_ujian = np.random.randint(50, 100, size=30)

print("Data nilai ujian awal:")
print(nilai_ujian)

nilai_sorted = np.sort(nilai_ujian)

nilai_terbesar_ke_terkecil = nilai_sorted[::-1]

print("\nNilai diurutkan dari yang terbesar ke terkecil:")
print(nilai_terbesar_ke_terkecil)

lima_nilai_terbesar = nilai_terbesar_ke_terkecil[:5]
print("\n5 nilai terbesar:")
print(lima_nilai_terbesar)