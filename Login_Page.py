from tkinter import messagebox
from Menu import *
def Login():
    root1=Tk()
    # defining all the attributes of our frame
    root1.title('Patient Details')
    height=400
    width=400
    screen_width = root1.winfo_screenwidth()
    screen_height = root1.winfo_screenheight()
    # calculate position x and y coordinates
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root1.geometry('%dx%d+%d+%d'%(width,height,x,y))
    root1.resizable(width=False, height=False)
    root1.title("Login Page")
    Name="Admin"
    Password="1234"
    # Creating all the labels and Entry text here
    l1 = Label(root1, text='Name', padx=5, pady=5,bg="#AFEEEE")
    l1.place(x=70, y=100)
    l2 = Label(root1, text='Password', padx=5, pady=5,bg="#AFEEEE")
    l2.place(x=50, y=150)
    t1 = Entry(root1)
    t1.place(x=120, y=100)
    t2 = Entry(root1,show="*")
    t2.place(x=120, y=150)
    Button(root1, text='Validate and Login', command=lambda: Validate(t1,t2)).place(x=150, y=200)
    # Function to check whether Entered details are correct or not
    def Validate(t1,t2):
        if(len(t1.get())==0 or t1.get()!=Name or len(t2.get())==0 or t2.get()!=Password):
            messagebox.showerror("Login Error", "Please Enter Correct Name or Password")
        else:
            messagebox.showinfo("Login Success", "Login Successful")
            Menu(root1)
    root1.configure(bg="#AFEEEE")
    root1.mainloop()
if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   Login()