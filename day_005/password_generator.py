import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
print("Choose your password mode:")
print("1 - Easy Level (ordered password)")
print("2 - Hard Level (shuffled password)")

# Escolha do modo
mode = int(input("Enter your choice (1 or 2):\n"))

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

if mode == 1:
    # Easy Level
    password = ""

    for char in range(0, nr_letters):
        password += random.choice(letters)

    for char in range(0, nr_symbols):
        password += random.choice(symbols)

    for char in range(0, nr_numbers):
        password += random.choice(numbers)

    print(f"Your Easy Level password is: {password}")

elif mode == 2:
    # Hard Level
    password_list = []

    for char in range(0, nr_letters):
        password_list.append(random.choice(letters))

    for char in range(0, nr_symbols):
        password_list.append(random.choice(symbols))

    for char in range(0, nr_numbers):
        password_list.append(random.choice(numbers))

    random.shuffle(password_list)

    password = "".join(password_list)
    print(f"Your Hard Level password is: {password}")

else:
    print("Invalid choice! Please restart the program and choose either 1 or 2.")
