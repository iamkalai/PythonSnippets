import sqlite3

def readSqliteTable():
    songs = []
    try:
        sqliteConnection = sqlite3.connect('Youtube')
        cursor = sqliteConnection.cursor()

        sqlite_select_query = """SELECT title from videos ORDER BY title ASC"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()

        for row in records:
            print(row[0])

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            return songs

print("The songs are \n\n")
readSqliteTable()

