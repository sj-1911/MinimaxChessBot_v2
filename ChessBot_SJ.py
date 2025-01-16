"""
Chess Bot v1
* With Libraries
Spencer Jackson
1/25
"""

import chess
import chess.engine
import random 


board = chess.Board()

while not board.is_game_over():
    legal_moves = list(board.legal_moves)
    random_move = random.choice(legal_moves)
    board.push(random_move)
    print(board)


# Minimax Algorithim evaluates board to find best move


def minimax(board, depth, is_maximizing):
    if depth == 0 or board.game_is_over():
        return evaluate_board(board)
    if is_maximizing:
        max_eval = float('-inf')
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth -1, False)
            board.pop()
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth -1, True)
            board.pop
            min_eval = min(min_eval, eval)
        return (min_eval)
    
    # Alpha Beta pruning optimizes the minimax algorithim by reducing the number of branches evaluated

def alphabeta(board,depth,alpha,beta, is_maximizing):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)
    
    if is_maximizing:
        max_eval = float('-inf')
        for move in board.legal_moves:
            board.push(move)
            eval = alphabeta(board, depth -1, alpha, beta, False)
            board.pop()
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval = alphabeta(board, depth -1, alpha, beta, True)
            board.pop()
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval
    # Board evaluation assigns scores to board based on pieces of the board
def evaluate_board(board):
    piece_values = {
        chess.PAWN: 1,
        chess.KNIGHT: 3,
        chess.BISHOP: 3,
        chess.ROOK: 5,
        chess.QUEEN: 9,
        chess.KING: 0  # King has no static value
    }
    eval = 0
    for piece_type in piece_values:
        eval += len(board.pieces(piece_type, chess.WHITE)) * piece_values[piece_type]
        eval -= len(board.pieces(piece_type, chess.BLACK)) * piece_values[piece_type]
    return eval




