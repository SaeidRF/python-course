
import time
class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.moves = 0
        self.result = "playing"
        self.game_time = 0

class Checker:
    def __init__(self, color):
        self.color = color
        self.king = False

    def make_king(self):
        self.king = True
class Board:
    def __init__(self):
        self.board = [[None for col in range(8)] for row in range(8)]
        self.create_board()

    def create_board(self):
        for row in range(3):
            for col in range(8):
                if (row + col) % 2 == 1:
                    self.board[row][col] = Checker("B")

        for row in range(5, 8):
            for col in range(8):
                if (row + col) % 2 == 1:
                    self.board[row][col] = Checker("W")

    def show_board(self):
        print("\n  0 1 2 3 4 5 6 7")
        for row in range(8):
            print(row, end=" ")
            for col in range(8):
                piece = self.board[row][col]

                if piece is None:
                    print(".", end=" ")
                elif piece.king:
                    print(piece.color.lower(), end=" ")
                else:
                    print(piece.color, end=" ")
            print()

    def get_checker(self, row, col):
        if row < 0 or row > 7 or col < 0 or col > 7:
            return None
        return self.board[row][col]

    def valid_move(self, start, end, color):
        r1, c1 = start
        r2, c2 = end

        piece = self.get_checker(r1, c1)

        if piece is None or piece.color != color:
            return False

        if self.get_checker(r2, c2) is not None:
            return False

        if (r2 + c2) % 2 == 0:
            return False

        dr = r2 - r1
        dc = c2 - c1

        if abs(dc) != abs(dr):
            return False

        if piece.king:
            pass
        elif piece.color == "B" and dr <= 0:
            return False
        elif piece.color == "W" and dr >= 0:
            return False

        if abs(dr) == 1:
            return True

        if abs(dr) == 2:
            middle_row = (r1 + r2) // 2
            middle_col = (c1 + c2) // 2
            middle = self.get_checker(middle_row, middle_col)

            if middle is not None and middle.color != color:
                return True

        return False

    def move_checker(self, start, end):
        r1, c1 = start
        r2, c2 = end

        piece = self.board[r1][c1]

        if abs(r2 - r1) == 2:
            middle_row = (r1 + r2) // 2
            middle_col = (c1 + c2) // 2
            self.board[middle_row][middle_col] = None

        self.board[r1][c1] = None
        self.board[r2][c2] = piece

        if piece.color == "B" and r2 == 7:
            piece.make_king()
        elif piece.color == "W" and r2 == 0:
            piece.make_king()

    def count_checkers(self, color):
        count = 0
        for row in self.board:
            for piece in row:
                if piece is not None and piece.color == color:
                    count += 1
        return count

    def has_moves(self, color):
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]

                if piece is None or piece.color != color:
                    continue

                directions = [-1, 1]

                for dr in directions:
                    for dc in directions:
                        if not piece.king:
                            if color == "B" and dr == -1:
                                continue
                            if color == "W" and dr == 1:
                                continue

                        for step in [1, 2]:
                            new_row = row + dr * step
                            new_col = col + dc * step

                            if self.valid_move(
                                (row, col), (new_row, new_col), color
                            ):
                                return True

        return False


class Game:
    def __init__(self):
        name1 = input("enter name of Black player: ")
        name2 = input("enter name of White player: ")

        self.players = [
            Player(name1, "B"),
            Player(name2, "W")
        ]

        self.board = Board()
        self.current = 0
        self.total_moves = 0
        self.start_time = 0

    def show_status(self):
        player = self.players[self.current]

        print("\nplayer:", player.name)
        print("color:", player.color)
        print("moves:", player.moves)
        print("total moves:", self.total_moves)
        self.board.show_board()

    def finish_game(self, winner=None):
        duration = time.time() - self.start_time

        for player in self.players:
            player.game_time = duration

            if winner is None:
                player.result = "Game ended"
            elif player == winner:
                player.result = "Won"
            else:
                player.result = "Lost"

        print("\n===== GAME SUMMARY =====")
        print("total moves:", self.total_moves)
        print("game time:", round(duration, 2), "seconds")

        for player in self.players:
            print("\nplayer:", player.name)
            print("color:", player.color)
            print("moves:", player.moves)
            print("time:", round(player.game_time, 2), "seconds")
            print("result:", player.result)

    def play(self):
        self.start_time = time.time()
        print("checkers Game Started")

        while True:
            player = self.players[self.current]
            color = player.color

            if (self.board.count_checkers(color) == 0
                    or not self.board.has_moves(color)):
                winner = self.players[1 - self.current]
                print(player.name, "cannot move. Game over!")
                self.board.show_board()
                self.finish_game(winner)
                break

            self.show_status()

            choice = input("move or finish? (m/f): ").strip().lower()

            if choice == "f":
                print("game finished by player.")
                self.board.show_board()
                self.finish_game()
                break

            if choice != "m":
                print("please enter m or f.")
                continue

            try:
                start_row = int(input("from row (0-7): "))
                start_col = int(input("from column (0-7): "))
                end_row = int(input("to row (0-7): "))
                end_col = int(input("to column (0-7): "))

                start = (start_row, start_col)
                end = (end_row, end_col)

                if not (0 <= start_row < 8 and 0 <= start_col < 8
                        and 0 <= end_row < 8 and 0 <= end_col < 8):
                    print("position is outside the board.")
                    continue

                if self.board.valid_move(start, end, color):
                    self.board.move_checker(start, end)
                    player.moves += 1
                    self.total_moves += 1
                    self.current = 1 - self.current
                else:
                    print("Invalid move. Try again.")

            except ValueError:
                print("please enter numbers from 0 to 7.")


if __name__ == "__main__":
    game = Game()
    game.play()
