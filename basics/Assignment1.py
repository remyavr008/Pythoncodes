a=int(input("Enter Number1- "))
b=int(input("Enter Number2- "))
#a)basic calculator operations
sum = a + b
dif = a - b
mul = a * b
div = a/b
mod = a%b
print("Sum is ",sum)
print("Difference is",dif)
print("Product is",mul)
print("Division is",div)
print("Modulus is", mod)

#b)Check first number is greater or lesser
if a>b:
    print("First number is greater",a)
elif a<b:
    print("First number is lesser",a)
else:
    print("Both numbers are equal")