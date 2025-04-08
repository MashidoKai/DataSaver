import mysql.connector
from src.access_database import accessDataBase

def uploadData(username, email, passwrd):
    try:
        db = accessDataBase()

        cursor = db.cursor()

        query = "INSERT INTO users (username, email, passwrd) VALUES (%s, %s, %s)"
        values = (username, email, passwrd)
        cursor.execute(query, values)
        db.commit()

        print(f"✅ User '{username}' uploaded successfully.")

    except mysql.connector.Error as err:
        print("❌ Database error:", err)

    finally:
        cursor.close()
        db.close()