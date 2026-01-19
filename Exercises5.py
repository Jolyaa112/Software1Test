'''1'''

import random

num_dice = int(input("How many dice do you want to roll? "))

rolls = []

for i in range(num_dice):
    roll = random.randint(1, 6)
    rolls.append(roll)

total = sum(rolls)

print("Rolls:", rolls)
print("The sum of the dice is:", total)

'''2'''

numbers = []

user_input = input("Enter a number (empty string to quit): ")

while user_input != "":
    number = int(user_input)
    numbers.append(number)

    user_input = input("Enter a number (empty string to quit): ")


numbers.sort()

print("The five greatest numbers are:")

for i in range(1,6):
    print(numbers[-i])


'''3'''

number = int(input("Enter an integer: "))

for i in range(2, number):
    if number % i == 0:
        print("Not a prime number")
        break
else:
    print("Prime number")


'''4'''

cities = []

for i in range(5):
    city = input("Enter the name of a city: ")
    cities.append(city)

print("Cities:")

for city in cities:
    print(city)