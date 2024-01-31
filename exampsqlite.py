import sqlite3

def insertdet(cur):
    cur.execute(""" INSERT INTO Passdet VALUES ("https://www.amazon.in", "123@gmail.com", "123456") """)
    
def updatedet(cur):
    cur.execute(""" INSERT INTO Passdet VALUES ("https://www.amazon.in", "123@gmail.com", "123456") """)
    
def deletedet(cur):
    cur.execute(""" INSERT INTO Passdet VALUES ("https://www.amazon.in", "123@gmail.com", "123456") """)
    
def getdet(cur, urlval, usernameval):
    cur.execute(""" SELECT password FROM Passdet WHERE url=:url AND username=:username """, {'url': urlval, 'username': usernameval})
    return cur.fetchone()


conn = sqlite3.connect('passman.db')

cur = conn.cursor()

# cur.execute("""CREATE TABLE Passdet (
#             url text,
#             username text,
#             password text
# )""")
print(''.join((getdet(cur, "https://www.amazon.in", "123@gmail.com"))))
conn.commit()
conn.close()