movies=[]
mov1=input("enter 1st movie:")
mov2=input("enter 2nd movie:")
mov3=input("enter 3rd movies:")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)


list1=[1,2,3,2,1]
list2=[1,2,3]
copy_list1=list1.copy()
copy_list1.reverse()

if(copy_list1==list1):
    print("palindrome")
else:
    print("NOT palindrome")



grade=["c","D","A","A","B","B","A"]
print(grade.count("A"))



grade=["c","D","A","A","B","B","A"]
grade.sort()
print(grade)