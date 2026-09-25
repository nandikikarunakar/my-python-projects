print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Enter your choice: ")

if choice == "1":
    celsius = float(input("Enter temperature in Celsius: "))

    fahrenheit = (celsius * 9/5) + 32

    print("Temperature in Fahrenheit:", fahrenheit)

elif choice == "2":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))

    celsius = (fahrenheit - 32) * 5/9

    print("Temperature in Celsius:", celsius)

else:
    print("Invalid choice")