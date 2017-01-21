from flask import Flask, render_template, url_for, request
from flask_login import LoginManager, UserMixin, login_required, current_user
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
    
@app.route('/login', methods=['GET', 'POST']) #log-in page 
def login():
    return "login screen"


@app.route('/feed', methods=["POST"])  #feedpage after login
@login_required
def index():
    if request.method == "POST":
        content = request.form["tweet"] #request.form is a dictionary
        username = current_user.username
        post = Post(username, content)
        postList.append(post)
    #return render_template() #enter html
    return postList
    
@app.route('/user/<username>') #user page 
def user(username):
    userPosts = []
    for each in postList:
        if each.username == username:
            userPosts.append(each)
    return "My name is {}".format(username)

@app.route('/logout')
def logout():
    return redirect(url_for('/login'))

if __name__ == "__main__":
    app.run()
