from flask import *
from flask_login import UserMixin, login_user, logout_user, login_manager, login_required

app = Flask(__name__)
loginManager = login_manager()
loginManager.init_app(app)
loginManager.login_view = "home"

class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(id):
    return User(id)

testuser = "test@test.com"
testpassword = "test"

@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        if email == testuser and password == testpassword:
            login_user()
    return render_template("index.html")

@app.route("/")
def redirectToHome():
    return redirect('/home')

@app.route("/register")
def register():
        return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=1)