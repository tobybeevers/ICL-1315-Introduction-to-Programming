#Create a print statement to direct the user to select from the list of choices 1, 2, 3, or 4 etc
print ("Select a Variable Type from this list to get started:")
print () #added an empty print statement to add a space 
print ("1 to understand more about Numeric Types,")
print ("2 to understand Text,")
print ("3 to understand Sequence Types,")
print ("4 to understand Mapping Types,")
print ("5 to understand Set Types ")
print ("6 to understand Boolean Types")
print ("7 to understand List & Tuple Types")
print () #added an empty print statement to add a space 

#Create a variable to store the user's choice, force and integer value
userChoice = int(input("Enter Your Selection between 1-7: "))

print () #added an empty print statement to add a space 

#Add the if & elif, print statement to display the user's choice and add else to capture incorrect User Selection
if userChoice == 1: #Numbers
  print ("You have selected to know more about Numbers in Python!")
  print () #added an empty print statement to add a space
  print ("Numbers can be Integers, Floating Point Numbers, or Complex Numbers")
  print () #added an empty print statement to add a space
  print (" - Int, or integer, is a whole number, positive or negative, without decimal.")
  print (" - Float, or \"floating point number\" is a number, positive or negative,")
  print ("   containing one or more decimals.")
  print (" - Complex is an advanced number, which take a real number and an imaginary number.")


elif userChoice == 2: #Text
  print ("You have selected to know more about Strings also know as Text in Python!")
  print() #added an empty print statement to add a space
  print ("Strings in python are surrounded by either single quotation marks, or double quotation marks.")
  print ("'Hello' is the same as \"hello\" You can display a string literally with the print() function")
  print ("A str can be letters of numbers but it's important to understand that numbers")
  print ("stored in str can not be calculated!")


elif userChoice == 3: #Sequence Types
  print ("You have selected to know more about Sequence Types in Python!")
  print () #added an empty print statement to add a space
  print ("An advanced data type, the sequence data type in Python is used to store")
  print ("sequential data. The sequence data type in python can be considered")
  print ("as a container that can store different data.")
  

elif  userChoice == 4: #Mapping Types
  print ("You have selected to know more about Mapping Type in Python!")
  print () #added an empty print statement to add a space
  print ("An advanced data type, a mapping type is a data type comprised of a collection")
  print ("of keys and associated values. Python's only built-in mapping type is the")
  print ("dictionary. Dictionaries implement the associative array abstract data type.")
  

elif userChoice == 5: #Set Types Lists & Tuples
  print ("You have selected to know more about Set Types in Python!")
  print () #added an empty print statement to add a space
  print ("Sets, Tuples & Lists are all similar in that they are ordered collections of data")
  print (" - A Set is a collection of unique values stored in a single variable.")
  print ("   A Set is a collection which is unordered, unchangeable, and unindexed.")
  print () #added an empty print statement to add a space
  print (" - A Tuple is a collection of values that are ordered.")
  print ("   A Tuple is a collection which is ordered, unchangeable, and indexed.")
  print () #added an empty print statement to add a space  
  print (" - A List is a collection of values that are ordered and change.")
  print ("   A List is a collection which is ordered, changeable, and indexed.")

elif userChoice == 6: #Boolean Types
  print ("You have selected to know more about Boolean Type in Python!")
  print () #added an empty print statement to add a space
  print ("In programming you often need to know if an expression is True or False,")
  print ("You can evaluate any expression in Python, and get either, True or False.")
  print ("When you compare two values, the expression is evaluated and")
  print ("Python returns the Boolean answer")

else:
  print ("You have selected an invalid choice, your selection must be between 1-6")
  
exit()
