from flask import Flask, redirect, url_for, render_template, request
from sudoku import *
import copy


app = Flask(__name__)

random_board = create_puzzle(sudoku_generator())
current_board = copy.deepcopy(random_board)

# Defining the home page of the web app
####TODO delete x and make it empty first and appear number when click button 
# (or use session to store the previous board)####
@app.route("/", methods=["POST", "GET"])
def sudoku():
    
    if request.method == "POST":
        if request.form.get("change_board"):
            global random_board 
            random_board = create_puzzle(sudoku_generator())
            global current_board 
            current_board = copy.deepcopy(random_board)
            return render_template("index.html", x = random_board, y = 0)
        
        elif request.form.get("check_answer"):
            input_number = request.form.getlist('num')
            row = request.form.getlist('row')
            col = request.form.getlist('column')
            new_board = place_number_in_square(random_board, input_number, row, col)
            return render_template("index.html", x = new_board, y = 0)
        
        elif request.form.get("see_solution"):
            solve_sudoku(random_board)
            return render_template("index.html", x = current_board, y = random_board)
        
        else: 
            return render_template("index.html", x = random_board, y = 0)
        
    else:
        return render_template("index.html", x = random_board, y = 0)

if __name__ == "__main__":
    app.debug = True
    app.run()