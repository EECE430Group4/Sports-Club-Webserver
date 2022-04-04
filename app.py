from flask import Flask, render_template, redirect, url_for, session, request, abort
from functions import *


app = Flask(__name__)
app.secret_key = "uehwr3493423j4j239k@#323i213ji3123"


@app.route('/')
def main():
    if 'user' in session:
        user = session['user']
    else:
        user = None
    return render_template('HomePage.html', user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user' in session:
        return redirect(url_for('main'))
    elif request.method == 'POST':
        user = request.form["userName"]
        password = request.form["password"]
        ret = authenticate(user, password)
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
    elif request.method == 'POST':
        name = request.form["Name"]
        user = request.form["userName"]
        password = request.form["password"]
        ret = register(name, user, password)
        if ret == 1:
            return render_template('signup.html', error="Username already exists!")
        elif ret == 0:
            session['user'] = user
            session['role'] = 'FAN'
            return redirect(url_for('main'))
    return render_template('signup.html')


@app.route('/news', methods=['GET'])
def getNews():
    if 'user' in session:
        user = session['user']
    else:
        user = None
    return render_template('news.html', user=user)


@app.route('/teams/<team>')
def getTeam(team):
    if 'user' in session:
        user = session['user']
    else:
        user = None

    if team == "womenfb":
        return(render_template('womenfb.html', user=user))
    elif team == "womenbb":
        return(render_template('womenbb.html', user=user))
    elif team == "menfb":
        return(render_template('menfb.html', user=user))
    elif team == "menbb":
        return(render_template('menbb.html', user=user))
    
    return(redirect(url_for('main')))

@app.route('/fixtures')
def getFixtures():
    if 'user' in session:
        user = session['user']
    else:
        user = None
    return render_template('fixtures.html', user=user)

@app.route('/shop')
def getShop():
    if 'user' in session:
        user = session['user']
    else:
        user = None
    return render_template('shop.html', user=user)
    
if __name__ == "__main__":
    app.run(debug=True)