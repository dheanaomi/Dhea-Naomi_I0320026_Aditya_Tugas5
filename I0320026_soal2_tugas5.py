nama = input("Masukkan Nama Anda:")
nilai = float(input("Masukkan Nilai Anda:"))
if nilai >= 85 :
    konversi = "A"
elif nilai >= 80 :
    konversi = "A-"
elif nilai >= 75 :
    konversi = "B+"
elif nilai >= 70 :
    konversi = "B"
elif nilai >= 65 :
    konversi = "C+"
elif nilai >= 60 :
    konversi = "C"
else :
    konversi = "E"
print("Halo,",nama,"! Nilai anda setelah dikonversi adalah",konversi)