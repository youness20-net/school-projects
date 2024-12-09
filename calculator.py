x: int = int(input("num1 : "))
oper = input("oppe : ")
y = int(input("num2 : "))

if oper == '/': 
    if y == 0:
        print("eror 404")
    else:
        print(x/y)

if oper == '+':
    print(x+y)
if oper == '-':
    print(x-y)
if oper == '*':
    print(x*y)

input("press enter tow time to live")

input()
