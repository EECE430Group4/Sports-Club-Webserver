import mysql.connector


def authenticate(username, password):
    conn = mysql.connector.connect(host='35.246.1.16',
                                   database='430Group4',
                                   user='root',
                                   password='root430group4root')
    cursor = conn.cursor()
    cursor.execute("select userid from users WHERE username='"+username+"'")
    res = cursor.fetchall()
    if len(res) == 0:
        return 1  # incorrect username, username does not exist
    userid = res[0][0]
    cursor.execute("select password from users WHERE userid='"+str(userid)+"'")
    res = cursor.fetchall()
    retPassword = res[0][0]
    if retPassword != password:
        return 2  # incorrect password
    cursor.execute("SELECT role from users where userid='"+str(userid)+"'")
    res = cursor.fetchall()
    role = res[0][0]
    return role


def register(name, username, password):
    conn = mysql.connector.connect(host='35.246.1.16',
                                   database='430Group4',
                                   user='root',
                                   password='root430group4root')
    cursor = conn.cursor()
    cursor.execute("select userid from users WHERE username='"+username+"'")
    res = cursor.fetchall()
    if len(res) != 0:
        return 1  # username already exists in database

    SQL = '''insert into users(name,username,password,role)
            values ('{}','{}','{}','FAN')'''.format(name, username, password)
    cursor.execute(SQL)
    conn.commit()
    return 0
