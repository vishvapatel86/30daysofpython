#day 11 : functions

#exercise 1
#1
def add_two_numbers(a, b):
    return a + b

# Example usage:
print(add_two_numbers(5, 7))  
print(add_two_numbers(-3, 10))

#2
import math

def area_of_circle(r):
    return math.pi * r * r

# Example usage:
print(area_of_circle(5)) 

#3
def add_all_nums(*args):
    # Check if all items in the arguments are int or float
    for item in args:
        if not isinstance(item, (int, float)):
            return f"Error: All items must be numbers. Found invalid type '{type(item).__name__}' for value: {item}"
    
    # If all items are valid, return the sum
    return sum(args)

# Example usage:
print(add_all_nums(1, 2, 3, 4.5))       
print(add_all_nums(1, "two", 3))       
print(add_all_nums(1, [2, 3]))         

#4
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Example usage:
print(convert_celsius_to_fahrenheit(25))

#5
def check_season(month):
    month = month.strip().capitalize()
    
    if month in ["December", "January", "February"]:
        return "Winter"
    elif month in ["March", "April", "May"]:
        return "Spring"
    elif month in ["June", "July", "August"]:
        return "Summer"
    elif month in ["September", "October", "November"]:
        return "Autumn"
    else:
        return "Invalid month entered"

# Example usage:
print(check_season("march"))

#6
def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        raise ValueError("Slope is undefined for vertical lines (division by zero).")
    return (y2 - y1) / (x2 - x1)

# Example usage:
print(calculate_slope(1, 2, 3, 4))


def solve_quadratic_eqn(a, b, c):
    """
    Calculates the solution set of a quadratic equation ax^2 + bx + c = 0.
    """
    # Check if it's a valid quadratic equation
    if a == 0:
        if b == 0:
            return () if c != 0 else ("Infinite solutions",)
        return (-c / b,)

    # Calculate the discriminant
    discriminant = b**2 - 4*a*c

    # Two real solutions
    if discriminant > 0:
        x1 = (-b + discriminant**0.5) / (2 * a)
        x2 = (-b - discriminant**0.5) / (2 * a)
        return (x1, x2)
    
    # One real solution (double root)
    elif discriminant == 0:
        x = -b / (2 * a)
        return (x,)
    
    # Two complex solutions
    else:
        real_part = -b / (2 * a)
        imag_part = (abs(discriminant)**0.5) / (2 * a)
        return (complex(real_part, imag_part), complex(real_part, -imag_part))

# --- Examples of use ---
print("Two real roots:", solve_quadratic_eqn(1, -5, 6))    # x^2 - 5x + 6 = 0 -> (3.0, 2.0)
print("One real root:", solve_quadratic_eqn(1, -6, 9))     # x^2 - 6x + 9 = 0 -> (3.0,)
print("Complex roots:", solve_quadratic_eqn(1, 1, 1))      # x^2 + x + 1 = 0  -> ((-0.5+0.866j), (-0.5-0.866j))
