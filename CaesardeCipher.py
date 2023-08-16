def caesar_decipher(text, key):
    res = ""
    for char in text:
        if char.isalpha():
            ascii_alphab = ord('A') if char.isupper()  else ord('a')
            decoded_char = chr((ord(char) - ascii_alphab - key) % 26 + ascii_alphab)
            res += decoded_char
        else:
            res += char
    return res

def main():
    text = input("Enter the text to decode: ")
    key = int(input("Enter the key: "))
    res = caesar_decipher(text, key)
    print("Decoded text:", res)

while True:
    main()

