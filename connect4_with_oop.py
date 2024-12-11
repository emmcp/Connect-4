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
        self.GameOverPopupWindow = GameOverPopupWindow(None)

    def play_piece(self, c):
        if self.pieces_in_rows[c] < 6:
            self.board_game[self.pieces_in_rows[c]][c] = self.current_player["Player Number"]
            self.last_played = (self.pieces_in_rows[c], c) # allows to look for surrounding area to see if there's a win
            self.pieces_in_rows[c] += 1 # adds one to piece
        else:
            messagebox.showinfo("Error: Column is full", "Pick another column.")

    def check_win(self):
        try: # rows
            row, column = self.last_played # takes first element to equal row, second to equal column
            for c in range(-3, 1):
                play = [self.board_game[row][column + c + t] for t in range(0, 4)]
                if all(play[t] == play[0] for t in range(0,4)): # returns True if all are player 1 or player 2
                    return True
        except:
            pass

        try: # columns
            row, column = self.last_played # takes first element to equal row, second to equal column

            for c in range(-3, 1):
                play = [self.board_game[row + c + t][column] for t in range(0, 4)]
                if all(play[t] == play[0] for t in range(0,4)): # returns True if all are player 1 or player 2
                    return True
        except:
            pass
        
        try: #diagonals bottom left to top right
            row, column = self.last_played # takes first element to equal row, second to equal column

            for c in range(-3, 1): # checks horizontal
                play = [self.board_game[row + c + t][column + c + t] for t in range(0, 4)]
                if all(play[t] == play[0] for t in range(0,4)): # returns True if all are player 1 or player 2
                    return True
        except:
            pass

        try: #diagonals bottom right to top left
            row, column = self.last_played # takes first element to equal row, second to equal column

            for c in range(-3, 1): # checks horizontal
                play = [self.board_game[row - c - t][column + c + t] for t in range(0, 4)]
                if all(play[t] == play[0] for t in range(0,4)): # returns True if all are player 1 or player 2
                    return True
        except:
            pass

    def players_swap(self):
        self.current_player["Turns Taken"] +=1
        self.current_player["Pieces"] -= 1
        if self.current_player == self.Players.player1:
            self.current_player = self.Players.player2
        else:
            self.current_player = self.Players.player1
    
# AK
class GUI: # interface elements
# Needs a circle grid (creating the board)
# Color correspondence for turns (can probably use modulus truth, if the turn is even, then whatever color goes first)

    def __init__(self):
        self.root = root
        self.board_initializer()
        self.button_initalizing() # call functions here so easier to call at end
        self.board = Board() # initialize previous class

    def clicked(self, c): # increment pieces in column, visually add piece
        self.board.play_piece(c)
        self.update_board()
        if self.board.check_win():
            self.board.GameOverPopupWindow.gameover_popup(self.board.current_player["Player Number"])
        self.board.players_swap()

    def button_initalizing(self): # making the buttons
        # lambda allows one to be added to each corresponding column of self.pieces_in_rows
        self.buttonA = Button(root, text="Column A", command = lambda: self.clicked(0), bg = "Navy")
        self.buttonA.grid(row=2, column=1)
        self.buttonB = Button(root, text="Column B", command = lambda: self.clicked(1), bg = "Navy")
        self.buttonB.grid(row=2, column=2)
        self.buttonC = Button(root, text="Column C", command = lambda: self.clicked(2), bg = "Navy")
        self.buttonC.grid(row=2, column=3)
        self.buttonD = Button(root, text="Column D", command = lambda: self.clicked(3), bg = "Navy")
        self.buttonD.grid(row=2, column=4)
        self.buttonE = Button(root, text="Column E", command = lambda: self.clicked(4), bg = "Navy")
        self.buttonE.grid(row=2, column=5)
        self.buttonF = Button(root, text="Column F", command = lambda: self.clicked(5), bg = "Navy")
        self.buttonF.grid(row=2, column=6)
        self.buttonG = Button(root, text="Column G", command = lambda: self.clicked(6), bg = "Navy")
        self.buttonG.grid(row=2, column=7)
    
    def board_initializer(self): # needs rest of parts
        self.board_canvas = Canvas(root, width=700, height=600, bg ='blue')
        self.board_canvas.grid(row=3, column=1, columnspan=7)
        self.circles = [[self.board_canvas.create_oval(j * 100, i * 100, (j +1) * 100, (i + 1) * 100, fill='white') for j in range(7)] for i in range(6)]

    def update_board(self):
        row, col = self.board.last_played
        color = self.board.current_player["Color"]
        bottom_row = 5 - row
        self.board_canvas.itemconfig(self.circles[bottom_row][col], fill=color)

# Charlotte pop-up window
class GameInstructions:
    def __init__(self):
        self.instructions = ("Take turns dropping one of your pieces onto the board.", 
        "The first player to get four pieces in a row, vertically, horizontally, or diagnoally, wins!"
        )
        self.display_instructions()
    
    def display_instructions(self):
        messagebox.showinfo("Connect 4 Instructions", "\n".join(self.instructions))

class GameOverPopupWindow:
    def __init__(self, winner, game):
        self.winner = winner
        self.game = game
        self.gameover_popup()

    def gameover_popup(self):
        player_input = messagebox.askyesno(
            "Game Over!",
            f" Player {self.winner} wins! Would you like to restart the game?"
        )
        if player_input:
            print("Restarting the game...")
            self.game_restart()
        else:
            print("Exiting the game...")
            self.game.exit_game()
            
    def game_restart(self):
        self.game.clear_board()
        self.game.setup_new_game()
        print("The game has been reset.") 

class Game:
    def __init__(self):
        self.root = root
        self.gui = GUI(self)
        self.winner = None
        self.start_game()

    def start_game(self):
        GameInstructions()
        self.play_game()

    def play_game(self):
        self.winner = 1
        self.end_game(self.winner)

    def end_game(self, winner):
        self.popup_window = GameOverPopupWindow(winner, self)

    # restarts the game 
    def restart(self):
        print("Restart initiated -- resetting the game...")        
        self.clear_board()
        self.setup_new_game()
        self.start_game()

     def clear_board(self):
        print("Board cleared.")
        self.gui.reset_canvas()

    def setup_new_game(self):
        print("Setting up new game...")
        self.winner = None
        
    # officially exits game 
    def exit_game(self):
        print("Exiting the game...")
        self.root.destroy()

# Emma
# class GameSave:
# Needs connection of removing pieces
# Needs to restart after game is reset
# Needs to start with data if re-opened

#     def __init__(self):
#         self.con = sqlite3.connect('game_progress.db')
#         self.cur = self.con.cursor()
#         self.retrieve_data()

#     def retrieve_data(self):
#         self.cur.execute('''CREATE TABLE IF NOT EXISTS gameprogress
#                 (Player_1_Score BIT, Player_2_Score BIT)''')
#         self.cur.execute('''INSERT INTO gameprogress VALUES 
#                 (self.player1[Score], self.player2["Score"])''')
#         self.con.commit()

# calling functions
#g = GUI()
i = GameInstructions()
#data = GameSave()

# starts the game
game = Game()

root.mainloop()
