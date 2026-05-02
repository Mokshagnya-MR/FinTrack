print("Hello world")
ch_name = "Mark"
ch_age = "20"
print("There was a viltrumite. His name was "+ch_name+".")
print("His age was "+ch_age+".")
num1 = float(input("Enter Number1: "))
num2 = float(input("Enter Number2: "))
op = input("Enter operation(+,-,/,*): ")
if op == "+":
    ans = num1 + num2
    print(ans)
elif op == "-":
    ans = num1 - num2
    print(ans)
elif op == "/":
    ans = num1 / num2
    print(ans)
elif op == "*":
    ans = num1 * num2
    print(ans)
else:
    print("Invalid Operation")