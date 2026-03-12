#empty set
set1={}
print(set1)

#set
set2={11,3,2,7,9,5}
print(set2)

#link set and list
list1=[2,"four",3,6]
set2.update(list1)
print(set2)

tuple1=("python", "java","CPP")
set2.add(tuple1)
print(set2)

set3={8,9,4,6,2,1,0,12}
#print(sorted(set3))

#frozen set
x=frozenset(set3)
print("x is",x)
print(sorted(x))
"""x.add(49) #Not able to add in frozen set
print(x)
"""
#set2.clear()
#print(set2)