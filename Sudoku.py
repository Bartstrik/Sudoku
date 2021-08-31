from math import floor
import tkinter as tk
from tkinter import ttk
# recommended improvements are the calculate_spot functions and making GUI
# Bart Strik


class sudoku():

    #where board is a 2 dimensional array of integers ranging between 0 and 9, 0 means empty 
    def __init__(self, _board):
        self.board = _board
        self.finished = False
        return

    def __repr__(self):      
        return self.board

    def calculate_options(self, row, column):
        options  = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        row_list = self.board[row]
        column_list = self.get_column_list(column)
        section_list  = self.get_section(row, column)
        for value in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            #if any of the options are already in the row, column or section: remove them from options
            if value in row_list:
                options.remove(value)
                continue
            
            if value in column_list:
                options.remove(value)
                continue

            if value in section_list:
                options.remove(value)
                continue

        return options

    def get_section(self, row, column):
        section_list = []
        row_index = floor(row / 3) * 3
        column_index = floor(column / 3) * 3
        
        for i in range(row_index, row_index + 3):
            for ii in range(column_index, column_index + 3):
                if self.board[i][ii]:
                    section_list.append(self.board[i][ii])
               
        return section_list
    
    

    def get_column_list(self, column):
        column_list = []
        for row in self.board:
            column_list.append(row[column])
        return column_list

   
    #this function definetly needs improvement, and maybe error handling aswell
    def calculate_spot(self, row, column):
        #print("row = {}, column = {}".format(row, column))
        if self.board[row][column] == 0:
            for option in self.calculate_options(row, column):
                #print(option)
                self.board[row][column] = option
                #recursive case, calls recursive functions
                if column < 8 and row < 9:
                    self.calculate_spot(row, (column + 1))
                elif row < 8:
                    self.calculate_spot(row + 1, 0)
                else:
                    self.finished = True 
                if self.finished:
                    break
            if not self.finished:
                #base case because none of the options worked, which means a previous choice was wrong
                self.board[row][column] = 0 
        else:
            if column < 8 and row < 9:
                self.calculate_spot(row, (column + 1))
            elif row < 8:
                self.calculate_spot(row + 1, 0)
            else:
                self.finished = True

            return

class window():
    
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Swagdoku")
        self.window.geometry("500x900")

        self.entry_frame = self.create_sudoku_frame()
        self.entry_frame.grid(column = 0, row = 0)
        
        return

    #this function is called by the submit button
    def submit_sudoku(self):

        tk.Label(self.window, text = "result").grid(column = 0, row = 2)
        #this can be made more efficient by removing the local board variable and parsing the values directly.
        self.board = []
        for i in range(9):
            self.board.append([])
            for j in range(9):
                self.board[i].append(int(self.spinbox_value[j][i].get()))
                
        
        
        #parse the board to the Sudoku() class, solve the sudoku and parse back.
        Sudoku = sudoku(self.board)
        Sudoku.calculate_spot(0, 0)
        self.board = Sudoku.board
        
        self.result_frame = self.create_sudoku_frame()
        self.result_frame.grid(column = 0, row = 3)
        for i in range(9):
            for j in range(9):
                tk.Label(self.result_frame, text = "{}".format(Sudoku.board[i][j])).grid(row = i, column = j, padx = 10, pady= 10)
        return

    def create_entry_sudoku(self):
        self.spinbox_value = []

        for i in range(9):
            self.spinbox_value.append([])
            for j in range(9):
                self.spinbox_value[i].append(tk.StringVar(value = 0))
                tk.Spinbox(self.entry_frame, from_ = 0, to = 9, textvariable = self.spinbox_value[i][j], wrap = True, width = 2).grid(row = j, column = i, padx = 10, pady= 10)

        tk.Button(self.window, text = "Submit", padx = 2, command = self.submit_sudoku).grid(column = 0, row = 1)
        return

    def create_sudoku_frame(self):
        sudoku_frame = tk.Frame(self.window)
        for i in range(10):
            ttk.Separator(sudoku_frame, orient="vertical").grid(column=i, row=0, rowspan=10, sticky = "nwsw")
            ttk.Separator(sudoku_frame, orient="horizontal").grid(column=0, row=i, columnspan=10, sticky = "nwne")
        return sudoku_frame

def main():
    Window = window() 
    Window.create_entry_sudoku()
    Window.window.mainloop()
    return

if __name__ == "__main__":
    main()
