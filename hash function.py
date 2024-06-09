import hashlib

def custom_hash(message):
    # Step 1: Convert the message to bytes
    message_bytes = message.encode('utf-8')

    # Step 2: Initialize variables (constants chosen arbitrarily for simplicity)
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    # Step 3: Pre-process the message (padding)
    message_bits = len(message_bytes) * 8
    padded_message = message_bytes + b'\x80' + b'\x00' * ((56 - (len(message_bytes) + 1) % 64) % 64) + message_bits.to_bytes(8, 'big')

    # Step 4: Process the message in 512-bit blocks
    for i in range(0, len(padded_message), 64):
        block = padded_message[i:i+64]

        # Break the block into 16 words
        words = [int.from_bytes(block[j:j+4], 'big') for j in range(0, 64, 4)]

        # Extend the 16 words into 80 words
        for j in range(16, 80):
            words.append((words[j-3] ^ words[j-8] ^ words[j-14] ^ words[j-16]) << 1)

        # Initialize hash values for this block
        a, b, c, d, e = h0, h1, h2, h3, h4

        # Main loop
        for j in range(80):
            if 0 <= j <= 19:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif 20 <= j <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= j <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            else:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            a, b, c, d, e = ((a << 5) | (a >> 27)) + f + e + k + words[j] & 0xFFFFFFFF, a, ((b << 30) | (b >> 2)), c, d

        # Update hash values for this block
        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF
        h4 = (h4 + e) & 0xFFFFFFFF

    # Step 5: Combine hash values
    hash_result = (h0 << 128) | (h1 << 96) | (h2 << 64) | (h3 << 32) | h4

    # Convert the hash to a hexadecimal string
    hash_hex = hex(hash_result)[2:]

    return hash_hex

# The main program loop
while True:
    # Get user input for the message
    user_input = input("Enter a message to hash: ")
    hashed_result = custom_hash(user_input)
    print("Custom Hash:", hashed_result)

    more_hashes = input("\nDo you want to make more hashes? (yes/no): ").lower()
    if more_hashes != "yes":
        break

print("Exiting the hash program.")
