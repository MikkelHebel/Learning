# A hashing function in cryptography is a mathematical algorithm that converts an input (or 'message') into a fixed-size string of numbers and letters.
# It generates a unique output, known as a hash, that represents the original data. This process is deterministic, meaning the same input will always
# produce the same hash. Hash functions are designed to be one-way, making it computationally infeasible to reverse the process and obtain the original
# input from the hash. They're widely used in security protocols to verify data integrity, securely store passwords, and ensure message authenticity.

# Hashing algorithms are also used in blockchain technology. In a blockchain, each block contains a hash of the previous block, which creates a chain
# of blocks. This process makes it easy to detect any changes to the data stored in previous blocks. If a hacker attempts to change a single block, the
# hash of the block would change and disrupt the entire chain.

# Salting is used to combat so called rainbow tables which are tables full of precomputed hashes.
# Salting is like adding a bit of extra salt to the spaghetti mix to change it's flavour. This way it changes the output completely.

import bcrypt

password = input("Enter your password: ").encode('utf-8')

# Add salt to the password and hash it.
salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(password, salt)

print("Password:")
print(password)

print("Salt:")
print(salt)

print("Hashed:")
print(hashed)