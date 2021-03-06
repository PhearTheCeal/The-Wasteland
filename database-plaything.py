"""Simple little program that takes name and age and puts them in a
   database, or views DB in nicely formatted manner. Why, you ask?
   Because learning, that's why."""

import sqlite3
import os.path

DATABASE_NAME = "people-to-kill.db"
PROMPT = ">>> "
CONNECTION = None
CURSOR = None

def valid_age(age):
    """checks if age (string) is int and above > 0"""
    if age.isdigit():
        return True
    else:
        return False 

def valid_name(name):
    """checks to make sure name < 64 characters, because anyone
       who has a longer name than that cannot be trusted."""
    if len(name) > 0 and len(name) < 64:
        return True
    else:
        return False

def database_exists(dbname):
    """Checks if database exists in current directory"""
    print("Creating database " + dbname)
    return os.path.isfile(dbname)

def create_database(dbname):
    """create database"""
    global CONNECTION
    global CURSOR
    CONNECTION = sqlite3.connect(DATABASE_NAME)
    CURSOR = CONNECTION.cursor()
    CURSOR.execute("""CREATE TABLE people
                 (name text, age integer)""")
    CONNECTION.commit()

def insert_data(name, age):
    """opens database, puts shit into it, commits and closes"""
    CURSOR.execute("""INSERT INTO people VALUES
                 (?, ?)""", (name, int(age)))
    CONNECTION.commit()

def view_data():
    """Prints the database contents."""
    table = []
    for row in CURSOR.execute("SELECT * FROM people ORDER BY name"):
        table.append(row)
    table.sort()
    print("Contents of " + DATABASE_NAME + ":")
    print("NAME | AGE")
    for entry in table:
        print("{} | {}".format(entry[0], entry[1]))


def take_input():
    """Gets name and age."""
    user_input = ""
    while user_input != "exit" and not valid_name(user_input):
        print("Name, please:")
        name = user_input = input(PROMPT)
    while user_input != "exit" and not valid_age(user_input):
        print("Age, please:")
        age = user_input = input(PROMPT)
    if user_input != "exit":
        insert_data(name, age)
        print("'{},' age {}, inserted into database.".format(name, age)) 

def main():
    """Sets up some shit and does the main loop."""
    if not database_exists(DATABASE_NAME):
        create_database(DATABASE_NAME)
    else:
        global CONNECTION
        global CURSOR
        CONNECTION = sqlite3.connect(DATABASE_NAME)
        CURSOR = CONNECTION.cursor()
    print("""Hello! Type "view" to view your database, or "insert" """)
    print("""to add a name and age. Type "exit" at any point to quit.""")
    user_input = ""
    while user_input != "exit":
        user_input = input(PROMPT).lower()
        if user_input == "insert":
            take_input()
        elif user_input == "view":
            view_data()
        else:
            if user_input != "exit":
                print("ERROR CODE ID-10-t; please contact system administrator.")
    print("Have a nice day!")

if __name__ == "__main__":
    main() 