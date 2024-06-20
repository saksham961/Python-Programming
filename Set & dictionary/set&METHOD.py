collection={3,4,5,6,"hello","HI",99.4,3}
print(type(collection ))
print(collection)


collection= set()#null set
print(type(collection))

#set Method

collection={2,3,4,5}
collection.add(6)
collection.add("world")
collection.remove(3)
collection.add(88.77)
#collection.clear() 

print(len(collection))
print(collection.pop())#random eliment

set1={2,4,7,77.88}
set2={3,5,7,"hello"}
print(set1.union(set2))

set1={1,2,3,4}
set2={4,5,3,7,8}
print(set1.intersection(set2))