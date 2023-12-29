#Create a print statement to direct the user to slect from the list of choices 1, 2, 3, or 4 etc
print ("Select a Variable Type from this list to get started:")
print ("1 for an Integer,")
print ("2 for a Float,")
print ("3 for a String,")
print ("or 4 for a Boolean,")
print () #added an empty print statement to add a space 

#Create a variable to store the user's choice, force and integer value
userChoice = int(input("Enter Your Selection between 1-4: "))

print () #added an empty print statement to add a space 

#Add the if & elif, print statement to display the user's choice and add else to capture incorrect User Selection
if userChoice == 1:
  print ("You have selected Integer,")
  print ("An Integer is a whole number and can be negative or positive")
  print ("but can't have a decimal point")
  print ("EXAMPLE 10")

elif userChoice == 2:
  print ("You have selected Float,")
  print ("a Float is a number with a decimal point and can be negative or positive")
  print ("but MUST have a decimal point")
  print ("EXAMPLE 10.8")

elif userChoice == 3:
  print ("You have selected String,")
  print ("a String is a series of letters or numbers surrounded by quotation marks,")
  print ("a number within a String can not be used in a calculation")
  print ("EXAMPLE 'Hello Word'")

elif  userChoice == 4:
  print ("You have selected Boolean,")
  print ("a boolean is a true or false value and used to represent Yes or No")
  print ("EXAMPLE True/False or 0/1")

else:
  print ("You have selected an invalid choice, your selection must be between 1 -4")
