import os
import time

# Password, intended for use during development in order to lock Maug form being used without intention. #
password = os.environ['password']
while input("Please input password : ") != password:
    print("Password invalid")
print("Password is correct")

# Function to clear the console. #
def cls():
  print("\033c\033[J")

# Function to be called when wanting to add a pause. #
def wait(dur):
  time.sleep(dur)

# Function for echoing given word. #
def echo():
  echoWord =  input("What would you like me to repeat?\n")
  wait(.5)
  print("You said: " + echoWord)

# Setting some global variables, as well as option aliases. #
global done
done = 0
global loop
loop = 0
echoOptions = {"echo bot", "echo"}
comingOptions = {"coming soon"}
clear = {"clear","cls"}


# Welcome 'screen' when bot is turned on and unlocked. #
print("\nHello! Welcome to MaugBot! I am a virtual chatbot for your enjoyment!")

print("With MaugBot, we have a few options! The first option is an Echo Bot! I will simply Echo what you say.\n")

# Function to be called for the menu 'screen' where users can select options. #
def menu():
  selection = input("What option would you like to select? Echo bot, Coming Soon\n")
  wait(.2)
  return selection

# Looping the chat feature so that Bot can be used repeatedly with less code. #
while loop == 0:

  # Setting variable for whether user is finished with selected option. #
  done = 0

  # Asking user for their selection from menu options. #
  selection = menu()

  wait(.2)
  
  # User selects Echo Bot option. #
  if selection.lower() in echoOptions:
    done = 0
    while done == 0:
      echo()
      wait(1)
      repeat = input("\nWould you like to try again?\n")
      wait(.5)
      if repeat.lower() == "no":
        done = 1
      elif repeat.lower() == "yes":
        done = 0
      else:
        print("I'm sorry, I misunderstood you! I'm going to assume you would like to try again!")
    wait(.5)
  
  # User selects Coming Soon option. #
  elif selection.lower() in comingOptions:
    print("We have many cool features prepared and being worked on! Please feel free to return and check them out later.")
    wait(2)

  # User selects hidden clear console option. # 
  elif selection.lower() in clear:
    cls()
  
  # User did not input a valid option selection. #
  else:
    print("I'm sorry, I didn't understand your request. Spaces and spelling are vital, but capitalization is not!\n Please try again!")
    wait(2)

  # Print function to be enabled for debugging purposes. #
  #print("Output of variable 'selection' is:" + selection)

# User should never receive this text, but it is here in case somehow user escapes loop so that the debugger knows they escaped the loop.
print("You aren't supposed to be on this side of the code.. How did you know this was here?! Go get someone important, quick!")