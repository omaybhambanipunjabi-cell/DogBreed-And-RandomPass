import random
import string

def generate_password(length=12):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    all_characters = lower + upper + digits
    
        random.choice(lower)
        random.choice(upper),
        random.choice(digits)
    ]

    password += random.choices(all_characters, length-3)
    
    random.shuffle(password)
    
    return "".join(password)
new_password = generate_password(14)
print(f"Your generated password is: {new_password}")