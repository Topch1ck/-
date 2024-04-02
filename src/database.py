# database.py

import sqlite3 as sq

class TicTacToeDB:
    def __init__(self):
        self.create_db()

    def create_db(self):
        with sq.connect("TicTacToe.db") as self.con:
            self.cur = self.con.cursor()

            self.cur.execute("""
                            CREATE TABLE IF NOT EXISTS Tictactoe(
                            game_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            winner TEXT,
                            first_step TEXT,
                            type_win TEXT,
                            cs_winner INTEGER,
                            cs_losser INTEGER,
                            сs_total INTEGER,
                            game_in_session INTEGER,
                            time_game DATETIME
                            )
                            """)
            self.con.commit()

    def send_to_database_w_l(self, current_player, first_player, way_to_win, count_steps_win, count_step_loss, game_number_in_session, time_game):
        self.cur.execute("""
        INSERT INTO Tictactoe(
            winner,
            first_step,
            type_win,
            cs_winner,
            cs_losser,
            сs_total,
            game_in_session,
            time_game
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            current_player,
            first_player,
            way_to_win,
            count_steps_win,
            count_step_loss,
            count_step_loss + count_steps_win,
            game_number_in_session, 
            time_game,
                )
                            )
        self.con.commit()

    def send_to_database_n(self, first_player, count_step_loss, count_steps_win, game_number_in_session, time_game):
        self.cur.execute("""
        INSERT INTO Tictactoe(
            winner,
            first_step,
            сs_total,
            game_in_session,
            time_game
        )
        VALUES (?, ?, ?, ?, ?)
        """, (
            "N",
            first_player,
            count_step_loss + count_steps_win,
            game_number_in_session, 
            time_game,
                )
                            )
        self.con.commit()
