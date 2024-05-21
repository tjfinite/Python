from datetime import datetime  # Import the datetime module

class retirementCalculator:
    def __init__(self):
        self.retirementAge = 86  # Define retirement age
        self.name = ""
        self.surname = ""
        self.age = 0
        self.addYears = 0
    
    def getInput(self):
        self.name = input('Name: ').strip().capitalize()  # Get user's name and capitalize the first letter
        self.surname = input("Surname: ").strip().capitalize()  # Get user's surname and capitalize the first letter
        
        # Loop until valid birth date is provided
        while True:
            birthDateInput = input("Birth date (DD-MM-YYYY): ")  # Get user's birth date
            try:
                birthDate = datetime.strptime(birthDateInput, "%d-%m-%Y")  # Parse birth date string to datetime object
                currentDate = datetime.now()  # Get current date and time
                self.age = currentDate.year - birthDate.year - ((currentDate.month, currentDate.day) < (birthDate.month, birthDate.day))  # Calculate age
                if self.age >= 0:
                    break  # Break the loop if age is valid
                else:
                    print("Invalid birth date! Please enter a valid date.")
            except ValueError:
                print("Invalid date format! Please enter date in DD-MM-YYYY format.")
        
        # Loop until valid number of years to add is provided
        while True:
            addYearsInput = input('Add years: ')  # Get number of years to add
            try:
                self.addYears = int(addYearsInput)
                if self.addYears >= 0:
                    break  # Break the loop if years to add is valid
                else:
                    print("Years to add have to be a positive number!")
            except ValueError:
                print("Years to add have to be an integer!")
    
    def setAnswer(self):
        totalYears = self.age + self.addYears
        if totalYears > self.retirementAge:
            return "in retirement age"
        elif totalYears < 19:
            return "underaged"
        else:
            return "in productive age"
    
    def setWordStyle(self, years):
        return "year" if years == 1 else "years"
    
    def run(self):
        self.getInput()  # Get user input
        status = self.setAnswer()  # Determine status
        word1 = self.setWordStyle(self.age)  # Determine word style for current age
        word2 = self.setWordStyle(self.addYears)  # Determine word style for years to add
        word3 = self.setWordStyle(self.age + self.addYears)  # Determine word style for total age after adding years

        # Print formatted output
        print(f"{self.name} {self.surname} is {self.age} {word1} old. {self.name} will be {status} at {self.age + self.addYears} {word3} old after adding {self.addYears} {word2}.")

# This block ensures that the main function is called only when the script is run directly
if __name__ == "__main__":
    calculator = retirementCalculator()
    calculator.run()
