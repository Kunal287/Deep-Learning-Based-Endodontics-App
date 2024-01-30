from tkinter import *
from Login_Page import *
splash_screen = Tk()
splash_screen.geometry('700x300+300+200')
splash_screen.overrideredirect(True) # remove border

# add text
text = Label(splash_screen, text ="Starting...", font = ('san-serf', 40), fg = "red")
text.place(x = 250, y = 100)

def hide():
    splash_screen.destroy()
    Login()



splash_screen.after(5000, hide)


mainloop()