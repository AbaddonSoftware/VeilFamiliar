class VeilFamiliarMoveset:
    def __init__(self, moves=None):
        self.moves = moves if moves is not None else []

    def add_move(self, move):
        self.moves.append(move)

    def add_moves(self, moves: list):
        self.moves.extend(moves)

    def get_moves(self) -> list:
        return self.moves
