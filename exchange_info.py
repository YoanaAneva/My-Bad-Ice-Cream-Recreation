class ExchangeInfo:
    def __init__(self, player_direction, player_rect, board):
        self.player_direction = player_direction
        self.player_rect = player_rect
        self.board = board

    def __str__(self):
        return f"({self.player_direction}, {self.player_rect}, {self.board})"

class PlayerInitInfo:
    def __init__(self, player_x, player_y, player_flavour):
            self.player_x = player_x
            self.player_y = player_y
            self.player_flavour = player_flavour        

class Info:
    def __init__(self, player_x=None, player_y=None, player_flavour=None, player_rect=None, player_direction="front"):
        self.player_x = player_x
        self.player_y = player_y
        self.player_flavour = player_flavour
        self.player_direction = player_direction
        self.player_rect = (player_x, player_y, player_x + 44, player_y + 44)