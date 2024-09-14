from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .VeilFamiliarMove import VeilFamiliarMove


class VeilFamiliarMoveset:
    def __init__(
        self,
        moveset: list["VeilFamiliarMove"] = None,
        selected_move: "VeilFamiliarMove" = None,
    ):
        self.moveset = moveset if moveset is not None else []
        self.selected_move = selected_move

    def add_move(self, moveset):
        self.moveset.append(moveset)

    def add_moves(self, moveset: list):
        self.moveset.extend(moveset)

    def get_moves(self) -> list:
        return self.moveset

    def set_selected(self, move: VeilFamiliarMove):
        if move in self.moveset:
            self.selected_move = move
        self.selected_move = None
