import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Input: Desired password length
try:
    length = int(input("Enter the length of the password: "))
    if length < 4:
        print("Please enter a valid password length greater than 4.")
    else:
        password = generate_password(length)
        print("Generated Password:", password)
except ValueError:
    print("Invalid input. Please enter a valid number for password length.")
