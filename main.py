from flask import Flask, redirect, url_for, render_template
from sudoku import *

app = Flask(__name__)

# Defining the home page of our site
@app.route("/")
def home():
    ####TODO delete x and make it empty first and appear number when click button 
    return render_template("index.html", x = create_puzzle(sudoku_generator()))

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

@app.route("/admin")
def admin():
	return redirect(url_for("home"))

if __name__ == "__main__":
    app.run()