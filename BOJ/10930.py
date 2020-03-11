import hashlib

value = input()
encoded_string = value.encode()
hexdigest = hashlib.sha256(encoded_string).hexdigest()
print(hexdigest)
