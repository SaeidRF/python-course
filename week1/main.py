from math import pi

def area_circle(r):
    area = pi * r ** 2
    print("The area of the circle is:", area)

area_circle(float(input("Please write radius of the circle: ")))