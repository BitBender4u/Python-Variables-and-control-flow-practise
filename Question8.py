side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

def triangle_type(side1, side2, side3):
  if side1 == side2 == side3:
    return "equilateral"
  elif side1 == side2 or side2 == side3 or side1 == side3:
    return "isosceles"
  else:
    return "scalene"


if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
  result = triangle_type(side1, side2, side3)
  print(f"The triangle is {result}.")
else:
  print("The input values do not form a valid triangle.")