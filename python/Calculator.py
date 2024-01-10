print("Basic Calculator")

num1 = float(input("Enter a number :"))
op = input("Enter a Operator :")
num2 = float(input("Enter another number :"))

result = 0
if op=="+" :
  result = num1 + num2
elif op=="-":
  result = num1 - num2
elif op=="*":
  result = num1 * num2
elif op=="/":
  result = num1 / num2
else:
  print("Invalid operator")

print(result)