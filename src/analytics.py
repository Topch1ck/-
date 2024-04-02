# analytics.py

import time

class Analytics:
    def calculate_time_game(self, start_time):
        end_time = time.time()
        return end_time - start_time
    
    def format_time(self, time_in_sec):
        minutes = int(time_in_sec / 60)
        seconds = int(time_in_sec % 60)
        millisecond = int((time_in_sec - int(time_in_sec)) * 100)
        return f"{minutes:02d}:{seconds:02d}:{millisecond:02d}"

    def time_game(self, start_time):
        return self.format_time(round(self.calculate_time_game(start_time), 2))

    def check_winner(self, board, current_player):
        def check_line(line):
            return all(cell == current_player for cell in line)

        def check_diagonals():
            return check_line([board[i][i] for i in range(len(board))]) \
                    or check_line([board[i][len(board) - 1 - i] for i in range(len(board))])

        return any(check_line(row) for row in board) or any(check_line([board[x][i] for x in range(len(board))]) for i in range(len(board))) \
                or check_diagonals()

    def way_to_win(self, board, current_player):
        def check_line(line):
            return all(cell == current_player for cell in line)

        def check_diagonals():
            return check_line([board[i][i] for i in range(len(board))]) \
                    or check_line([board[i][len(board) - 1 - i] for i in range(len(board))])

        for i in range(len(board)):
            if check_line(board[i]):
                return f"row{i+1}"
            if check_line([board[x][i] for x in range(len(board))]):
                return f"column{i+1}"
        if check_diagonals():
            return "diagonal"
        return "unknown"

    def count_steps_win(self, board, current_player):
        return sum([row.count(current_player) for row in board])

    def count_step_loss(self, board, current_player):
        opponent = "X" if current_player == "O" else "O"
        return sum([row.count(opponent) for row in board])
