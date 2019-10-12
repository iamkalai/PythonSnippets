import sqlite3, pandas as pd

conn = sqlite3.connect('stockprices.db')
cur = conn.cursor()
df = pd.read_csv('Nifty50.csv')
df.to_sql(name='Prices', con=conn, if_exists='append')
cur.execute('SELECT * FROM Prices')
names = list(map(lambda x: x[0], cur.description)) #Returns the column names
print(names)

cur.close()
