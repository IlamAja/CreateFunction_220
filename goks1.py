def convert_temperature(value, unit):
    if unit.upper() == 'C':
        return (value * 9/5) + 32, 'F'
    elif unit.upper() == 'F':
        return (value - 32) * 5/9, 'C'
    else:
        raise ValueError("Invalid unit. Please provide 'C' for Celsius or 'F' for Fahrenheit.")

# Input
temperature = float(input("Enter the temperature value: "))
unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ")

# Output
converted_value, converted_unit = convert_temperature(temperature, unit)
print(f"The converted temperature is: {converted_value:.2f} {converted_unit}")