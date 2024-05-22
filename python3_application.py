import sqlite3
from datetime import datetime  # Import the datetime module

class retirementCalculator:
    def __init__(self):
        self.retirementAge = 86  # Define retirement age
        self.name = ""
        self.surname = ""
        self.age = 0
        self.addYears = 0
        self.birth_date = ""
        self.memory_conn = sqlite3.connect(':memory:')  # Temporary in-memory database
        self.file_conn = sqlite3.connect('retirement_data.db')  # Permanent file-based database
        self.createTable(self.memory_conn)
        self.createTable(self.file_conn)

    def createTable(self, conn):
        # Create a table to store user information
        with conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    surname TEXT NOT NULL,
                    birth_date TEXT NOT NULL,
                    add_years INTEGER NOT NULL
                )
            ''')  

    def checkExistingFile(self):
        cursor = self.file_conn.cursor()
        cursor.execute('SELECT name, surname, birth_date, add_years FROM users ORDER BY id DESC LIMIT 1')
        row = cursor.fetchone()
        if row:
            # Display the fetched data to the user
            name, surname, birth_date, add_years = row
            print(f"Found existing data: Name: {name.capitalize()}, Surname: {surname.capitalize()}, Birth date: {birth_date}, Add years: {add_years}")

            # Ask if the user wants to autofill the data
            autofill = input("Do you want to autofill from existing data? (yes/no): ").lower()
            if autofill == "yes":
                # Autofill the fields with the fetched data
                self.name, self.surname, self.birth_date, self.addYears = row
                self.name = self.name.capitalize()
                self.surname = self.surname.capitalize()
                print("Autofilled data successfully.")         
    
    def insertUser(self, conn):
        # Insert user information into the specified table
        with conn:
            conn.execute('''
                INSERT INTO users (name, surname, birth_date, add_years)
                VALUES (?, ?, ?, ?)
            ''', (self.name, self.surname, self.birth_date, self.addYears))
    
    def getInput(self):
        # Call method to check for existing file
        self.checkExistingFile()

        # If name is not filled, ask for input
        if not self.name:  
            self.name = input('Name: ').strip().capitalize()  # Get user's name and capitalize the first letter

        # If surname is not filled, ask for input
        if not self.surname:  
            self.surname = input("Surname: ").strip().capitalize()  # Get user's surname and capitalize the first letter
        
        # If birth date is not filled, ask for input
        if not self.birth_date:  
            # Loop until valid birth date is provided
            while True:
                birthDateInput = input("Birth date (DD-MM-YYYY): ")  # Get user's birth date
                try:
                    birthDate = datetime.strptime(birthDateInput, "%d-%m-%Y")  # Parse birth date string to datetime object
                    self.birth_date = birthDateInput  # Store the birth date string
                    currentDate = datetime.now()  # Get current date and time
                    self.age = currentDate.year - birthDate.year - ((currentDate.month, currentDate.day) < (birthDate.month, birthDate.day))  # Calculate age
                    if self.age >= 0:
                        break  # Break the loop if age is valid
                    else:
                        print("Invalid birth date! Please enter a valid date.")
                except ValueError:
                    print("Invalid date format! Please enter date in DD-MM-YYYY format.")
        
        # If addYears is not filled, ask for input
        if not self.addYears:
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
    
        # Ask user where to save the data
        while True:
            save_location = input("Where do you want to save the data? (file/memory): ").lower()
            if save_location in ["file", "memory"]:
                break
            else:
                print("Invalid choice! Please enter 'file' or 'memory'.")

        # Insert the user data into the chosen database
        if save_location == "file":
            self.insertUser(self.file_conn)
        else:
            self.insertUser(self.memory_conn)

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

        # Query and print all user data from the in-memory database
        print("Data from in-memory database:")
        cursor = self.memory_conn.cursor()
        cursor.execute('SELECT * FROM users')
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        # Query and print all user data from the file-based database
        print("Data from file-based database:")
        cursor = self.file_conn.cursor()
        cursor.execute('SELECT * FROM users')
        rows = cursor.fetchall()
        for row in rows:
            print(row)

# This block ensures that the main function is called only when the script is run directly
if __name__ == "__main__":
    calculator = retirementCalculator()
    calculator.run()
