import sqlite3

con = sqlite3.connect("test.db")

cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS USERS (
    id INTEGER PRIMARY KEY,
               name TEXT
            )""")
con.commit()

def omonullo():
    print("""
1.Add New User
2.Delete User
3.Change User
4.Show All User          
""")
    a = int(input("Tanlang:"))
    if a == 1:
        addnewuser()
    elif a == 4:
        showalluser()
    elif a == 2:
        deleteUser()
    elif a == 3:
        ChanguUser()

def addnewuser():
    username = input("Ismingni kirit : ")
    cur.execute("INSERT INTO USERS (name) VALUES (?)", (str(username),))
    con.commit()
    print(f"{username} degan user yaratildi")
    omonullo()

def showalluser():
    userlar = cur.execute("SELECT name FROM USERS").fetchall()
    print(userlar)
    omonullo()

def deleteUser():
    choiceuser = str(input("Qaysi userni ochirmoqchisiz : "))
    delete = cur.execute("DELETE FROM users WHERE name=?", (choiceuser,))
    if delete:
        print("User ochirildi")
        con.commit()
        omonullo()
    else:
        print("User ochirilmadi")
        omonullo()

def ChanguUser():
    a = input("Userni tanlang :")
    b = input("Yangi ism kiriting :")
    changeuser = cur.execute("UPDATE users SET name=? WHERE name=?", (b,a))
    if changeuser:
        print("User ozgartirildi.")
        con.commit()
        omonullo()
    else:
        print("User ozgartirilmadi.")
        omonullo()

omonullo()

