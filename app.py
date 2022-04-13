from asyncio import trsock
from turtle import update
from flask import Flask, render_template, redirect, url_for, session, request, abort
import functions
import sqlite3

import datetime


app = Flask(__name__)
app.secret_key = "uehwr3493423j4j239k@#323i213ji3123"

# --------------------------- HOMEPAGE ---------------------------


@app.route('/')
def main():
    if 'user' in session:
        user = session['user']
    else:
        user = None
    if 'cart' not in session:
        session['cart'] = []
    return render_template('HomePage.html', user=user)

# --------------------------- LOGIN + SIGNUP + LOGOUT ---------------------------


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user' in session:
        return redirect(url_for('main'))
    elif request.method == 'POST':
        user = request.form["userName"]
        password = request.form["password"]
        ret = functions.authenticate(user, password)
        if ret == 1:
            return render_template('login.html', error="Username does not exist!")
        elif ret == 2:
            return render_template('login.html', error="Incorrect Password!")
        elif ret == 'FAN' or ret == 'PLAYER' or ret == 'ADMIN':
            session['user'] = user
            session['role'] = ret
            session['cart'] = []
        return redirect(url_for('main'))
    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if 'user' in session:
        return redirect(url_for('main'))
    if request.method == 'POST':
        name = request.form["Name"]
        user = request.form["userName"]
        password = request.form["password"]
        ret = functions.register(name, user, password)
        if ret == 1:
            return render_template('signup.html', error="Username already exists!")
        elif ret == 0:
            session['user'] = user
            session['role'] = 'FAN'

            return redirect(url_for('main'))
    return render_template('signup.html')


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()
    return redirect(url_for('main'))


# --------------------------- NEWS ---------------------------


@app.route('/news', methods=['GET', 'POST'])
def getNews():
    if 'user' in session:
        user = session['user']
        role = session['role']
    else:
        user = None
        role = ""

    articles = []
    for i in range(1, 6):
        articles.append(functions.getArticle(i))

    if request.method == 'POST':
        if 'readbut' in request.form:
            if request.form["readbut"] == "1":
                return redirect(url_for('getArticle', anum=1))
            elif request.form["readbut"] == "2":
                return redirect(url_for('getArticle', anum=2))
            elif request.form["readbut"] == "3":
                return redirect(url_for('getArticle', anum=3))
            elif request.form["readbut"] == "4":
                return redirect(url_for('getArticle', anum=4))
            elif request.form["readbut"] == "5":
                return redirect(url_for('getArticle', anum=5))
        elif 'editbut' in request.form:
            if request.form["editbut"] == "1":
                return redirect(url_for('editArticle', anum=1))
            elif request.form["editbut"] == "2":
                return redirect(url_for('editArticle', anum=2))
            elif request.form["editbut"] == "3":
                return redirect(url_for('editArticle', anum=3))
            elif request.form["editbut"] == "4":
                return redirect(url_for('editArticle', anum=4))
            elif request.form["editbut"] == "5":
                return redirect(url_for('editArticle', anum=5))

    return render_template('news.html', user=user, role=role, articles=articles)


@app.route('/news/article/<anum>', methods=['GET'])
def getArticle(anum):
    if 'user' in session:
        user = session['user']
        role = session['role']
    else:
        user = None
        role = ""
    article = functions.getArticle(anum)
    return render_template('article.html', user=user, role=role, article=article)


@app.route('/news/article/edit/<anum>', methods=['GET', 'POST'])
def editArticle(anum):
    if 'user' in session:
        user = session['user']
        role = session['role']
        if role != 'ADMIN':
            return redirect(url_for('main'))
        if request.method == 'POST':
            title = request.form['title']
            headline = request.form['headline']
            body = request.form['body']
            functions.updateArticle(anum, title, headline, body)
            return redirect(url_for('getNews'), code=303)
        article = functions.getArticle(anum)
        return render_template('editarticle.html', user=user, role=role, article=article, anum=anum)
    else:
        return redirect(url_for('main'))

# --------------------------- TEAMS ---------------------------


@app.route('/teams/<team>')
def getTeam(team):
    if 'user' in session:
        user = session['user']
    else:
        user = None

    if team == "womenfb":
        return(render_template('womenfb.html', user=user))
    elif team == "womenbb":
        players = functions.getPlayers(team)
        return(render_template('womenbb.html', user=user, players=players))
    elif team == "menfb":
        return(render_template('menfb.html', user=user))
    elif team == "menbb":
        return(render_template('menbb.html', user=user))

    return(redirect(url_for('main')))


@app.route('/<team>/addPlayer', methods=['POST'])
def addPlayer(team):
    if 'user' in session:
        user = session['user']
        role = session['role']
    else:
        user = None

    name = request.form["playerNameAdd"]
    age = request.form["playerAgeAdd"]
    position = request.form["playerPositionAdd"]
    points = request.form["playerPointsAdd"]
    assists = request.form["playerAssistsAdd"]

    if team == "womenfb":
        return(render_template('womenfb.html', user=user))
    elif team == "womenbb":
        players = functions.getPlayers(team)
        functions.addPlayerWomenbb(name, age, position, points, assists)
        return(render_template('womenbb.html', user=user, players=players))
    elif team == "menfb":
        return(render_template('menfb.html', user=user))
    elif team == "menbb":
        return(render_template('menbb.html', user=user))

    return(redirect(url_for('main')))


@app.route('/<team>/deletePlayer', methods=['POST'])
def deletePlayer(team):
    if 'user' in session:
        user = session['user']
    else:
        user = None

    playerid = request.form["playerIdDelete"]

    if team == "womenfb":
        return(render_template('womenfb.html', user=user))
    elif team == "womenbb":
        players = functions.getPlayers(team)
        functions.deletePlayerWomenbb(playerid)
        return(render_template('womenbb.html', user=user, players=players))
    elif team == "menfb":
        return(render_template('menfb.html', user=user))
    elif team == "menbb":
        return(render_template('menbb.html', user=user))

    return(redirect(url_for('main')))

# --------------------------- FIXTURES ---------------------------


@app.route('/fixtures')
def getFixtures():
    if 'user' in session:
        user = session['user']
        role = session['role']
    else:
        user = None
        role = ''
    return render_template('fixtures.html', user=user, role=role)

# --------------------------- SHOP ---------------------------


@app.route('/shop', methods=['GET', 'POST'])
def getShop():
    if 'user' in session:
        user = session['user']
        role = session['role']
    else:
        user = None
        role = ""

    items = []
    for i in range(1, 9):
        items.append(functions.getItem(i))

    if request.method == 'POST':
        if 'addcartbut' in request.form:
            return redirect(url_for('addItemCart', itemid=request.form["itemid"]))

    return render_template('shop.html', user=user, role=role, items=items)


@app.route('/shop/additemcart/<itemid>')
def addItemCart(itemid):
    if 'user' in session:
        user = session['user']
        role = session['role']
    else:
        user = None
        role = ""
    session['cart'].append(itemid)

    return(redirect(url_for('getShop')))


@app.route('/shop/additem', methods=['POST'])
def addItem():
    if 'user' in session:
        user = session['user']
        role = session['role']
    else:
        user = None

    name = request.form["itemNameAdd"]
    price = request.form["itemPriceAdd"]
    Sstock = request.form["itemsizeSAdd"]
    Mstock = request.form["itemsizeMAdd"]
    Lstock = request.form["itemsizeLAdd"]

    functions.addItem(name, Sstock, Mstock, Lstock, price)

    return(redirect(url_for('getShop')))


@app.route('/shop/deleteItem', methods=['POST'])
def deleteItem():
    if 'user' in session:
        user = session['user']
    else:
        user = None

    itemid = request.form["itemidRemove"]

    functions.deleteItem(itemid)

    return(redirect(url_for('getShop')))

# --------------------------- PROFILE ---------------------------


@app.route('/profile')
def getProfile():
    if 'user' in session:
        user = session['user']
        role = session['role']
    else:
        user = None
        role = ""
    return render_template('profile_edit_prof.html', user=user, role=role)


@app.route('/profile/settings')
def getProfileSetting():
    if 'user' in session:
        user = session['user']
        role = session['role']
    else:
        user = None
        role = ""
    conn = sqlite3.connect('database/430Group4.db')
    cursor = conn.cursor()
    cursor.execute("select password from users WHERE username='" + user+"'")
    res = cursor.fetchall()[0][0]
    return render_template('profile_account_settings.html', user=user, role=role, oldpass=res)


@app.route('/profile/change', methods=['POST'])
def changeProfile():
    if 'user' in session:
        user = session['user']
        role = session['role']
    else:
        return redirect(url_for('main'))

    username = request.form['newuser']
    functions.changeUser(user, username)
    session['user'] = username
    return redirect(url_for('getProfile'))


@app.route('/profile/settings/change', methods=['POST'])
def changeProfileSetting():
    if 'user' in session:
        user = session['user']
        role = session['role']
    else:
        return redirect(url_for('main'))

    oldpassword = request.form['oldpwd']
    password = request.form['password']
    functions.changePassword(user, password)
    return redirect(url_for('getProfileSetting'))

# --------------------------- TICKETS ---------------------------


@app.route('/tickets')
def getTickets():
    if 'user' in session:
        user = session['user']
    else:
        user = None
    return render_template('tickets.html', user=user)

# --------------------------- HONORS FOOTBALL---------------------------


@app.route('/honorsfb', methods=['GET', 'POST'])
def getHonorsFB():
    if 'user' in session:
        user = session['user']
        role = session['role']
    else:
        user = None
        role = ""
    trophies = []
    for i in range(1, 6):
        trophies.append(functions.getTrophyB(i, "football"))

    return render_template('honorsfb.html', user=user, role=role, trophies=trophies)


@app.route('/honorsfb/addTrophyF', methods=['POST'])
def addTrophyF():
    if 'user' in session:
        user = session['user']
        role = session['role']
    else:
        user = None
        role = ""
    if role != 'ADMIN':
        return redirect(url_for('main'))
    title = request.form["title_add"]
    year = request.form["year_add"]
    trophyF = []
    for i in range(1, 6):
        trophyF.append(functions.getTrophyB(i, "football"))
    functions.addTrophiesB(title, year, "football")
    return(redirect(url_for('getHonorsFB')))


@app.route('/honorsfb/deleteTrophyF', methods=['POST'])
def deleteTrophyF():
    if 'user' in session:
        user = session['user']
    else:
        user = None

    trophy_id = request.form["trophy_id_delete"]
    trophyF = []
    for i in range(1, 6):
        trophyF.append(functions.getTrophyB(i, "football"))
    functions.deleteTrophyB(trophy_id, "football")
    return(redirect(url_for('getHonorsFB')))

# --------------------------- HONORS BASKETBALL ---------------------------


@app.route('/honorsbb', methods=['GET', 'POST'])
def getHonorsBB():
    if 'user' in session:
        user = session['user']
        role = session['role']
    else:
        user = None
        role = ""
    trophies = []
    for i in range(1, 6):
        trophies.append(functions.getTrophyB(i, "basketball"))

    return render_template('honorsbb.html', user=user, role=role, trophies=trophies)


@app.route('/honorsbb/addTrophyB', methods=['POST'])
def addTrophyB():
    if 'user' in session:
        user = session['user']
        role = session['role']
    else:
        user = None
        role = ""
    if role != 'ADMIN':
        return redirect(url_for('main'))
    title = request.form["title_add"]
    year = request.form["year_add"]
    trophyB = []
    for i in range(1, 6):
        trophyB.append(functions.getTrophyB(i, "basketball"))
    functions.addTrophiesB(title, year, "basketball")
    return(redirect(url_for('getHonorsBB')))


@app.route('/honorsbb/deleteTrophyB', methods=['POST'])
def deleteTrophyB():
    if 'user' in session:
        user = session['user']
    else:
        user = None

    trophy_id = request.form["trophy_id_delete"]
    trophyB = []
    for i in range(1, 6):
        trophyB.append(functions.getTrophyB(i, "basketball"))
    functions.deleteTrophyB(trophy_id, "basketball")
    return(redirect(url_for('getHonorsFB')))


# -------------------------- COMMUNITY -------------------------------


@app.route('/community', methods=['GET', 'POST'])
def getCommunity():
    if 'user' in session:
        user = session['user']
        role = session['role']
    else:
        user = None
        role = ""

    posts = functions.getPosts()
    return render_template('community.html', user=user, role=role, posts=posts)


@app.route('/community/addPost', methods=['POST'])
def postCommunity():
    if 'user' in session:
        user = session['user']
        role = session['role']
    else:
        user = None
        role = ""

    if user is not None:
        dateposted = datetime.datetime.now().date()
        body = request.form['body']
        functions.addPost(user, dateposted, body)

    return(redirect(url_for('getCommunity')))


@app.route('/community/clearPosts', methods=['GET', 'POST'])
def delCommunity():
    if 'user' in session:
        user = session['user']
        role = session['role']
        if role != 'ADMIN':
            return(redirect(url_for('getCommunity')))
    else:
        return(redirect(url_for('getCommunity')))

    functions.deletePosts()
    return(redirect(url_for('getCommunity')))


if __name__ == "__main__":
    app.run(debug=True)
