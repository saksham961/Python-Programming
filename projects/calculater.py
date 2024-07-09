def calc_sum():
    a = int(input("enter first number :"))
    b = int(input("enter second number :"))
    c = int(input("enter 1 for addition ,enter 2 for substraction ,enter 3 for multipiction,enter 4 for divid:"))

    if c == 1:
        print(a+b)
    elif c == 2 :
        print(a-b)
    elif c == 3:
        print(a*b)
    elif c == 4:
        print(a/b)
    else:
        print("Invalid operater enter 1,2,3,4,5")

        calc_sum()

calc_sum()



