import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)


def initCursor():
    cursor = mydb.cursor(buffered=True)
    cursor.execute("USE playersdb")
    return cursor


def insertPlayer(query, val, urlToCheck):
    cursor = initCursor()
    checkDuplicateQuery = 'SELECT * FROM player WHERE url=\'' + urlToCheck + '\''
    cursor.execute(checkDuplicateQuery)
    res = cursor.fetchone()
    if res is not None:
        print('giocatore già presente')
    else:
        cursor.execute(query, val)
        mydb.commit()
        print('Inserimento riuscito')


