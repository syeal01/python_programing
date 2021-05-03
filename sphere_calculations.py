# Author: Aliabbas Syed

# The Volume of a sphere with radius r is V=(4/3)3πr^3.
# The Diameter of a sphere with radius r is D=2r
# The Surface Area of a sphere with radius r is A=4πr^2
# Circumference of a sphere with radius r is C=2πr

import math

def sphere_volume(radius):
    volume = (4 / 3) * math.pi * math.pow(radius, 3)
    return volume    

def sphere_diameter(radius):
    diameter = 2 * radius
    return diameter

def sphere_surface_area(radius):
    surface_area = 4 * math.pi * math.pow(radius, 2)
    return surface_area

def sphere_circumference(radius):
    circumference = 2 * math.pi * radius
    return circumference

radius = float(input("Radius of circle? "))
print(f"Sphere of radius {radius} has a Volume of {sphere_volume(radius)}")
print(f"Sphere of radius {radius} has a Diameter of {sphere_diameter(radius)}")
print(f"Sphere of radius {radius} has a Surface Area of {sphere_surface_area(radius)}")
print(f"Sphere of radius {radius} has a Circumference of {sphere_circumference(radius)}")
