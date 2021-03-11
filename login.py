from tkinter import *

def login():
    window = Tk()
    window.title('Login Details..!')
    window.configure(bg='cadetblue')
    window.geometry('530x230+500+300')

    lbl1 = Label(window,text='Login Details:-',fg='white',font=('helvetica',9),bg="cadetblue")
    lbl1.place(x=10,y=10)

    lbl2 = Label(window,text='USERNAME',font=('Arial',15,'bold'),bg="cadetblue")
    lbl2.place(x=60,y=80)

    usrnmtxt= Entry(window,text='This is entry widget ',bd=4,fg='blue',width=30)
    usrnmtxt.place(x=230,y=80)

    lbl3 = Label(window,text='PASSWORD',font=('Arial',15,'bold'),bg="cadetblue")
    lbl3.place(x=60,y=120)

    passtxt = Entry(window,text='This is entry widget ',bd=4,fg='blue',show='*',width=30)
    passtxt.place(x=230,y=120)
    #img = ImageTk.PhotoImage(Image.open("E:\login"))
    #img.place(x=250,y=50)

    btn = Button(window,text='LOGIN',bg='whitesmoke',fg='black',font=('Arial',8,'bold'),command=login)
    btn.place(x=100,y=180)
    btn = Button(window,text='RESET',bg='whitesmoke',fg='black',font=('Arial',8,'bold'))
    btn.place(x=200,y=180)
    btn = Button(window,text='FORGET PASSWORD ',bg='whitesmoke',fg='black',font=('Arial',8,'bold'))
    btn.place(x=300,y=180)

login()
mainloop()