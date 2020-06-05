def is_on_line(slope, y_int, px, py):
  if (py== ((slope*px) +y_int)):
    print("is_on_line: True")
  else:
    print("is_on_line: false")
    
slope=int(input("Enter slope:"))
y_int=int(input("Enter y_intercept"))
px=int(input("Enter px:"))
py=int(input("Enter py:"))
print(is_on_line(slope, y_int, px, py))

