0
#1.Take user input numbers in a loop and stope when 0
while True:
    x= int(input("Enter the number"))
    if x == 0:
        break
    else:
        print("Number is",x)


#2.Print all characters in a string expect vowels
x=input('Enter a string')
l=len(x)
vowels = ['a','e','i','o','u','A','E','I','O','U']
for i in range(l):
    if x[i] not in vowels:
        print(x[i])

#3.Print 1 to 50,skip multiples of 5 stop if number greater than 40
for i in range(1, 50):

    if i % 5 == 0:
        continue
    elif i >= 40:
        break
    else:
        print(i)

