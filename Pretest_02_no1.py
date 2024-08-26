def is_palindrome(text):
    # Membalikkan teks
    reversed_text = text[::-1]
    # Memeriksa apakah teks asli sama dengan teks yang dibalik
    return text == reversed_text, reversed_text

# Contoh penggunaan
text = input("Masukkan teks: ")
text2 = text.casefold()
rev_str = reversed(text2)
palindrome, reversed_text = is_palindrome(text)

if list(text2) == list(rev_str):
    print(f'"{text}" merupakan kata/kalimat palindrom.')
else:
    print(f'"{text}" bukan kata/kalimat palindrom.')

print(f'Dibalik dengan case sensitive: {reversed_text}')