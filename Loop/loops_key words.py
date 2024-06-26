a = 1
while a<=10:
    print(a)
    if(a==7):
        break
    a=a+1



a = 0
while a<=10:
    if(a == 6):
        a = a+1
        continue#skip
    print(a)
    a = a+1

#Odd number
a = 1
while a<=20:
    if(a%2 == 0):
        a = a+1
        continue#skip
    print(a)
    a = a+1
