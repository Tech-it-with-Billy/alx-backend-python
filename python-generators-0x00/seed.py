import csv
import uuid
import mysql.connector
from mysql.connector import errorcode

# MySQL connection parameters
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'your_password'  # Replace with your MySQL root password
DB_NAME = 'ALX_prodev'

def connect_db():
    """Connect to MySQL server (without specifying database)."""
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD
        )
        print("✅ Connected to MySQL server.")
        return conn
    except mysql.connector.Error as err:
        print(f"❌ Connection error: {err}")
        return None

def create_database(connection):
    """Create ALX_prodev database if it doesn't exist."""
    cursor = connection.cursor()
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        print(f"✅ Database '{DB_NAME}' checked/created.")
    except mysql.connector.Error as err:
        print(f"❌ Failed creating database: {err}")
    cursor.close()

def connect_to_prodev():
    """Connect directly to the ALX_prodev database."""
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        print("✅ Connected to ALX_prodev database.")
        return conn
    except mysql.connector.Error as err:
        print(f"❌ Error connecting to database: {err}")
        return None

def create_table(connection):
    """Create user_data table with defined schema."""
    cursor = connection.cursor()
    create_table_query = """
    CREATE TABLE IF NOT EXISTS user_data (
        user_id VARCHAR(36) PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        age DECIMAL NOT NULL,
        INDEX(user_id)
    );
    """
    try:
        cursor.execute(create_table_query)
        print("✅ Table 'user_data' checked/created.")
    except mysql.connector.Error as err:
        print(f"❌ Error creating table: {err}")
    cursor.close()

def insert_data(connection, data):
    """Insert data into user_data table, avoid duplicate emails."""
    cursor = connection.cursor()
    for name, email, age in data:
        try:
            # Check for duplicate email
            cursor.execute("SELECT email FROM user_data WHERE email = %s", (email,))
            if cursor.fetchone():
                print(f"⚠️ Skipping duplicate email: {email}")
                continue
            user_id = str(uuid.uuid4())
            cursor.execute(
                "INSERT INTO user_data (user_id, name, email, age) VALUES (%s, %s, %s, %s)",
                (user_id, name, email, age)
            )
        except mysql.connector.Error as err:
            print(f"❌ Insert error for {email}: {err}")
    connection.commit()
    print("✅ Data inserted into table.")
    cursor.close()

def read_csv(filepath):
    """Read user data from CSV file."""
    data = []
    try:
        with open(filepath, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            headers = next(reader, None)  # skip header if present
            for row in reader:
                if len(row) >= 3:
                    data.append((row[0], row[1], row[2]))
    except FileNotFoundError:
        print(f"❌ File not found: {filepath}")
    return data

# === Main Script ===
if __name__ == "__main__":
    conn = connect_db()
    if conn:
        create_database(conn)
        conn.close()

    conn_prodev = connect_to_prodev()
    if conn_prodev:
        create_table(conn_prodev)
        user_data = read_csv('user_data.csv')
        insert_data(conn_prodev, user_data)
        conn_prodev.close()
