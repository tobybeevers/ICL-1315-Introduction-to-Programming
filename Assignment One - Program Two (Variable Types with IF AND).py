# /This is simple Python program that asks a user for the Date of Birth /#
# /The DoB is then used for various calculation to present back interesting facts /#
# /NB extra *print ()* statments have been used to add white space into the Terminal as there is no UI /#

# Begin by importing the Python DataTime Library, then set a variable with todays date
import datetime
dateNow = datetime.datetime.now()

def handle_invalid_date_input():
    print()
    print("Error: Invalid date format. Please enter your Date of Birth in the format DD-MM-YYYY.")

# I did get some help on this error function from the Devs at work, however I did write 
# this code myself they just guided me as I wanted something that I hadn't used before
# def is used to define a function, the funtion is then called further down the code
# https://www.w3schools.com/python/python_functions.asp
# https://www.w3schools.com/python/python_try_except.asp#:~:text=The%20try%20block%20lets%20you,when%20there%20is%20no%20error.

# Now created another function for the main program
def main():
    # Ask the User to enter their DOB, collect this into a Variable called userAge
    print() #*
    print("Would you like to know some interesting facts about your age?")
    print() #*
    userAge = str(input("Enter your Date of Birth DD-MM-YYYY: ")) 
    
    # This function uses the Variable parseDate and collects the data from the Variable 
    # userAge before checking the date format is DD-MM-YYYY
    # This code is attempting to parse a user's date in the format "DD-MM-YYYY" using the 
    # strptime method from the datetime library. The strptime method stands for "string parse time" 
    # and is used to convert a string representation of a date into a datetime object.

    try:
        parsedDate = datetime.datetime.strptime(userAge, "%d-%m-%Y").date()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        handle_invalid_date_input()
        print() #*
        userAge = str(input("Enter your Date of Birth DD-MM-YYYY: "))
        return

    # Check for future dates
    if parsedDate > dateNow.date():
        print("You entered a future date. Please enter a valid Date of Birth that is not in the future.")
        print() #*
        return
            
    # This variable stores the date after it has been converted into a usable date format 
    # using the datatime library > strptime function
    # https://docs.python.org/3/library/datetime.html?highlight=datetime#module-datetime
    # print (parsedDate) # Keep as debug test to see if the date format is parsed correctly
    
    # Now start returning values
    print() #*
    print("So you are: ")
    
    # Variable to store the age of the user in years
    userYearsOld = dateNow.year - parsedDate.year # Calculate the Users Age in Years
    print("   * " +str(userYearsOld) + " Years Old")
    
    # Variable to store the age of the user in days
    numberOfDaysOld = (dateNow.date() - parsedDate).days # Calculate the Users Age in Days
    userDaysOld = numberOfDaysOld - dateNow.day # Calculate the Users Age in Days
    print("   * That's " + str(userDaysOld) + " Days Old")
    
    # Add some calc to use if & and statements
    if userYearsOld >= 18:
      print() #*
      print("And")
      print("   * It looks like your old enough to vote!")
      print("   * You can grab a beer at the bar!")
      print("   * Plus you can also rent a car!")
    
    else:
      userAgeCalc = 18 - userYearsOld
      print() #*
      print("Not quite there, only " + str(userAgeCalc) + " years until you can vote & grab a beer!")
    
    #Add some trivia statements
    print() #*
    print("Did you know:")
    print("   * Your age in dog years is over " + str(userYearsOld * 7))
    print("   * Your age in cat years is over " + str(userYearsOld * 4))
    print("   * You probably had something like " + str(round(userDaysOld / 7)) + " Sunday Lunches!")
    
    #Add calcs about Driving ages if & and statements
    print() #*
    print() #*
    print("What about Driving:")
    if userYearsOld < 16:
      print("    * Sorry you can't start Driving just yet!")
      print() #*
    
    elif 16 <= userYearsOld <= 70:
      print("    * Yep, you're good with driving as long as you've past your test!")
      print() #*
    
    else:
      print("    * Did you know you need to be retesting every three years to keep you Licence?")
      print() #*

# This is a While Loop to ask the user if they want to run the program again
# This checks if the Python script is being run as the main program and not imported as a module. 
#When a Python script is executed, the interpreter assigns the special variable __name__ the value "__main__" if it is the main program.
if __name__ == "__main__":
  while True:
      main()
      
      runEnd = input("Would you like to run this program again? ").lower()
      if runEnd not in {"yes", "y"}:
          print()
          print("Thanks for using my Program")
          break