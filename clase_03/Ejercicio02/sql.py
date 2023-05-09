import sqlite3

conn=sqlite3.connect('basev1.db')
co=conn.cursor()

cTableUser="""
    create table users(
        ID INTEGER PRIMARY KEY,
        USUARIO VARCHAR (25),
        PASSWORD VARCHAR(255),
        EMAIL VARCHAR(255)
    )
"""
co.execute("DROP TABLE IF EXISTS users")
co.execute(cTableUser)
data="insert into users(USUARIO,PASSWORD,EMAIL) values ('user1','password','alex@gmail.com')"
co.execute(data)

user="userx"
password="12342233"
email="eieur@gmail.com"

insertParametrizada="insert into users(USUARIO,PASSWORD,EMAIL) values (?,?,?)"
dataParametrizada=(user,password,email)
co.execute(insertParametrizada,dataParametrizada)
conn.commit()
conn.close()