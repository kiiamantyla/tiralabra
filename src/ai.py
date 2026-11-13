"""2048-pelin tekoälyn heuristiikka ja logiikka"""

weight_matrix = [
    [65536, 32768, 16384, 8129],
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

    empty_cells = count_empty_cells(board)
    score += empty_cells * 100.0 #Tyhjät ruudut ovat arvokkaita

    return score
