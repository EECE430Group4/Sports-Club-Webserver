import mysql.connector
import sqlite3


def authenticate(username, password):
    conn = sqlite3.connect('database/430Group4.db')
    cursor = conn.cursor()
    cursor.execute("select username from users WHERE username='"+username+"'")
    res = cursor.fetchall()
    if len(res) == 0:
        return 1  # incorrect username, username does not exist

    cursor.execute(
        "select password from users WHERE username='"+str(username)+"'")
    res = cursor.fetchall()
    retPassword = res[0][0]
    if retPassword != password:
        return 2  # incorrect password
    cursor.execute("SELECT role from users where username='"+str(username)+"'")
    res = cursor.fetchall()
    role = res[0][0]
    cursor.close()
    conn.close()
    return role


def register(name, username, password):
    conn = sqlite3.connect('database/430Group4.db')
    cursor = conn.cursor()
    cursor.execute("select username from users WHERE username='"+username+"'")
    res = cursor.fetchall()
    if len(res) != 0:
        return 1  # username already exists in database

    SQL = '''insert into users(name,username,password,role)
            values ('{}','{}','{}','FAN')'''.format(name, username, password)
    cursor.execute(SQL)
    conn.commit()
    cursor.close()
    conn.close()
    return 0


def getArticle(aid):
    conn = sqlite3.connect('database/430Group4.db')
    cursor = conn.cursor()
    cursor.execute(
        "select articletitle, articleheadline, articlebody from article WHERE articleid='"+str(aid)+"'")
    res = cursor.fetchall()
    cursor.close()
    conn.close()
    return (res[0][0], res[0][1], res[0][2])


def updateArticle(aid, title, hd, body):
    conn = sqlite3.connect('database/430Group4.db')
    cursor = conn.cursor()
    SQL = "UPDATE article SET articletitle ='" + title+"', articleheadline ='" + \
        hd+"', articlebody ='"+body+"' WHERE articleid='"+str(aid)+"'"
    cursor.execute(SQL)
    conn.commit()
    cursor.close()
    conn.close()


def getPlayers(team):
    conn = sqlite3.connect('database/430Group4.db')
    cursor = conn.cursor()
    cursor.execute("select * from players WHERE team='"+team+"'")
    res = cursor.fetchall()
    players = []
    for row in res:
        players.append(row)
    conn = sqlite3.connect('database/430Group4.db')
    cursor = conn.cursor()
    return players
