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


def getArticle(aid):
    conn = mysql.connector.connect(host='35.246.1.16',
                                   database='430Group4',
                                   user='root',
                                   password='root430group4root')
    cursor = conn.cursor()
    cursor.execute("select articletitle, articleheadline, articlebody from article WHERE articleid='"+str(aid)+"'")
    res = cursor.fetchall()
    return (res[0][0],res[0][1],res[0][2])

def updateArticle(aid,title,hd,body):
    conn = mysql.connector.connect(host='35.246.1.16',
                                   database='430Group4',
                                   user='root',
                                   password='root430group4root')
    cursor = conn.cursor()
    SQL = "UPDATE article SET articletitle ='" +title+"', articleheadline ='" +hd+"', articlebody ='"+body+"' WHERE articleid='"+str(aid)+"'"
    cursor.execute(SQL)
    conn.commit()

def getPlayers(team):
    conn = mysql.connector.connect(host='35.246.1.16',
                                   database='430Group4',
                                   user='root',
                                   password='root430group4root')
    cursor = conn.cursor()
    cursor.execute("select * from players WHERE team='"+team+"'")
    res = cursor.fetchall()
    players = []
    for row in res:
        players.append(row)
    return players

print(getPlayers('womenbb'))
    

