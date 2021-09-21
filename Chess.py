import chess
import random
import chess.svg

board = chess.Board()
legal_move_list = []

while not board.is_stalemate() and not board.is_insufficient_material() and not board.is_checkmate():
    legal_list = board.legal_moves
    for move in legal_list:
        legal_move_list.append(move)
    board.push(random.choice(legal_move_list))
    legal_move_list.clear()
    print(board)
    print("_")
print(board.outcome())