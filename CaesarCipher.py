import string
import sys
alph = str(string.ascii_lowercase)
input_str = input("Enter text: ")
res = ""
key = int(sys.argv[1])
for letter in input_str: 
    position = alph.find(letter) 
    new_position = position + key 
    if letter in alph: 
        res += alph[new_position] 
    else: 
        res += letter 
print(res)
