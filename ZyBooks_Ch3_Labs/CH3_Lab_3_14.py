'''Given three floating-point numbers x, y, and z, output x to the power of z, x to the power of (y to the power of z), 
the absolute value of (x minus y), and the square root of (x to the power of z).'''
import math

x = float(input("Enter floating point for x: "))
y = float(input("Enter floating point for y: "))
z = float(input("Enter value for z: "))

print(f'{math.pow(x, z)}, {math.pow(x, math.pow(y,z))}, {math.fabsabs(x - y)}, {math.sqrt(math.pow(x, z))}')

