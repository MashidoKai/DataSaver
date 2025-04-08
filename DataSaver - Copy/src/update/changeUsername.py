import mysql.connector
from src.access_database import accessDataBase

def changeUsername(email, new_username):
    try:
        db = accessDataBase()

        cursor = db.cursor()

        # SQL Query to update the password
        query = "UPDATE users SET username = %s WHERE email = %s"
        values = (new_username, email)

        cursor.execute(query, values)
        db.commit()  # Don't forget to commit the changes!

        if cursor.rowcount > 0:
            print(f"✅ Username for user '{email}' changed successfully.")
        else:
            print(f"❌ Email '{email}' not found.")

    except mysql.connector.Error as err:
        print("❌ Database error:", err)

    finally:
        cursor.close()
        db.close()