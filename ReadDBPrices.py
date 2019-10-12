import sqlite3, pandas as pd

conn = sqlite3.connect('stockprices.db')
cur = conn.cursor()
cur.execute('SELECT * FROM Prices')
names = list(map(lambda x: x[0], cur.description)) #Returns the column names
print(names)

cur.close()
