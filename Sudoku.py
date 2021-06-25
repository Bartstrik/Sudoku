from math import floor

# My first attempt at making a sudoku solver, took about 5 hours total
# recommended improvements are the calculate_spot functions and making GUI
# Bart Strik







class sudoku():

    #where board is a 2 dimensional array of integers ranging between 0 and 9, 0 means empty 
    def __init__(self, board_in):
        self.board = board_in
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

   
    #this function definetly needs improvement
    def calculate_spot(self, row, column):
        if not self.board[row][column]:
            for option in self.calculate_options(row, column):
                print(option)
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



def main():
    board = [[0, 1, 3, 6, 4, 0, 9, 0, 2], 
            [0, 0, 6, 9, 5, 0, 3, 0, 0],
            [0, 5, 0, 0, 0, 0, 0, 0, 4],
            
            [0, 0, 0, 0, 6, 0, 7, 0, 0],
            [3, 0, 7, 0, 8, 0, 4, 0, 5],
            [0, 0, 2, 0, 7, 0, 0, 0, 0],
            
            [9, 0, 0, 0, 0, 0, 0, 7, 0],
            [0, 0, 1, 0, 9, 7, 2, 0, 0],
            [8, 0, 5, 0, 2, 3, 1, 6, 0]]

    Sudoku = sudoku(board)

    Sudoku.calculate_spot(0, 0)
    
    for i in Sudoku.board:
        print(*i)
    return

if __name__ == "__main__":
    main()