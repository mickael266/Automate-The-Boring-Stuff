

#pieces in chess: 'pawn', 'knight', 'bishop', 'rook', 'queen', 'king'.
def isValidChessBoard(dictionary):
   
    correct_order_up = {"8a":"rook", "8b":"knight", "8c":"bishop", "8d":"queen", "8e":"king",
    "8f":"bishop","8g":"knight", "8h":"rook",
    "a7":"pawn","b7":"pawn","c7":"pawn","d7":"pawn","e7":"pawn","f7":"pawn","g7":"pawn","h7":"pawn"}

    correct_order_down = {"1a":"rook", "1b":"knight", "1c":"bishop", "1d":"queen", "1e":"king",
    "1f":"bishop","1g":"knight", "1h":"rook", 
    "a2":"pawn","b2":"pawn","c2":"pawn","d2":"pawn","e2":"pawn","f2":"pawn","g2":"pawn","h2":"pawn"}

  
    for location, chess_piece  in dictionary.items():
        if correct_order_up.get(location, 0):
            if chess_piece[1:len(chess_piece)] != correct_order_up[location]:
                return False
        elif correct_order_down.get(location, 0):
            if chess_piece[1:len(chess_piece)] != correct_order_down[location]:
                
                return False
           
    first_piece_in_up_board = dictionary["8a"]
    color_up = first_piece_in_up_board[0]
    for correct_location_up, piece_up in correct_order_up.items():
        piece_in_up_board = dictionary[correct_location_up] 
        if piece_in_up_board[0] != color_up:
            return False

    first_piece_in_down_board = dictionary["1a"]
    color_down = first_piece_in_down_board[0]
    for correct_location_down, piece_down in correct_order_down.items():
        piece_in_down_board = dictionary[location] 
        if piece_in_down_board[0] != color_down:
            return False

        return True 


def main():
    board = {"8a":"wrook", "8b":"wknight", "8c":"wbishop", "8d":"wqueen", "8e":"wking",
        "8f":"wbishop","8g":"wknight", "8h":"wrook",
        "a7":"wpawn","b7":"wpawn","c7":"wpawn","d7":"wpawn","e7":"wpawn","f7":"wpawn","g7":"wpawn","h7":"wpawn",
        "1a":"brook", "1b":"bknight", "1c":"bbishop", "1d":"bqueen", "1e":"bking",
        "1f":"bbishop","1g":"bknight", "1h":"brook", 
        "a2":"bpawn","b2":"bpawn","c2":"bpawn","d2":"bpawn","e2":"bpawn","f2":"bpawn","g2":"bpawn","h2":"bpawn"}

    print(isValidChessBoard(board))

# Driver program
if __name__ == "__main__":
    main()
