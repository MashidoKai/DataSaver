import mysql.connector

def accessDataBase():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Password",
            database="Whatever Database"
        )
        return db
    
    except mysql.connector.Error as err:
        print(f"❌ Error: {err}")
        return None