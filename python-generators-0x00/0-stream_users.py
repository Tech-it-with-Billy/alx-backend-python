import mysql.connector

def stream_users():
    # Connect to the ALX_prodev database
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='your_password',
        database='ALX_prodev'
    )
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM user_data")

    # Use one loop to yield each row
    for row in cursor:
        yield row

    cursor.close()
    conn.close()
