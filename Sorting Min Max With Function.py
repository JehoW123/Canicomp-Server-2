angka = input("Masukkan angka (pisahkan dengan spasi): ")
angka_list = [int(x) for x in angka.split()]
        
print("\nPilih opsi:")
print("1. Urutkan dari kecil ke besar")
print("2. Urutkan dari besar ke kecil")
pilihan = int(input("Masukkan pilihan (1/2): "))

if pilihan == 1:
    angka_list.sort()
elif pilihan == 2:
    angka_list.sort(reverse=True)
else:
    print("Pilihan tidak valid. Program berakhir.")    

print("Hasil setelah diurutkan:")
print(angka_list)