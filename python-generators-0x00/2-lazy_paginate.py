import mysql.connector

def paginate_users(page_size, offset):
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='your_password',  
        database='ALX_prodev'
    )
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM user_data ORDER BY user_id LIMIT %s OFFSET %s",
        (page_size, offset)
    )
    rows = cursor.fetchall()

    cursor.close()
    conn.close()
    return rows

def lazy_paginate(page_size):
    offset = 0
    while True:  
        page = paginate_users(page_size, offset)
        if not page:
            break
        for row in page:
            yield row
        offset += page_size
    return  