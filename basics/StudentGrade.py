x=int(input("Enter the students mark"))
if x>90:
    print(" Grade is A")
elif (x<=89) and (x>=75):
    print("Grade is B")
elif (x<=74) and (x>=50):
    print("Grade is C")
elif (x<=49) and (x>=35):
    print("Grade is D")
else:
    print("Failed")
