import csv
import sqlite3


def create_connection():
    try:
        con = sqlite3.connect('user.sqlite3')
        return con 
    except Exception as e:
        print("Error", e)


INPUT_STRING = """
Enter the option:
    1. Create table
    2. Dump user from csv file into user table
    3. Add new user into user table
    4. Query all user from user table
    5. Query user by id from user table
    6. Query specified no. of user from user table
    7. Delete all user from user table
    8. Delete user by id from user table
    9. Update user by id from user table
    10. Exit
"""

def create_table(con):
    CREATE_USER_TABLE_QUERE = """
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name CHAR(255) NOT NULL,
            last_name CHAR(255) NOT NULL,
            company_name CHAR(255) NOT NULL,
            address CHAR(255) NOT NULL,
            city CHAR(255) NOT NULL,
            county CHAR(255) NOT NULL,
            state CHAR(255) NOT NULL,
            zip REAL NOT NULL,
            phone1 CHAR(255) NOT NULL,
            phone2 CHAR(255),
            email CHAR(255) NOT NULL,
            web text
        );
    """
    cur = con.cursor()
    cur.execute(CREATE_USER_TABLE_QUERE)
    print("user table was creted successfully.")



def read_csv():
    with open('sample_users.csv', 'r') as file:
        users = []
        data = csv.reader(file)
        for i in data:
            users.append(tuple(i))
        return users[1:]

def insert_users(con, users):
    user_add_quere = """
    INSERT into user
    ('first_name', 'last_name','company_name','address','city','county','state','zip','phone1','phone2','email','web')
    values
    (?,?,?,?,?,?,?,?,?,?,?,?);
    
    """
    cur = con.cursor()
    cur.executemany(user_add_quere, users)
    con.commit()
    print(f"{len(users)} inserted successfully.")

def select_users(con):
    cur = con.cursor()
    users = cur.execute("SELECT * FROM user;")
    for user in users:
        print(user)

def select_user_by_id(con, user_id):
    cur = con.cursor()
    users = cur.execute("SELECT * FROM user WHERE id = ?;", (user_id,))
    for user in users:
        print(user)

def select_specified_users(con,no_of_user):
    cur = con.cursor()
    users = cur.execute("SELECT * FROM user LIMIT ?;", (no_of_user,))
    for user in users:
        print(user)

def delete_user(con):
     cur = con.cursor()
     users = cur.execute("DELETE FROM user")
     con.commit()
     print("All user were deleted successfully.")

def delete_user_by_id(con,user_id):
    cur = con.cursor()
    users = cur.execute("DELETE FROM user WHERE id = ?;", (user_id,))
    con.commit()
    for user in users:
        print(user)
def add_user_by_id(con,first_name, last_name, company_name, address, city, county, state, zip, phone1, phone2, email, web
):
    cur = con.cursor()
    cur.execute("INSERT INTO user ('first_name', 'last_name','company_name','address','city','county','state','zip','phone1','phone2','email','web' ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?);",(first_name, last_name, company_name, address, city, county, state, zip, phone1, phone2, email, web
 ))
    con.commit()
    print("User added successfully.")

def exit_program( con):
    con.close()
    print("Program exited successfully.")


def main():
    con = create_connection()
    user_input = input(INPUT_STRING)
    if user_input == "1":
        create_table(con)
    elif user_input == "2":
        users = read_csv()
        insert_users(con, users)
    elif user_input == "3":
        pass
    elif user_input == "4":
        select_users(con)
    elif user_input == "5":
        user_id = input("Enter user id: ")
        select_user_by_id (con, user_id)
    elif user_input == "6":
       no_of_user = input("Enter number of user: ")
       if no_of_user.isdigit():
            select_specified_users (con,no_of_user)
    elif user_input == "7":
            conformation = input("Are you sure you want to delete all user? (yes): ")
            if conformation == "yes":
                delete_user(con)
    elif user_input == "8":
        user_id = input("Enter user id: ")
        delete_user_by_id(con,user_id)
    elif user_input == "9":
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        company_name = input("Enter company name: ")
        address = input("Enter address: ")
        city = input("Enter city: ")
        county = input("Enter county: ")
        state = input("Enter state: ")
        zip = input("Enter zip: ")
        phone1 = input("Enter phone1: ")
        phone2 = input("Enter phone2: ")
        email = input("Enter email: ")
        web = input("Enter web: ")
        add_user_by_id(con,first_name, last_name, company_name, address, city, county, state, zip, phone1, phone2, email, web)
    elif user_input == "10":
        exit_program(con) 
    else:
        print("Invalid option. Please choose a valid option.")
        con.close()
main()

