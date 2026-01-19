seasons = ("winter", "spring", "summer", "autumn")

month = int(input("Enter month number (1-12): "))

if 1 <= month <= 12:

    index = (month % 12) // 3
    print(seasons[index])
else:
    print("Invalid month number.")

"_______________-2"

names = set()

while True:
    name = input("Enter name (empty to stop): ")
    if name == "":
        break

    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)

print("Names entered:")
for n in names:
    print(n)


"__________________3"

airports = {}

while True:
    print("\nChoose an option:")
    print("1 = Enter new airport")
    print("2 = Fetch airport information")
    print("3 = Quit")

    choice = input("Your choice: ")

    if choice == "1":
        icao = input("Enter ICAO code: ").strip().upper()
        name = input("Enter airport name: ").strip()
        airports[icao] = name
        print(f"Saved: {icao} -> {name}")

    elif choice == "2":
        icao = input("Enter ICAO code: ").strip().upper()
        if icao in airports:
            print(f"{icao}: {airports[icao]}")
        else:
            print("Airport not found.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please choose 1, 2, or 3.")

