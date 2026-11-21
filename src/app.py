"""2048-pelin flask-käyttöliittymän logiikka"""

import random
from flask import Flask, render_template, redirect, url_for, session
from ai import get_best_move
from game import move_map

app = Flask(__name__)
app.secret_key = "2048_ai_secret_key"  # Vaaditaan session käyttöön


def init_board():
    """Luo uuden 4x4-pelilaudan."""
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


def has_valid_moves(board):
    """Tarkistaa, onko pelilaudalla vähintään yksi validi siirto."""
    for move_func in move_map.values():
        new_board, _ = move_func(board)
        if new_board != board:
            return True
    return False


def apply_move(board, direction):
    """Kokeilee siirtoa ja arpoo uuden laatan, jos lauta muuttui."""
    if direction not in move_map:
        return False

    new_board, points_earned = move_map[direction](board)
    if new_board != board:
        spawn_tile(new_board)
        session["board"] = new_board
        session["score"] = session.get("score", 0) + points_earned
        return True
    return False


@app.route("/")
def index():
    """Näyttää pelilaudan etusivulla."""
    if "board" not in session:
        session["board"] = init_board()
        session["score"] = 0

    board = session["board"]
    game_over = not has_valid_moves(board)

    return render_template(
        "index.html",
        board=board,
        score=session["score"],
        game_over=game_over,
    )


@app.route("/move/<direction>", methods=["POST"])
def make_move(direction):
    """Käsittelee pelaajan tekemän siirron."""
    board = session.get("board")
    if not board:
        return redirect(url_for("index"))

    apply_move(board, direction)
    return redirect(url_for("index"))


@app.route("/ai-move", methods=["POST"])
def ai_move():
    """Pyytää tekoälyä (get_best_move) tekemään siirron."""
    board = session.get("board")
    if not board:
        return redirect(url_for("index"))

    best_move = get_best_move(board, depth=3)
    if best_move:
        apply_move(board, best_move)

    return redirect(url_for("index"))


@app.route("/restart", methods=["POST"])
def restart():
    """Aloittaa uuden pelin."""
    session["board"] = init_board()
    session["score"] = 0
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
