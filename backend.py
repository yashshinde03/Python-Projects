import sqlite3
def connect():
    conn = sqlite3.connect('first.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS first (Id INTEGER PRIMARY KEY ,date text,earnings integer,exercise text,study text,diet text,python text)")
    conn.commit()
    conn.close()

def insert(date,earnings,exercise,study,diet,python):
    conn = sqlite3.connect('first.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO first VALUES (NULL ,?,?,?,?,?,?) ",(date,earnings,exercise,study,diet,python))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect('first.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM first")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect('first.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM first WHERE id = ? ",(id,))
    conn.commit()
    conn.close()

def search(date='',earnings='',exercise='',study='',diet='',python=''):
    conn = sqlite3.connect('first.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM first WHERE date=? OR earnings=? OR exercise=? OR study=? OR diet = ? OR python = ?",(date,earnings,exercise,study,diet,python))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

connect()
# insert('16-7-2021','200','no exercise','no study','diet not taken','did python')

