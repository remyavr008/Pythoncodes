d1={1:"apple",2:"orange",3:"mango"}
print(d1)
print(d1.get(2)) #inbuit method used to get a value from a dictionary associated with the key
print(d1[3])
#using dict method create
d2=dict(a="parrot",b="pigeon",c="crow")
print(d2)

#updation
d2['b']='e'
print(d2)

#remove
del d2['c']
print(d2)