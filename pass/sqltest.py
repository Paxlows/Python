import sqlite3

print("press \"0\" for help:\n")

while True:

    def _help():
        print("""        1:to check contents in database
            2:to add contents in database
            3:to delete contents in database
            4:to exit\n""")
    checkval = int(input("Enter the number:"))

    if checkval == 0:
        _help()

    conn = sqlite3.connect('pass.db')

    c = conn.cursor()
    def valin():
        # c.execute('''CREATE TABLE Pass(
        #     App_Name text,
        #     User_Name text,
        #     Password text,
        #     Address text);''')  
        appname = input("Enter the app name:\n")
        username = input("Enter the user name:\n")
        password = input("Enter the password:\n")
        address = input("Enter the address:\n")
        c.execute("INSERT INTO Pass VALUES(:App_Name,:User_Name,:Password,:Address)",{'App_Name':appname,'User_Name':username,'Password':password,'Address':address})

    def valout():
        c.execute("SELECT * FROM Pass")
    if checkval ==2:
        valin()
    if checkval == 1:
        valout()

    # print(c.fetchone())
    
    conn.commit()

    conn.close()
    if(checkval==4):
        print("bye")
        break
