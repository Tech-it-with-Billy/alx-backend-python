import mysql.connector

def stream_users_in_batches(batch_size):
    """Generator that yields batches of users from the user_data table."""
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='your_password',
        database='ALX_prodev'
    )
    cursor = conn.cursor(dictionary=True)

    offset = 0
    while True:
        cursor.execute(
            "SELECT * FROM user_data ORDER BY user_id LIMIT %s OFFSET %s",
            (batch_size, offset)
        )
        batch = cursor.fetchall()
        if not batch:
            break
        yield batch
        offset += batch_size

    cursor.close()
    conn.close()

def batch_processing(batch_size):
    for batch in stream_users_in_batches(batch_size):
        # Loop over users in batch (2nd loop)
        for user in batch:
            if user['age'] > 25:
                yield user 