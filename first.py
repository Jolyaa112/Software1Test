name=str(input("Enter your name: "))
print('Hello, '+name+'!')

radius=float(input("Enter the radius of the circle: "))
circle_area=(radius**2)*3.14159

print("The area of the circle is",circle_area)

length=float(input("Enter your length of the rectangle: "))
width=float(input("Enter your width of the rectangle: "))
perimeter_rectangle=2*(length+width)
area_rectangle=length*width

print("The perimeter of the rectangle is",perimeter_rectangle)
print("The area of the rectangle is",area_rectangle)

print("Enter 3 integer numbers...")
num1=int(input("Enter your first number: "))
num2=int(input("Enter your second number: "))
num3=int(input("Enter your third number: "))

sum=num1+num2+num3
print("The sum is ",sum)
product=num1*num2*num3
print("The product is ",product)
average=sum/3
print("The average is ",average)

talents = float(input("Enter talents:\n"))
pounds = float(input("\nEnter pounds:\n"))
lots = float(input("\nEnter lots:\n"))

lots_per_pounds = 32
pounds_per_talents = 20
grams_per_lots = 13.3

total_lots = (talents *pounds_per_talents * lots_per_pounds) + (pounds * lots_per_pounds) + lots
total_grams = total_lots * grams_per_lots
kilograms = int(total_grams // 1000)
grams = total_grams % 1000

print("\nThe weight in modern units:")
print(f"{kilograms} kilograms and {grams:.2f} grams.")


import random
code3 = [random.randint(0, 9) for _ in range(3)]
code4 = [random.randint(1, 6) for _ in range(4)]

print("3-digit combination:", "".join(map(str, code3)))
print("4-digit combination:", "".join(map(str, code4)))





