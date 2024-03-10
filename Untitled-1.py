print("Program to find gcd")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a >= b:
    max_num = a
    div = b
else:
    max_num = b
    div = a

while div != 0:
    temp = max_num
    max_num = div
    div = temp % div

print(f"The greatest common divisor (gcd) is {max_num}")
