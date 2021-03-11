from tkinter import *
import MySQLdb
from tkinter import messagebox

def loanplandetail():

    def cancel():
        root.quit()
    def delete():
        
        
            txt_name2.delete(0,END)
            txt_name3.delete(0,END)
            txt_name4.delete(0,END)
            
            txt_name1.delete(0,END)
    def add():
        delete()
        connection=MySQLdb.connect(host='127.0.0.1',user='root',passwd='shreya',db='userlogin')
        cur=connection.cursor()
        query1="select pid from loanplandet order by pid desc limit 1"
        cur.execute(query1)
        for var in cur:
            v=int(var[0])+1
            txt_name1.insert(0,str(v))
            break    
        txt_name2["state"]="normal"
        txt_name3["state"]="normal"  
        txt_name4["state"]="normal"

        connection.commit()
        connection.close()
    def search():
        txt_name2["state"]="normal"
        txt_name3["state"]="normal"  
        txt_name4["state"]="normal"
        
        pid=txt_name1.get()
        connection=MySQLdb.connect(host='127.0.0.1',user='root',passwd='shreya',db='userlogin')
        cur=connection.cursor()
        print("connected")

        query1="select * from loanplandet where pid=%s "
        cur.execute(query1,pid)
        

        for var in cur:
            
            txt_name2.insert(0,var[1])
            txt_name3.insert(0,var[2])
            txt_name4.insert(0,var[3])
            

        connection.commit()
        connection.close()


    def first():
        delete()
        txt_name2["state"]="normal"
        txt_name3["state"]="normal"  
        txt_name4["state"]="normal"
        connection=MySQLdb.connect(host='127.0.0.1',user='root',passwd='shreya',db='userlogin')
        cur=connection.cursor()


        query1="select * from loanplandet limit 1 "
        cur.execute(query1)
       

        for var in cur:
            
            txt_name2.insert(0,var[1])
            txt_name3.insert(0,var[2])
            txt_name4.insert(0,var[3])

            txt_name1.insert(0,var[0])

        
        connection.close()
    
    def last():
        delete()
        txt_name2["state"]="normal"
        txt_name3["state"]="normal"  
        txt_name4["state"]="normal"
        connection=MySQLdb.connect(host='127.0.0.1',user='root',passwd='shreya',db='userlogin')
        cur=connection.cursor()

        
        query1="select * from loanplandet order by id desc limit 1 "
        cur.execute(query1)
        #data= cur.fetchmany(2)

        for var in cur:
            
            txt_name2.insert(0,var[1])
            txt_name3.insert(0,var[2])
            txt_name4.insert(0,var[3])
           
            txt_name1.insert(0,var[0])
        connection.close()
        
      
    def nxt():
        delete()                     
        txt_name2["state"]="normal"
        txt_name3["state"]="normal"  
        txt_name4["state"]="normal"
        connection=MySQLdb.connect(host='127.0.0.1',user='root',passwd='shreya',db='userlogin')
        cur=connection.cursor()


        query1="select * from loanplandet "
        cur=cur+1
        cur.execute(query1)
        #data= cur.fetchmany(2)

        for var in cur:
            
            txt_name2.insert(0,var[1])
            txt_name3.insert(0,var[2])
            txt_name4.insert(0,var[3])
            
            txt_name1.insert(0,var[0])

        
        connection.close()
    def previous():
        delete()                     
        txt_name2["state"]="normal"
        txt_name3["state"]="normal"  
        txt_name4["state"]="normal"
        connection=MySQLdb.connect(host='127.0.0.1',user='root',passwd='shreya',db='userlogin')
        cur=connection.cursor()


        query1="select * from loanplandet limit 1 "
        cur.execute(query1)
        #data= cur.fetchmany(2)

        for var in cur:
            
            txt_name2.insert(0,var[1])
            txt_name3.insert(0,var[2])
            txt_name4.insert(0,var[3])
           
            txt_name1.insert(0,var[0])
        connection.close()
        
        
    def update():
                             
        connection=MySQLdb.connect(host='127.0.0.1',user='root',passwd='shreya',db='userlogin')
        cur=connection.cursor()

        pn=txt_name2.get()
        ir=int(txt_name3.get())
        
        d=txt_name4.get()
       
        
        pid=int(txt_name1.get())
        
        sqlquery = "UPDATE loanplandet SET pname=%s,interestrate=%s ,description=%s WHERE pid=%s"
        #ir=str(ir) 
        
        try:
            #executing the query
            cur.execute(sqlquery,(pn,str(ir),d,str(pid)))
            
            #commit the changes
            connection.commit()
            print("Record updated succesfully....!")

        except Exception as e:
            print(e)
            #Rollback the changes
            connection.rollback()
            connection.close()

    def save():
        connection=MySQLdb.connect(host='127.0.0.1',user='root',passwd='shreya',db='userlogin')
        cur=connection.cursor()

        pn=txt_name2.get()
        ir=int(txt_name3.get())
        d=txt_name4.get()
       
        
        pid=int(txt_name1.get())
        
        MsgBox = messagebox.askquestion ('SAVE DETAILS..','Are you sure you want to save the details',icon = 'warning')
        if MsgBox == 'yes':


            query1=("INSERT INTO loanplandet(pid,pname,interestrate,description)"  "VALUES(%s,%s,%s,%s)")
            data=(str(pid),pn,str(ir),d)
            cur.execute(query1,data)

            connection.commit()
            connection.close()
            

    root=Tk()
    root.title("Loan Plan Detail")
    root.geometry('900x660+310+100')

    Manage_frame = Frame(root, bd=4, relief=RIDGE, bg="white")
    Manage_frame.place(x=20, y=20, width=850, height=620)

    Manage_frame1= Frame(Manage_frame, bd=4, relief=RIDGE, bg="whitesmoke")
    Manage_frame1.place(x=30, y=60, width=670, height=410)

    Manage_frame2 = Frame(Manage_frame, bd=4, relief=RIDGE, bg="teal")
    Manage_frame2.place(x=200, y=10, width=290, height=45)

    lbl_name1 = Label(Manage_frame2, text="Loan Plan Detail", fg="white", bg="teal", font=('times new roman', 20, 'bold'))
    lbl_name1.place(x=30, y=2)

    Manage_frame3 = Frame(Manage_frame, bd=4, relief=RIDGE, bg="darkslategray")
    Manage_frame3.place(x=30, y=480, width=670, height=120)



    lbl_name1 = Label(Manage_frame1, text="Plan ID", fg="black", bg="whitesmoke", font=('times new roman', 20, 'bold'))
    lbl_name1.grid(row=1, column=0, pady=40, padx=30, sticky="W")
    txt_name1 = Entry(Manage_frame1, font=('times new roman', 15, 'bold'), bd=2,width=10,
                     relief=GROOVE)
    txt_name1.grid(row=1, column=1, pady=10, padx=30, sticky="W")

    lbl_name2 = Label(Manage_frame1, text="Plan Name", fg="black", bg="whitesmoke", font=('times new roman', 20, 'bold'))
    lbl_name2.grid(row=2, column=0, pady=10, padx=30, sticky="W")
    txt_name2 = Entry(Manage_frame1, state='disable',font=('times new roman', 15, 'bold'), bd=2,width=20,
                     relief=GROOVE)
    txt_name2.grid(row=2, column=1, pady=10, padx=30, sticky="W")

    lbl_name3 = Label(Manage_frame1, text="Interest Rate", fg="black", bg="whitesmoke", font=('times new roman', 20, 'bold'))
    lbl_name3.grid(row=3, column=0, pady=10, padx=30, sticky="W")
    txt_name3 = Entry(Manage_frame1,state='disable', font=('times new roman', 15, 'bold'), bd=2,width=20,
                     relief=GROOVE)
    txt_name3.grid(row=3, column=1, pady=10, padx=30, sticky="W")

    lbl_name4 = Label(Manage_frame1, text="Description", fg="black", bg="whitesmoke", font=('times new roman', 20, 'bold'))
    lbl_name4.grid(row=4, column=0, pady=10, padx=30, sticky="W")
    txt_name4 = Entry(Manage_frame1, state='disable',font=('times new roman', 58, 'bold'), bd=2,width=7,
                     relief=GROOVE)
    txt_name4.grid(row=4, column=1, pady=10, padx=30, sticky="W")



    first_btn = Button(Manage_frame3, text="First", width=13, pady=5, bg="lightcyan", fg="black", bd=5,command=first,
                        font=('times new roman', 11, 'bold'))
    first_btn.place(x=40, y=5)

    previous_btn=Button(Manage_frame3,text="Previous",width=13, pady=5,bg="lightcyan",fg="black",bd=5,command=previous, font=('times new roman', 11, 'bold'))
    previous_btn.place(x=190,y=5)

    next_btn = Button(Manage_frame3, text="Next", width=13, pady=5,bg="lightcyan",fg="black",bd=5,command=nxt, font=('times new roman', 11, 'bold'))
    next_btn.place(x=340, y=5)

    last_btn = Button(Manage_frame3, text="Last", width=13, pady=5, bg="lightcyan", fg="black", bd=5,command=last,
                        font=('times new roman', 11, 'bold'))
    last_btn.place(x=490, y=5)


    add_btn = Button(Manage_frame3, text="Add", width=13, pady=5, bg="lightcyan", fg="black", bd=5,command=add,
                     font=('times new roman', 11, 'bold'))
    add_btn.place(x=40, y=60)

    update_btn = Button(Manage_frame3, text="Update", width=13, pady=5, bg="lightcyan", fg="black", bd=5,command=update,
                        font=('times new roman', 11, 'bold'))
    update_btn.place(x=190, y=60)

    save_btn = Button(Manage_frame3, text="Save", width=13, pady=5, bg="lightcyan", fg="black", bd=5,command=save,
                      font=('times new roman', 11, 'bold'))
    save_btn.place(x=340, y=60)

    cancel_btn = Button(Manage_frame3, text="Cancel", width=13, pady=5, bg="lightcyan", fg="black", bd=5,command=cancel,
                        font=('times new roman', 11, 'bold'))
    cancel_btn.place(x=490, y=60)

    search_btn = Button(Manage_frame1, text="Search", width=9, pady=3, bg="whitesmoke", fg="black", bd=3,command=search,
                      font=('times new roman', 11, 'bold'))
    search_btn.place(x=500, y=15)

    mainloop()