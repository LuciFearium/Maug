import os
my_secret = os.environ['password']
while input("Please input password : ") != my_secret:
    print("Password invalid")
print("Password is correct")



print("Hello! Welcome to MaugBot! I am a virtual chatbot for your enjoyment!")

print("With MaugBot, we have a few options! The first option is an Echo Bot! I will simply Echo what you say.")

echoWord = input("What you like me to repeat?")

print("You said: " + echoWord)