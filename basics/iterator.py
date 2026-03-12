list1=[1,2,5,8,10]
length=len(list1)
i=1

iterator=iter(list1) #iter is a keyword that is used to initialize iterator
while i<=length:
    print(next(iterator))
    i=i+1
"""print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))"""
#print(next(iterator))

