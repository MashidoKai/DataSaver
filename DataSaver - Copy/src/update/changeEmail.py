import mysql.connector
from src.access_database import accessDataBase

def changeEmail(username, new_email):
    try:
        db = accessDataBase()

        cursor = db.cursor()

        # SQL Query to update the password
        query = "UPDATE users SET email = %s WHERE username = %s"
        values = (new_email, username)

        cursor.execute(query, values)
        db.commit()  # Don't forget to commit the changes!

        if cursor.rowcount > 0:
            print(f"✅ Email for user '{username}' changed successfully.")
        else:
            print(f"❌ User '{username}' not found.")

    except mysql.connector.Error as err:
        print("❌ Database error:", err)

    finally:
        cursor.close()
        db.close()