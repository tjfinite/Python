import sqlite3
from datetime import datetime
from contextlib import closing

class DataStorage:
    def __init__(self, storage_type):
        self.storage_type = storage_type
        if self.storage_type == "memory":
            self.conn = sqlite3.connect(':memory:')  # Temporary in-memory database
        elif self.storage_type == "file":
            self.db_file = 'retirement_data.db'
            self.conn = sqlite3.connect(self.db_file)  # Permanent file-based database
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
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute('SELECT * FROM users')
            return cursor.fetchall()

    def get_last_user(self):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users ORDER BY id DESC LIMIT 1')
            return cursor.fetchone()

    def close_connection(self):
        self.conn.close()

class RetirementCalculator:
    RETIREMENT_AGE = 86

    def __init__(self):
        self.data_storage = None

    def get_input(self):
        name = input('Name: ').strip().capitalize()
        surname = input("Surname: ").strip().capitalize()
        
        while True:
            birth_date_input = input("Birth date (DD-MM-YYYY): ")
            try:
                birth_date = datetime.strptime(birth_date_input, "%d-%m-%Y")
                age = datetime.now().year - birth_date.year
                if age >= 0:
                    break
                else:
                    print("Invalid birth date! Please enter a valid date.")
            except ValueError:
                print("Invalid date format! Please enter date in DD-MM-YYYY format.")
        
        while True:
            add_years_input = input('Add years: ')
            try:
                add_years = int(add_years_input)
                if add_years >= 0:
                    break
                else:
                    print("Years to add have to be a positive number!")
            except ValueError:
                print("Years to add have to be an integer!")
        
        return name, surname, birth_date.strftime("%d-%m-%Y"), add_years

    def run(self):
        storage_type = input("Where do you want to save the data? (file/memory): ").lower()
        if storage_type not in ["file", "memory"]:
            print("Invalid choice! Please enter 'file' or 'memory'.")
            return

        self.data_storage = DataStorage(storage_type)

        name, surname, birth_date, add_years = self.get_input()
        total_years = datetime.now().year - datetime.strptime(birth_date, "%d-%m-%Y").year + add_years
        status = "in retirement age" if total_years > self.RETIREMENT_AGE else ("underaged" if total_years < 19 else "in productive age")

        print(f"{name} {surname} is {total_years} {'year' if total_years == 1 else 'years'} old. {name} will be {status} after adding {add_years} {'year' if add_years == 1 else 'years'}.")

        self.data_storage.insert_user(name, surname, birth_date, add_years)

        print("Data from chosen storage:")
        users = self.data_storage.get_all_users()
        for user in users:
            print(user)

        self.data_storage.close_connection()

if __name__ == "__main__":
    calculator = RetirementCalculator()
    while True:
        calculator.run()
        choice = input("Do you want to add another line to the database? (yes/no): ").lower()
        if choice != "yes":
            print_last_record = input("Do you want to print the last record? (yes/no): ").lower()
            if print_last_record == "yes":
                if calculator.data_storage:
                    last_user = calculator.data_storage.get_last_user()
                    if last_user:
                        print("Last record:")
                        print(last_user)
                    else:
                        print("No records in the database.")
                else:
                    print("No data storage object available.")
            break
