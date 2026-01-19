'''1'''

import random

def roll_dice():
    return random.randint(1, 6)

result = 0

while result != 6:
    result = roll_dice()
    print(result)

'''2'''

import random

def roll_dice(sides):
    return random.randint(1, sides)

sides = int(input("Enter the number of sides on the dice: "))

result = 0

while result != sides:
    result = roll_dice(sides)
    print(result)


'''3'''

def gallons_to_litres(gallons):
    return gallons * 3.785

gallons = float(input("Enter the amount of gasoline in gallons: "))

while gallons >= 0:
    litres = gallons_to_litres(gallons)
    print("Litres:", litres)

    gallons = float(input("Enter the amount of gasoline in gallons: "))


'''4'''

def sum_list(numbers):
    total = 0
    for i in numbers:
        total = total + i
    return total

numbers = [1, 2, 3, 4, 5]

print(sum_list(numbers))


'''5'''

def remove_uneven(numbers):
    even_numbers = []

    for n in numbers:
        if n % 2 == 0:
            even_numbers.append(n)

    return even_numbers

original_list = [1, 2, 3, 4, 5, 6, 7, 8]

new_list = remove_uneven(original_list)

print("Original list:", original_list)
print("Even numbers only:", new_list)


'''6'''

import math

def pizza_unit_price(diameter, price):
    radius = diameter / 2
    area = math.pi * radius * radius
    unit_price = price / area
    return unit_price


diameter1 = float(input("Enter the diameter of the first pizza (cm): "))
price1 = float(input("Enter the price of the first pizza (€): "))

diameter2 = float(input("Enter the diameter of the second pizza (cm): "))
price2 = float(input("Enter the price of the second pizza (€): "))

unit1 = pizza_unit_price(diameter1, price1)
unit2 = pizza_unit_price(diameter2, price2)

if unit1 < unit2:
    print("The first pizza gives better value for money.")
else:
    print("The second pizza gives better value for money.")