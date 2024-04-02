# app.py

import tkinter as tk
import time
import random
import database
import analytics
from tkinter import messagebox

class TicTacToe:
    BOARD_SIZE = 3
    
    def __init__(self, game_board):
        self.analytics = analytics.Analytics()
        self.db = database.TicTacToeDB()
        
        self.game_board = game_board
        self.game_board.title("TicTacToe")
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
        self.start_time = 0
        


    def random_player(self):
        players = ["O", "X"]
        random.shuffle(players)
        return random.choice(players)

    def create_button(self, c, r):
        return tk.Button(self.game_board, text=" ", font=("Arial", 20),
                            height=2, width=5,
                            command=lambda c=c, r=r: self.on_button_click(c, r))

    def create_reset_button(self):
        return tk.Button(self.game_board, text="New Game", command=self.reset_game)
    
    def on_button_click(self, c, r):
        if self.start_time == 0:
            self.start_time = time.time()

        if self.board[c][r] == " ":
            self.board[c][r] = self.current_player
            self.buttons[c][r].config(text=self.current_player)
            if self.analytics.check_winner(self.board, self.current_player):
                self.game_number_in_session += 1
                self.show_message(f"Player '{self.current_player}' wins!")
                self.db.send_to_database_w_l(self.current_player, 
                                            self.first_player, 
                                            self.analytics.way_to_win(self.board, self.current_player), 
                                            self.analytics.count_steps_win(self.board, self.current_player), 
                                            self.analytics.count_step_loss(self.board, self.current_player), 
                                            self.game_number_in_session, 
                                            self.analytics.time_game(self.start_time))
                self.reset_game()         
            elif all(cell != " " for row in self.board for cell in row):
                self.game_number_in_session += 1
                self.show_message("It's a tie!")
                self.db.send_to_database_n(self.current_player, 
                                        self.analytics.count_step_loss(self.board, self.current_player), 
                                        self.analytics.count_steps_win(self.board, self.current_player),
                                        self.game_number_in_session, 
                                        self.analytics.time_game(self.start_time))
                self.reset_game()            
            else:
                self.switch_player()

    def show_message(self, message):
        messagebox.showinfo("Game Over", message)

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def reset_game(self):
        self.current_player = self.random_player()
        self.first_player = self.current_player
        self.start_time = 0
        self.board = [[" " for _ in range(self.BOARD_SIZE)] for _ in range(self.BOARD_SIZE)]
        for row in self.buttons:
            for button in row:
                button.config(text='')

root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
