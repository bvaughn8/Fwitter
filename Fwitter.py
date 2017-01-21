from flask import Flask, render_template, url_for, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_required, current_user, login_user
app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)

class Post:
    def __init__(self, username, content):
        self.username = username
        self.content = content
postList = []
user_dataBase = {"txtxxu":"tiffanyxu816","bvaughn":"123","adam":"234","chris":"234"}

class User(UserMixin):
    def __init__(self, username, password):
        self.username = username
        self.password = password

@app.route('/feed', methods=["GET", "POST"])  #feedpage after login
#@login_required
def index():
    if request.method == "POST":
        content = request.form["tweet"] #request.form is a dictionary
        username = current_user.username
        post = Post(username, content)
        postList.append(post)
    #return render_template() #enter html
    return postList

@app.route('/login', methods=['GET', 'POST']) #log-in page
def login():
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        login_action(username, password)
        redirect(url_for('index'))
    return render_template('loginScript2.html')

@login_manager.user_loader
def login_action(username, password):
    if(username in user_dataBase and user_dataBase[username] == password):
        return User(username, password)
    return None



@app.route('/user/<username>') #user page
#@login_required
def user(username):
    return "My name is {}".format(username)

@app.route('/logout')
def logout():
    return redirect(url_for('/login'))

if __name__ == "__main__":
    app.run()
