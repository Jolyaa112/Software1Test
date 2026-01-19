length=int(input("Enter the length of the zander (cm): "))

if length < 42:
    difference = 42 - length
    print(f"It is {difference} cm below the size limit.")

else:
    print("The fish meets the size limit.")

#------------------------------------------ 2

cabin_class = input("Enter cabin class (LUX, A, B, C): ")

if cabin_class == "LUX":
    print("upper-deck cabin with a balcony.")

elif cabin_class == "A":
    print("above the car deck, equipped with a window.")

elif cabin_class == "B":
    print("windowless cabin above the car deck.")

elif cabin_class == "C":
    print(" windowless cabin below the car deck.")

else :
    print("invalid cabin class.")

#------------------------------------------------------------- 3

gender = input("Enter biological gender (female/male): ")
hemoglobin = int(input("Enter hemoglobin value (g/l): "))

if gender == "female":
    if hemoglobin < 117:
        print("Hemoglobin level is low.")
    elif hemoglobin > 155:
        print("Hemoglobin level is high.")
    else:
        print("Hemoglobin level is normal.")

elif gender == "male":
    if hemoglobin < 134:
        print("Hemoglobin level is low.")
    elif hemoglobin > 167:
        print("Hemoglobin level is high.")
    else:
        print("Hemoglobin level is normal.")

else:
    print("Invalid gender.")

#------------------------------------------------- 4

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("The year is a leap year.")
else:
    print("The year is not a leap year.")