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
    length = len(players)
    remaining = 50-length
    i = 0
    for i in range(0, remaining):
        players.append([None])
        i = i+1

    cursor.close()
    conn.close()
    return players



def getItem():
    conn = sqlite3.connect('database/430Group4.db')
    cursor = conn.cursor()
    cursor.execute("select * from shop")
    res = cursor.fetchall()
    items = []
    for row in res:
        items.append(row)
    length = len(items)
    remaining = 50-length
    i = 0
    for i in range(0, remaining):
        items.append([None])
        i = i+1

    cursor.close()
    conn.close()
    return items


def addItem(name, Sstock, Mstock, Lstock, price):
    conn = sqlite3.connect('database/430Group4.db')
    cursor = conn.cursor()
    cursor.execute(
        "select shopitemid from shop ORDER BY shopitemid DESC LIMIT 1")
    res = cursor.fetchall()
    lastId = res[0][0]
    newId = str(int(lastId)+1)

    cursor.execute("INSERT INTO shop (shopitemid, sizeSstock, sizeMstock, sizeLstock, itemprice, itemName) VALUES ('" +
                   newId+"', '"+Sstock+"', '"+Mstock+"','"+Lstock+"', '"+price+"', '"+name+"')")
    conn.commit()
    cursor.close()
    conn.close()



def deleteItem(itemid):
    conn = sqlite3.connect('database/430Group4.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM shop WHERE shopitemid= '"+itemid+"'")
    conn.commit()
    cursor.close()
    conn.close()


def getTicket():
    conn = sqlite3.connect('database/430Group4.db')
    cursor = conn.cursor()
    cursor.execute("select * from tickets")
    res = cursor.fetchall()
    tickets = []
    for row in res:
        tickets.append(row)
    length = len(tickets)
    remaining = 50-length
    i = 0
    print(remaining)
    for i in range(0, remaining):
       ## tickets.append([None])
        i = i+1
    cursor.close()
    conn.close()
    return tickets

def addTicket(oppteam, tickettime, arena, price, stock):
    conn = sqlite3.connect('database/430Group4.db')
    cursor = conn.cursor()
    cursor.execute(
        "select ticketid from tickets ORDER BY ticketid ASC LIMIT 1")
    res = cursor.fetchall()
    lastId = res[0][0]
    newId = str(int(lastId)-1)

    cursor.execute("INSERT INTO tickets (ticketid, oppteam, tickettime, arena, ticketprice, stock) VALUES ('" +
                   newId+"', '"+oppteam+"', '"+tickettime+"','"+arena+"', '"+price+"', '"+stock+"')")
    conn.commit()
    cursor.close()
    conn.close()

def deleteTicket(ticketid):
    conn = sqlite3.connect('database/430Group4.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tickets WHERE ticketid= '"+ticketid+"'")
    conn.commit()
    cursor.close()
    conn.close()


def addGames(sport, club1, score, club2, date):
    conn = sqlite3.connect('database/430Group4.db')
    cursor = conn.cursor()
    SQL = '''insert into games (sport,club1,score,club2,gamedate) values ('{}','{}','{}','{}','{}')'''.format(
        sport, club1, score, club2, date)
    cursor.execute(SQL)
    conn.commit()
    cursor.close()
    conn.close()


def editGames(ID, sport, club1, score, club2, date):
    conn = sqlite3.connect('database/430Group4.db')
    cursor = conn.cursor()
    SQL = "UPDATE games set sport='"+sport+"',club1='"+club1+"', club2='" + \
        club2+"',gamedate='"+date+"',score='"+score+"' WHERE ID="+ID
    cursor.execute(SQL)
    conn.commit()
    cursor.close()
    conn.close()


def deleteGames(ID):
    conn = sqlite3.connect('database/430Group4.db')
    cursor = conn.cursor()
    SQL = "DELETE from games where ID="+ID
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


def deletePosts():
    conn = sqlite3.connect('database/430Group4.db')
    cursor = conn.cursor()
    cursor.execute("delete from posts")
    conn.commit()
    cursor.close()
    conn.close()


def getPosts():
    conn = sqlite3.connect('database/430Group4.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * from posts")
    res = cursor.fetchall()
    posts = []
    for row in res:
        posts.append(row)
    return posts


def getPosts():
    conn = sqlite3.connect('database/430Group4.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * from posts")
    res = cursor.fetchall()
    posts = []
    for row in res:
        posts.append(row)
    return posts


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


def getTrophyB(aid, sport):
    conn = sqlite3.connect('database/430Group4.db')
    cursor = conn.cursor()
    cursor.execute("select trophy, year from honors WHERE trophy_id='" +
                   str(aid)+"' AND sport='"+sport+"'")

    res = cursor.fetchall()
    cursor.close()
    conn.close()
    return res


def addTrophiesB(title, year, sport):
    conn = sqlite3.connect('database/430Group4.db')
    cursor = conn.cursor()
    cursor.execute(
        "select trophy_id from honors ORDER BY trophy_id DESC LIMIT 1")
    res = cursor.fetchall()
    lastId = res[0][0]
    newId = str(int(lastId)+1)

    cursor.execute("INSERT INTO honors (trophy_id, trophy, year, sport) VALUES ('" +
                   newId+"', '"+title+"', '"+year+"', '"+sport+"')")

    conn.commit()
    cursor.close()
    conn.close()


def deleteTrophyB(trophy_id, sport):
    conn = sqlite3.connect('database/430Group4.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM honors WHERE trophy_id= '" +
                   trophy_id+"' AND sport='"+sport+"'")

    conn.commit()
    cursor.close()
    conn.close()


def getGames():
    conn = sqlite3.connect('database/430Group4.db')
    cursor = conn.cursor()
    cursor.execute("select * from games")
    res = cursor.fetchall()
    games = []
    for row in res:
        games.append(row)
    cursor.close()
    conn.close()
    return games


def getGames():
    conn = sqlite3.connect('database/430Group4.db')
    cursor = conn.cursor()
    cursor.execute("select * from games")
    res = cursor.fetchall()
    games = []
    for row in res:
        games.append(row)
    cursor.close()
    conn.close()
    return games


def getTrophyBS(sport):
    conn = sqlite3.connect('database/430Group4.db')
    cursor = conn.cursor()
    cursor.execute("select * from honors WHERE sport='"+sport+"'")
    res = cursor.fetchall()
    trophies = []
    for row in res:
        trophies.append(row)
    length = len(trophies)
    remaining = 50-length
    i = 0
    for i in range(0, remaining):
        trophies.append([None])
        i = i+1

    cursor.close()
    conn.close()
    return trophies


def changeUser(user, username):
    conn = sqlite3.connect('database/430Group4.db')
    cursor = conn.cursor()
    SQL = "UPDATE users SET username ='" + username+"' WHERE username='"+user+"'"
    try:
        cursor.execute(SQL)
        conn.commit()
    except Exception as e:
        print(e)
        cursor.close()
        conn.close()
        return "err"
    cursor.close()
    conn.close()
    return 0


def changePassword(user,  password):
    conn = sqlite3.connect('database/430Group4.db')
    cursor = conn.cursor()
    SQL = "UPDATE users SET password ='" + password + \
        "' WHERE username='"+user+"'"
    try:
        cursor.execute(SQL)
        conn.commit()
    except Exception as e:
        print(e)
        cursor.close()
        conn.close()
        return "err"
    cursor.close()
    conn.close()
    return 0
