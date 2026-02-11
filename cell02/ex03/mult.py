a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

ans = a * b

print(f"{a} X {b} = {ans}")

if ans > 0:
    print("The result is positive")
elif ans < 0:
    print("The result is negative")
else:
    print("The result is positive and negative")