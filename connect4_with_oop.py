from tkinter import *
from tkinter import messagebox
import random
import sqlite3

global root # allows root to be accessed through all classes
root = Tk()
root.title("Connect4")

# Emma
class Players:
    def __init__(self):
        self.player1 = {"Player Number": 1, "Turns Taken": 0, "Pieces": 21} # can use dictionaries to count turns and number of pieces gone
        self.player2 = {"Player Number": 2, "Turns Taken": 0, "Pieces": 21}
        self.colors = ["Red", "Yellow"]
        self.color_assignment()
    
    def color_assignment(self):
        self.player1_color = random.choice(self.colors)
        self.player1.update({"Color": self.player1_color})
        self.colors.remove(self.player1_color)
        self.player2_color = random.choice(self.colors)
        self.player2.update({"Color": self.player2_color})

class Board: # game logic, game progress

    def __init__(self):
        self.rows = 6
        self.columns = 7
        self.pieces_in_rows = [0, 0, 0, 0, 0, 0, 0]
        self.board_game = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]] # 6 rows with seven columns
        self.Players = Players()
        self.current_player = self.Players.player1 # starts off with a player 1
        self.last_played = None  # placeholder until it's defined below

    def play_piece(self, c):
        if self.pieces_in_rows[c] < 6:
            self.board_game[self.pieces_in_rows[c]][c] = self.current_player["Player Number"]
            self.last_played = (self.pieces_in_rows[c], c) # allows to look for surrounding area to see if there's a win
            self.pieces_in_rows[c] += 1 # adds one to piece
            self.current_player["Turns Taken"] +=1
            self.current_player["Pieces"] -= 1
        else:
            messagebox.showinfo("Error: Column is full", "Pick another column.")

    def check_win(self):
        row, column = self.last_played # takes first element to equal row, second to equal column
        for c in range(-3, 1): # checks horizontal
            try: # rows
                play = [self.board_game[row][column + c + t] for t in range(0, 4)]
                if all(play[t] == play[0] for t in range(0,4)): # returns True if all are player 1 or player 2
                    return True
            except:
                pass
            try: # columns                
                play = [self.board_game[row + c + t][column] for t in range(0, 4)]
                if all(play[t] == play[0] for t in range(0,4)): # returns True if all are player 1 or player 2
                    return True
            except:
                pass

            try: #diagonals bottom left to top right
                row, column = self.last_played # takes first element to equal row, second to equal column
                play = [self.board_game[row + c + t][column + c + t] for t in range(0, 4)]
                if all(play[t] == play[0] for t in range(0,4)): # returns True if all are player 1 or player 2
                    return True
            except:
                pass

            try: #diagonals bottom right to top left
                row, column = self.last_played # takes first element to equal row, second to equal column
                play = [self.board_game[row + c + t][column - c - t] for t in range(0, 4)]
                if all(play[t] == play[0] for t in range(0,4)): # returns True if all are player 1 or player 2
                    return True
            except:
                pass

    def players_swap(self):
        if self.current_player == self.Players.player1:
            self.current_player = self.Players.player2
        else:
            self.current_player = self.Players.player1
    
# AK
class GUI: # interface elements
# Needs a circle grid (creating the board)
# Color correspondence for turns (can probably use modulus truth, if the turn is even, then whatever color goes first)

    def __init__(self, game):
        self.board_initializer()
        self.button_initalizing() # call functions here so easier to call at end
        self.board = Board() # initialize previous class
        self.GameOverPopupWindow = GameOverPopupWindow(game)
        self.score_tracker()

    def clicked(self, c): # increment pieces in column, visually add piece
        self.board.play_piece(c)
        self.update_board()
        if self.board.check_win():
            data.save_winners(self.board)
            self.GameOverPopupWindow.gameover_popup(self.board.current_player["Player Number"])
            self.score_tracker()
        self.board.players_swap()

    def button_initalizing(self): # making the buttons
        # lambda allows one to be added to each corresponding column of self.pieces_in_rows
        self.buttonA = Button(root, text="Column 1", command = lambda: self.clicked(0), bg = "blue", borderwidth = 0)
        self.buttonA.grid(row=2, column=1)
        self.buttonB = Button(root, text="Column 2", command = lambda: self.clicked(1), bg = "blue", borderwidth = 0)
        self.buttonB.grid(row=2, column=2)
        self.buttonC = Button(root, text="Column 3", command = lambda: self.clicked(2), bg = "blue", borderwidth = 0)
        self.buttonC.grid(row=2, column=3)
        self.buttonD = Button(root, text="Column 4", command = lambda: self.clicked(3), bg = "blue", borderwidth = 0)
        self.buttonD.grid(row=2, column=4)
        self.buttonE = Button(root, text="Column 5", command = lambda: self.clicked(4), bg = "blue", borderwidth = 0)
        self.buttonE.grid(row=2, column=5)
        self.buttonF = Button(root, text="Column 6", command = lambda: self.clicked(5), bg = "blue", borderwidth = 0)
        self.buttonF.grid(row=2, column=6)
        self.buttonG = Button(root, text="Column 7", command = lambda: self.clicked(6), bg = "blue", borderwidth = 0)
        self.buttonG.grid(row=2, column=7)
    
    def board_initializer(self): # needs rest of parts
        root.configure(bg='blue')
        self.board_canvas = Canvas(root, width=700, height=600, bg ='blue')
        self.board_canvas.grid(row=3, column=1, columnspan=7)
        self.circles = [[self.board_canvas.create_oval(j * 100, i * 100, (j +1) * 100, (i + 1) * 100, fill='white') for j in range(7)] for i in range(6)]
    
    def score_tracker(self):
        player1wins, player2wins = data.query_it()
        if player1wins > 0 or player2wins >0:
            best_score = data.win_count()
        self.scores = Label(root, text="Player Stats", bg= "blue", font=("Arial", 13, "bold"))
        self.scores.grid(row=4, column=1, columnspan=4)

        self.leaderboard = Label(root, text="Leaderboard", bg= "blue", font=("Arial", 13, "bold"))
        self.leaderboard.grid(row=4, column=5, columnspan=4)

        self.player1_wins = Label(root, text=f"Player 1 Score: {player1wins}", bg= "blue", font=("Arial", 13))
        self.player1_wins.grid(row=5, column=1, columnspan=2)

        self.player2_wins = Label(root, text=f"Player 2 Score: {player2wins} ", bg= "blue", font=("Arial", 13))
        self.player2_wins.grid(row=5, column=3, columnspan=2)

        if player1wins==0 and player2wins==0:
            self.no_top_score = Label(root, text="No high score yet", bg="blue",font=("Arial", 13))
            self.no_top_score.grid(row=5, column=5, columnspan=3)
        else:
            self.topscore = Label(root, text=f"Player {self.board.current_player["Player Number"]} won in {best_score} moves", bg="blue", font=("Arial", 13))
            self.topscore.grid(row=5, column=5, columnspan=3)

    def update_board(self):
        row, col = self.board.last_played
        color = self.board.current_player["Color"]
        bottom_row = 5 - row
        self.board_canvas.itemconfig(self.circles[bottom_row][col], fill=color)

    def reset_canvas(self): # allows access to Board reset in class Game
        self.board = Board()
        self.board_initializer()

# Charlotte pop-up window
class GameInstructions:
    def __init__(self):
        self.instructions = ("Take turns dropping one of your pieces onto the board.", 
        "The first player to get four pieces in a row, vertically, horizontally, or diagonally, wins!"
        )
        self.display_instructions()
    
    def display_instructions(self):
        messagebox.showinfo("Connect 4 Instructions", "\n".join(self.instructions))

class GameOverPopupWindow:
    def __init__(self,game):
        self.game = game

    def gameover_popup(self, winner):
        player_input = messagebox.askyesno(
            "Game Over!",
            f" Player {winner} wins! Would you like to restart the game?"
        )
        if player_input:
            self.game_restart()
        else:
            self.game.exit_game()
            data.reset_game_stats()
            
    def game_restart(self):
        self.game.clear_board()
        self.game.setup_new_game()
        data.query_it()

class Game:
    def __init__(self):
        self.gui = GUI(self)
        self.start_game()

    def start_game(self):
        GameInstructions()

    def clear_board(self):
        self.gui.reset_canvas()

    def setup_new_game(self):
        self.winner = None
        
    # officially exits game 
    def exit_game(self):
        root.destroy()
        data.reset_game_stats()
        
# Emma
class GameSave:
# delete gatabase when game closed out
# display best scores

    def __init__(self):
        self.con = sqlite3.connect('game_progress.db')
        self.cur = self.con.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS gameprogress
                (Player_1_Score BIT, Player_2_Score BIT, Winner BIT)''')
        self.con.commit()

    def save_winners (self, board):
        winner = board.current_player["Player Number"]
        insert = "INSERT INTO gameprogress VALUES (?, ?, ?)"
        data = (board.Players.player1['Turns Taken'], board.Players.player2['Turns Taken'], winner)
        self.cur.execute(insert, data)
        self.con.commit()

    def query_it(self):
        # win count
        player1_win_count = self.cur.execute("SELECT Player_1_Score, Winner FROM gameprogress WHERE Winner=1")
        player1_win_count = len([row for row in player1_win_count])

        player2_win_count = self.cur.execute("SELECT Player_2_Score, Winner FROM gameprogress WHERE Winner=2")
        player2_win_count = len([row for row in player2_win_count])

        return player1_win_count, player2_win_count
    
    def win_count(self):
        try: # defining, if first game, sets to 0 so no errors.
            player1highscore = self.cur.execute("SELECT Player_1_Score FROM gameprogress WHERE Winner=1")
            player1min = min([row for row in player1highscore])
            player1min = player1min[0]
        except:
            player1min=0
        try:
            player2highscore = self.cur.execute("SELECT Player_2_Score FROM gameprogress WHERE Winner=2")
            player2min = min([row for row in player2highscore])
            player2min = player2min[0]
        except:
            player2min=0
        
        if player1min > 0 and player2min> 0:
            if player1min < player2min:
                best_score = player1min
            else:
                best_score = player2min
        else:
            best_score = max(player1min, player2min)

        return best_score

    def reset_game_stats(self):
        self.scrap_data = self.cur.execute('DROP TABLE gameprogress')
        self.con.commit()
        self.con.close()

#initalizing game and data save
data = GameSave()
game = Game()

root.mainloop()