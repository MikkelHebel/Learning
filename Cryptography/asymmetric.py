# Encryption is the process of converting information into a code to secure it from unauthorized access or use. It uses algorithms to transform
# plaintext (readable data) into ciphertext (encoded data) using keys. There are two primary types: symmetric and asymmetric encryption.
# Symmetric encryption uses a single key for both encryption and decryption, making it faster but necessitating a secure key exchange.
# Asymmetric encryption uses a pair of keys, public and private, allowing one key to encrypt information and the other to decrypt information.

from cryptography.fernet import Fernet

message = "My other super secret message."

# Generate key for encryption and decryption
key = Fernet.generate_key()
fernet = Fernet(key)

# Encrypt the message
encMessage = fernet.encrypt(message.encode())
print("original string: ", message)
print("encrypted string: ", encMessage)

# Decrypt the message
decMessage = fernet.decrypt(encMessage).decode()
print("decrypted string: ", decMessage)