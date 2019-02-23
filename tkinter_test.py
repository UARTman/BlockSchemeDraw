import tkinter as tk
import tkinter.ttk as ttk


class CodeFrame(tk.Frame):
    def __init__(self, master=None, codetxt='', **kwargs):
        super().__init__(master, **kwargs)
        self.codetxt = tk.Text(self)
        self.codetxt.insert(1.0, codetxt)
        self.codetxt.pack()
        self.conf()

    def conf(self):
        pass


root = tk.Tk()
root.geometry('500x500')
a = ttk.Button(root)
b = CodeFrame(root, bg='gray', codetxt='Hello World!')
# a.pack()
b.pack()
root.mainloop()
