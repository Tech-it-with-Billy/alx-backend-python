import mysql.connector

def fetch_limited_users(limit_count):
    try:
        # Connect to the MySQL database
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password', 
            database='ALX_prodev'
        )
        cursor = conn.cursor(dictionary=True)

        # Execute SELECT with LIMIT
        query = "SELECT * FROM user_data ORDER BY user_id LIMIT %s"
        cursor.execute(query, (limit_count,))

        # Fetch and return results
        results = cursor.fetchall()

        cursor.close()
        conn.close()

        return results

    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return []
