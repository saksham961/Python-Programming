info = {
    "name": "saksham",
    "class": 11,
    "age": 17,
    "marks":88.8,
    "subjects":["python","english","eco"],
    33:99.44
    
}
print(type(info))
print(info["age"])
print(info["subjects"])
print(info[33])
info["age"]=88
print(info["age"])


info["house"]=557
print(info["house"])
print(info)

#nesting

student={
     "name":"saksham",
     "subject":{
         "accounts":77,
         "Bst":78,  

     }
}
print(student["name"])