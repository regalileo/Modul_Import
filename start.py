# Regal Nugraha - 20230040175 - TI23C

from luas import lingkaran, persegi, segitiga
from volume import bola, kubik, trapesium

while True:
    print("===== Menghitung Rumus =====")
    print("1. Hitung Rumus Lingkaran")
    print("2. Hitung Rumus Persegi")
    print("3. Hitung Rumus Segitiga")
    print("4. Hitung Volume Bola")
    print("5. Hitung Volume Kubik")
    print("6. Hitung Volume Trapesium")
    print("7. Keluar dari Program")
        
    pilih_program = input("Pilih Program (1-7): ")

    if pilih_program == "1":
        print(lingkaran.luas_lingkaran())
    elif pilih_program == "2":
        print(persegi.luas_persegi())
    elif pilih_program == "3":
        print(segitiga.luas_segitiga())
    elif pilih_program == "4":
        print(bola.volume_bola())
    elif pilih_program == "5":
        print(kubik.volume_kubik())
    elif pilih_program == "6":
        print(trapesium.volume_trapesium())
    elif pilih_program == "7":
        print("Terima kasih telah menggunakan program ini!")
        break
    else:
        print("Pilihan tidak valid. Silakan masukkan angka 1-7.")
        