def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius
temperature_fahrenheit = 68
temperature_celsius = convert_to_celsius(temperature_fahrenheit)
print(temperature_celsius)
