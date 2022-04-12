from turtle import update
from flask import Flask, render_template, redirect, url_for, session, request, abort
import functions


app = Flask(__name__)
app.secret_key = "uehwr3493423j4j239k@#323i213ji3123"

#--------------------------- HOMEPAGE ---------------------------
@app.route('/')
def main():
    if 'user' in session:
        user = session['user']
    else:
        user = None
    return render_template('HomePage.html', user=user)

#--------------------------- LOGIN + SIGNUP ---------------------------
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

#--------------------------- NEWS ---------------------------
@app.route('/news', methods=['GET','POST'])
def getNews():
    if 'user' in session:
        user = session['user']
        role = session['role']
    else:
        user = None
        role = ""

    articles = []
    for i in range(1,6):
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

    return render_template('news.html', user=user, role=role,articles=articles)

@app.route('/news/article/<anum>', methods=['GET'])
def getArticle(anum):
    if 'user' in session:
        user = session['user']
        role = session['role']
    else:
        user = None
        role = ""
    article = functions.getArticle(anum)
    return render_template('article.html', user=user, role=role,article=article)

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
            functions.updateArticle(anum,title,headline,body)
            return redirect(url_for('getNews'),code=303)
        article = functions.getArticle(anum)
        return render_template('editarticle.html', user=user, role=role,article=article,anum=anum)
    else:
        return redirect(url_for('main'))
    
#--------------------------- TEAMS ---------------------------

@app.route('/teams/<team>')
def getTeam(team):
    if 'user' in session:
        user = session['user']
    else:
        user = None

    if team == "womenfb":
        return(render_template('womenfb.html', user=user))
    elif team == "womenbb":
        players= functions.getPlayers(team)
        return(render_template('womenbb.html', user=user, players=players))
    elif team == "menfb":
        return(render_template('menfb.html', user=user))
    elif team == "menbb":
        return(render_template('menbb.html', user=user))
    
    return(redirect(url_for('main')))

#--------------------------- FIXTURES ---------------------------

@app.route('/fixtures')
def getFixtures():
    if 'user' in session:
        user = session['user']
        role = session['role']
    else:
        user = None
        role = ''
    return render_template('fixtures.html', user=user, role=role)

#--------------------------- SHOP ---------------------------

@app.route('/shop')
def getShop():
    if 'user' in session:
        user = session['user']
    else:
        user = None
    return render_template('shop.html', user=user)

#--------------------------- PROFILE ---------------------------

@app.route('/profile')
def getProfile():
    if 'user' in session:
        user = session['user']
        role = session['role']
    else:
        user = None
        role = ""
    return render_template('profile_edit_prof.html ', user=user, role=role)

@app.route('/profileSetting')
def getprofileSetting():
    if 'user' in session:
        user = session['user']
        role = session['role']
    else:
        user = None
        role = ""
    return render_template('profile_account_settings.html', user=user, role=role)

#--------------------------- TICKETS ---------------------------

@app.route('/tickets')
def getTickets():
    if 'user' in session:
        user = session['user']
    else:
        user = None
    return render_template('tickets.html', user=user)

#--------------------------- HONORS FOOTBALL---------------------------
@app.route('/honorsfb')
def getHonors():
    if 'user' in session:
        user = session['user']
    else:
        user = None
    return render_template('honorsfb.html', user=user)

#--------------------------- HONORS BASKETBALL ---------------------------
@app.route('/honorsbb')
def getHonorsB():
    if 'user' in session:
        user = session['user']
    else:
        user = None
    return render_template('honorsbb.html', user=user)



if __name__ == "__main__":
    app.run(debug=True)


