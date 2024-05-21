from datetime import datetime  # Import the datetime module

def getInput():
    retirementAge = 86  # Define retirement age
    name = input('Name: ')  # Get user's name
    surname = input("Surname: ")  # Get user's surname
    
    # Loop until valid birth date is provided
    while True:
        birthDateInput = input("Birth date (DD-MM-YYYY): ")  # Get user's birth date
        try:
            birthDate = datetime.strptime(birthDateInput, "%d-%m-%Y")  # Parse birth date string to datetime object
            currentDate = datetime.now()  # Get current date and time
            age = currentDate.year - birthDate.year - ((currentDate.month, currentDate.day) < (birthDate.month, birthDate.day))  # Calculate age
            if age >= 0:
                break  # Break the loop if age is valid
            else:
                print("Invalid birth date! Please enter a valid date.")
        except ValueError:
            print("Invalid date format! Please enter date in DD-MM-YYYY format.")
    
    # Loop until valid number of years to add is provided
    while True:
        addYears = input('Add years: ')  # Get number of years to add
        try:
            addYears = int(addYears)
            if addYears >= 0:
                break  # Break the loop if years to add is valid
            else:
                print("Years to add have to be a positive number!")
        except ValueError:
            print("Years to add have to be an integer!")
    
    return name, surname, age, retirementAge, addYears  # Return user input as tuple

# Function to determine status based on age and retirement age
def setAnswer(retirementAge, addYears):
    totalYears = age + addYears
    if totalYears > retirementAge:
        return "in retirement age"
    elif totalYears < 19:
        return "underaged"
    else:
        return "in productive age"

# Function to determine word style (singular or plural) based on number of years
def setWordStyle(years):
    return "year" if years == 1 else "years"

# Main program
name, surname, age, retirementAge, addYears = getInput()  # Get user input
status = setAnswer(retirementAge, addYears)  # Determine status
word1 = setWordStyle(age)  # Determine word style for current age
word2 = setWordStyle(addYears)  # Determine word style for years to add
word3 = setWordStyle(age + addYears)  # Determine word style for total age after adding years

# Print formatted output
print(f"{name} {surname} is {age} {word1} old. {name} will be {status} at {age + addYears} {word3} old after adding {addYears} {word2}.")
