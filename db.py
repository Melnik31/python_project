import sqlite3



# query the db and return all records
def show_all():
    #connect to db
    con = sqlite3.connect('budget.db')
    #create a courser
    cur = con.cursor()  

    #Query the database 
    cur.execute("SELECT rowid, * FROM transactions")
    items = cur.fetchall()

    print(f'ID Store Price')
    print(f'---------------')
    for i in items:
     print(f'{i[0]}: {i[1]} ${i[2]} {i[3]}')
  
    cur.execute("SELECT SUM(amount) FROM transactions")
    total = cur.fetchone()
    print(f'Total: ${total[0]}')

    

    #commit our command
    con.commit()

    #close our commit
    con.close()
    return items


#add record to the table
def add_one(name, amount, date):
    con = sqlite3.connect('budget.db')
    cur = con.cursor()  

    cur.execute("INSERT INTO transactions VALUES (?,?,?)", (name, amount, date))
    con.commit()
    con.close()

def add_many(list):
    con = sqlite3.connect('budget.db')
    cur = con.cursor()
    
    cur.executemany("INSERT INTO transactions VALUES (?,?,?)", (list))
    
    con.commit()
    con.close()  

def delete_one(id):
    con = sqlite3.connect('budget.db')
    cur = con.cursor() 
    cur.execute("DELETE from transactions WHERE rowid = ?", (id,))

    con.commit()
    con.close()



show_all()