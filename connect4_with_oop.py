from tkinter import *

global root # allows root to be accessed through all classes
root = Tk()
root.title("Connect4")

class Players:
    def __init__(self):
        self.player1 = {"Name": "Player 1", "Turns Taken": 0, "Pieces": 21} # can use dictionaries to count turns and number of pieces gone
        self.player2 = {"Name": "Player 2", "Turns Taken": 0, "Pieces": 21}
        self.colors = ["Red", "Yellow"]
        self.color_assignment()
    
    def color_assignment(self):
        self.player_1_choice = input("Player 1, pick red or yellow: ")
        self.player_1_choice.lower()
        self.player_1_choice.strip()
        if self.player_1_choice == "red":
            self.player1.update({"Color": "Red"})
            self.player2.update({"Color": "Yellow"})
        elif self.player_1_choice == "yellow":
            self.player1.update({"Color": "Yellow"})
            self.player2.update({"Color": "Red"})
        else:
            print("That is not a valid color option. Pick yellow or red.")

class Board: # setting up the board, tracking game
    def __init__(self):
        self.rows = 6
        self.columns = 7
        self.pieces = [0, 0, 0, 0, 0, 0, 0]
        self.piece_options = {"Player 1": 21, "Player 2": 21}

    def add_to_column(self, c):
        if self.pieces[c] < 6:
            self.pieces[c] += 1

    def check_win(self, c):
        if self.pieces(c) == 6: # need to add parameter where only displays if the corresponding button is pressed
            print("This column is full. Go elsewhere.")
    
    def turn(self):
        self.piece = piece
        while True:
            if self.player1["Color"] == "Red":
                piece = "Red"
            elif self.player1["Color"] == "Yellow":
                piece = "Yellow"
        

class GUI: # interface elements
    def __init__(self):
        self.root = root
        self.board_initializer()
        self.button_initalizing() # call functions here so easier to call at end
        self.board = Board() # initialize previous class

    def clicked(self, c): # increment pieces in column, visually add piece
        self.board.add_to_column(c)
        print(self.board.pieces)

    def button_initalizing(self): # making the buttons
        # lambda allows one to be added to each corresponding column of self.pieces
        self.buttonA = Button(self.root, text="Column A", command = lambda: self.clicked(0), bg = "Navy")
        self.buttonA.grid(row=2, column=1)
        self.buttonB = Button(self.root, text="Column B", command = lambda: self.clicked(1), bg = "Navy")
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

class GameInstructions:
    def __init__(self):
        self.instructions = instructions

    def game_instructions(self):
        instructions = ("Take turns dropping one of your pieces onto the board.", 
        "The first player to get four pieces in a row, vertically, horizontally, or diagnoally, wins!")
    
    def display_instructions():
        messagebox.showinfo("Connect 4 Instructions", instructions)

# class DataSave:
#     def __init__(self, database_routing):
#         self.game_save = game_save
#         self.con = sqlite3.connect('game_progress.db')
#         self.cur = con.cursor()
#     # to be continued once rest is done; need save variables before
# #    cur.execute('''CREATE TABLE IF NOT EXISTS gameprogress
# #                (Player 1 Score, Player 2 Score, Position)''')

# calling functions
b = Board()
g = GUI()
root.mainloop()
