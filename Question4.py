a=float(input("Enter the number a: "))
s=input("Enter the operation sign(+,-,*,/): ")
b=float(input("Enter the number b: "))
z=a+b
y=a-b
x=a/b
w=a*b

if s=="+":
    print(z)
elif s=="-":
    print(y)
elif s=="*":
    print(w)
else:
    print(x)