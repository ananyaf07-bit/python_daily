username=input("Enter Username")
if(len(username.strip())>5 and username.isalnum()):
    print("Username accepted!")
elif(len(username.strip())>5):
    print("Username rejected: Only numbers and digits allowed")
else:
    print("Username rejected")