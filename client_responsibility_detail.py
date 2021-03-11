from tkinter import *
import MySQLdb
from tkinter import messagebox


def clientresponsibilitydetail():
    def add():
        delete()
        connection=MySQLdb.connect(host='127.0.0.1',user='root',passwd='shreya',db='userlogin')
        cur=connection.cursor()
        query1="select id from clientres order by id desc limit 1"
        cur.execute(query1)
        for var in cur:
            v=int(var[0])+1
            txt_name1.insert(0,str(v))
            break    
        txt_name2["state"]="normal"
        txt_name3["state"]="normal"  
        txt_name4["state"]="normal"
        txt_name5["state"]="normal" 
        txt_name6["state"]="normal" 
        txt_name7["state"]="normal" 
        txt_name8["state"]="normal" 
        connection.commit()
        connection.close()
    def search():
        txt_name2["state"]="normal"
        txt_name3["state"]="normal"  
        txt_name4["state"]="normal"
        txt_name5["state"]="normal" 
        txt_name6["state"]="normal" 
        txt_name7["state"]="normal" 
        txt_name8["state"]="normal" 
        uid=txt_name1.get()
        connection=MySQLdb.connect(host='127.0.0.1',user='root',passwd='shreya',db='userlogin')
        cur=connection.cursor()
        print("connected")

        query1="select * from clientres where id=%s "
        cur.execute(query1,uid)
        

        for var in cur:
            
            txt_name2.insert(0,var[1])
            txt_name3.insert(0,var[2])
            txt_name4.insert(0,var[3])
            txt_name5.insert(0,var[4])
            txt_name6.insert(0,var[5])
            txt_name7.insert(0,var[6])
            txt_name8.insert(0,var[6])

        connection.commit()
        connection.close()

    def delete():
        
        
            txt_name2.delete(0,END)
            txt_name3.delete(0,END)
            txt_name4.delete(0,END)
            txt_name5.delete(0,END)
            txt_name6.delete(0,END)
            txt_name7.delete(0,END)
            txt_name1.delete(0,END)

    
    def first():
        delete()
        connection=MySQLdb.connect(host='127.0.0.1',user='root',passwd='shreya',db='userlogin')
        cur=connection.cursor()


        query1="select * from clientres limit 1 "
        cur.execute(query1)
       

        for var in cur:
            
            txt_name2.insert(0,var[1])
            txt_name3.insert(0,var[2])
            txt_name4.insert(0,var[3])
            txt_name5.insert(0,var[4])
            txt_name6.insert(0,var[5])
            txt_name7.insert(0,var[6])
           
            txt_name1.insert(0,var[0])

        
        connection.close()
    
    def last():
        delete()
        connection=MySQLdb.connect(host='127.0.0.1',user='root',passwd='shreya',db='userlogin')
        cur=connection.cursor()

        
        query1="select * from clientres order by id desc limit 1 "
        cur.execute(query1)
        #data= cur.fetchmany(2)

        for var in cur:
            
            txt_name2.insert(0,var[1])
            txt_name3.insert(0,var[2])
            txt_name4.insert(0,var[3])
            txt_name5.insert(0,var[4])
            txt_name6.insert(0,var[5])
            txt_name7.insert(0,var[6])
            txt_name1.insert(0,var[0])
        connection.close()
        
      
    def nxt():
        delete()                     
        connection=MySQLdb.connect(host='127.0.0.1',user='root',passwd='shreya',db='userlogin')
        cur=connection.cursor()


        query1="select * from clientres limit 1,1 "
        cur=cur+1
        cur.execute(query1)
        #data= cur.fetchmany(2)

        for var in cur:
            
            txt_name2.insert(0,var[1])
            txt_name3.insert(0,var[2])
            txt_name4.insert(0,var[3])
            txt_name5.insert(0,var[4])
            txt_name6.insert(0,var[5])
            txt_name7.insert(0,var[6])
            txt_name1.insert(0,var[0])

        
        connection.close()
    def previous():
        delete()                     
        connection=MySQLdb.connect(host='127.0.0.1',user='root',passwd='shreya',db='userlogin')
        cur=connection.cursor()


        query1="select * from clientres order by id desc limit 1,1 "
        cur.execute(query1)
        #data= cur.fetchmany(2)

        for var in cur:
            
            txt_name2.insert(0,var[1])
            txt_name3.insert(0,var[2])
            txt_name4.insert(0,var[3])
            txt_name5.insert(0,var[4])
            txt_name6.insert(0,var[5])
            txt_name7.insert(0,var[6])
            txt_name1.insert(0,var[0])
        connection.close()
        
        
    def update():
       
        cid=int(txt_name1.get())
        td=int(txt_name2.get())
        le=int(txt_name3.get())
        ie=int(txt_name4.get())
        hr=int(txt_name5.get())
        d=int(txt_name6.get())
        pe=int(txt_name7.get())
        he=int(txt_name8.get())
        connection=MySQLdb.connect(host='127.0.0.1',user='root',passwd='shreya',db='userlogin')

        cursor = connection.cursor()

        sqlquery = "UPDATE clientres SET taxdeduction=%s,loanemi=%s,insuranceemi=%s,houserent=%s,dependents=%s,personalexpenditure=%s,healthexpenditure=%s WHERE id=%s"

        try:
            #executing the query
            cursor.execute(sqlquery,(str(td),str(le),str(ie),str(hr),str(d),str(pe),str(he),str(cid)))

            #commit the changes
            connection.commit()
            print("Record updated succesfully....!")

        except Exception as e:
            print(e)
            #Rollback the changes
            connection.rollback()
        connection.close()

    def save():
        cid=int(txt_name1.get())
        td=int(txt_name2.get())
        le=int(txt_name3.get())
        ie=int(txt_name4.get())
        hr=int(txt_name5.get())
        d=txt_name6.get()
        pe=int(txt_name7.get())
        he=int(txt_name8.get())
        MsgBox = messagebox.askquestion ('SAVE DETAILS..','Are you sure you want to save the details',icon = 'warning')
        if MsgBox == 'yes':


            connection=MySQLdb.connect(host='127.0.0.1',user='root',passwd='shreya',db='userlogin')
            cur=connection.cursor()
            query1="INSERT INTO clientres(id,taxdeduction,loanemi,insuranceemi,houserent,dependents,personalexpenditure,healthexpenditure) VALUES(' "+str(cid)+" ',' "+str(td)+" ',' "+str(le)+" ',' "+str(ie)+" ',' "+str(hr)+" ',' "+str(d)+" ',' "+str(pe)+" ',' "+str(he)+" ')"
            cur.execute(query1)

            connection.commit()
            connection.close()
        
    root=Tk()
    root.title("Client Responsibility Detail")
    root.geometry("1080x750+200+40")

    Manage_frame = Frame(root, bd=4, relief=RIDGE, bg="white")
    Manage_frame.place(x=20, y=20, width=1030, height=710)

    Manage_frame1= Frame(Manage_frame, bd=4, relief=RIDGE, bg="whitesmoke")
    Manage_frame1.place(x=30, y=60, width=785, height=500)

    Manage_frame2 = Frame(Manage_frame, bd=4, relief=RIDGE, bg="teal")
    Manage_frame2.place(x=230, y=10, width=370, height=45)

    lbl_name1 = Label(Manage_frame2, text="Client Responsibility Detail", fg="white", bg="teal", font=('times new roman', 20, 'bold'))
    lbl_name1.place(x=20, y=2)

    Manage_frame3 = Frame(Manage_frame, bd=4, relief=RIDGE, bg="darkslategray")
    Manage_frame3.place(x=30, y=570, width=785, height=120)



    lbl_name1 = Label(Manage_frame1, text="Client ID", fg="black", bg="whitesmoke", font=('times new roman', 20, 'bold'))
    lbl_name1.grid(row=0, column=0, pady=20, padx=30, sticky="W")
    txt_name1 = Entry(Manage_frame1, font=('times new roman', 12, 'bold'), bd=2,width=10,
    relief=GROOVE)
    txt_name1.grid(row=0, column=1, pady=10, padx=30, sticky="W")



    lbl_name2 = Label(Manage_frame1, text="Tax Deduction", fg="black", bg="whitesmoke", font=('times new roman', 20, 'bold'))
    lbl_name2.grid(row=2, column=0, pady=10, padx=30, sticky="W")
    txt_name2 = Entry(Manage_frame1,state='disable',  font=('times new roman', 12 ,'bold'), bd=2,width=20,
    relief=GROOVE)
    txt_name2.grid(row=2, column=1, pady=10, padx=30, sticky="W")

    lbl_name2 = Label(Manage_frame1, text="(...yearly)", fg="black", bg="whitesmoke",
    font=('times new roman', 20, 'bold'))
    lbl_name2.place(x=540,y=85)



    lbl_name3 = Label(Manage_frame1, text="Loan EMI", fg="black", bg="whitesmoke", font=('times new roman', 20, 'bold'))
    lbl_name3.grid(row=3, column=0, pady=10, padx=30, sticky="W")
    txt_name3 = Entry(Manage_frame1, state='disable', font=('times new roman', 12, 'bold'), bd=2,width=30,
    relief=GROOVE)
    txt_name3.grid(row=3, column=1, pady=10, padx=30, sticky="W")

    lbl_name3 = Label(Manage_frame1, text="(...monthly)", fg="black", bg="whitesmoke",
    font=('times new roman', 20, 'bold'))
    lbl_name3.place(x=620,y=140)

    lbl_name4 = Label(Manage_frame1, text="Insurance EMI", fg="black", bg="whitesmoke", font=('times new roman', 20, 'bold'))
    lbl_name4.grid(row=4, column=0, pady=10, padx=30, sticky="W")
    txt_name4 = Entry(Manage_frame1,state='disable',  font=('times new roman', 12, 'bold'), bd=2,width=30,
    relief=GROOVE)
    txt_name4.grid(row=4, column=1, pady=10, padx=30, sticky="W")

    lbl_name4 = Label(Manage_frame1, text="(...monthly)", fg="black", bg="whitesmoke",
    font=('times new roman', 20, 'bold'))
    lbl_name4.place(x=620, y=200)

    lbl_name5 = Label(Manage_frame1, text="House Rent", fg="black", bg="whitesmoke", font=('times new roman', 20, 'bold'))
    lbl_name5.grid(row=5, column=0, pady=10, padx=30, sticky="W")
    txt_name5 = Entry(Manage_frame1,state='disable',  font=('times new roman', 12, 'bold'), bd=2, width=30,
    relief=GROOVE)
    txt_name5.grid(row=5, column=1, pady=10, padx=30, sticky="W")

    lbl_name5 = Label(Manage_frame1, text="(...monthly)", fg="black", bg="whitesmoke",
    font=('times new roman', 20, 'bold'))
    lbl_name5.place(x=620, y=260)

    lbl_name6 = Label(Manage_frame1, text="Dependents", fg="black", bg="whitesmoke", font=('times new roman', 20, 'bold'))
    lbl_name6.grid(row=6, column=0, pady=10, padx=30, sticky="W")
    txt_name6 = Entry(Manage_frame1,state='disable',  font=('times new roman', 12, 'bold'), bd=2, width=30,
    relief=GROOVE)
    txt_name6.grid(row=6, column=1, pady=10, padx=30, sticky="W")

    lbl_name7 = Label(Manage_frame1, text="Personal Expenditure", fg="black", bg="whitesmoke",
    font=('times new roman', 20, 'bold'))
    lbl_name7.grid(row=7, column=0, pady=10, padx=30, sticky="W")
    txt_name7 = Entry(Manage_frame1,state='disable',  font=('times new roman', 12, 'bold'), bd=2, width=30,
    relief=GROOVE)
    txt_name7.grid(row=7, column=1, pady=10, padx=30, sticky="W")

    lbl_name7 = Label(Manage_frame1, text="(...monthly)", fg="black", bg="whitesmoke",
    font=('times new roman', 20, 'bold'))
    lbl_name7.place(x=620, y=370)

    lbl_name8 = Label(Manage_frame1, text="Health Expenditure", fg="black", bg="whitesmoke",
    font=('times new roman', 20, 'bold'))
    lbl_name8.grid(row=8, column=0, pady=10, padx=30, sticky="W")
    txt_name8 = Entry(Manage_frame1,state='disable',  font=('times new roman', 12, 'bold'), bd=2, width=30,
    relief=GROOVE)
    txt_name8.grid(row=8, column=1, pady=10, padx=30, sticky="W")

    lbl_name8 = Label(Manage_frame1, text="(...monthly)", fg="black", bg="whitesmoke",
    font=('times new roman', 20, 'bold'))
    lbl_name8.place(x=620, y=430)

    first_btn = Button(Manage_frame3, text="First", width=15, pady=5, bg="lightcyan", fg="black", bd=5,command=first,
    font=('times new roman', 11, 'bold'))
    first_btn.place(x=60, y=8)

    previous_btn=Button(Manage_frame3,text="Previous",width=15, pady=5,bg="lightcyan",command=previous,fg="black",bd=5, font=('times new roman', 11, 'bold'))
    previous_btn.place(x=230,y=8)

    next_btn = Button(Manage_frame3, text="Next", width=15, pady=5,bg="lightcyan",command=nxt,fg="black",bd=5, font=('times new roman', 11, 'bold'))
    next_btn.place(x=400, y=8)

    last_btn = Button(Manage_frame3, text="Last", width=15, pady=5, bg="lightcyan", fg="black", bd=5,command=last,
    font=('times new roman', 11, 'bold'))
    last_btn.place(x=570, y=8)


    add_btn = Button(Manage_frame3, text="Add", width=15, pady=5, bg="lightcyan", fg="black", bd=5,command=add,
    font=('times new roman', 11, 'bold'))
    add_btn.place(x=60, y=60)

    update_btn = Button(Manage_frame3, text="Update", width=15, pady=5, bg="lightcyan", fg="black", bd=5,command=update,
    font=('times new roman', 11, 'bold'))
    update_btn.place(x=230, y=60)

    save_btn = Button(Manage_frame3, text="Save", width=15, pady=5, bg="lightcyan", fg="black", bd=5,command=save,
    font=('times new roman', 11, 'bold'))
    save_btn.place(x=400, y=60)

    cancel_btn = Button(Manage_frame3, text="Cancel", width=15, pady=5, bg="lightcyan", fg="black", bd=5,command=delete,
    font=('times new roman', 11, 'bold'))
    cancel_btn.place(x=570, y=60)
    search_btn = Button(Manage_frame1, text="Search", width=9, pady=3, bg="whitesmoke", fg="black", bd=3,command=search,
                      font=('times new roman', 11, 'bold'))
    search_btn.place(x=500, y=15)

    mainloop()