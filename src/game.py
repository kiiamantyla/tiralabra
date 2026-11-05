"""2048-pelin sovelluslogiikka"""

def move_left(board: list[list[int]]) -> tuple[list[list[int]], int]:
    """Siirtää koko pelilaudan laatat vasemmalle

    Args:
        board: 4x4-lista pelilaudan tilasta

    Returns:
        tuple: uusi pelilauta ja kierroksen pisteet
    """
    new_board = []
    total_score = 0
    for row in board:
        new_row, score = merge_row(row)
        new_board.append(new_row)
        total_score+= score
    return new_board, total_score

def move_right(board: list[list[int]]) -> tuple[list[list[int]], int]:
    """Siirtää koko pelilaudan laatat oikealle

    Args:
        board: 4x4-lista pelilaudan tilasta

    Returns:
        tuple: uusi pelilauta ja kierroksen pisteet
    """
    new_board = []
    total_score = 0
    for row in board:
        reversed_row = row[::-1]
        new_row, score = merge_row(reversed_row)
        new_board.append(new_row[::-1])
        total_score += score
    return new_board, total_score


def merge_row(row: list[int]) -> tuple[list[int], int]:
    """Yhdistää yhden rivin laatat 2048-sääntöjen mukaisesti

    Args:
        row: lista, joka edustaa yhtä riviä pelilaudalla

    Returns:
        tuple: uusi rivi ja kierroksen pisteet
    """
    filtered = [val for val in row if val != 0]
    new_row = []
    score_gained = 0
    i = 0

    while i < len(filtered):
        if i + 1 < len(filtered) and filtered[i] == filtered[i + 1]:
            combined_value = filtered[i] * 2
            new_row.append(combined_value)
            score_gained += combined_value
            i += 2
        else:
            new_row.append(filtered[i])
            i += 1

    while len(new_row) < 4:
        new_row.append(0)

    return new_row, score_gained

def transpose_board(board: list[list[int]]) -> list[list[int]]:
    """Kääntää pelilaudan rivit ja sarakkeet keskenään

    Args:
        board: 4x4-lista pelilaudan tilasta

    Returns:
        lista: uusi pelilauta
    """
    n = len(board)
    new_board = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            new_board[i][j] = board[j][i]

    return new_board

def move_up(board: list[list[int]]) -> tuple[list[list[int]], int]:
    """Siirtää koko pelilaudan laatat ylöspäin

    Args:
        board: 4x4-lista pelilaudan tilasta

    Returns:
        tuple: uusi pelilauta ja kierroksen pisteet
    """
    transposed_board = transpose_board(board)
    new_transposed_board, total_score = move_left(transposed_board)
    new_board = transpose_board(new_transposed_board)
    return new_board, total_score

def move_down(board: list[list[int]]) -> tuple[list[list[int]], int]:
    """Siirtää koko pelilaudan laatat alaspäin

    Args:
        board: 4x4-lista pelilaudan tilasta

    Returns:
        tuple: uusi pelilauta ja kierroksen pisteet
    """
    transposed_board = transpose_board(board)
    new_transposed_board, total_score = move_right(transposed_board)
    new_board = transpose_board(new_transposed_board)
    return new_board, total_score
