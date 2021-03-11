from tkinter import *
import MySQLdb
from tkinter import messagebox

def profileaccountdetail():
    
    def update():
        usernm=txt_name2.get()
        passwrd=txt_name4.get()
        scrtq=txt_name4.get()
        scrtans=txt_name5.get()
        uid=int(txt_name1.get())
        connection=MySQLdb.connect(host='127.0.0.1',user='root',passwd='shreya',db='userlogin')

        cursor = connection.cursor()

        sqlquery = "UPDATE login SET username=%s, password=%s ,securityquestion=%s,securityanswer=%s where id=%s"

        try:
            #executing the query
            cursor.execute(sqlquery,(usernm,passwrd,scrtq,scrtans,uid))

            #commit the changes
            connection.commit()
            print("Record updated succesfully....!")

        except Exception as e:
            print(e)
            #Rollback the changes
            connection.rollback()

        connection.close()
    def delete():


        txt_name2.delete(0,END)
        txt_name3.delete(0,END)
        txt_name4.delete(0,END)
        txt_name5.delete(0,END)
        
        txt_name1.delete(0,END)

    def save():
        usernm=txt_name2.get()
        passwrd=txt_name4.get()
        scrtq=txt_name4.get()
        scrtans=txt_name5.get()
        uid=txt_name1.get() 
        MsgBox = messagebox.askquestion ('SAVE DETAIL..','Are you sure you want to save the details',icon = 'warning')
        if MsgBox == 'yes':

        
            connection=MySQLdb.connect(host='127.0.0.1',user='root',passwd='shreya',db='userlogin')
            cur=connection.cursor()
            query="SELECT username,password,securityquestion,securityanswer FROM login"
            cur.execute(query)
            data = cur.fetchall()
            for var in data:
                print(var[0]," ",var[1]," ",var[2]," ",var[3])

            query1="INSERT INTO login(username,password,securityquestion,securityanswer)"    " VALUES(%s,%s,%s,%s,%s)"
            cur.execute(query1,(uid,usernm,passwrd,scrtq,scrtans))

            connection.commit()
            connection.close()
        
            
    def add():
        delete()
        connection=MySQLdb.connect(host='127.0.0.1',user='root',passwd='shreya',db='userlogin')
        cur=connection.cursor()
        query1="select id from login order by id desc limit 1"
        cur.execute(query1)
        for var in cur:
            v=int(var[0])+1
            txt_name1.insert(0,str(v))
            break    
        txt_name2["state"]="normal"
        txt_name3["state"]="normal"  
        txt_name4["state"]="normal"
        txt_name5["state"]="normal" 
       
        connection.commit()
        connection.close()
    def search():
        txt_name2["state"]="normal"
        txt_name3["state"]="normal"  
        txt_name4["state"]="normal"
        txt_name5["state"]="normal" 
        
        uid=txt_name1.get()
        connection=MySQLdb.connect(host='127.0.0.1',user='root',passwd='shreya',db='userlogin')
        cur=connection.cursor()
        print("connected")

        query1="select * from login where id=%s "
        cur.execute(query1,uid)
        

        for var in cur:
            
            txt_name2.insert(0,var[1])
            txt_name3.insert(0,var[2])
            txt_name4.insert(0,var[3])
            txt_name5.insert(0,var[4])
           

        connection.commit()
        connection.close()
        
    root=Tk()
    root.title("Profile Account Detail")
    root.geometry('900x580+310+100')

    Manage_frame = Frame(root, bd=4, relief=RIDGE, bg="white")
    Manage_frame.place(x=20, y=20, width=850, height=530)

    Manage_frame1= Frame(Manage_frame, bd=4, relief=RIDGE, bg="whitesmoke")
    Manage_frame1.place(x=30, y=60, width=670, height=370)

    Manage_frame2 = Frame(Manage_frame, bd=4, relief=RIDGE, bg="teal")
    Manage_frame2.place(x=210, y=10, width=290, height=45)

    lbl_name1 = Label(Manage_frame2, text="Profile Account Detail", fg="white", bg="teal", font=('times new roman', 20, 'bold'))
    lbl_name1.place(x=5, y=2)

    Manage_frame3 = Frame(Manage_frame, bd=4, relief=RIDGE, bg="darkslategray")
    Manage_frame3.place(x=30, y=440, width=670, height=70)



    lbl_name1 = Label(Manage_frame1, text="User ID", fg="black", bg="whitesmoke", font=('times new roman', 20, 'bold'))
    lbl_name1.grid(row=1, column=0, pady=40, padx=30, sticky="W")
    txt_name1 = Entry(Manage_frame1,  font=('times new roman', 15, 'bold'), bd=2,width=10,
                     relief=GROOVE)
    txt_name1.grid(row=1, column=1, pady=10, padx=30, sticky="W")

    lbl_name2 = Label(Manage_frame1, text="Username",  fg="black", bg="whitesmoke", font=('times new roman', 20, 'bold'))
    lbl_name2.grid(row=2, column=0, pady=10, padx=30, sticky="W")
    txt_name2 = Entry(Manage_frame1,state='disable', font=('times new roman', 15, 'bold'), bd=2,width=20,
                     relief=GROOVE)
    txt_name2.grid(row=2, column=1, pady=10, padx=30, sticky="W")

    lbl_name3 = Label(Manage_frame1, text="Password", fg="black", bg="whitesmoke",  font=('times new roman', 20, 'bold'))
    lbl_name3.grid(row=3, column=0, pady=10, padx=30, sticky="W")
    txt_name3 = Entry(Manage_frame1, state='disable',font=('times new roman', 15, 'bold'), bd=2,width=20,
                     relief=GROOVE)
    txt_name3.grid(row=3, column=1, pady=10, padx=30, sticky="W")

    lbl_name4 = Label(Manage_frame1, text="Security Question", fg="black", bg="whitesmoke",  font=('times new roman', 20, 'bold'))
    lbl_name4.grid(row=4, column=0, pady=10, padx=30, sticky="W")
    txt_name4 = Entry(Manage_frame1,  state='disable',font=('times new roman', 15, 'bold'), bd=2,width=30,
                     relief=GROOVE)
    txt_name4.grid(row=4, column=1, pady=10, padx=30, sticky="W")

    lbl_name5 = Label(Manage_frame1, text="Security Answer", fg="black", bg="whitesmoke",font=('times new roman', 20, 'bold'))
    lbl_name5.grid(row=5, column=0, pady=10, padx=30, sticky="W")
    txt_name5 = Entry(Manage_frame1, state='disable', font=('times new roman', 15, 'bold'), bd=2,width=30,
                      relief=GROOVE)
    txt_name5.grid(row=5, column=1, pady=30, padx=30, sticky="W")


    update_btn = Button(Manage_frame3, text="Update", width=13, pady=5, bg="lightcyan", fg="black", bd=5,command=update,
                        font=('times new roman', 11, 'bold'))
    update_btn.place(x=310, y=10)

    save_btn = Button(Manage_frame3, text="Save", width=13, pady=5, bg="lightcyan", fg="black", bd=5,command=save,
                      font=('times new roman', 11, 'bold'))
    save_btn.place(x=460, y=10)
    add_btn = Button(Manage_frame3, text="Add", width=13, pady=5, bg="lightcyan", fg="black", bd=5,command=add,
                      font=('times new roman', 11, 'bold'))
    add_btn.place(x=160, y=10)
    search_btn = Button(Manage_frame1, text="Search", width=9, pady=3, bg="lightcyan", fg="black", bd=3,command=search,
                      font=('times new roman', 11, 'bold'))
    search_btn.place(x=400, y=15)

    mainloop()