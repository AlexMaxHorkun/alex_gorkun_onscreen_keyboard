__author__ = 'Alexander Gorkun'

import tkinter as tk
import math


class OnscreenKeyboardApp(tk.Frame):
    """
    Показывает экранную клавиатуру для воода текста в поле.
    """
    __quit_button = None

    __text_edit = None

    __keys = ['A', 'B', 'C', 'D', 'E', 'F', 'G', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    max_key_cols = 5

    def __init__(self):
        super().__init__(master=tk.Tk(), cnf={'width': 640, 'height': 480})
        self.master.title('Экранная клавиатура. Александр Горкун')
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(640, 480))

    def __init_widgets(self):
        self.__quit_button = tk.Button(self, text='Выйти')
        self.__quit_button.grid(column=self.max_key_cols, row=math.ceil(len(self.__keys)/self.max_key_cols))

        self.__text_edit=tk.Text(self)
        self.__text_edit.grid(column=0, row=0, columnspan=self.max_key_cols)

        def put_text(text):
            self.__text_edit.insert(tk.INSERT, text)

        cur_col = 0
        cur_row = 1
        for key in self.__keys:
            tk.Button(self, text=key, command=lambda: put_text(key)).grid(column=cur_col, row=cur_row)
            cur_col+=1
            if cur_col >= self.max_key_cols:
                cur_col=0
                cur_row+=1

    def run(self):
        self.grid()
        self.__init_widgets()
        self.mainloop()


app = OnscreenKeyboardApp()
app.run()