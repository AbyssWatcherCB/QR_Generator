import qrcode
from tkinter import *

cp = Tk()
cp.title('QR Generator')
cp.geometry('700x300')
cp.config(bg="#393d49")

def generate():
    img = qrcode.make(msg.get())

    type(img)
    img.save(f'{save_name.get()}.png')
    Label(cp, text='Saved', bg='green', fg='black', font=('Lucida Console', 8)).pack()

def show():
    img = qrcode.make(msg.get())
    type(img)
    img.show()
    
frame = Frame(cp, bg='#393d49')
frame.pack(expand=True)


Label(frame, text='Enter the URL : ', font=('Lucida Console', 12),
      bg='#393d49').grid(row=0, column=0, sticky='w')
msg = Entry(frame)
msg.grid(row=0, column=1)


Label(frame, text='File Name : ', font=('Lucida Console', 12),
      bg='#393d49').grid(row=1, column=0, sticky='w')
save_name = Entry(frame)
save_name.grid(row=1, column=1)


btn = Button(cp, text='Show QR code', bd='5', command=show, width=15)
btn.pack()
btn = Button(cp, text='Save QR code', command=generate, bd='5', width=15)
btn.pack()


cp.mainloop()