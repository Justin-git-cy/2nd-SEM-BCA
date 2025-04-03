def temperature_converter():
    print("Temperature Converter")
    choice = input("Convert (C to F) or (F to C)? ").strip().upper()

    if choice == "C TO F":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is {fahrenheit}°F")
    elif choice == "F TO C":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F is {celsius}°C")
    else:
        print("Invalid choice!")

temperature_converter()
