import sys
from flask import Flask, render_template, url_for, request, redirect, url_for, session
app = Flask(__name__)

class Post:
    def __init__(self, username, content):
        self.username = username
        self.content = content
    def __str__(self):
        return self.username, self.content
postList = []
user_dataBase = {"txtxxu":"tiffanyxu816","bvaughn":"123","adam":"234","chris":"234"}

@app.route('/feed', methods=["GET", "POST"])  #feedpage after login
def feed():
     print("indx")
     if(session['logged_in'] == False):
         app.logger.info("I reached here")
         return redirect(url_for("login"))
     else:
         if request.method == "POST":
             content = request.form["tweet"] #request.form is a dictionary
             username = session['username']
             post = Post(username, content)
             postList.append(post)
             #return render_template() #enter html
         return render_template('NewsFeed.html')


@app.route('/login', methods=['GET', 'POST']) #log-in page
def login():
    if(session['logged_in'] == True):
        app.logger.info("trying to redirect")
        return redirect((url_for("feed")))
    app.logger.info("heyo")

    app.logger.info(request.method)
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        app.logger.info("before" + str(session['logged_in']))
        login_action(username, password)
        app.logger.info("logged_in" + str(session['logged_in']))
        return redirect(url_for("feed"))

    return render_template('prettyLogin.html')

def login_action(username, password):
     app.logger.info("loginac")
     if(username in user_dataBase and user_dataBase[username] == password):
        app.logger.info("yay")
        session['logged_in'] = True
        session["username"] = username


@app.route('/user/<username>') #user page
def user(username):
    userPosts = []
    for each in postList:
        if each.username == username:
            userPosts.append(each)
    for each in userPosts:
        print(each)
    return "My name is {}".format(username)

@app.route('/logout')
def logout():
    session['logged_in'] = False
    session['username'] = None
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.config["SECRET_KEY"] = "ITSASECRET"
    app.run(debug=True, use_reloader=False)
