angka = input("Masukkan angka (pisahkan dengan spasi): ")
angka_list = [int(x) for x in angka.split()]
        
print("\nPilih opsi:")
print("1. Urutkan dari kecil ke besar")
print("2. Urutkan dari besar ke kecil")
pilihan = int(input("Masukkan pilihan (1/2): "))

if pilihan == 1:
    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0]
            less = [x for x in arr[1:] if x <= pivot]
            greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

    angka_list = [int(x) for x in angka.split()]
    sorted_angka = quick_sort(angka_list)


elif pilihan == 2:
    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0]
            less = [x for x in arr[1:] if x >= pivot]
            greater = [x for x in arr[1:] if x < pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

    angka_list = [int(x) for x in angka.split()]
    sorted_angka = quick_sort(angka_list)

else:
    print("Pilihan tidak valid. Program berakhir.")    

print("Hasil setelah diurutkan:")
print(sorted_angka)