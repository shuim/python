from tkinter import Tk,Button,Entry,Label

my_window = Tk()

# window close
def window_close():
    my_window.quit()

def say_hello():
    print("hello!")

# buttons
my_button = Button(master=my_window,text="Close me!",command=window_close )
my_button.pack()

hello_button = Button(master=my_window, text="Say Hello", command=say_hello)
hello_button.pack()

# box
TextBox = Entry(master=my_window)
TextBox.pack()

# label
my_label = Label(master=my_window,text = "This is Label")
my_label.pack()

# window size
my_window.geometry("500x250")

my_window.mainloop()
