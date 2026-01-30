import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#print(f"chars: {chars}")
#print(f"Keys: {key}")

#Encyption

plain_text = input("Enter a message to Encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Original Messege: {plain_text}")
print(f"Encrypted Messege: {cipher_text}")


#Dycrypt

cipher_text = input("Enter a message to Encrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"Encrypted Messege: {cipher_text}")
print(f"Decrypted Messege: {plain_text}")