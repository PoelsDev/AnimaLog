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

if __name__ == "__main__":
    app.run(debug=1)