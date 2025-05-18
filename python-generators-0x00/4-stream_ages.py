import mysql.connector

def stream_user_ages():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='your_password',  
        database='ALX_prodev'
    )
    cursor = conn.cursor()

    cursor.execute("SELECT age FROM user_data")
    for (age,) in cursor:  
        yield age

    cursor.close()
    conn.close()
    return  # End of generator

def compute_average_age():
    total_age = 0
    count = 0

    for age in stream_user_ages():  # Loop 2
        total_age += age
        count += 1

    average = total_age / count if count > 0 else 0
    print(f"Average age of users: {average:.2f}")

if __name__ == "__main__":
    compute_average_age()
