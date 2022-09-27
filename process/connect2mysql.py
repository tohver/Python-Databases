from mysql.connector import connect, Error, Warning
import data.mysqldata as dt

def openConnection():
    try:
        connection = connect(
                host = dt.host,
                user = dt.user,
                password = dt.password,
                database = dt.database
            )
        print(connection)
        cursor = connection.cursor(buffered=True)
        return cursor, connection
    except Error as e:
        print(e)
        
def executeQuery(cursor, query):
    try: 
        cursor.execute(query)
    except (Error, Warning) as e:
        print(e)
        return None

def closeAll():
    cursor.close()
    connection.close()

def printa():
    print("aaa")