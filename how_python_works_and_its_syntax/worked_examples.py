''' AREA OF CIRCUMFERENCE OF A CIRCLE '''


import math # Give us math.pi

radius = 7 # cm
area = math.pi * radius ** 2 # ** means 'to the power'
circumference = 2 * math.pi * radius

print("Radius:", radius, "cm")
print("Area", round(area, 2), "sq cm")
print(f"circumference: {circumference:.2f} cm")


''' TEMPERATURE CONVERSION '''

celsius = 37
fahrenhite = celsius * 9 / 5 + 32
kelvin = celsius + 273.15

print("celsius", "C =", fahrenhite, "F")
print("celsius", "C =", kelvin, "K")
