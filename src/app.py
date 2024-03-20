import tkinter as tk
import time
import random
from tkinter import messagebox

class TicTacToe:
    BOARD_SIZE = 3
    first_player = None
    
    def __init__(self, game_board):
        self.game_board = game_board
        self.game_board.title("Крестики Нолики")
        self.current_player = self.random_player()
        self.first_player = self.current_player
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

        self.game_number_in_session = 0
        
    
    def random_player(self):
        players = ["O", "X", "O", "X", "O", "X", "O", "X", "O", "X"]
        random.shuffle(players)
        return random.choice(players)

    def create_button(self, i, j):
        return tk.Button(self.game_board, text=" ", font=("Arial", 20),
                            height=2, width=5,
                            command=lambda i=i, j=j: self.on_button_click(i, j))

    def create_reset_button(self):
        return tk.Button(self.game_board, text="Новая Игра", command=self.reset_game)

    def start_time(self):
        if self.board == [[" " for _ in range(self.BOARD_SIZE)] for _ in range(self.BOARD_SIZE)]:
            global start_time
            start_time = time.time()
    
    def calculate_time_game(self, start_time):
        end_time = time.time()
        return end_time - start_time
    
    def on_button_click(self, c, r):
        self.start_time()
        if self.board[c][r] == " ":
            self.board[c][r] = self.current_player
            self.buttons[c][r].config(text=self.current_player)
            if self.check_winner(c, r):
                self.show_message(f"Победил игрок '{self.current_player}' ")
                self.game_number_in_session += 1
                print(self.current_player, round(self.calculate_time_game(start_time),2), self.game_number_in_session, self.first_player, self.way_to_win(c,r), self.count_steps_win(), self.count_step_loss())
                self.reset_game()
                
            
            elif all(cell != " " for row in self.board for cell in row):
                self.show_message("Ничья!")
                self.game_number_in_session += 1
                print("N", round(self.calculate_time_game(start_time),2), self.game_number_in_session)
                self.reset_game()
            
            else:
                self.switch_player()

    def show_message(self, message):
        messagebox.showinfo("Игра окончена", message)

    def check_line(self, line):
        return all(cell == self.current_player for cell in line)

    def check_diagonals(self):
        return self.check_line([self.board[i][i] for i in range(self.BOARD_SIZE)]) \
                or self.check_line([self.board[i][self.BOARD_SIZE - 1 - i] for i in range(self.BOARD_SIZE)])
    
    def check_winner(self, i, j):

        return self.check_line(self.board[i]) or self.check_line([self.board[x][j] for x in range(self.BOARD_SIZE)]) \
                or self.check_diagonals()

    def way_to_win(self,i,j):
        if self.check_line(self.board[i]):
            return f"row{i+1}"
        elif self.check_line([self.board[x][j] for x in range(self.BOARD_SIZE)]):
            return f"column{j+1}"
        elif self.check_line([self.board[i][i] for i in range(self.BOARD_SIZE)]):
            return f"diag1"
        elif self.check_line([self.board[i][self.BOARD_SIZE - 1 - i] for i in range(self.BOARD_SIZE)]):
            return f"diag2"
        
    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def count_steps_win(self):
        return sum([row.count(self.current_player) for row in self.board])
    
    def count_step_loss(self):
        self.switch_player()
        return sum([row.count(self.current_player) for row in self.board])

    def reset_game(self):
        self.current_player = self.random_player()
        self.first_player = self.current_player
        self.board = [[" " for _ in range(self.BOARD_SIZE)] for _ in range(self.BOARD_SIZE)]
        for row in self.buttons:
            for button in row:
                button.config(text='')

root = tk.Tk()
game = TicTacToe(root)
root.mainloop()