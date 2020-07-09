from Crypto.Cipher import AES
from Crypto import Random
import hashlib

def pad(s):
    return s.encode() + b'\0' * (16 - len(s) % 16)

# encryptor
iv = Random.new().read(16)
key = hashlib.sha256('Til'.encode()).digest()
encryptor = AES.new(key, AES.MODE_CBC, iv)
enced = encryptor.encrypt(pad('Hello'))

# decryptor
decryptor = AES.new(key, AES.MODE_CBC, iv)
deced = decryptor.decrypt((enced))

print(enced)
print(deced.rstrip(b'\0'))