import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")

    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            raise ValueError("Length must be a positive integer.")
    except ValueError as e:
        print(f"Error: {e}")
        return

    password = generate_password(length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
