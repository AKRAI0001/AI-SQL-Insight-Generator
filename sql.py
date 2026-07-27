import sqlite3
con=sqlite3.connect("Naresh_it_employee.db")
cur=con.cursor()
table_info='''
create table Employees (Name varchar(20), Role varchar(20) , Salary_pm float)'''

cur.execute(table_info)
cur.execute('''Insert into Employees Values('Omkar Nallagoni Sir','Data Science',75000000)''')
cur.execute('''Insert into Employees Values ('Abhishek','Data Science',80000)''')
cur.execute('''Insert into Employees Values ('Swayam','Data Science',70000)''')
cur.execute('''Insert into Employees Values ('Harsh','Data Science',75000)''')
cur.execute('''Insert into Employees Values ('Adarsh','Data Science',75000)''')
con.commit()
con.close()