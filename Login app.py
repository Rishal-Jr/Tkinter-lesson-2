from tkinter import *
root=Tk()
root.title("Number pad")
root.geometry("400x400")

frame=Frame(master=root, borderwidth=1, relief="sunken",
    bg="black",width=360,height=200)

lbl1=Label(master=frame, text="Fullname", bg="black", fg="white",font=("Arial", 24),width=12)
lbl2=Label(master=frame, text="email", bg="black", fg="white",font=("Arial", 24),width=12)
lbl3=Label(master=frame, text="Password", bg="black", fg="white",font=("Arial", 24),width=12)

name_entry=Entry(frame)
email_entry=Entry(frame)
password_entry=Entry(frame, show="*")

def display():
    name=name_entry.get()
    greet="Hello "+name
    Message="\n Welcome to the login app"
    textbox.insert(END, greet)
    textbox.insert(END, Message)

    textbox=Text(bg="black", fg="white")

    btn=Button(master=frame, text="Create Account", command=display, bg="red", fg="white",font=("Arial", 24),width=12)

    frame.place(x=20, y=0)
    lbl1.place(x=20, y=20)
    name_entry.place(x=150, y=80)
    lbl2.place(x=20, y=80)
    email_entry.place(x=150, y=80)
    lbl3.place(x=20, y=140)
    password_entry.place(x=150, y=140)
    btn.place(x=20, y=200)
    textbox.place(y=250)

    root.mainloop()

