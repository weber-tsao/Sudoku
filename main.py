from flask import Flask, redirect, url_for, render_template, request
from sudoku import *

app = Flask(__name__)

random_board = create_puzzle(sudoku_generator())

# Defining the home page of the web app
####TODO delete x and make it empty first and appear number when click button 
# (or use session to store the previous board)####
@app.route("/sudoku", methods=["POST", "GET"])
def sudoku():
    
    if request.method == "POST":
        if request.form.get("change_board"):
            global random_board 
            random_board = create_puzzle(sudoku_generator())
            return render_template("index.html", x = random_board)
        
        elif request.form.get("check_answer"):
            return render_template("index.html", x = random_board)
        
        elif request.form.get("see_solution"):
            solve_sudoku(random_board)
            return render_template("index.html", x = random_board)
        
        else: 
            return render_template("index.html", x = random_board)
        
    else:
        return render_template("index.html", x = random_board)

if __name__ == "__main__":
    app.run()