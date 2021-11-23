import os
import time
my_secret = os.environ['password']
while input("Please input password : ") != my_secret:
    print("Password invalid")
print("Password is correct")

def echo():
  echoWord =  input("What would you like me to repeat?\n")
  time.sleep(.5)
  print("You said: " + echoWord)

global done
done = 0
global loop
loop = 0
echoOptions = {"echo bot", "echo"}
comingOptions = {"coming soon"}

print("Hello! Welcome to MaugBot! I am a virtual chatbot for your enjoyment!")

print("With MaugBot, we have a few options! The first option is an Echo Bot! I will simply Echo what you say.")

def menu():
  selection = input("\nWhat option would you like to select? Echo bot, Coming Soon\n")
  return selection


#def userChoice(selection):
#  switcher = {
#
#    echo
#
#  }
while loop == 0:

  done = 0

  selection = menu()

  time.sleep(.2)
  
  if selection.lower() in echoOptions:
    while done == 0:
      echo()
      again = input("Would you like to try again?\n")
      time.sleep(.5)
      if again.lower() == "no":
        done = 1
      elif again.lower() == "yes":
        done = 0
      else:
        print("I'm sorry, I misunderstood you! I'm going to assume you would like to try again!")
    time.sleep(2)
  
  elif selection.lower() in comingOptions:
    print("We have many cool features prepared and being worked on! Please feel free to return and check them out later.")
    time.sleep(2)
  
  else:
    print("I'm sorry, I didn't understand your request. Spaces and spelling are vital, but capitalization is not!\n Please try again!")
    time.sleep(2)

  #print("Output of variable 'selection' is:" + selection)


print("We have arrived at the end of our Chatbot Capabilities! Thank you for trying out Maug.")