"""2048-pelin tekoälyn heuristiikka ja logiikka"""

def count_empty_cells(board: list[list[int]]) -> int:
    """Laskee tyhjien ruutujen määrän pelilaudalla

    Args:
        board: 4x4-lista pelilaudan tilasta

    Returns:
        int: tyhjien ruutujen lukumäärä
    """
    return sum(row.count(0) for row in board)

def evaluate_board(board: list[list[int]]) -> float:
    """Arvioi pelilaudan tilan numeerisesti
    Korkeampi pistemäärä tarkoittaa parempaa pelilautaa

    Args:
        board: 4x4-lista pelilaudan tilasta

    Returns:
        float: arvioin pelilaudan hyvyydestä
    """
    empty_cells = count_empty_cells(board)
    score = empty_cells * 100.0 #Tyhjät ruudut ovat arvokkaita

    max_tile = max(max(row) for row in board)
    if board[0][0] == max_tile:
        score += 1000.0

    return score
