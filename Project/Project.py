# Encryption function
def encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            shift = key % 26
            if char.islower():
                result += chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                result += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            result += char
    return result


# Decryption function
def decrypt(text, key):
    return encrypt(text, -key)


print("=== File Encryption/Decryption Tool ===")

try:
    print("\n[STEP 1] Choose operation")
    choice = input("Enter E to Encrypt or D to Decrypt: ").upper()

    print("\n[STEP 2] Enter key")
    key = int(input("Enter key (number): "))

    print("\n[STEP 3] Enter file names")
    input_file = input("Enter input file name: ")
    output_file = input("Enter output file name: ")

    print("\n[STEP 4] Reading file...")
    with open(input_file, "r") as file:
        data = file.read()
    print("✔ File read successfully")

    print("\n[STEP 5] Processing data...")
    if choice == "E":
        result = encrypt(data, key)
        print("✔ Encryption completed")
    elif choice == "D":
        result = decrypt(data, key)
        print("✔ Decryption completed")
    else:
        print("❌ Error: Invalid choice! Please enter E or D.")
        exit()

    print("\n[STEP 6] Writing to file...")
    with open(output_file, "w") as file:
        file.write(result)
    print("✔ File written successfully")

    print("\n✅ Operation completed successfully!")

# Error handling
except FileNotFoundError:
    print("\n❌ Error: Input file not found! Please check the file name.")

except ValueError:
    print("\n❌ Error: Invalid key! Please enter a number.")

except Exception as e:
    print("\n❌ Unexpected Error:", e)