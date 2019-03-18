from flask import *

app = Flask(__name__)
@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        email = request.form["email"]
        print(email)
        password = request.form["password"]
        print(password)
    return render_template("index.html")

@app.route("/")
def redirectToHome():
    return redirect('/home')

@app.route("/register")
def register():
        return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=1)