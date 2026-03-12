#Print even numbers from 1 to 30 using for loop
for i in range(1,30):
    if i%2==0:
        print(i)

#Read number until user enters N from the prompt
while True:
    x=input("Do you want to continue Y/N")
    print(x)
    if x=="Y":
        print(input("Enter the number"))
    else:
       break





