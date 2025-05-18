import mysql.connector

def paginate_users(page_size, offset):
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='your_password', 
        database='ALX_prodev'
    )
    cursor = conn.cursor(dictionary=True)

    # Explicitly using LIMIT and OFFSET in SQL as required
    query = "SELECT * FROM user_data LIMIT %s OFFSET %s"
    cursor.execute(query, (page_size, offset))
    rows = cursor.fetchall()

    cursor.close()
    conn.close()
    return rows

def lazy_paginate(page_size):
    offset = 0
    while True:  # One loop only
        # Required: call to paginate_users(page_size, offset)
        page = paginate_users(page_size, offset)
        if not page:
            break
        for row in page:
            yield row
        offset += page_size
    return  # Explicit return after generator completes
