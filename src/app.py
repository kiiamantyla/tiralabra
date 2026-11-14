"""2048-pelin flask-käyttöliittymän logiikka"""

import random
from flask import Flask, render_template, redirect, url_for, session
from ai import get_best_move
from game import move_left, move_right, move_up, move_down

app = Flask(__name__)
app.secret_key = "2048_ai_secret_key"  # Vaaditaan session käyttöön

def init_board():
    """Luo uuden 4x4-pelilaudan"""
    board = [[0, 0, 0, 0] for _ in range(4)]
    spawn_tile(board)
    spawn_tile(board)
    return board

def spawn_tile(board):
    """Arpoo uuden laatan (2 tai 4) tyhjään ruutuun."""
    empty_cells = [(r, c) for r in range(4) for c in range(4) if board[r][c] == 0]
    if empty_cells:
        r, c = random.choice(empty_cells)
        board[r][c] = 2 if random.random() < 0.9 else 4

@app.route("/")
def index():
    """Näyttää pelilaudan etusivulla."""
    if "board" not in session:
        session["board"] = init_board()
        session["score"] = 0

    return render_template("index.html", board=session["board"], score=session["score"])

@app.route("/move/<direction>", methods=["POST"])
def make_move(direction):
    """Käsittelee pelaajan tai tekoälyn tekemän siirron."""
    board = session.get("board")
    if not board:
        return redirect(url_for("index"))

    move_map = {
        "left": move_left,
        "right": move_right,
        "up": move_up,
        "down": move_down
    }

    if direction in move_map:
        new_board, points_earned = move_map[direction](board)
        # Jos lauta muuttui, siirto oli validi -> arvotaan uusi laatta
        if new_board != board:
            spawn_tile(new_board)
            session["board"] = new_board
            session["score"] = session.get("score", 0) + points_earned

    return redirect(url_for("index"))

@app.route("/ai-move", methods=["POST"])
def ai_move():
    """Pyytää tekoälyä (get_best_move) tekemään siirron."""
    board = session.get("board")
    if not board:
        return redirect(url_for("index"))

    # Haetaan paras siirto tekoälyltä (syvyyttä voi säätää, esim. 3)
    best_move = get_best_move(board, depth=3)

    if best_move:
        move_map = {
            "left": move_left,
            "right": move_right,
            "up": move_up,
            "down": move_down
        }
        new_board, points_earned = move_map[best_move](board)
        if new_board != board:
            spawn_tile(new_board)
            session["board"] = new_board
            session["score"] = session.get("score", 0) + points_earned

    return redirect(url_for("index"))

@app.route("/restart", methods=["POST"])
def restart():
    """Aloittaa uuden pelin."""
    session["board"] = init_board()
    session["score"] = 0
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
