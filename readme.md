# User Management CLI

A simple command-line-based user management system using SQLite and CSV for storing and managing user records.

## Features
- Create a user table in SQLite.
- Import users from a CSV file.
- Add, update, delete, and query users.
- Fetch users by ID or retrieve a specific number of users.
- Delete all users or specific users by ID.

## Requirements
Ensure you have Python installed on your system.

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/repository-name.git
   cd repository-name
   ```

2. Install required dependencies (if any):
   ```sh
   pip install -r requirements.txt
   ```
   *(Currently, no additional dependencies are required.)*

## Usage
Run the script:
   ```sh
   python user.py
   ```

Follow the on-screen menu options:
```
Enter the option:
    1. Create table
    2. Dump user from CSV file into user table
    3. Add new user into user table
    4. Query all users from the user table
    5. Query user by ID from user table
    6. Query a specified number of users from the user table
    7. Delete all users from the user table
    8. Delete a user by ID from the user table
    9. Update user by ID from the user table
    10. Exit
```

## Sample CSV File
Make sure you have a CSV file named `sample_users.csv` in the same directory, structured like this:
```
first_name,last_name,company_name,address,city,county,state,zip,phone1,phone2,email,web
John,Doe,CompanyX,123 Street,New York,NY,NY,10001,1234567890,0987654321,john.doe@example.com,www.example.com
Jane,Smith,CompanyY,456 Avenue,Los Angeles,CA,CA,90001,2345678901,,jane.smith@example.com,www.companyy.com
```

## Notes
1. The database file (`user.sqlite3`) is created automatically.
2. Make sure `sample_users.csv` is properly formatted before importing users.

## License 
**This project is open-source and available under the MIT License.**

## Author
[Your Name](https://github.com/yourusername)
