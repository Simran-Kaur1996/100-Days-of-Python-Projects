#For Loops,Range and Code Blocks

'''
for item in list_of_items:
    #Do something to each item

for i in range(1,5):
    print(i)
'''
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

#create a Password Generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
passwordList = []

#Easy Level

for char in range(1, nr_letters + 1):
    random_letter = random.choice(letters)
    passwordList.append(random_letter)

for char in range(1, nr_symbols + 1):
    random_s = random.choice(symbols)
    passwordList.append(random_s)

for char in range(1, nr_numbers + 1):
    random_n = random.choice(numbers)
    passwordList.append(random_n)

random.shuffle(passwordList)
password = "".join(passwordList)
print(f"Your password is: {password}")








