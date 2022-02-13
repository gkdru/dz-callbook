import sqlite3
from sqlite3 import Error

def connect_to_db():
    try:
             connection = sqlite3.connect("app.db")
             print("Connection succesfully")
             return connection
    except Error:
             print(Error)
        
        
def create_table(con):
     cur = con.cursor()
     cur.execute("CREATE TABLE  callbook(id INTEGER PRIMARY KEY, name TEXT,phone TEXT,count_call INTEGER)")
     con.commit()
     
def select_table(con):
     cur=con.cursor()
     cur.execute("SELECT * FROM callbook")
     result= cur.fetchall()
     return result
  
     
def insert_table(con,data2):
   cur = con.cursor()
   cur.execute('''INSERT INTO callbook(id,name,phone,count_call) VALUES(?,?,?,?)''', newtablename)
   
   con.commit()


def update_table(con):
    cur = con.cursor()
    cur.execute("UPDATE callbook SET name='stone' WHERE id = 2 ")
    con.commit()

def select_tovar(con):
    cur = con.cursor()
    cur.execute("SELECT name FROM callbook")
    result= cur.fetchall()
    return result


def delete_table(con,data3):
    cur = con.cursor()
    cur.execute('''DELETE FROM callbook  WHERE id = ? ''',delname)
  

def count(con,callscounter):
    cur = con.cursor()
    cur.execute('''UPDATE callbook SET count_call =?  WHERE id = ? ''',callscounter)
    con.commit()
    
   

newtablename = [1,'Emma',"887555355",1]
delname=[3]
callscounter=[2,1]




 
con = connect_to_db()
#create_table(con)
#insert_table(con,newtablename)
#update_table(con)
#delete_table(con,delname)
count(con,callscounter)
tableRows=select_table(con)
con.close()
print(tableRows)



