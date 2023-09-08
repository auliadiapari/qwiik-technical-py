# triangle_logic.py

def triangle_type(side1, side2, side3):
    # Check equations of quilateral triangle
    if side1 == side2 == side3:
        return "Equilateral"
    # Check equations of isosceles triangle
    elif side1 == side2 or side1 == side3 or side2 == side3:
        return "Isosceles"
    # Check equations of sclene triangle
    else:
        return "Scalene"
