from tkinter import *
import MySQLdb
from tkinter import messagebox


def clientpersonaldetail():
   
    def add():
        delete()
        connection=MySQLdb.connect(host='127.0.0.1',user='root',passwd='shreya',db='userlogin')
        cur=connection.cursor()
        query1="select id from clientpersonal order by id desc limit 1"
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
       
        connection.commit()
        connection.close()
    def search():
        txt_name2["state"]="normal"
        txt_name3["state"]="normal"  
        txt_name4["state"]="normal"
        txt_name5["state"]="normal" 
        txt_name6["state"]="normal" 
 
        uid=txt_name1.get()
        connection=MySQLdb.connect(host='127.0.0.1',user='root',passwd='shreya',db='userlogin')
        cur=connection.cursor()
        print("connected")

        query1="select * from clientpersonal where id=%s "
        cur.execute(query1,uid)
        

        for var in cur:
            
            txt_name2.insert(0,var[1])
            txt_name3.insert(0,var[2])
            txt_name4.insert(0,var[3])
            txt_name5.insert(0,var[4])
            txt_name6.insert(0,var[5])
            txt_name7.insert(0,var[6])
            

        connection.commit()
        connection.close()

    def delete():
        
        
            txt_name2.delete(0,END)
            txt_name3.delete(0,END)
            txt_name4.delete(0,END)
            txt_name5.delete(0,END)
            txt_name6.delete(0,END)
            txt_name1.delete(0,END)

    
    def first():
        delete()
        connection=MySQLdb.connect(host='127.0.0.1',user='root',passwd='shreya',db='userlogin')
        cur=connection.cursor()


        query1="select * from clientpersonal limit 1 "
        cur.execute(query1)
       

        for var in cur:
            
            txt_name2.insert(0,var[1])
            txt_name3.insert(0,var[2])
            txt_name4.insert(0,var[3])
            txt_name5.insert(0,var[4])
            txt_name6.insert(0,var[5])
           
            txt_name1.insert(0,var[0])

        
        connection.close()
    
    def last():
        delete()
        connection=MySQLdb.connect(host='127.0.0.1',user='root',passwd='shreya',db='userlogin')
        cur=connection.cursor()

        
        query1="select * from clientpersonal order by id desc limit 1 "
        cur.execute(query1)
        #data= cur.fetchmany(2)

        for var in cur:
            
            txt_name2.insert(0,var[1])
            txt_name3.insert(0,var[2])
            txt_name4.insert(0,var[3])
            txt_name5.insert(0,var[4])
            txt_name6.insert(0,var[5])
            
            txt_name1.insert(0,var[0])
        connection.close()
        
      
    def nxt():
        delete()                     
        connection=MySQLdb.connect(host='127.0.0.1',user='root',passwd='shreya',db='userlogin')
        cur=connection.cursor()


        query1="select * from clientpersonal "
        cur=cur+1
        cur.execute(query1)
        #data= cur.fetchmany(2)

        for var in cur:
            
            txt_name2.insert(0,var[1])
            txt_name3.insert(0,var[2])
            txt_name4.insert(0,var[3])
            txt_name5.insert(0,var[4])
            txt_name6.insert(0,var[5])
           
            txt_name1.insert(0,var[0])

        
        connection.close()
    def previous():
        delete()                     
        connection=MySQLdb.connect(host='127.0.0.1',user='root',passwd='shreya',db='userlogin')
        cur=connection.cursor()


        query1="select * from clientpersonal limit 1 "
        cur.execute(query1)
        #data= cur.fetchmany(2)

        for var in cur:
            
            txt_name2.insert(0,var[1])
            txt_name3.insert(0,var[2])
            txt_name4.insert(0,var[3])
            txt_name5.insert(0,var[4])
            txt_name6.insert(0,var[5])
            
            txt_name1.insert(0,var[0])
        connection.close()
        
        
    def update():
        nm=txt_name2.get()
       
        add=txt_name3.get()
        ph=txt_name4.get()
        mb=txt_name5.get()
        pn=txt_name6.get()
        uid=int(txt_name1.get())
        connection=MySQLdb.connect(host='127.0.0.1',user='root',passwd='shreya',db='userlogin')

        cursor = connection.cursor()

        sqlquery = "UPDATE clientpersonal SET name=%s,address=%s,phone=%s,mobile=%s,pan=%s where id=%s"

        try:
            #executing the query
            cursor.execute(sqlquery,(nm,add,ph,mb,pn,str(uid)))

            #commit the changes
            connection.commit()
            print("Record updated succesfully....!")

        except Exception as e:
            print(e)
            #Rollback the changes
            connection.rollback()
        connection.close()

    def save():
        nm=txt_name2.get()
        
        add=txt_name3.get()
        ph=txt_name4.get()
        mb=txt_name5.get()
        pn=txt_name6.get()
        uid=int(txt_name1.get())
        MsgBox = messagebox.askquestion ('SAVE DETAILS..','Are you sure you want to save the details',icon = 'warning')
        if MsgBox == 'yes':


            connection=MySQLdb.connect(host='127.0.0.1',user='root',passwd='shreya',db='userlogin')
            cur=connection.cursor()
            query1=("INSERT INTO clientpersonal(id,name,address,phone,mobile,pan)"  "VALUES(%s,%s,%s,%s,%s,%s)")
            
            cur.execute(query1,(str(uid),nm,add,ph,mb,pn))
            connection.commit()
            connection.close()

    root=Tk()
    root.title(" Client Personal Detail ")
    root.geometry("880x700+350+40")
    Manage_frame = Frame(root, bd=4, relief=RIDGE, bg="white")
    Manage_frame.place(x=20, y=20, width=830, height=660)

    Manage_frame1= Frame(Manage_frame, bd=4, relief=RIDGE, bg="whitesmoke")
    Manage_frame1.place(x=30, y=60, width=600, height=440)

    Manage_frame2 = Frame(Manage_frame, bd=4, relief=RIDGE, bg="teal")
    Manage_frame2.place(x=150, y=10, width=330, height=45)

    lbl_name1 = Label(Manage_frame2, text="Client Personal Detail", fg="white", bg="teal", font=('times new roman', 20, 'bold'))
    lbl_name1.place(x=20, y=2)

    Manage_frame3 = Frame(Manage_frame, bd=4, relief=RIDGE, bg="darkslategray")
    Manage_frame3.place(x=30, y=515, width=600, height=120)



    lbl_name1 = Label(Manage_frame1, text="Client ID", fg="black", bg="whitesmoke", font=('times new roman', 20, 'bold'))
    lbl_name1.grid(row=0, column=0, pady=20, padx=30, sticky="W")
    txt_name1 = Entry(Manage_frame1, font=('times new roman', 12, 'bold'), bd=2,width=10,
                     relief=GROOVE)
    txt_name1.grid(row=0, column=1, pady=10, padx=30, sticky="W")



    lbl_name2 = Label(Manage_frame1, text="Client Name*", fg="black", bg="whitesmoke", font=('times new roman', 20, 'bold'))
    lbl_name2.grid(row=2, column=0, pady=10, padx=30, sticky="W")
    txt_name2 = Entry(Manage_frame1, state='disable',font=('times new roman', 12 ,'bold'), bd=2,width=20,
                     relief=GROOVE)
    txt_name2.grid(row=2, column=1, pady=10, padx=30, sticky="W")


    lbl_name3 = Label(Manage_frame1, text="Address", fg="black", bg="whitesmoke", font=('times new roman', 20, 'bold'))
    lbl_name3.grid(row=3, column=0, pady=10, padx=30, sticky="W")
    txt_name3 = Entry(Manage_frame1,state='disable', font=('times new roman', 45, 'bold'), bd=2,width=8,
                     relief=GROOVE)
    txt_name3.grid(row=3, column=1, pady=10, padx=30, sticky="W")


    lbl_name4 = Label(Manage_frame1, text="Phone*", fg="black", bg="whitesmoke", font=('times new roman', 20, 'bold'))
    lbl_name4.grid(row=4, column=0, pady=10, padx=30, sticky="W")
    txt_name4 = Entry(Manage_frame1,state='disable', font=('times new roman', 12, 'bold'), bd=2,width=30,
                     relief=GROOVE)
    txt_name4.grid(row=4, column=1, pady=10, padx=30, sticky="W")



    lbl_name5 = Label(Manage_frame1, text="Mobile*", fg="black", bg="whitesmoke", font=('times new roman', 20, 'bold'))
    lbl_name5.grid(row=5, column=0, pady=10, padx=30, sticky="W")
    txt_name5 = Entry(Manage_frame1,state='disable', font=('times new roman', 12, 'bold'), bd=2, width=30,
                      relief=GROOVE)
    txt_name5.grid(row=5, column=1, pady=10, padx=30, sticky="W")



    lbl_name6 = Label(Manage_frame1, text="Pan*", fg="black", bg="whitesmoke", font=('times new roman', 20, 'bold'))
    lbl_name6.grid(row=6, column=0, pady=10, padx=30, sticky="W")
    txt_name6 = Entry(Manage_frame1,state='disable', font=('times new roman', 12, 'bold'), bd=2, width=30,
                      relief=GROOVE)
    txt_name6.grid(row=6, column=1, pady=10, padx=30, sticky="W")


    first_btn = Button(Manage_frame3, text="First", width=11, pady=5, bg="lightcyan", fg="black", bd=5,command=first,
                        font=('times new roman', 11, 'bold'))
    first_btn.place(x=30, y=8)

    previous_btn=Button(Manage_frame3,text="Previous",width=11, pady=5,bg="lightcyan",fg="black",bd=5,command=previous, font=('times new roman', 11, 'bold'))
    previous_btn.place(x=170,y=8)

    next_btn = Button(Manage_frame3, text="Next", width=11, pady=5,bg="lightcyan",fg="black",bd=5,command=nxt, font=('times new roman', 11, 'bold'))
    next_btn.place(x=310, y=8)

    last_btn = Button(Manage_frame3, text="Last", width=11, pady=5, bg="lightcyan", fg="black", bd=5,command=last,
                        font=('times new roman', 11, 'bold'))
    last_btn.place(x=450, y=8)


    add_btn = Button(Manage_frame3, text="Add", width=11, pady=5, bg="lightcyan", fg="black", bd=5,command=add,
                     font=('times new roman', 11, 'bold'))
    add_btn.place(x=30, y=60)

    update_btn = Button(Manage_frame3, text="Update", width=11, pady=5, bg="lightcyan", fg="black", bd=5,command=update,
                        font=('times new roman', 11, 'bold'))
    update_btn.place(x=170, y=60)

    save_btn = Button(Manage_frame3, text="Save", width=11, pady=5, bg="lightcyan", fg="black", bd=5,command=save,
                      font=('times new roman', 11, 'bold'))
    save_btn.place(x=310, y=60)

    cancel_btn = Button(Manage_frame3, text="Cancel", width=11, pady=5, bg="lightcyan", fg="black", bd=5,command=delete,
                        font=('times new roman', 11, 'bold'))
    cancel_btn.place(x=450, y=60)

    search_btn = Button(Manage_frame1, text="Search", width=9, pady=3, bg="whitesmoke", fg="black", bd=3,command=search,
                      font=('times new roman', 11, 'bold'))
    search_btn.place(x=500, y=15)

    mainloop()