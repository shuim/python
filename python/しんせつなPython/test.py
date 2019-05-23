import tkinter
from tkinter import filedialog as tkFileDialog

my_file = tkFileDialog.askopenfilename()
print(type(my_file))
print(my_file)
