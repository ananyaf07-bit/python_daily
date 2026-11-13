import re
text="I have 2 cats,3 dogs and 15 birds."
num=re.findall(r"\d+",text)
print(num)

text2 = "Python is very powerful"
sep=re.findall(r"\w+",text2)
print(sep)

text3 = "I love Java. Java is powerful."
change=re.sub("Java","Python",text3)
#print(text3)
print(change)

print("\nPHONE NUMBER VALIDATOR\n")
phone_number=input("Enter a phone number:")
if re.fullmatch(r"\d{10}",phone_number):
    print("Valid Phone Number")
else:
    print("Invalid Phone Number")

print("\nEMAIL VALIDATOR\n")
email=input("Enter a email:")
pattern=r"^[\w.-]+@[\w.-]+\.\w+$"

if re.fullmatch(pattern,email):
    print("Valid Email")
else:
    print("Invalid Email")

print("\nPASSWORD VALIDATOR\n")
password=input("Enter a password")
validate=r"\w+">=8 and r"\d"==True
if re.fullmatch(validate,password):
    print("Valid Password")
else:
    print("Invalid password")

