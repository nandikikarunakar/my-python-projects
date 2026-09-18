import random
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

numbers = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
]

symbols = [
    '!', '#', '$', '%', '&', '(', ')', '*', '+'
]

print("Welcome to the PyPassword Generator!")
user_letter = int(input("How many letters Would you like in your password? "))
user_number = int(input("How many numbers Would you like? "))
user_symbol = int(input("How many symbols Would you like? "))

#Easy level
# password = ""
# for char in range(0, user_letter):
#     password += random.choice(letters)

# for char in range(0, user_number):
#     password += random.choice(numbers)

# for char in range(0, user_symbol):
#     password += random.choice(symbols)

# print(password)


#Hard level --> order suffle
password_list = []
for char in range(0, user_letter):
    password_list += random.choice(letters)

for char in range(0, user_number):
    password_list += random.choice(numbers)

for char in range(0, user_symbol):
    password_list += random.choice(symbols)

# print(password)

random.shuffle(password_list)

# print(password)
password = ""
for char in password_list:
    password += char
print(password)