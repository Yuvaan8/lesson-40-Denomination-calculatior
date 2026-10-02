from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
root = Tk()
root.title('Denomination Calculator')
root.configure(bg ='light grey')
root.geometry('650x400')
upload = Image.open('hii.png')
upload = upload.resize((300,300))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg='light blue')
label.place(x=180, y=20)
label1 = Label(
    root,
    text= 'Hey user! Welcome to denomination calculator!',
    bg='light blue',
)
label1.place(relx=0.5, y=320, anchor=CENTER)
def msg():
    Msgbox = messagebox.showinfo(
        'Alert!',
        'Are you sure you want to calculate the denomination count?',
    )
    if Msgbox == 'ok':
        topwin()
button1 = Button(
    root,
    text = 'lets get started!',
    command=msg,
    bg='brown',
    fg='white'
)
button1.place(x=260, y=360)
def topwin():
    top = Toplevel()
    top.title('Denomination Calculator')
    top.configure(bg = 'light grey')
    top.geometry('650x400+50+50')
    label = Label(top, text='this is the total amount', bg = 'light grey')
    entry= Entry(top)
    IbI = Label(
        top,
        text='here are notes for each denominatio ',
        bg='light grey'
    )
    l1 = Label(top, text=2000, bg='light grey')
    l2 = Label(top, text=500, bg='light grey')
    l3 = Label(top, text=100, bg='light grey')
    t1= Entry(top)
    t2= Entry(top)
    t3= Entry(top)
    def calculator():
        try:
            amount = int(entry.get())
            note2000= amount // 2000
            note%= 2000
            note500 = amount // 500
            note%= 500
            note100 = amount // 100
            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)
            t1.insert(0, str(note2000))
            t2.insert(0, str(note500))
            t3.insert(0, str(note100))
        except ValueError:
            messagebox.showerror('Error', 'Please enter a valid amount')
        btn = Button(
            top,
            text='calculate',
            command=calculator,
            bg='brown',
            fg='white',
        )
        label.place(x=230, y=50)
        entry.place(x=200, y=80)
        btn.place(x=240, y=120)
        IbI.place(x=140, y=170)
        l1.place(x=180, y=200)
        l2.place(x=180, y=230)
        l3.place(x=180, y=260)
        t1.place(x=180, y=200)
        t2.place(x=180, y=230)
        t3.place(x=180, y=260)
        top.mainloop()
root.mainloop()
        
        
