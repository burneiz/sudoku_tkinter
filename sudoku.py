import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configure the root windows
        self.title('Suduko')
        self.geometry('500x500+500+150')

        # Labels
        self.label = ttk.Label(self, text='Sudoku')
        self.label.grid(row=0, columnspan=2)

        # Button
        self.button = ttk.Button(self, text='New Sudoku')
        self.button['command'] = self.new_sudoku
        self.button.grid(row=1, columnspan=2)

    def new_sudoku(self):
        showinfo(title='Sudoku', message='New Sudoku generated')

if __name__ == '__main__':
    app = App()
    app.mainloop()
    







