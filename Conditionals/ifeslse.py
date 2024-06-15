a=int(input("enter first number "))
b=int(input("enter second number "))
c=int(input("enter third number "))


if(a>=b and b>=a):
    print("first number is largest",a)
elif(b>=c):
    print("second numder is largest",b)
else:
    print("third number is largest",c)