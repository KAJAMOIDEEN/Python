import mysql.connector
import datetime as dt

#pip install mysql-connector-python
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)

mycursor = mydb.cursor()

#create db
#mycursor.execute("create database test")

mycursor.execute("use test")
#create table
#mycursor.execute("create table employee(empid int primary key auto_increment,empName varchar(255) not null,empDesg varchar(255) not null,empSal double check (empSal>10000.00),empJoiningDate date,empCity varchar(155) default 'chennai')")

#Insert data
date= dt.datetime.now()
sql = "insert into employee(empName,empDesg,empSal,empJoiningDate) values(%s,%s,%s,%s)"
#val = ('Rahul','Software Engineer',50000,date)
valArr = [('mathew','Software Engineer',50000,date),
('joseph','Desk Engineer',30000,date),
('vijay','Human Resource',45000,date),
('suriya','Senior Software Engineer',80000,date)]
#mycursor.executemany(sql,valArr)
#mydb.commit()


#Select data from table
mycursor.execute("select * from employee where empid=8 ")

res = mycursor.fetchone()

print(res)

