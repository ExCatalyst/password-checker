import string

def check_password_strength(password: str) -> int:
    """
    Higher score means stronger password.The score is calculated based on the following criteria:
    - length
    - complexity
    """

    global x
    score = 0

    #Check complexity
    if any(char.islower() for char in password):
        score += 1
        x=1
    if any(char.isupper() for char in password):
        score += 1
        x += 1
    if any (char.isdigit() for char in password):
        score += 1
        x += 1
    if any(char in string.punctuation for char in password):
        score += 1
        x += 1

    if(x < 4):
        return score

    #Check length
    if (len(password) >= 8):
        score += 1
    if(len(password) >= 12):
        score += 1
    if(len(password) >= 16):
        score += 1
    if(len(password) >= 20):
        score += 1

    return score

def check_password(password: str)-> None:
    #Read the list ofcommon passwords from the file
    with open("common_passwords.txt", "r") as f:
        common_passwords = set(f.read().splitlines())
    
    #Check if password too common
    if password in common_passwords:
        print("Password is too common. Please choose a different password.")
        return
    
    if score == 0:
        print("Password is very weak. Please choose a stronger password.")
        if x < 4:
            print("Password should contain at least one lowercase letter, one uppercase letter, one digit, and one special character.")
    elif score == 1:
        print("Password is weak. Please choose a stronger password.")
        if x < 4:
            print("Password should contain at least one lowercase letter, one uppercase letter, one digit, and one special character.")
    elif score == 2:
        print("Password is moderate. Consider choosing a stronger password.")
        if x < 4:
            print("Password should contain at least one lowercase letter, one uppercase letter, one digit, and one special character.")
    elif score == 3:
        print("Password is slightly strong. Still need to improve.")
        if x < 4:
            print("Password should contain at least one lowercase letter, one uppercase letter, one digit, and one special character.")
    elif score == 4:
        print("Password is strong. Good job!")
        if x < 4:
            print("Password should contain at least one lowercase letter, one uppercase letter, one digit, and one special character.")
    else:
        print("Password is very strong. Excellent choice!")

while True:
    password = input("Enter a password to check its strength (or type 'exit' to quit): ")
    if password.lower() == "exit":
        break
    score = check_password_strength(password)
    check_password(password)