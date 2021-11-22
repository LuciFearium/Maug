import os
my_secret = os.environ['password']
while input("Please input password : ") != my_secret:
    print("Password invalid")
print("Password is correct")



