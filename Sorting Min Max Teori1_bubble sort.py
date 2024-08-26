angka = input("Masukkan angka (pisahkan dengan spasi): ")
angka_list = [int(x) for x in angka.split()]
        
print("\nPilih opsi:")
print("1. Urutkan dari kecil ke besar")
print("2. Urutkan dari besar ke kecil")
pilihan = int(input("Masukkan pilihan (1/2): "))

if pilihan == 1:
    def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    
    angka_list = [int(x) for x in angka.split()]
    bubble_sort(angka_list)

elif pilihan == 2:
    def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] < arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    
    angka_list = [int(x) for x in angka.split()]
    bubble_sort(angka_list)
else:
    print("Pilihan tidak valid. Program berakhir.")    

print("Hasil setelah diurutkan:")
print(angka_list)