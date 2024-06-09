import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def get_prime_input(prompt):
    while True:
        value = int(input(prompt))
        if is_prime(value) and value > 100:
            return value
        else:
            print("Please enter a prime number greater than 100.")

def get_valid_e(phi_n):
    while True:
        e = int(input(f"Enter a value for e (1 < e < {phi_n}, coprime with {phi_n}): "))
        if 1 < e < phi_n and math.gcd(e, phi_n) == 1:
            return e
        else:
            print(f"Invalid e. Please enter a value in the range (1, {phi_n}) that is coprime with {phi_n}.")

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def generate_rsa_keys():
    print("RSA Key Generation:")
    p = get_prime_input("Enter a prime number (p > 100): ")
    q = get_prime_input("Enter another prime number (q > 100): ")

    phi_n = (p - 1) * (q - 1)
    e = get_valid_e(phi_n)

    n = p * q
    d = mod_inverse(e, phi_n)

    public_key = (n, e)
    private_key = d
    print("\nRSA public key: ", public_key)
    print("RSA private key: ", private_key)

    return input("\nDo you want to perform more operations? (yes/no): ").lower() == "yes"

def make_digital_signature():
    print("\nMake a Digital Signature:")
    hash_digest = input("Enter a hash digest: ")
    x = int(hash_digest, 16)  # Convert hash digest to numeric value

    n = int(input("Enter private key value for n: "))
    d = int(input("Enter private key value for d: "))

    signature = pow(x, d, n)
    print("Digital Signature :", signature)

    return input("\nDo you want to perform more operations? (yes/no): ").lower() == "yes"

def verify_digital_signature():
    print("\nVerify a Digital Signature:")
    signature = int(input("Enter a digital signature : "))
    n = int(input("Enter public key value for n: "))
    e = int(input("Enter public key value for e: "))

    # Verify the signature
    hash_result = pow(signature, e, n)
    hash_result_hex = hex(hash_result)[2:]

    original_hash_digest = input("Enter the original hash digest: ")
    if original_hash_digest.lower() == hash_result_hex.lower():
        print("Digital signature verification passed.")
    else:
        print("Digital signature verification failed.")

    return input("\nDo you want to perform more operations? (yes/no): ").lower() == "yes"

# The main program loop
while True:
    print("\nOptions:")
    print("1) RSA Key Generation")
    print("2) Make a Digital Signature")
    print("3) Verify a Digital Signature")
    print("4) Exit")

    choice = input("Select an option (1-4): ")

    if choice == "1":
        if not generate_rsa_keys():
            break
    elif choice == "2":
        if not make_digital_signature():
            break
    elif choice == "3":
        if not verify_digital_signature():
            break
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please enter a valid option.")

print("Exiting the program.")
