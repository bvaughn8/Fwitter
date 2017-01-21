from flask import Flask
app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST']) #log-in page 
def login():
    return 


@app.route('/')  #feedpage after login
def index():
    return "FWITTER"


@app.route('/user/<username>') #user page 
def user(username):
    return "My name is {}".format(username)




if __name__ == "__main__":
    app.run()
