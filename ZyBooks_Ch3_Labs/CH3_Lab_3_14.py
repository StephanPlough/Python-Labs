'''Given three floating-point numbers x, y, and z, output x to the power of z, x to the power of (y to the power of z), 
the absolute value of (x minus y), and the square root of (x to the power of z).'''
import math

x = float(input("Enter floating point for x: "))
y = float(input("Enter floating point for y: "))
z = float(input("Enter value for z: "))

print(f'{math.pow(x, z):.2f}, {math.pow(x, math.pow(y,z)):.2f}, {math.fabs(x - y):.2f}, {math.sqrt(math.pow(x, z)):.2f}')

