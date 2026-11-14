"""2048-pelin tekoälyn heuristiikka ja expectimax-algoritmi"""

from game import move_left, move_right, move_up, move_down

weight_matrix = [
    [65536, 32768, 16384, 8192],
    [512,   1024,  2048,  4096],
    [256,   128,   64,    32],
    [1,     2,     4,     16]
]

def count_empty_cells(board: list[list[int]]) -> int:
    """Laskee tyhjien ruutujen määrän pelilaudalla

    Args:
        board: 4x4-lista pelilaudan tilasta

    Returns:
        int: tyhjien ruutujen lukumäärä
    """
    return sum(row.count(0) for row in board)

def evaluate_board(board: list[list[int]]) -> float:
    """Arvioi pelilaudan tilan numeerisesti käärmeheuristiikalla.
    Korkeampi pistemäärä tarkoittaa parempaa pelilautaa

    Args:
        board: 4x4-lista pelilaudan tilasta

    Returns:
        float: arvio pelilaudan hyvyydestä
    """
    score = 0.0

    #Käärmeheuristiikka
    for r in range(4):
        for c in range(4):
            score += board[r][c] * weight_matrix[r][c]

    #Tyhjät ruudut ovat arvokkaita
    empty_cells = count_empty_cells(board)
    score += empty_cells * 100.0
    return score

def expectimax(board: list[list[int]], depth: int, is_player: bool) -> float:
    """Expectimax-algoritmi pelitilan arvioimiseen syvyydellä d.

    Args:
        board: 4x4-lista pelilaudan tilasta
        depth: hakupuun jäljellä oleva syvyys
        is_player: True, jos max-solmu ja False jos chance-solmu

    Returns:
        float: arvio pelilaudan tilan hyvyydestä
    """
    if depth == 0:
        return evaluate_board(board)

    move_map = {
        "left": move_left,
        "right": move_right,
        "up": move_up,
        "down": move_down
    }

    #Max-solmu
    if is_player:
        max_val = float("-inf")
        valid_move_found = False

        for move_func in move_map.values():
            new_board, _ = move_func(board)
            if new_board != board:  #Siirto muutti lautaa eli oli validi
                valid_move_found = True
                val = expectimax(new_board, depth - 1, is_player=False)
                if val > max_val:
                    max_val = val

        if not valid_move_found:
            return evaluate_board(board)

        return max_val

    #Chance-solmu
    else:
        empty_cells = [(r, c) for r in range(4) for c in range(4) if board[r][c] == 0]
        if not empty_cells:
            return evaluate_board(board)

        total_score = 0.0

        #Lasketaan odotusarvo kaikille mahdollisille uusille laatoille
        for r, c in empty_cells:
            #Laatta 2, 0.9 todennäköisyys
            board_with_2 = [row[:] for row in board]
            board_with_2[r][c] = 2
            score_2 = expectimax(board_with_2, depth - 1, is_player=True)

            #Laatta 4, 0.1 todennäköisyys
            board_with_4 = [row[:] for row in board]
            board_with_4[r][c] = 4
            score_4 = expectimax(board_with_4, depth - 1, is_player=True)

            #Painotettu keskiarvo laatalle
            total_score += 0.9 * score_2 + 0.1 * score_4

        return total_score / len(empty_cells)

def get_best_move(board: list[list[int]], depth: int = 3) -> str | None:
    """Palauttaa parhaan siirron

    Args:
        board: 4x4-lista pelilaudan tilasta
        depth: hakupuun syvyys

    Returns:
        str | None: paras siirto nimeltä tai None, jos ei ole siirtoa
    """
    best_val = float("-inf")
    best_move = None

    move_map = {
            "left": move_left,
            "right": move_right,
            "up": move_up,
            "down": move_down
    }

    for name, move_func in move_map.items():
        new_board, _ = move_func(board)
        if new_board != board:
            val = expectimax(new_board, depth - 1, is_player=False)
            if val > best_val:
                best_val = val
                best_move = name

    return best_move
