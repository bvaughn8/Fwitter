import sys
from flask import Flask, render_template, url_for, request, redirect, url_for, session
app = Flask(__name__)

class Post:
    def __init__(self, username, content):
        self.username = username
        self.content = content
postList = []
user_dataBase = {"txtxxu":"tiffanyxu816","bvaughn":"123","adam":"234","chris":"234"}

@app.route('/feed', methods=["GET", "POST"])  #feedpage after login
def feed():
     print("indx")
     if(session['logged_in'] == False):
         app.logger.info("I reached here")
         redirect(url_for("login"))
     else:
         if request.method == "POST":
             content = request.form["tweet"] #request.form is a dictionary
             username = session['username']
             post = Post(username, content)
             postList.append(post)
             #return render_template() #enter html
         return postList


@app.route('/login', methods=['GET', 'POST']) #log-in page
def login():
    if(session['logged_in'] == True):
        app.logger.info("trying to redirect")
        redirect(url_for("feed"))
    app.logger.info("heyo")

    if request.method == 'POST':
         username = request.form["username"]
         password = request.form["password"]
         app.logger.info("before" + str(session['logged_in']))
         login_action(username, password)
         app.logger.info("logged_in" + str(session['logged_in']))
         redirect(url_for("feed"))
    return render_template('loginScript2.html')
    return "mfw"

def login_action(username, password):
     print("loginac")
     if(username in user_dataBase and user_dataBase[username] == password):
        print("yay")
        session['logged_in'] = True
        session["username"] = username


@app.route('/user/<username>') #user page
def user(username):
     userPosts = []
     for each in postList:
         if each.username == username:
             userPosts.append(each)
     return "My name is {}".format(username)

@app.route('/logout')
def logout():
    session['logged_in'] = False
    session['username'] = None
    return #redirect(url_for('/login'))

if __name__ == "__main__":
    app.config["SECRET_KEY"] = "ITSASECRET"
    app.run(debug=True, use_reloader=False)
