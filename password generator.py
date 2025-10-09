import random
import string

def generate_password(length, use_uppercase, use_digits, use_special):
    chars = string.ascii_lowercase  # base letters

    if use_uppercase:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_special:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    print("------ PASSWORD GENERATOR ------")
    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            print(" Length must be greater than 0.")
            return
    except ValueError:
        print(" Invalid input! Please enter a number.")
        return

    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, use_uppercase, use_digits, use_special)
    print(f"\n Generated Password: {password}")

if __name__ == "__main__":
    main()
