import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()

def create_table():
    c.execute("""CREATE TABLE user (
        id integer PRIMARY KEY AUTOINCREMENT,
        firstname text,
        lastname text
        )""")
    conn.commit()


def insert(firstname, lastname):
    c.execute("INSERT INTO user (firstname, lastname) VALUES (?, ?)", (firstname, lastname))
    conn.commit()

def select():
    c.execute("SELECT * FROM user WHERE lastname='Cordes'")
    #fetchs all row and puts these into a array with tuples
    print(c.fetchall())
    # fetch only one row and puts it into a tuple
    c.execute("SELECT * FROM user WHERE firstname='Til'")
    print(c.fetchone())
    conn.commit()

select()

conn.close()