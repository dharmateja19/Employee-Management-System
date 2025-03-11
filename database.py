import pymysql
from tkinter import messagebox
def connect_database():
    global mycursor,conn
    try:
        conn = pymysql.connect(host='localhost',user='root',password='Dharma@09')
        mycursor=conn.cursor()
    except:
        messagebox.showerror('Eroor','something went wrong.please open mysql before running again')
        return
    mycursor.execute('CREATE DATABASE IF NOT EXISTS employeedata')
    mycursor.execute('USE employeedata')
    mycursor.execute('''
        CREATE TABLE IF NOT EXISTS employee (
            Id INT(6) PRIMARY KEY,
            Name VARCHAR(100),
            Phone INT(10),
            Role VARCHAR(50),
            Gender VARCHAR(10),
            Salary DECIMAL(10,2)
        )
    ''')
def insert(id,name,phone,role,gender,salary):
    mycursor.execute('''
        INSERT INTO employee (Id, Name, Phone, Role, Gender, Salary)
        VALUES (%s, %s, %s, %s, %s, %s)
    ''', (id, name, phone, role, gender, salary))
    conn.commit()

def id_exists(id):
    mycursor.execute('SELECT COUNT(*) FROM employee WHERE Id = %s',id)
    result=mycursor.fetchone()
    return result[0]>0

def fetch_employees():
    mycursor.execute('SELECT * from employee')
    result = mycursor.fetchall()
    return result

def update(id,name,phone,role,gender,salary):
    mycursor.execute('''
        UPDATE employee
        SET name=%s,phone=%s,role=%s,gender=%s,salary=%s WHERE id=%s
    ''',(name,phone,role,gender,salary,id))
    conn.commit()

def delete(id):
    mycursor.execute('''
        DELETE FROM employee
        WHERE id=%s    
    ''',id)
    conn.commit()

def deleteall():
    mycursor.execute('TRUNCATE TABLE employee')
    conn.commit()

def search(option,value):
    mycursor.execute(f'SELECT * FROM employee WHERE {option}=%s',value)
    result=mycursor.fetchall()
    return result
connect_database()