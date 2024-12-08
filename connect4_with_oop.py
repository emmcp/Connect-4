from tkinter import *
from tkinter import messagebox
import random
import sqlite3

class Board: # setting up the board
    root = Tk()

    def __init__(self):
        self.rows = 6
        self.columns = 7

    def boardgrid(self, rows, column): # set up board grid
        for row in range(self.rows):
            for column in range(self.columns):
                x1 = column * 100 + 10
                y1 = row * 100 + 10
                x2 = x1 + 80
                y2 = y1 + 80

    def board_set_up(self, root): # board interactivity
        self.board = [[ '' for _ in range(self.COLS)] for _ in range(self.ROWS)]

        # Creating a frame to hold the buttons for dropping the discs
        self.frame = Frame(self.root)
        self.frame.pack()

        self.buttons = [Button(self.frame, text=f"Drop {i+1}", command = lambda col=i: self.drop_disc(col)) for i in range(self.COLS)]
        for button in self.buttons:
            button.pack(side="left", padx=10) # placing the buttons side by side
            # creating a canvas to draw the game board

    def draw_board(self, root): # set up tkinter functions of board
        canvas = tk.Canvas(self.root, width = 700, height=600, bg = "blue")
        #self.Canvas.pack = Canvas(self.root, width = 700, height=600, bg = "blue")
        self.Canvas.pack()
        # create the empty game board
        self.draw_board()

class Players: # player initialization, player switching, etc.
    def __init__(self):
        self.colors = ("Red", "Yellow")
        self.player1 = player1
        self.player2 = player2
        self.players = (player1, player2)

class GamePlay: # put game functions: dropping pieces, etc.

class CheckWin: # checking for win, try/except features, etc.

class GameProgress: # save current player turn, where they went on the board, etc.
    def __init__(self):
        self.currentplayer = currentplayer
        self.takenspaces = takenspaces
    
class GameInstructions:
    def __init__(self):
        self.instructions = instructions

    def game_instructions(self):
        instructions = ("Take turns dropping one of your pieces onto the board.", 
        "The first player to get four pieces in a row, vertically, horizontally, or diagnoally, wins!")
    
    def display_instructions():
        messagebox.showinfo("Connect 4 Instructions", instructions)

class DataSave:
    def __init__(self, database_routing):
        self.game_save = game_save
        self.con = sqlite3.connect('game_progress.db')
        self.cur = con.cursor()
    # to be continued once rest is done; need save variables before
#    cur.execute('''CREATE TABLE IF NOT EXISTS gameprogress
#                (Player 1 Score, Player 2 Score, Position)''')

root = Tk()
root.mainloop()
