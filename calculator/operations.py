import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        print("Error: Division by zero.")
        return None
    return x / y

def exponentiate(x, y):
    return x ** y

def sqrt(x):
    if x < 0:
        print("Error: Cannot calculate square root of a negative number.")
        return None
    return math.sqrt(x)

def modulo(x, y):
    if y == 0:
        print("Error: Division by zero for modulo operation.")
        return None
    return x % y
