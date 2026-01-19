number = 1
while number <= 1000:
    if number % 3 == 0:
        print(number)
    number += 1

#____________________________________2

inches = 0

while True:
    inches = float(input("Enter length in inches (negative to quit): "))

    if inches < 0:
        break

    centimeters = inches * 2.54
    print("In centimeters:", centimeters)

#___________________________________3

smallest = None
largest = None

while True:
    text = input("Enter a number (empty to quit): ")

    if text == "":
        break

    number = float(text)

    if smallest is None or number < smallest:
        smallest = number

    if largest is None or number > largest:
        largest = number

print("Smallest number:", smallest)
print("Largest number:", largest)


#___________________________________4

import random

secret = random.randint(1, 10)
guess = 0

while guess != secret:
    guess = int(input("Guess a number between 1 and 10: "))

    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
    else:
        print("Correct!")

#___________________________________5

correct_username = "python"
correct_password = "rules"

attempts = 0

while attempts < 5:
    username = input("Username: ")
    password = input("Password: ")

    if username == correct_username and password == correct_password:
        print("Welcome")
        break
    else:
        print("Incorrect credentials")
        attempts = attempts + 1

if attempts == 5:
    print("Access denied")

#________________________________________6

import random

n = int(input("How many random points? "))
inside = 0
total = 0

while total < n:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x * x + y * y < 1:
        inside = inside + 1

    total = total + 1

pi = 4 * inside / n
print("Approximation of pi:", pi)