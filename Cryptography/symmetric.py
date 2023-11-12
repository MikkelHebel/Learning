# Encryption is the process of converting information into a code to secure it from unauthorized access or use. It uses algorithms to transform
# plaintext (readable data) into ciphertext (encoded data) using keys. There are two primary types: symmetric and asymmetric encryption.
# Symmetric encryption uses a single key for both encryption and decryption, making it faster but necessitating a secure key exchange.
# Asymmetric encryption uses a pair of keys, public and private, allowing one key to encrypt information and the other to decrypt information.

from cryptography.fernet import Fernet
  
# Generate key and store the value in a variable
key = Fernet.generate_key()
keyVar = Fernet(key)

# Converted plain text to cipher text
token = keyVar.encrypt(b"My super secret message.") 
print("Encrypted text:")
print(token)

d = keyVar.decrypt(token)
print("Plain text:")
print(d)