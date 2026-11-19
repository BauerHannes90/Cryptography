import hashlib

password = input("Bitte Passwort eingeben: ")
password_bytes = password.encode('utf-8')
sha256_hash = hashlib.sha256(password_bytes)
hex_digest = sha256_hash.hexdigest()

print(f"The SHA-256 Hash is: {hex_digest}")