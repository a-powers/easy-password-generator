import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Super Safe Password Generator!")
print("Follow the prompts to make your password simple or complex.")
print("")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


random_chars = []
for char in range(1, nr_letters + 1):
    random_chars += random.choice(letters)

for char in range(1, nr_symbols + 1):
    random_chars += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    random_chars += random.choice(numbers)

random.shuffle(random_chars)


pswrd = ""
for i in random_chars:
    pswrd += i


print(f"Your random generated password is {pswrd}.")


