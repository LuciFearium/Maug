import os
import time
password = os.environ['password']
while input("Please input password : ") != password:
    print("Password invalid")
print("Password is correct")

def cls():
  print("\033c\033[J")


def wait(dur):
  time.sleep(dur)

def echo():
  echoWord =  input("What would you like me to repeat?\n")
  wait(.5)
  print("You said: " + echoWord)


global done
done = 0
global loop
loop = 0
echoOptions = {"echo bot", "echo"}
comingOptions = {"coming soon"}
clear = {"clear","cls"}

print("\nHello! Welcome to MaugBot! I am a virtual chatbot for your enjoyment!")

print("With MaugBot, we have a few options! The first option is an Echo Bot! I will simply Echo what you say.\n")

def menu():
  selection = input("What option would you like to select? Echo bot, Coming Soon\n")
  wait(.2)
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

  wait(.2)
  
  if selection.lower() in echoOptions:
    while done == 0:
      echo()
      wait(1)
      again = input("\nWould you like to try again?\n")
      wait(.5)
      if again.lower() == "no":
        done = 1
      elif again.lower() == "yes":
        done = 0
      else:
        print("I'm sorry, I misunderstood you! I'm going to assume you would like to try again!")
    wait(.5)
  
  elif selection.lower() in comingOptions:
    print("We have many cool features prepared and being worked on! Please feel free to return and check them out later.")
    wait(2)

  elif selection.lower() in clear:
    cls()
  
  else:
    print("I'm sorry, I didn't understand your request. Spaces and spelling are vital, but capitalization is not!\n Please try again!")
    wait(2)

  #print("Output of variable 'selection' is:" + selection)


print("We have arrived at the end of our Chatbot Capabilities! Thank you for trying out Maug.")