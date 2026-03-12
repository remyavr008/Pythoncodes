#Based on condition it works
"""str = "Hi this is Remya"
i = 0
counter = 0
#inbuilt function to find the length of a string
length = len(str)
print(length)
while i < (length):
    if str[i] == "a" or str(i) == "e" or str(i) == "i" or str(i) == "o" or str(i) == "u":
        counter += 1
    i+=1
print("no of vowels in string is ",counter)"""
#Based on condition it works
#str = "hi this is remya"
str = input(print("enter string"))
i = 0
counter = 0
#inbuilt function to find the length of a string
length = len(str)
#print(length)
while i < (length):
    if str[i] == "a" or str[i] == "e" or str[i] == "i" or str[i] == "o" or str[i] == "u":
        counter += 1

    i+=1

else:
    print("No vowels found")
print("no of vowels in string is ",counter)
