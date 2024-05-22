import sqlite3
import csv
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

    def edit_user(self, user_id, name, surname, birth_date, add_years):
        with closing(self.conn.cursor()) as cursor:
            cursor.execute('''
                UPDATE users
                SET name=?, surname=?, birth_date=?, add_years=?
                WHERE id=?
            ''', (name, surname, birth_date, add_years, user_id))
        self.conn.commit()

    def remove_user(self, user_id):
        with closing(self.conn.cursor()) as cursor:
            cursor.execute('''
                DELETE FROM users
                WHERE id=?
            ''', (user_id,))
        self.conn.commit()

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
    
    def export_to_csv(self, filename='users_data.csv'):
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute('SELECT * FROM users')
            users = cursor.fetchall()

            with open(filename, 'w', newline='') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(['id', 'name', 'surname', 'birth_date', 'add_years'])
                csvwriter.writerows(users)

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

    def print_database(self):
        print("Data from chosen storage:")
        users = self.data_storage.get_all_users()
        for user in users:
            print(user)

    def run(self):
        while True:
            storage_type = input("Where do you want to save the data? (file/memory): ").lower()
            if storage_type not in ["file", "memory"]:
                print("Invalid choice! Please enter 'file' or 'memory'.")
                continue
            
            self.data_storage = DataStorage(storage_type)
            self.print_database()

            while True:
                action = input("What do you want to do? (add/edit/delete/export/finish): ").lower()
                if action == "add":
                    name, surname, birth_date, add_years = self.get_input()
                    self.data_storage.insert_user(name, surname, birth_date, add_years)
                    self.print_database()
                elif action == "edit":
                    user_id = int(input("Enter the ID of the user you want to edit: "))
                    name, surname, birth_date, add_years = self.get_input()
                    self.data_storage.edit_user(user_id, name, surname, birth_date, add_years)
                    self.print_database()
                elif action == "delete":
                    user_id = int(input("Enter the ID of the user you want to remove: "))
                    self.data_storage.remove_user(user_id)
                    self.print_database()
                elif action == "export":
                    filename = input("Enter the filename for the CSV export (default 'users_data.csv'): ").strip()
                    if not filename:
                        filename = 'users_data.csv'
                    self.data_storage.export_to_csv(filename)
                    print(f"Data exported to {filename}")
                elif action == "finish":
                    break
                else:
                    print("Invalid action! Please enter 'add', 'edit', 'delete', 'export', or 'finish'.")

            break  # Exit loop after finishing

if __name__ == "__main__":
    calculator = RetirementCalculator()
    while True:
        calculator.run()
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
