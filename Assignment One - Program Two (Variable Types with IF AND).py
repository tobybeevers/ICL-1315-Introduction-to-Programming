#import the DataTime Library and set a variable with todays date
import datetime
dateNow = datetime.datetime.now()

# I did get some help on this error function from the Devs at work, def is used to define a function
# The funtion is then called further down the code
# https://www.w3schools.com/python/python_functions.asp
def handle_invalid_date_input():
    print ()
    print("Error: Invalid date format. Please enter your Date of Birth in the format DD-MM-YYYY.")

# Create a Program that will capture a Users Age and return information about Key Events
# Ask the User to enter their DOB
print ("Would you like to know some interesting facts about your age?")
print () # Print a blank line
userAge = str(input("Enter your Date of Birth DD-MM-YYYY: ")) # Capture the Users DOB in this variable

# I did get some help on this error function from the Devs at work
# The try and except functions are used to try and catch errors
# https://www.w3schools.com/python/python_try_except.asp#:~:text=The%20try%20block%20lets%20you,when%20there%20is%20no%20error.
try:
    parsedDate = datetime.datetime.strptime(userAge, "%d-%m-%Y").date()
except ValueError:
    handle_invalid_date_input()
    exit()


# This variable stores the date after is has been converted into a usable date format using the datatime library > strptime function
# https://docs.python.org/3/library/datetime.html?highlight=datetime#module-datetime
parsedDate = datetime.datetime.strptime(userAge, "%d-%m-%Y").date()
#print (parsedDate) #Keep as debug test to see if the date is parsed correctly

#now start returning values
print () # Print a blank line
print ("So you are: ")

#Variable to store the age of the user in years
userYearsOld = dateNow.year - parsedDate.year # Calculate the Users Age in Years
print ("   * " +str(userYearsOld) + " Years Old")

#Variable to store the age of the user in days
numberOfDaysOld = (dateNow.date() - parsedDate).days # Calculate the Users Age in Days
userDaysOld = numberOfDaysOld - dateNow.day # Calculate the Users Age in Days
print ("   * That's " + str(userDaysOld) + " Days Old")

#Add some calc to use in if & and statements
if userYearsOld >= 18:
  print () # Print a blank line
  print ("And")
  print ("   * It looks like your old enough to vote!")
  print ("   * You can grab a beer at the bar!")
  print ("   * Plus you can also rent a car!")

elif userYearsOld < 18:
  userAgeCalc = 18 - userYearsOld
  print () # Print a blank line
  print ("Not quite there, only " + str(userAgeCalc) + " years until you can vote & grab a beer!")

#Add some trivia statements
print () # Print a blank line
print ("Did you know:")
print ("   * Your age in dog years is over " + str(userYearsOld * 7))
print ("   * Your age in cat years is over " + str(userYearsOld * 4))
print ("   * You probably had somewhere near " + str(round(userDaysOld / 7)) + " Sunday Lunches!")

#Add calcs about Driving ages if & and statements
print () # Print a blank line
print () # Print a blank line
print ("What about Driving:")
if userYearsOld < 16:
  print ("    * Sorry you can't start Driving just yet!")
    
elif userYearsOld >= 16 and userYearsOld <= 70:
  print ("    * Yep, you're good with driving as long as you've past your test!")

elif userYearsOld > 70:
  print ("    * Did you know you need to be retesting every three years to keep you Licence?")


exit ()






