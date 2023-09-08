# triangle_web.py
from triangle_logic import triangle_type

def get_user_input():
    # Using float instead of int, float wil accept decimals
    side1 = int(input("Enter the length of side 1: "))
    side2 = float(input("Enter the length of side 2: "))
    side3 = float(input("Enter the length of side 3: "))
    return side1, side2, side3

def display_triangle_type(side1, side2, side3):
    result = triangle_type(side1, side2, side3)
    print(f"The triangle is of type: {result}")

if __name__ == "__main__":
    side1, side2, side3 = get_user_input()
    display_triangle_type(side1, side2, side3)