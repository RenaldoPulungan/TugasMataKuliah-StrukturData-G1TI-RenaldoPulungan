#Program Kalkulator
print ("Pilihan Operator")
print ("1. penjumlahan")
print ("2. pengurangan")
print ("3. perkalian")
print ("4. pembagian")

bil1 = int(input("Masukkan Bilangan Pertama = "))
bil2 = int(input("Masukkan Bilangan Kedua = "))
pilihan = input("Pilihan Operator = ")

if pilihan == "1":
    print("Hasil = ", bil1 + bil2)
elif pilihan == "2":
    print("Hasil = ", bil1 - bil2)
elif pilihan == "3":
    print("Hasil = ", bil1 * bil2)
elif pilihan == "4":
    print("Hasil = ", bil1 / bil2)
else:
    print("Pilihan Tidak Valid")