
import requests

from Crypto.Cipher import AES
import hashlib
import random




BASE_URL = "http://aes.cryptohack.org/passwords_as_keys"

# 1) get the ciphertext of the encrypted flag
r = requests.get(f"{BASE_URL}/encrypt_flag")
data = r.json()
ciphertext = data["ciphertext"]
print("ciphertext", ciphertext)

with open('words.txt') as f:
    words = [w.strip() for w in f.readlines()]
for word in words:
    key = hashlib.md5(word.encode()).digest()
    cipher = AES.new(key, AES.MODE_ECB)
    try:
        plaintext = cipher.decrypt(bytes.fromhex(ciphertext))
        if plaintext.startswith(b"crypto"):
            print("flag", plaintext.decode())
            break
    except Exception as e:
        continue
#flag crypto{k3y5__r__n07__p455w0rdz?}
