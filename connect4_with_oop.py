from tkinter import *
from tkinter import messagebox
import random
import sqlite3

global root # allows root to be accessed through all classes
root = Tk()
root.title("Connect4")

# Emma
class Players: #need to add later in code functions that will add their turns taken when they go and removes pieces
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

class Board: # setting up the board, tracking game
# Need to add: Way to check a win 
# Color corresponding to pieces and player

    def __init__(self):
        self.rows = 6
        self.columns = 7
        self.pieces_in_rows = [0, 0, 0, 0, 0, 0, 0]
        self.board_game = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]] # 6 rows with seven columns
        self.Players = Players()
        self.current_player = self.Players.player1 # starts off with a player 1

    def add_to_column(self, c):
        if self.pieces_in_rows[c] < 6:
            self.board_game[self.pieces_in_rows[c]][c] = self.current_player["Player Number"]
            self.pieces_in_rows[c] += 1 # adds one to piece
            print(self.board_game)
        else:
            messagebox.showinfo("Error: Column is full", "Pick another column.")

    #def check_win(self, c): # needs to clear board, check win, check if all pieces gone

    def players_swap(self):
        if self.current_player == self.player_1:
            self.current_player = self.player_2

        else:
            self.current_player = self.player_1
            
    # def turn(self):
    #     self.piece = piece
    #     while True:
    #         if self.player1["Color"] == "Red":
    #             piece = "Red"
    #         elif self.player1["Color"] == "Yellow":
    #             piece = "Yellow"

    
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
        self.board.add_to_column(c)
        print(self.board.pieces_in_rows)

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

        self.buttons = [self.buttonA, self.buttonB, self.buttonB, self.buttonC, 
        self.buttonD, self.buttonE, self.buttonF, self.buttonG]
    
    def board_initializer(self): # needs rest of parts
        self.root.configure(bg='navy')

# Charlotte
class GameInstructions: # pop-up window
    def __init__(self):
        self.instructions = ("Take turns dropping one of your pieces onto the board.", 
        "The first player to get four pieces in a row, vertically, horizontally, or diagnoally, wins!")
        self.display_instructions()
    
    def display_instructions(self):
        messagebox.showinfo("Connect 4 Instructions", self.instructions)

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
b = Board()
g = GUI()
i = GameInstructions()
#data = GameSave()
root.mainloop()
