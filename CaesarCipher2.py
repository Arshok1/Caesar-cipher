def caesar_cipher(text, key):
    res = ""
    for char in text:
        if char.isalpha():
            ascii_alphab = ord('A') if char.isupper()  else ord('a')
            encoded_char = chr((ord(char) - ascii_alphab + key) % 26 + ascii_alphab)
            res += encoded_char
        else:
            res += char
    return res
def main():
    text = input("Enter the text to encode: ")
    key = int(input("Enter the key: "))
    res = caesar_cipher(text, key)
    print("Encoded text:", res)
while True: 
    main()

