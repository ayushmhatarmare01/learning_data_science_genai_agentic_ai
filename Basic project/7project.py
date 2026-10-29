#Login security simulation.
# Store a correct username and password in variables. 
# Ask the user to enter both.
# If both match, print Login successful.
# If the username matches but password doesn't, print Wrong password.
# Otherwise, print Unknown username.
username=input("Enter the username : ")
if username!="Ayush":
    print("Unknown username")
elif username=="Ayush" :
    password=input("Enter the password : ")
    if password=="ABC":
        print("Login Successfully")
    else:
        print("Wrong password")