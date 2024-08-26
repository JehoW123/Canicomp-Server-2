def find_min_max_algorithm(numbers):
    min_value = numbers[0]
    max_value = numbers[0]
    for num in numbers[1:]:
        if num < min_value:
            min_value = num
        if num > max_value:
            max_value = num
    
    return min_value, max_value
if __name__ == "__main__":
    numbers = list(map(int, input("Masukkan sekumpulan bilangan, dipisahkan dengan spasi: ").split()))
    min_value, max_value = find_min_max_algorithm(numbers)
    print(f"Nilai minimum: {min_value}")
    print(f"Nilai maksimum: {max_value}")