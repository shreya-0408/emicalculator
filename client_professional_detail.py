from tkinter import *

def clientprofessionaldetail():
    root=Tk()
    root.title("Profile Account Detail")
    root.geometry('950x750+310+30')

    Manage_frame = Frame(root, bd=4, relief=RIDGE, bg="white")
    Manage_frame.place(x=20, y=20, width=900, height=710)

    Manage_frame1= Frame(Manage_frame, bd=4, relief=RIDGE, bg="whitesmoke")
    Manage_frame1.place(x=30, y=60, width=690, height=500)

    Manage_frame2 = Frame(Manage_frame, bd=4, relief=RIDGE, bg="teal")
    Manage_frame2.place(x=190, y=10, width=370, height=45)

    lbl_name1 = Label(Manage_frame2, text="Client Professional Detail", fg="white", bg="teal", font=('times new roman', 20, 'bold'))
    lbl_name1.place(x=20, y=2)

    Manage_frame3 = Frame(Manage_frame, bd=4, relief=RIDGE, bg="darkslategray")
    Manage_frame3.place(x=30, y=570, width=690, height=120)

    lbl_name1 = Label(Manage_frame1, text="Client ID", fg="black", bg="whitesmoke", font=('times new roman', 20, 'bold'))
    lbl_name1.grid(row=1, column=0, pady=40, padx=30, sticky="W")
    txt_name1 = Entry(Manage_frame1, font=('times new roman', 15, 'bold'), bd=2,width=30,
                     relief=GROOVE)
    txt_name1.grid(row=1, column=1, pady=10, padx=50, sticky="W")

    lbl_name2 = Label(Manage_frame1, text="Profession", fg="black", bg="whitesmoke", font=('times new roman', 20, 'bold'))
    lbl_name2.grid(row=2, column=0, pady=10, padx=30, sticky="W")
    txt_name2 = Entry(Manage_frame1, font=('times new roman', 15, 'bold'), bd=2,width=30,
                     relief=GROOVE)
    txt_name2.grid(row=2, column=1, pady=10, padx=50, sticky="W")



    lbl_name3 = Label(Manage_frame1, text="Designation", fg="black", bg="whitesmoke", font=('times new roman', 20, 'bold'))
    lbl_name3.grid(row=3, column=0, pady=10, padx=30, sticky="W")
    txt_name3 = Entry(Manage_frame1, font=('times new roman', 15, 'bold'), bd=2,width=30,
                     relief=GROOVE)
    txt_name3.grid(row=3, column=1, pady=10, padx=50, sticky="W")

    lbl_name4 = Label(Manage_frame1, text="Office Phone", fg="black", bg="whitesmoke", font=('times new roman', 20, 'bold'))
    lbl_name4.grid(row=4, column=0, pady=10, padx=30, sticky="W")
    txt_name4 = Entry(Manage_frame1, font=('times new roman', 15, 'bold'), bd=2,width=30,
                     relief=GROOVE)
    txt_name4.grid(row=4, column=1, pady=10, padx=50, sticky="W")

    lbl_name5 = Label(Manage_frame1, text="Office Address", fg="black", bg="whitesmoke", font=('times new roman', 20, 'bold'))
    lbl_name5.grid(row=5, column=0, pady=10, padx=30, sticky="W")
    txt_name5 = Entry(Manage_frame1, font=('times new roman', 15, 'bold'), bd=2, width=30,
                      relief=GROOVE)
    txt_name5.grid(row=5, column=1, pady=10, padx=50, sticky="W")

    lbl_name6 = Label(Manage_frame1, text="Annual Income", fg="black", bg="whitesmoke", font=('times new roman', 20, 'bold'))
    lbl_name6.grid(row=6, column=0, pady=10, padx=30, sticky="W")
    txt_name6 = Entry(Manage_frame1, font=('times new roman', 15, 'bold'), bd=2, width=30,
                      relief=GROOVE)
    txt_name6.grid(row=6, column=1, pady=10, padx=50, sticky="W")

    lbl_name7 = Label(Manage_frame1, text="Other Income", fg="black", bg="whitesmoke",
                      font=('times new roman', 20, 'bold'))
    lbl_name7.grid(row=7, column=0, pady=10, padx=30, sticky="W")
    txt_name7 = Entry(Manage_frame1, font=('times new roman', 15, 'bold'), bd=2, width=30,
                      relief=GROOVE)
    txt_name7.grid(row=7, column=1, pady=10, padx=50, sticky="W")



    first_btn = Button(Manage_frame3, text="First", width=13, pady=5, bg="lightcyan", fg="black", bd=5,
                        font=('times new roman', 11, 'bold'))
    first_btn.place(x=50, y=5)

    previous_btn=Button(Manage_frame3,text="Previous",width=13, pady=5,bg="lightcyan",fg="black",bd=5, font=('times new roman', 11, 'bold'))
    previous_btn.place(x=200,y=5)

    next_btn = Button(Manage_frame3, text="Next", width=13, pady=5,bg="lightcyan",fg="black",bd=5, font=('times new roman', 11, 'bold'))
    next_btn.place(x=350, y=5)

    last_btn = Button(Manage_frame3, text="Last", width=13, pady=5, bg="lightcyan", fg="black", bd=5,
                        font=('times new roman', 11, 'bold'))
    last_btn.place(x=500, y=5)


    add_btn = Button(Manage_frame3, text="Add", width=13, pady=5, bg="lightcyan", fg="black", bd=5,
                     font=('times new roman', 11, 'bold'))
    add_btn.place(x=50, y=60)

    update_btn = Button(Manage_frame3, text="Update", width=13, pady=5, bg="lightcyan", fg="black", bd=5,
                        font=('times new roman', 11, 'bold'))
    update_btn.place(x=200, y=60)

    save_btn = Button(Manage_frame3, text="Save", width=13, pady=5, bg="lightcyan", fg="black", bd=5,
                      font=('times new roman', 11, 'bold'))
    save_btn.place(x=350, y=60)

    cancel_btn = Button(Manage_frame3, text="Cancel", width=13, pady=5, bg="lightcyan", fg="black", bd=5,
                        font=('times new roman', 11, 'bold'))
    cancel_btn.place(x=500, y=60)



    mainloop()