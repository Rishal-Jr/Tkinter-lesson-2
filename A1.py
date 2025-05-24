from tkinter import *
root=Tk()
root.title("Number pad")
root.geometry("300x200")

nums=[[9,8,7],[6,5,4],[3,2,1],['*',0,"#"]]

for i in range(4):
    root.columnconfigure(i, weight=1, minsize=75)
    root.rowconfigure(i, weight=1, minsize=50)

for i in range(4):
    for j in range(3):
        frame=Frame(master=root, borderwidth=1, relief="sunken",
            bg="black")
        frame.grid(row=i, column=j, sticky="nsew")
        label=Label(master=frame, text=nums[i][j], bg="black", fg="white",font=("Arial", 24))
        label.pack(expand=True, fill="both",pad=5,pady=5)
root.mainloop()        
           


