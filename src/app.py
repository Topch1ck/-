import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    BOARD_SIZE = 3

    def __init__(self, game_board):
        self.game_board = game_board
        self.game_board.title("Крестики Нолики")
        self.current_player = "X"
        self.board = [[" " for _ in range(self.BOARD_SIZE)] for _ in range(self.BOARD_SIZE)]
        self.buttons = []

        for i in range(self.BOARD_SIZE):
            row = []
            for j in range(self.BOARD_SIZE):
                button = self.create_button(i, j)
                button.grid(row=i, column=j, sticky="nsew")
                row.append(button)
            self.buttons.append(row)

        self.reset_button = self.create_reset_button()
        self.reset_button.grid(row=self.BOARD_SIZE, column=0, columnspan=self.BOARD_SIZE, sticky="nsew")

    def create_button(self, i, j):
        return tk.Button(self.game_board, text=" ", font=("Arial", 20),
                            height=2, width=5,
                            command=lambda i=i, j=j: self.on_button_click(i, j))

    def create_reset_button(self):
        return tk.Button(self.game_board, text="Новая Игра", command=self.reset_game)

    def on_button_click(self, c, r):
        if self.board[c][r] == " ":
            self.board[c][r] = self.current_player
            self.buttons[c][r].config(text=self.current_player)
            if self.check_winner(c, r):
                self.show_message(f"Победил игрок '{self.current_player}' ")
                self.reset_game()
            elif all(cell != " " for row in self.board for cell in row):
                self.show_message("Ничья!")
                self.reset_game()
            else:
                self.switch_player()

    def show_message(self, message):
        messagebox.showinfo("Игра окончена", message)

    def check_winner(self, i, j):
        def check_line(line):
            return all(cell == self.current_player for cell in line)

        def check_diagonals():
            return check_line([self.board[i][i] for i in range(self.BOARD_SIZE)]) \
                    or check_line([self.board[i][self.BOARD_SIZE - 1 - i] for i in range(self.BOARD_SIZE)])

        return check_line(self.board[i]) or check_line([self.board[x][j] for x in range(self.BOARD_SIZE)]) \
                or check_diagonals()

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def reset_game(self):
        self.current_player = "X"
        self.board = [[" " for _ in range(self.BOARD_SIZE)] for _ in range(self.BOARD_SIZE)]
        for row in self.buttons:
            for button in row:
                button.config(text='')

root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
