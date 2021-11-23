import os
my_secret = os.environ['password']
while input("Please input password : ") != my_secret:
    print("Password invalid")
print("Password is correct")

def echo():
  echoWord =  input("What would you like me to repeat?\n")
  print("You said: " + echoWord)

global done
done = 0
global loop
loop = 0

print("Hello! Welcome to MaugBot! I am a virtual chatbot for your enjoyment!")

print("With MaugBot, we have a few options! The first option is an Echo Bot! I will simply Echo what you say.")

def menu():
  selection = input("What option would you like to select? Echo bot, Coming Soon\n")
  return selection


#def userChoice(selection):
#  switcher = {
#
#    echo
#
#  }

while loop == 0:
  selection = menu()
  if selection.lower() == "echo bot":
    while done == 0:
      echo()
      again = input("Would you like to try again?\n")
      if again.lower() == "no":
        done = 1
      elif again.lower() == "yes":
        done = 0
      else:
        print("I'm sorry, I misunderstood you! I'm going to assume you would like to try again!")
  elif selection.lower() == "coming soon":
    print("We have many cool features prepared and being worked on! Please feel free to return and check them out later.")
  else:
    print("I'm sorry, I didn't understand your request. Please try select a new option!")
  #print("Output of variable 'selection' is:" + selection)


print("We have arrived at the end of our Chatbot Capabilities! Thank you for trying out Maug.")