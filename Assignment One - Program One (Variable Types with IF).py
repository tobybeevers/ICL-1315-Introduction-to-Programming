# /This is a simple Python program to collect a users name before presenting /#
# /info about Variables. The user can select through choices using Strings and Numbers /#
# /NB extra *print ()* statments have been used to add white space into the Terminal as there is no UI /#

# Ask the User their Name, collect this into a variable called name
print () #*
name = input("What is your name? ")  
print () #* 

# Now ask the user if they would like to know about Words, Numbers or something else
print("Hello", name, "welcome to my program about Variables in Python.")
print("What would you like to learn about today?")
print() #*

# Collect user response in a new variable called userChoice1 with some validation on the String
userChoice1 = input("Type Words for Words, Numbers for Numbers, or Other for something else: ")
valid1 = '' # This variable is empty, until the user enters a value. 
            # If the users entry matches the strings correctly 
            # it will set to True and end the While loop.
while valid1 is not True:
  if userChoice1 == 'Words' or userChoice1 == 'Numbers' or userChoice1 == 'Other':
      valid1 = True
      # If the user enters the correct string then the variable will become True, 
      # if not it will loop through again
      print() #* 
  else:
      print () #* 
      print (userChoice1, "is not a valid choice.")
      print () #*
      userChoice1 = input("Type Words for Words, Numbers for Numbers, or Other for something else: ")

# These are the User choices, if the user selects "Other" then they will be asked to 
# enter a new variable called userChoice2 which will enter the Nested If's
      
# This is the user selection for Words, it tells the user about using Strings in Python
if userChoice1 == "Words":
      print ("You have selected to know more about Words, known as Strings or Text in Python!")
      print () #*
      print ("Strings in python are surrounded by either single quotation marks, or double quotation marks.")
      print ("'Hello' is the same as \"hello\" You can display a string literally with the print() function")
      print ("A str can be letters of numbers but it's important to understand that numbers")
      print ("stored in str can not be calculated!")
      print () #*

# This is the user selection for Numbers, it tells the user about numbers in Python
elif userChoice1 == "Numbers":
      print ("You have selected to know more about Numbers in Python!")
      print () #*
      print ("Numbers can be Integers, Floating Point Numbers, or Complex Numbers")
      print () #*
      print (" - Int, or integer, is a whole number, positive or negative, without decimal.")
      print (" - Float, or \"floating point number\" is a number, positive or negative,")
      print ("   containing one or more decimals.")
      print (" - Complex is an advanced number, which take a real number and an imaginary number.")
      print () #*

# This the user slection for Other, this opens a Nest If with a While Loop.
# the user is asked to select further from 1,2,3,4 to find out more
else: 
      print ("You have selected to know more about something else in Python!")
      print () #*
      print ("Enter 1 to understand Sequence Types")
      print ("Enter 2 to understand Mapping Types")
      print ("Enter 3 to understand Set Types")
      print ("Enter 4 to understand Boolean Types")
      print () #* 
  
      # Nested If with a While Loop
      userChoice2 = input("Enter Your Selection between 1-4: ")
      valid2 = '' 
      
      # While Loop is used to validate the variable userChoice2
      # isdigit() is a built-in method for strings that returns True if all characters in the string are digits (numeric characters 0 to 9), or False
      while valid2 is not True:   
        if userChoice2.isdigit() and 1 <= int(userChoice2) <= 4:
            valid2 = True
        else: 
            print () #*
            print(userChoice2, "is not a valid choice. Please try again.")
            print () #*
            userChoice2 = input("Enter Your Selection between 1-4: ")
        # These are the user choices if the user has selected Other > 1 or 2 or 3 or 4
         
      # This Variable is Casting the data in the Variable userChoice2 to an Interger
      userChoice2 = int(userChoice2)
      
      # This is the user selection for Sequence type 
      if userChoice2 == 1: 
          print () #* 
          print ("Thanks", name, "you selected", userChoice2)
          print ("So you want to know more about Sequence Types in Python!")
          print () #*
          print ("An advanced data type, the sequence data type in Python is used to store")
          print ("sequential data. The sequence data type in python can be considered")
          print ("as a container that can store different data.")
          print () #*

        # This is the user selection for Mapping type     
      elif  userChoice2 == 2: 
          print () #* 
          print ("Thanks", name, "you selected", userChoice2)
          print ("So you want to know more about Mapping Type in Python!")
          print () #*
          print ("An advanced data type, a mapping type is a data type comprised of a collection")
          print ("of keys and associated values. Python's only built-in mapping type is the")
          print ("dictionary. Dictionaries implement the associative array abstract data type.")
          print () #*
                
        # This is the user selection for Sets, List & Tuples 
      elif userChoice2 == 3:
          print () #* 
          print ("Thanks", name, "you selected", userChoice2)
          print ("So you want to know more about Sets Types in Python!")
          print () #*
          print ("Sets, Tuples & Lists are all similar in that they are ordered collections of data")
          print (" - A Set is a collection of unique values stored in a single variable.")
          print ("   A Set is a collection which is unordered, unchangeable, and unindexed.")
          print () #*
          print (" - A Tuple is a collection of values that are ordered.")
          print ("   A Tuple is a collection which is ordered, unchangeable, and indexed.")
          print () #*  
          print (" - A List is a collection of values that are ordered and change.")
          print ("   A List is a collection which is ordered, changeable, and indexed.")
          print () #*

        # This is the user selection for Boolean type 
      elif userChoice2 == 4:
          print () #* 
          print ("Thanks", name, "you selected", userChoice2)
          print ("So you want to know more about Boolean Type in Python!")
          print () #*
          print ("In programming you often need to know if an expression is True or False,")
          print ("You can evaluate any expression in Python, and get either, True or False.")
          print ("When you compare two values, the expression is evaluated and")
          print ("Python returns the Boolean answer.")
          print () #*
        

# The program will now ask the user if they would like to continue, this sets a Variable to Run or End the program. 
# If the user enter a value that is not Yes or No (and see or statements), the While Loop will continue until the user enters the correct value.
          
# If the User enters YES the Variable is not used and the Program will use the exec and run again 
# If the user enters NO the variable runEnd is set to True and will use exit
          
runEnd = ''
while runEnd is not True:
  runEnd = input("Would you like to run this program again? ")
  if runEnd == "No" or runEnd == "no" or runEnd == "N" or runEnd == "n":
    runEnd = True
    print ("Thanks for using my Program")
    exit ()
  elif runEnd == "Yes" or runEnd == "yes" or runEnd == "Y" or runEnd == "y":
    print ("Lets Go again")
    exec(open("Assignment One - Program One (Variable Types with IF).py").read())
    # The exec starment will need to contain the file name with .py as the extention
  else:
    print () #*
    print(runEnd, "is not a valid choice. Please try again.")
    runEnd = '' # This empty's the Variable to NULL so the While Loop will run again