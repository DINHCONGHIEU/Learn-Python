
import sqlite3
from sqlite3 import Error

def welcome():
    entry = int(input(""""
        1. Hiển thị
        2. Thêm liên lạc
        3. Kiểm tra danh bạ
        4. Xóa liên lạc
        5. Thoát
        Enter your number: 
    """))
    return entry

def sql_connection():
    con = sqlite3.connect('Phonebook.db')
    return con

def create_database(con):
    try:
        cur = con.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS Phonebook(Number, Name)')
        con.commit()
        return 1
    except Error:
        return -1

def insert_data(con,data):
    cur = con.cursor()
    cur.execute('INSERT INTO Phonebook(Number, Name) VALUES(?, ?)',data)
    con.commit()

def delete_data(con,data):
    cur = con.cursor()
    cur.execute("DELETE FROM Phonebook WHERE Name = '" + data + "'")
    con.commit()

def get_data(con):
    cur = con.cursor()
    cur.execute("SELECT * FROM Phonebook")
    rows = cur.fetchall()
    return rows

def phonebook():
    con = sql_connection()
    while True:
        entry = welcome()
        if entry == 1:
            data = get_data(con)
            if not data:
                print("Bạn chưa có danh sách liên lạc nào!")
            else: 
                for item in data:
                    print(item)
        elif entry == 2:
            data = get_data(con)
            checked = False 
            phone_number = input("Số điện thoại: ")
            contact_name = input("Tên liên lạc: ")
            data_input = (phone_number,contact_name)
            for item in data:
                if item[0] == phone_number:
                    print("Liên lạc này đã tồn tại. Mời bạn nhập số khác!")
                    checked = True 
            if checked == False:
                insert_data(con,data_input)
                print("Đã thêm liên lạc!")
        elif entry == 3:
            data = get_data(con)
            checked  = False 
            name = input("Nhập tên liên lạc:")
            for item in data:
                if item[1] == name:
                    print("Số điện thoại là: ",item[0])
                    checked = True
            if checked == False:
                print("Liên lạc không tồn tại")

        elif entry == 4:
            data = get_data(con)
            checked = False 
            name = input("Nhập tên liên lạc:")
            for item in data:
                if item[1] == name:
                    checked = True
                    confirm = input("Bạn có chắc chắn xóa? Y/N:")
                    if confirm.capitalize() =="Y":
                        delete_data(con,name)
                        print("Đã xóa!")
                    else:
                        print("Quay trở lại menu!")
                    break
            if checked == False:
                print("Liên lạc không tồn tại")
            
        elif entry == 5:
            print("Xin cảm ơn!")
            break
        
        else:
            print("Mời bạn nhập lại!")

con = sql_connection()
create_database(con)
con.close()
phonebook()