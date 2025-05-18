The seed.py script automates the setup and population of a MySQL database for user data management. It performs the following steps:

1. Connect to MySQL Server: Establishes a connection to the MySQL server without specifying a database.

2. Create Database: Checks for the existence of a database named ALX_prodev and creates it if it doesn’t exist.

3. Connect to ALX_prodev: Establishes a new connection to the newly created (or existing) ALX_prodev database.

4. Create user_data Table: Ensures the user_data table exists with the required schema:

- user_id (UUID, Primary Key, Indexed)

- name (VARCHAR, NOT NULL)

- email (VARCHAR, NOT NULL)

- age (DECIMAL, NOT NULL)

5. Read CSV File: Loads user data from user_data.csv.

6. Insert Data: Iterates through the CSV data and inserts each user into the table, skipping duplicate emails.