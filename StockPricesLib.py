import sqlite3, pandas as pd

# load the stock prices to db from excel
def loadstockprices(filename):
    conn = sqlite3.connect('stockprices.db')
    cur = conn.cursor()
    df = pd.read_csv(filename)
    df.to_sql(name='Prices', con=conn, if_exists='append')
    cur.close()

# read the prices from local db
def readlocalstockprices():
    conn = sqlite3.connect('stockprices.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM Prices')
    names = list(map(lambda x: x[0], cur.description))  # Returns the column names
    cur.close()
    return names


loadstockprices("Nifty50.csv")
lst = readlocalstockprices()
for lElement in lst:
    print(lElement + '\n')


