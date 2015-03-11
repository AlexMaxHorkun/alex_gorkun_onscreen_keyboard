__author__ = 'Alexander Gorkun'

import tkinter as tk
import math

from agorkun_onscreenkeyboard import widgets


class OnscreenKeyboardApp(tk.Frame):
    """
    Показывает экранную клавиатуру для воода текста в поле.
    """
    __quit_button = None

    __text_edit = None

    __keys = ['A', 'B', 'C', 'D', 'E', 'F', 'G', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', ',', '?']

    max_key_cols = 5

    def __init__(self):
        super().__init__(master=tk.Tk(), cnf={'width': 640, 'height': 480})
        self.master.title('Экранная клавиатура. Александр Горкун')
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(600, 280))

    def __init_widgets(self):
        self.__quit_button = tk.Button(self, text='Выйти', command=self.master.destroy)
        self.__quit_button.grid(column=self.max_key_cols, row=math.ceil(len(self.__keys) / self.max_key_cols) + 2)

        self.__text_edit = tk.Text(self, height=4)
        self.__text_edit.grid(column=0, row=0, columnspan=self.max_key_cols + 1, pady=8)
        self.__text_edit.focus()

        def put_text(text):
            self.__text_edit.insert(tk.INSERT, text)

        cur_col = 0
        cur_row = 1
        for key in self.__keys:
            widgets.KeyButton(self, self.__text_edit, symbol=key).grid(column=cur_col, row=cur_row)
            cur_col += 1
            if cur_col >= self.max_key_cols:
                cur_col = 0
                cur_row += 1
        if cur_col != 0:
            cur_row += 1
        widgets.KeyButton(self, self.__text_edit, symbol=' ', text='SPACE').grid(column=0, row=cur_row,
                                                                                 columnspan=self.max_key_cols, ipadx=90)
        widgets.Backspace(self, self.__text_edit).grid(column=self.max_key_cols, row=1, ipadx=10)

    def run(self):
        self.grid(padx=15, pady=10)
        self.__init_widgets()
        self.mainloop()


app = OnscreenKeyboardApp()
app.run()