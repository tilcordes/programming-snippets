import hashlib

hash = hashlib.sha512('Hello'.encode())
print(hash.hexdigest())
print(hash.digest())