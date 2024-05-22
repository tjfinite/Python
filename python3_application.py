import sqlite3
from datetime import datetime  # Import the datetime module

class DataStorage:
    def __init__(self, storage_type):
        self.storage_type = storage_type
        if self.storage_type == "memory":
            self.conn = sqlite3.connect(':memory:')  # Temporary in-memory database
        elif self.storage_type == "file":
            self.conn = sqlite3.connect('retirement_data.db')  # Permanent file-based database
        else:
            raise ValueError("Invalid storage type. Choose 'memory' or 'file'.")
        
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    surname TEXT NOT NULL,
                    birth_date TEXT NOT NULL,
                    add_years INTEGER NOT NULL
                )
            ''')

    def insert_user(self, name, surname, birth_date, add_years):
        with self.conn:
            self.conn.execute('''
                INSERT INTO users (name, surname, birth_date, add_years)
                VALUES (?, ?, ?, ?)
            ''', (name, surname, birth_date, add_years))

    def get_all_users(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM users')
        return cursor.fetchall()

    def close_connection(self):
        self.conn.close()

class retirementCalculator:
    def __init__(self):
        self.retirementAge = 86  # Define retirement age
        self.name = ""
        self.surname = ""
        self.age = 0
        self.addYears = 0
        self.birthDate = ""
        self.data_storage = None

    def getInput(self):

        self.name = input('Name: ').strip().capitalize()
        self.surname = input("Surname: ").strip().capitalize()
        
        # Loop until valid birth date is provided
        while True:
            birthDateInput = input("Birth date (DD-MM-YYYY): ")  # Get user's birth date
            try:
                self.birth_date = datetime.strptime(birthDateInput, "%d-%m-%Y")
                currentDate = datetime.now()  # Get current date and time
                self.age = currentDate.year - self.birth_date.year - ((currentDate.month, currentDate.day) < (self.birth_date.month, self.birth_date.day))
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
        storage_type = input("Where do you want to save the data? (file/memory): ").lower()
        if storage_type not in ["file", "memory"]:
            print("Invalid choice! Please enter 'file' or 'memory'.")
            return

        self.data_storage = DataStorage(storage_type)

        self.getInput()  # Get user input
        status = self.setAnswer()  # Determine status
        word1 = self.setWordStyle(self.age)  # Determine word style for current age
        word2 = self.setWordStyle(self.addYears)  # Determine word style for years to add
        word3 = self.setWordStyle(self.age + self.addYears)  # Determine word style for total age after adding years

        # Print formatted output
        print(f"{self.name} {self.surname} is {self.age} {word1} old. {self.name} will be {status} at {self.age + self.addYears} {word3} old after adding {self.addYears} {word2}.")

        self.data_storage.insert_user(self.name, self.surname, self.birth_date.strftime("%d-%m-%Y"), self.addYears)

        print("Data from chosen storage:")
        users = self.data_storage.get_all_users()
        for user in users:
            print(user)

        self.data_storage.close_connection()

# This block ensures that the main function is called only when the script is run directly
if __name__ == "__main__":
    calculator = retirementCalculator()
    while True:
        calculator.run()
        choice = input("Do you want to add another line to the database? (yes/no): ").lower()
        if choice != "yes":
            break
