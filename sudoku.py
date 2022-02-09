import tkinter as tk
from tkinter import ttk
from tkinter import *

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # Configure the root windows
        self.title('Suduko')
        self.configure(padx=20)
        # Labels
        overskrift = ttk.Label(self, text='Sudoku', font=('Sans-Serif', 40))
        overskrift.grid(row=0, columnspan=10, padx=5, pady=20)

        # Crate the Sudoku boards
        self.entries = []
        grid_dim = 9

        for row in range(grid_dim):
            for col in range(grid_dim):

                entry = tk.Entry(self, justify='center', width=3, highlightthickness=1, highlightbackground='#000000')
    
                pad_y = (0, 0)
                pad_x = (0, 0)
                
                if (row+1) % 3 == 0 and (row+1) < grid_dim: # skip for last row
                    pad_y = (0, 10)
                    
                if (col+1) % 3 == 0 and (col+1) < grid_dim: # skip for last column
                    pad_x = (0, 10)

                entry.grid(row=1+row, column=1+col, ipadx=10, ipady=10, padx=pad_x, pady=pad_y)
        self.entries.append(entry)

        # Buttons on the bottom of the screen
        # Reset the board and start over
        reset = ttk.Button(self, text='Reset', command=self.reset_sudoku)
        reset.grid(row=10, column=0, columnspan=10, sticky='W', padx=5, pady=15)

        # Generate new sudoku
        generate = ttk.Button(self, text='Generate', command=self.generate_sudoku)
        generate.grid(row=10, column=0, columnspan=10, padx=5, pady=15)

        # Finish
        finish = ttk.Button(self, text='Finish', command=self.finish_sudoku)
        finish.grid(row=10, column=0, columnspan=10, sticky='E', padx=5, pady=15)

        # Copyright label
        copyright = Label(self, text='© Bjørnar Borge', font=('Sans-Serif', '8'))
        copyright.grid(row=11, columnspan=10, padx=5, pady=10)


    def reset_sudoku(self):
        print('Resetting Sudoku')
        # for entry in self.entries:
        #    entry = ''
        #    self.entries(entry)

    def generate_sudoku(self):
        print('generate_sudoku')

    def finish_sudoku(self):
        print('finish_sudoku')

if __name__ == '__main__':
    App().mainloop()
    







