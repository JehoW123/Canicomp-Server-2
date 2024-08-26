def find_min_max_builtin(numbers):
    min_value = min(numbers)
    max_value = max(numbers)
    return min_value, max_value

if __name__ == "__main__":
    numbers = list(map(int, input("Masukkan sekumpulan bilangan, dipisahkan dengan spasi: ").split()))
    min_value, max_value = find_min_max_builtin(numbers)
    print(f"Nilai minimum: {min_value}")
    print(f"Nilai maksimum: {max_value}")