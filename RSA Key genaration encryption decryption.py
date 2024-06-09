#Sudam Sanjula
#ECU ID - 10660248
#Portfolio Part 2

import math

# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to get a prime input from the user
def get_prime_input(prompt):
    while True:
        value = int(input(prompt))
        if is_prime(value) and value > 100:
            return value
        else:
            print("Please enter a prime number greater than 100.")

# Function to get a valid e value from the user
def get_valid_e(phi_n):
    while True:
        e = int(input(f"Enter a value for e (1 < e < {phi_n}, coprime with {phi_n}): "))
        if 1 < e < phi_n and math.gcd(e, phi_n) == 1:
            return e
        else:
            print(f"Invalid e. Please enter a value in the range (1, {phi_n}) that is coprime with {phi_n}.")

# Function to calculate the modular inverse using Extended Euclidean Algorithm
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Function for RSA key generation
def generate_rsa_keys():
    print("RSA Key Generation:")
    # Step 1: Input two prime numbers
    p = get_prime_input("Enter a prime number (p > 100): ")
    q = get_prime_input("Enter another prime number (q > 100): ")

    # Step 2: Input a value for e
    phi_n = (p - 1) * (q - 1)
    e = get_valid_e(phi_n)

    # Step 3: Compute n
    n = p * q

    # Step 4: Compute Φ(n)
    phi_n = (p - 1) * (q - 1)

    # Step 5: Find d
    d = mod_inverse(e, phi_n)

    # Step 6: Display keys
    public_key = (n, e)
    private_key = d
    print("\nRSA public key: ", public_key)
    print("RSA private key: ", private_key)

    # Step 7: Ask for more operations
    return input("\nDo you want to perform more operations? (yes/no): ").lower() == "yes"

# Function for RSA key encryption
def encrypt_text():
    print("\nEncrypt a Key:")
    plaintext = input("Enter plaintext: ")
    # Convert text to numeric values
    x = [ord(char) for char in plaintext]

    # Get public key values
    n = int(input("Enter public key value for n: "))
    e = int(input("Enter public key value for e: "))

    # Encrypt
    cipher_text = [pow(char, e, n) for char in x]

    # Show cipher text as a single message
    cipher_text_message = ' '.join(map(str, cipher_text))
    print("Cipher text (as a single message):", cipher_text_message)

    # Ask for more operations
    return input("\nDo you want to perform more operations? (yes/no): ").lower() == "yes"

# Function for RSA key decryption
def decrypt_text():
    print("\nDecrypt a Key:")
    # Step 1: Ask the user to enter cipher text
    cipher_text_input = input("Enter cipher text : ")

    # Remove square brackets and split the input into a list of numerical values
    cipher_text_values = [int(val) for val in cipher_text_input.replace("[", "").replace("]", "").replace(',', ' ').split()]

    # Step 2: Ask the user to enter private key values for n and d
    n = int(input("Enter private key value for n: "))
    d = int(input("Enter private key value for d:"))

    # Step 3: Decrypt each numerical value using the formula plaintext = y^d mod n
    plaintext_values = [pow(val, d, n) for val in cipher_text_values]

    # Step 4: Convert the plaintext values back to text values
    plaintext_text = ''.join([chr(val) for val in plaintext_values])

    # Step 5: Show plaintext as text value
    print("Plaintext: ", plaintext_text)

    # Step 6: Ask the user if they want to perform more operations
    return input("\nDo you want to perform more operations? (yes/no): ").lower() == "yes"


# The main program loop
while True:
    print("\nOptions:")
    print("1) RSA Key Generation")
    print("2) Encrypt a Key")
    print("3) Decrypt a Key")
    print("4) Exit")

    choice = input("Select an option (1-4): ")

    if choice == "1":
        if not generate_rsa_keys():
            break
    elif choice == "2":
        if not encrypt_text():
            break
    elif choice == "3":
        if not decrypt_text():
            break
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please enter a valid option.")

print("Exiting the program.")
