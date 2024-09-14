class TicTac:
    def __init__(self):
        self.turns = {1:0, 2:2, 3:4, 4:0, 5:2, 6:4, 7:0, 8:2, 9:4}
        self.list_a = ["_", "|", "_", "|", "_"]
        self.list_b = ["_", "|", "_", "|", "_"]
        self.list_c = ["_", "|", "_", "|", "_"]
        self.player = 1

    def show_output(self, list):
        a = str(list)
        value_to_replace = ["[", "]", "'", ","]
        for value in value_to_replace:
            a = a.replace(value, "")
        print(a)

    def game_input(self, turn):
        for number in self.turns:
            if number == turn:
                index = self.turns[number]
        if turn in [1, 2, 3]:
            if self.player % 2 != 0:
                self.list_a[index] = "X"
                self.player += 1
            else:
                self.list_a[index] = "O"
                self.player += 1
        elif turn in [4, 5, 6]:
            if self.player % 2 != 0:
                self.list_b[index] = "X"
                self.player += 1
            else:
                self.list_b[index] = "O"
                self.player += 1
        elif turn in [7, 8, 9]:
            if self.player % 2 != 0:
                self.list_c[index] = "X"
                self.player += 1
            else:
                self.list_c[index] = "O"
                self.player += 1
        self.show_output(self.list_a)
        self.show_output(self.list_b)
        self.show_output(self.list_c)

    def check_position(self, turn):
        check = False
        for number in self.turns:
            if number == turn:
                index = self.turns[number]
        if turn in [1, 2, 3]:
            if self.list_a[index] == "_":
                check = True
                return check
        elif turn in [4, 5, 6]:
            if self.list_b[index] == "_":
                check = True
                return check
        elif turn in [7, 8, 9]:
            if self.list_c[index] == "_":
                check = True
                return check

    def check_winner(self):
        winner = ""
        if self.list_a[0] == "X" and self.list_a[2] == "X" and self.list_a[4] == "X":
            winner = "X"
            return winner
        elif self.list_b[0] == "X" and self.list_b[2] == "X" and self.list_b[4] == "X":
            winner = "X"
            return winner
        elif self.list_c[0] == "X" and self.list_c[2] == "X" and self.list_c[4] == "X":
            winner = "X"
            return winner
        elif self.list_a[0] == "X" and self.list_b[0] == "X" and self.list_c[0] == "X":
            winner = "X"
            return winner
        elif self.list_a[2] == "X" and self.list_b[2] == "X" and self.list_c[2] == "X":
            winner = "X"
            return winner
        elif self.list_a[4] == "X" and self.list_b[4] == "X" and self.list_c[4] == "X":
            winner = "X"
            return winner
        elif self.list_a[0] == "X" and self.list_b[2] == "X" and self.list_c[4] == "X":
            winner = "X"
            return winner
        elif self.list_a[4] == "X" and self.list_b[2] == "X" and self.list_c[0] == "X":
            winner = "X"
            return winner

        elif self.list_a[0] == "O" and self.list_a[2] == "O" and self.list_a[4] == "O":
            winner = "O"
            return winner
        elif self.list_b[0] == "O" and self.list_b[2] == "O" and self.list_b[4] == "O":
            winner = "O"
            return winner
        elif self.list_c[0] == "O" and self.list_c[2] == "O" and self.list_c[4] == "O":
            winner = "O"
            return winner
        elif self.list_a[0] == "O" and self.list_b[0] == "O" and self.list_c[0] == "O":
            winner = "O"
            return winner
        elif self.list_a[2] == "O" and self.list_b[2] == "O" and self.list_c[2] == "O":
            winner = "O"
            return winner
        elif self.list_a[4] == "O" and self.list_b[4] == "O" and self.list_c[4] == "O":
            winner = "O"
            return winner
        elif self.list_a[0] == "O" and self.list_b[2] == "O" and self.list_c[4] == "O":
            winner = "O"
            return winner
        elif self.list_a[4] == "O" and self.list_b[2] == "O" and self.list_c[0] == "O":
            winner = "O"
            return winner

    def reset_game(self):
        reset_game = False
        if not "_" in self.list_a and not "_" in self.list_b and not "_" in self.list_c:
            reset_game = True
            return reset_game

game = TicTac()
game_on = True
while game_on:
    if game.check_winner() == "X" or game.check_winner() == "O":
        print(f"{game.check_winner()} is winner")
        game_on = False
    elif game.reset_game() == True:
        print("Draw")
        game_on = False
    else:
        turn = int(input("What's your turn? "))
        if game.check_position(turn) == True:
            game.game_input(turn)
        else:
            game.check_winner()
            turn = int(input())
            if game.check_position(turn) == True:
                game.game_input(turn)
