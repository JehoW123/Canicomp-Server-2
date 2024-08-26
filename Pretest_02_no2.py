def print_pattern(n):
    if n == 1:
        print('*')
    elif n == 2:
        print('***')
        print('*@*')
        print('***')
    elif n == 3:
        print('*****')
        print('*@@@*')
        print('*@*@*')
        print('*@@@*')
        print('*****')
    elif n >= 4:
        # Print the top border
        print('*' * (2 * n - 1))  # 7 stars for n=4
        
        # Print the middle rows with patterns
        for i in range(n - 2):
            if i == 0 or i == n - 3:
                # Rows with all @
                print('*' + '@' * (2 * n - 3) + '*')  # 5 @ for n=4
            else:
                # Rows with @ and *
                middle = (2 * n - 3) // 2
                row = '*' + '@' * middle + '*' + '@' * middle + '*'
                print(row)  # Row with @ and * pattern
        
        # Print the bottom border
        print('*' * (2 * n - 1))  # 7 stars for n=4

# Example usage:
n = int(input("Enter a number: "))
print_pattern(n)
