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
    cursor.close()
    conn.close()
    return players


def getItem(row):
    conn = sqlite3.connect('database/430Group4.db')
    cursor = conn.cursor()
    cursor.execute(
        "select sizeSstock, sizeMstock, sizeLstock, itemprice, itemName, shopitemid from shop WHERE rownum="+str(row)+"")
    res = cursor.fetchall()
    cursor.close()
    conn.close()
    return (res[0][0], res[0][1], res[0][2], res[0][3], res[0][4], res[0][5])


def addGames(sport, club1, score, club2, date):
    conn = sqlite3.connect('database/430Group4.db')
    cursor = conn.cursor()
    SQL = '''insert into games (sport,club1,score,club2,date) values ('{}','{}','{}','{}','{}')'''.format(
        sport, club1, score, club2, date)
    cursor.execute(SQL)
    conn.commit()
    cursor.close()
    conn.close()


def editGames(sport, club1, club2, date, score):
    conn = sqlite3.connect('database/430Group4.db')
    cursor = conn.cursor()
    SQL = "UPDATE games set sport='"+sport+"',club1='"+club1 + \
        "', club2='"+club2+"',date='"+date+"',score='"+score+"'"
    cursor.execute(SQL)


def deleteGames(sport, club1, club2, date):
    conn = sqlite3.connect('database/430Group4.db')
    cursor = conn.cursor()
    SQL = "DELETE from games where sport='"+sport + \
        "',club1='"+club1+"', club2='"+club2+"',date='"+date+"'"
    cursor.execute(SQL)
    conn.commit()
    cursor.close()
    conn.close()


def addPost(username, dateposted, body):
    conn = sqlite3.connect('database/430Group4.db')
    cursor = conn.cursor()
    cursor.execute("insert into posts VALUES('{}','{}','{}')".format(
        username, dateposted, body))
    conn.commit()
    cursor.close()
    conn.close()


def deletePost(username, dateposted):
    conn = sqlite3.connect('database/430Group4.db')
    cursor = conn.cursor()
    cursor.execute("delete from posts where username='" +
                   username+"' and dateposted='"+dateposted+"'")
    conn.commit()
    cursor.close()
    conn.close()


def addPlayerWomenbb(name, age, position, points, assists):
    conn = sqlite3.connect('database/430Group4.db')
    cursor = conn.cursor()
    cursor.execute(
        "select playerid from players ORDER BY playerid DESC LIMIT 1")
    res = cursor.fetchall()
    lastId = res[0][0]
    newId = str(int(lastId)+1)

    cursor.execute("INSERT INTO players (playerid, name, age, team, position, points, assists) VALUES ('" +
                   newId+"', '"+name+"', '"+age+"', 'womenbb', '"+position+"', '"+points+"', '"+assists+"')")
    conn.commit()
    cursor.close()
    conn.close()


def deletePlayerWomenbb(playerid):
    conn = sqlite3.connect('database/430Group4.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM players WHERE playerid= '"+playerid+"'")
    conn.commit()
    cursor.close()
    conn.close()


def getTrophyB(aid):
    conn = sqlite3.connect('database/430Group4.db')
    cursor = conn.cursor()
    cursor.execute(
        "select trophy, year from honorsBB WHERE trophy_id='"+str(aid)+"'")
    res = cursor.fetchall()
    cursor.close()
    conn.close()
    return (res[0][0], res[0][1], res[0][2])


def updateTrophyB(aid, title, year):
    conn = sqlite3.connect('database/430Group4.db')
    cursor = conn.cursor()
    SQL = "UPDATE honorsBB SET trophy ='" + title+"', year ='" + \
        year+"' WHERE trophy_id='"+str(aid)+"'"
    cursor.execute(SQL)
    conn.commit()
    cursor.close()
    conn.close()
