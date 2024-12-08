import tkinter as tk
from tkinter import messagebox
import random
class Connect4:
    def __init__(self, root):
        self.ROWS = 6  #number of rows on the board
        self.COLS = 7  #number of colums of the board 
        self.current_player = random.choice(["Red", "Yellow"]) # randomizes player
        # Creating a 2D 6x7 grid to represent the game board 
        self.board = [[ '' for _ in range(self.COLS)] for _ in range(self.ROWS)]

        #game instructtions 
        self.game_instructions
        # Creating a frame to hold the buttons for dropping the discs
        self.frame = tk.Frame(self.root)
        self.frame.pack()
            # Creating a button at the top of each column
        self.buttons = [tk.Button(self.frame, text=f"Drop {i+1}", command = lambda col=i: self.drop_disc(col)) for i in range(self.COLS)]
        for button in self.buttons:
            button.pack(side=tk.LEFT, padx=10) # placing the buttons side by side
            # creating a canvas to draw the game board
        self.canvas.pack = tk.Canvas(self.root, width = 700, hight=600, bg = "blue")
        self.canvas.pack()
# create the empty game board
        self.draw_board()
    def game_instructions(self):
        instructions = (
            game instructions go here
        )
        messagebox.showinfo("Connect 4 Instructions", instructions)
    def draw_board(self):
    
        self.canvas.delete("all") # this clears the entire canvas 
        for row in range(self.ROWS):
                for col in range(self.COLS):
                    # find the coordinates for each slot
                    X1, y1 = col * 100 +10 , row * 100 + 10
                    X2, y2 = x1 + 80, y1 +80
                    # specify the slot colors between Yellow and Red if occupied otherwise white
                    color = self.board[row][col] if self.board[row][col] else "white"
                    #make a circle representing the slots
                    self.canvas.create_oval(x1, y1, x2, y2, fill=color, outline="black")
        def drop_disc(self, col):
                # check if theres been a move made for the bottom to the top 
            for row in range(self.ROWS -1, -1, -1):
                if not self.board[row][col]: #see if the slot is empty
                    self.board[row][col] = self.current_player #drop the current players disc
                    self.draw_board() # updates the boards visuals 
                    self.root.upadate() # makes sure the GUI is updating 
                if self.check_winner(row, col):
                    messagebox.showinfo("Game Over", f"{self.current_player} wins!") #visual for winner
                    self.rest_game() #rests the game after a win 
                    return 
                elif all(self.board[0][col] for col in range(self.COLS)):
                    messagebox.showinfo("Game Over", "It's a draw!")  # Handle a draw scenario
                    self.reset_game()  # Reset the game
                    return

                # Switch to the other player for the next turn
                self.current_player = "Yellow" if self.current_player == "Red" else "Red"
                return

        # If no empty slots are found in the column, show a warning
        messagebox.showwarning("Invalid Move", "Column is full!")
   
if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk()
    # Start the Connect 4 game
    game = Connect4(root)
    # Run the Tkinter event loop
    root.mainloop()

# Emma's Code
class GameSave:
    def __init__(self):
        self.game_save = game_save
        self.con = sqlite3.connect('game_progress.db')
        self.cur = con.cursor()
# will finish once all variables are made; need to save by creating player move and player move count to store here
