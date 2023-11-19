import math

def hitung_rumus_segitiga(alas, tinggi):
    luas = 0.5 * alas * tinggi
    return luas

def hitung_rumus_persegi(sisi):
    luas = sisi * sisi
    return luas

while True:
    print("Menu:")
    print("1. Hitung rumus segitiga")
    print("2. Hitung rumus persegi")
    print("3. Keluar")
    
    pilihan = input("Masukkan pilihan (1/2/3): ")
    
    if pilihan == '1':
        alas = float(input("Masukkan panjang alas segitiga: "))
        tinggi = float(input("Masukkan tinggi segitiga: "))
        hasil = hitung_rumus_segitiga(alas, tinggi)
        print("Luas segitiga:", hasil)
    elif pilihan == '2':
        sisi = float(input("Masukkan panjang sisi persegi: "))
        hasil = hitung_rumus_persegi(sisi)
        print("Luas persegi:", hasil)
    elif pilihan == '3':
        print("Keluar dari program.")
        break
    else:
        print("Masukkan Inputan Yang Benar")
