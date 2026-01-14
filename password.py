import random
import string

def generate_password(length):
    # Define possible characters: letters, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    # Randomly select characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Step 1: User Input
try:
    length = int(input("Enter the desired password length: "))
    if length < 4:
        print("Password length should be at least 4 characters.")
    else:
        # Step 2: Generate Password
        password = generate_password(length)
        # Step 3: Display the Password
        print("Generated Password:", password)
except ValueError:
    print("Please enter a valid number.")
