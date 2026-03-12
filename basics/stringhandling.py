#stringhandling- Collection of or sequence of characters
message='this IS a sample message'
"""print(message[-1]) #displays from right
print(message[0]) #displays from left"""
length = len(message)
"""for i in range(length):
    print(message[i])
#slicing
print(message[1:5])
print(message[:5]) #start from 0

#concatination
greeting='heloo ' + message
print(greeting)

#case changing
print(message.upper())
print(message.capitalize()) #First character capital
print(message.lower())
print(message.title()) #each word first letter in capital"""

"""#Searching
print("this" in message)
print("title" in message)"""

#replacing
msg = message.replace("this","that")
print(msg)