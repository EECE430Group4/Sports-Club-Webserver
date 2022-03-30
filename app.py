from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def main():
    return redirect(url_for('getLogin'))


@app.route('/login', methods=['GET'])
def getLogin():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def postLogin():
    # logging in code goes here
    return render_template('login.html')


@app.route('/signup', methods=['GET'])
def getSignup():
    return render_template('signup.html')


@app.route('/signup', methods=['GET'])
def postSignup():
    # signing up code goes here
    return render_template('signup.html')


@app.route('/news', methods=['GET'])
def getNews():
    return render_template('news.html')


if __name__ == "__main__":
    app.run(debug=True)
