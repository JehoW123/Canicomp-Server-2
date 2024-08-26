# Input deret bilangan
inputan = input('Masukkan deret bilangan (pisahkan dengan koma): ')
numbers = [int(bilangan.strip()) for bilangan in inputan.split(',')]

# Menghitung rata-rata
total = sum(numbers)
cont = len(numbers)
rata = total / cont

# Menghitung median
sorted_numbers = sorted(numbers)
mid = cont // 2
if cont % 2 == 0:
    median = (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
else:
    median = sorted_numbers[mid]

# Menghitung modus
modus = {}
for number in numbers:
    if number in modus:
        modus[number] += 1
    else:
        modus[number] = 1

max_freq = max(modus.values())
modes = [key for key, value in modus.items() if value == max_freq]

# Menentukan modus
if len(modes) == len(numbers):
    mode = "Tidak ada modus (semua angka muncul dengan frekuensi yang sama)"
elif len(modes) == 1:
    mode = modes[0]
else:
    mode = modes

print("data anda =", numbers)
print(f'Rata-rata: {rata}')
print(f'Median: {median}')
print(f'Modus: {mode}')

