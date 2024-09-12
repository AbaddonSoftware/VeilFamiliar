from VeilFamiliarMove import VeilFamiliarMove
class VeilFamiliarMoveset:
    def __init__(self, moves: list["VeilFamiliarMove"] = None, selected_move: "VeilFamiliarMove" = None):
        self.moves = moves if moves is not None else []
        self.selected_move = selected_move

    def add_move(self, move):
        self.moves.append(move)

    def add_moves(self, moves: list):
        self.moves.extend(moves)

    def get_moves(self) -> list:
        return self.moves
