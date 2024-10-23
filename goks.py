import math
circle_area = lambda r: math.pi * r**2
radius = float(input("Enter the radius of the circle (jari-jari lingkaran): "))
area = circle_area(radius)
print(f"The area of the circle with radius {radius} is: {area:.2f}")
