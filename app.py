import tkinter as tk
from tkinter import messagebox

class TicTacToe:

    def __init__(self, game_board):
        self.game_board = game_board  # создание игрового окна
        self.game_board.title("Крестики Нолики")
        self.current_player = "X"  # установка начального игрока
        self.board = [" " for _ in range(9)]  # создание пустого игрового поля
        self.buttons = []  # список для хранения кнопок

        for i in range(3):
            row = []  # список кнопок
            for j in range(3):
                button = tk.Button(self.game_board, text=" ",
                                   font=("Arial", 20),
                                   height=2,
                                   width=5,
                                   command=lambda i=i, j=j: self.on_button_click(i, j))
                button.grid(row=i, column=j, sticky="nsew")
                row.append(button)
            self.buttons.append(row)

        self.reset_button = tk.Button(self.game_board,
                                      text="Новая Игра",
                                      command = self.reset_game)
        self.reset_button.grid(row=3, column=0, columnspan=3, sticky="nsew")

    def on_button_click(self, i, j):  # Функция которая ставит знак игрока.
        if self.board[i*3+j] == " ":  # Проверяем пустая ли клетка.
            self.board[i*3+j] = self.current_player  # Устанавливаем знак текущего игрока.
            self.buttons[i][j].config(text=self.current_player)  # Обновляем клетку на знак текущего игрока.
            # Ниже логика для оповещающего окна об исходе игры.
            if self.check_winner(i,j):
                messagebox.showinfo("Победа!", f"Победи игрок '{self.current_player}' ")
                self.reset_game()
            elif " " not in self.board:
                messagebox.showinfo("Ничья!", f"Ничья!")
                self.reset_game()
            else:
                # Смена текущего игрока
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self, i, j):  # Функция для проверки выигрыша.
        row = all(self.board[i * 3 + col] == self.current_player for col in range(3))
        col = all(self.board[row * 3 + j] == self.current_player for row in range(3))
        diag1 = all(self.board[i * 3 + i] == self.current_player for i in range(3))
        diag2 = all(self.board[i * 3 + 2 - i] == self.current_player for i in range(3))
        return any([row, col, diag1, diag2])  # Вернет истину если один из вариантов окажется истиной.

    def reset_game(self):  # Функция сброса игры
        self.current_player = "X"
        self.board = [" " for _ in range(9)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text='')

root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
