import random
import string

def generate_password(length):
    # Define the character sets to use in generating the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate password using random.choice
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

if __name__ == "__main__":
    # Prompt user to specify the desired length of the password
    try:
        password_length = int(input("Enter the desired length of the password: "))
        
        if password_length <= 0:
            print("Password length should be greater than zero.")
        else:
            # Generate the password
            generated_password = generate_password(password_length)
            
            # Display the generated password
            print("Generated password:", generated_password)
            
    except ValueError:
        print("Invalid input. Please enter a valid integer for the password length.")
