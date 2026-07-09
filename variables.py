print("Assign Multiple values to multiple variables")
num1 = 10
num2 = 20
num3 = 30
print(id(num1), id(num2), id(num3))


print("Assign single value to multiple variables")
num1 = num2 = num3 = 10
print(id(num1), id(num2), id(num3))
