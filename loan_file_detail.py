from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk,Image
import MySQLdb
from tkinter import messagebox
def loanfiledetail():
    root=Tk()
    root.title("Loan File Detail")
    root.geometry('1450x770+30+10')

    Manage_frame1= Frame(root, bd=4, relief=RIDGE, bg="whitesmoke")
    Manage_frame1.place(x=30, y=60, width=520, height=580)

    """img = ImageTk.PhotoImage(Image.open("loan1.jpg"))
    l = Label(root, image=img)
    l.place(x=600, y=0)"""

    v1 = tk.IntVar()
    v2 = tk.IntVar()
    v3 = tk.IntVar()
    v4 = tk.IntVar()
    def insert():
        la = txt_name4.get()
        name1.insert(0,la)
        pl = txt_name2.get()
        connection = MySQLdb.connect(host='127.0.0.1',user='root',passwd='shreya',db='userlogin')
        cur = connection.cursor()
        
        cur.execute("SELECT interestrate FROM loanplandet WHERE pname LIKE %s",[pl])
        for var in cur:
            p=int(var[0])
            name2.insert(0,str(p))
        client = txt_name3.get()
       
        cur.execute("SELECT id FROM clientpersonal WHERE name LIKE %s",[client])
        for var in cur:
            cl=var[0]
     
        cur.execute("select annualincome from clientprofessional where id like %s ",[cl])
        for var in cur:
            m=var[0]
            
        name3.insert(0,str(m))
                   
        
        cur.execute("select * from clientres where id=%s",[cl])
        for var in cur:
            td=var[1]
            le=var[2]
            ie=var[3]
            hr=var[4]
            d=var[5]
            pe=var[6]
            he=var[7]
              
        ex=(le+ie+hr+d+pe+he)
        name4.insert(0,str(ex))             
        connection.commit()
        connection.close()
        
    
    def add():
        delete()
        connection=MySQLdb.connect(host='127.0.0.1',user='root',passwd='shreya',db='userlogin')
        cur=connection.cursor()
        query1="select id from loanfiledet order by fid desc limit 1"
        cur.execute(query1)
        for var in cur:
            v=int(var[0])+1
            txt_name.insert(0,str(v))
            break    
        txt_name2["state"]="normal"
        txt_name3["state"]="normal"  
        txt_name4["state"]="normal"
        txt_name10["state"]="normal" 
        txt_name9["state"]="normal"
        connection.commit()
        connection.close()
    def search():
        txt_name2["state"]="normal"
        txt_name3["state"]="normal"  
        txt_name4["state"]="normal"
        txt_name10["state"]="normal" 
        txt_name9["state"]="normal"
        uid=txt_name.get()
        connection=MySQLdb.connect(host='127.0.0.1',user='root',passwd='shreya',db='userlogin')
        cur=connection.cursor()
        print("connected")

        
        cur.execute("select * from loanfiledet where fid=%s ",[uid])
        

        for var in cur:
            
            txt_name2.insert(0,var[1])
            txt_name3.insert(0,var[2])
            txt_name4.insert(0,var[3])
            txt_name9.insert(0,var[8])
            txt_name10.insert(0,var[9])
            
        connection.commit()
        connection.close()
        insert()
    def delete1():
        txt_name2.delete(0, END)
        txt_name3.delete(0, END)
        txt_name10.delete(0, END)
        txt_name.delete(0, END)
        txt_name4.delete(0, END)
        txt_name9.delete(0, END)
        name1.delete(0, END)
        name2.delete(0, END)
        name3.delete(0, END)
        name4.delete(0, END)
        name5.delete(0, END)


    def first():
        delete1()
        con = MySQLdb.connect(host='127.0.0.1',user='root',passwd='shreya',db='userlogin')
        cursor = con.cursor()
        cursor.execute("select * from loanfiledet order by fid limit 1 ")
        rows = cursor.fetchall()
        for row in rows:
            txt_name.insert(0, row[0])
            txt_name2.insert(0, row[1])
            txt_name3.insert(0, row[2])
            txt_name4.insert(0, row[3])
            txt_name9.insert(0, row[8])
            txt_name10.insert(0, row[9])
            name1.insert(1, row[10])
            name2.insert(0, row[11])
            name3.insert(0, row[12])
            name4.insert(0, row[13])
            name5.insert(0, row[14])
        con.close()
        insert()
    def previous():
        delete1()
        con = MySQLdb.connect(host='127.0.0.1',user='root',passwd='shreya',db='userlogin')
        cursor = con.cursor()
        cursor.execute("select * from loanfiledet order by fid limit 1")
        rows = cursor.fetchall()
        for row in rows:
            txt_name.insert(0, row[0])
            txt_name2.insert(0, row[1])
            txt_name3.insert(0, row[2])
            txt_name4.insert(0, row[3])
            txt_name9.insert(0, row[8])
            txt_name10.insert(0, row[9])
            name1.insert(1, row[10])
            name2.insert(0, row[11])
            name3.insert(0, row[12])
            name4.insert(0, row[13])
            name5.insert(0, row[14])
        con.close()
        insert()
    def nxt():
        delete1()
        con = MySQLdb.connect(host='127.0.0.1',user='root',passwd='shreya',db='userlogin')
        cursor = con.cursor()
        cursor.execute("select * from loanfiledet order by fid desc limit 1")
        rows = cursor.fetchall()
        for row in rows:
            txt_name.insert(0, row[0])
            txt_name2.insert(0, row[1])
            txt_name3.insert(0, row[2])
            txt_name4.insert(0, row[3])
            txt_name9.insert(0, row[8])
            txt_name10.insert(0, row[9])
            name1.insert(1, row[10])
            name2.insert(0, row[11])
            name3.insert(0, row[12])
            name4.insert(0, row[13])
            name5.insert(0, row[14])
        con.close()
        con.close()
        insert()
    def last():
        delete1()
        con = MySQLdb.connect(host='127.0.0.1',user='root',passwd='shreya',db='userlogin')
        cursor = con.cursor()
        cursor.execute("select * from loanfiledet order by fid desc limit 1")
        rows = cursor.fetchall()
        for row in rows:
            txt_name.insert(0, row[0])
            txt_name2.insert(0, row[1])
            txt_name3.insert(0, row[2])
            txt_name4.insert(0, row[3])
            txt_name9.insert(0, row[8])
            txt_name10.insert(0, row[9])
            name1.insert(1, row[10])
            name2.insert(0, row[11])
            name3.insert(0, row[12])
            name4.insert(0, row[13])
            name5.insert(0, row[14])
        con.close()
        insert
    def delete():
        txt_name.delete(0, END)
        txt_name4.delete(0, END)
        txt_name9.delete(0, END)
        name1.delete(0,END)
        name2.delete(0,END)
        name3.delete(0,END)
        name4.delete(0,END)
        name5.delete(0,END)



    def cancel():
        root.quit()


    def update():

        connection = MySQLdb.connect(host='127.0.0.1',user='root',passwd='shreya',db='userlogin')
        cur = connection.cursor()

        pl = txt_name2.get()
        client = txt_name3.get()
        la = txt_name4.get()
        idp = v1.get()
        rp = v2.get()
        ip = v3.get()
        bs = v4.get()
        r = txt_name9.get()
        st = txt_name10.get()
        fd = int(txt_name.get())
        la2 = name1.get()
        roi = name2.get()
        ci = name3.get()
        ce = name4.get()
        ny = name5.get()

        sqlquery = "UPDATE loan_file_detail SET plan=%s,client=%s,loanamount=%s,idproof=%s,rdproof=%s,inproof=%s,bankst=%s,remarks=%s,status=%s,loanamount2=%s,rateofinterest=%s,clientincome=%s,clientexpenses=%s,numberofyears=%s where fileid=%s"

        try:
            # executing the query
            cur.execute(sqlquery, ((str(fd)),pl, client, la, idp, rp, ip, bs, r, st,la2,roi,ci,ce,ny))

            # commit the changes
            connection.commit()
            print("Record updated succesfully....!")

        except Exception as e:
            print(e)
            # Rollback the changes
            connection.rollback()
            connection.close()
      

    def save():
        
        connection = MySQLdb.connect(host='127.0.0.1',user='root',passwd='shreya',db='userlogin')
        cur = connection.cursor()
        pl = txt_name2.get()
        client = txt_name3.get()
        la = txt_name4.get()
        idp = v1.get()
        rp = v2.get()
        ip = v3.get()
        bs = v4.get()
        r = txt_name9.get()
        st = txt_name10.get()
        fd = int(txt_name.get())
        
        """la2=name1.get()
        roi=name2.get()
        ci=name3.get()
        ce=name4.get()
        ny=name5.get()"""
        MsgBox = messagebox.askquestion('SAVE DETAILS..', 'Are you sure you want to save the details', icon='warning')
        if MsgBox == 'yes':
            query1 = (
                "INSERT INTO loanfiledet(fid,plan,client,loanamount,idproof,residenceproof,incomeproof,bankstatement,remark,status)"
                "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
            data = (str(fd), pl, client, la, idp, rp, ip, bs, r, st)
            cur.execute(query1, data)

            connection.commit()
            connection.close()
           
   
        insert()
    def evaluate():


        status = txt_name10.get()

        r = float(name2.get()) / 1200
        n = int(name5.get())
        p = float(name1.get())
        for i in range(1, n + 1):
            n = i
            monthly = float(p * r * (1 + r) * (i * 12)) / (((1 + r) * (i * 12)) - 1)
            table.insert('', 'end', value=n)
            table.insert('', 'end', value=monthly)
            table.insert('', 'end', value=status)

    def issue():
        status = name3.get()
        table.insert('', 'end', value=status)
        if status >1000:
            
            messagebox.showinfo(" ","loan approved")
        else:
            messagebox.showinfo(" ","loan denied")
    Manage_frame2 = Frame(root, bd=4, relief=RIDGE, bg="teal")
    Manage_frame2.place(x=150, y=10, width=270, height=45)

    lbl_name1 = Label(Manage_frame2, text="Loan File Detail", fg="white", bg="teal", font=('times new roman', 20, 'bold'))
    lbl_name1.place(x=20, y=2)

    Manage_frame3 = Frame(root, bd=4, relief=RIDGE, bg="darkslategray")
    Manage_frame3.place(x=30, y=645, width=520, height=115)

    Manage_frame4 = Frame(root, bd=4, relief=RIDGE, bg="whitesmoke")
    Manage_frame4.place(x=560, y=60, width=880, height=700)

    Manage_frame5 = Frame(  Manage_frame4, bd=4, relief=RIDGE, bg="white")
    Manage_frame5.place(x=20, y=220, width=830, height=450)

    """frm1 = Frame(Manage_frame5)
    frm1.place(x=60, y=70)
    tb1 = ttk.Treeview(frm1, column=(1), show="headings", height=6)
    tb1.pack()
    tb1.heading(1, text="Number Of Years")

    frm2 = Frame(Manage_frame5)
    frm2.place(x=260, y=70)
    tb2 = ttk.Treeview(frm2, column=(1), show="headings", height=6)
    tb2.pack()
    tb2.heading(1, text="Monthly Installment")

    frm3 = Frame(Manage_frame5)
    frm3.place(x=460, y=70)
    tb3 = ttk.Treeview(frm3, column=(1), show="headings", height=6)
    tb3.pack()
    tb3.heading(1, text="Issue Status?")"""




    scroll_x = Scrollbar(Manage_frame5, orient=HORIZONTAL)
    scroll_y = Scrollbar(Manage_frame5, orient=VERTICAL)
    table = ttk.Treeview(Manage_frame5,
                                      columns=("Number Of Years", "Monthly Installment", "Issue Status??"),
                                      xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM, fill=X)
    scroll_y.pack(side=RIGHT, fill=Y)

    scroll_x.config(command=table.xview)
    scroll_y.config(command=table.yview)

    table.heading("Number Of Years", text="   Number Of Years   ")
    table.heading("Monthly Installment", text="   Monthly Installment   ")
    table.heading("Issue Status??", text="  Issue Status??   ")
    table['show'] = "headings"
    table.column("Number Of Years", width=100)
    table.column("Monthly Installment", width=100)
    table.column("Issue Status??", width=100)
    table.pack(fill=BOTH, expand=1)

    Manage_frame6 = Frame(root, bd=4, relief=RIDGE, bg="teal")
    Manage_frame6.place(x=850, y=10, width=260, height=45)

    lbl_name1 = Label(Manage_frame6, text="Loan Evaluation", fg="white", bg="teal",
                      font=('times new roman', 20, 'bold'))
    lbl_name1.place(x=20, y=2)


    lbl_name1 = Label(Manage_frame1, text="File ID", fg="black", bg="whitesmoke", font=('times new roman', 13, 'bold'))
    lbl_name1.grid(row=1, column=0, pady=40, padx=30, sticky="W")
    txt_name = Entry(Manage_frame1, font=('times new roman', 13), bd=2,width=10,
                     relief=GROOVE)
    txt_name.grid(row=1, column=1, pady=10, padx=30, sticky="W")

    lbl_name2 = Label(Manage_frame1, text="Plan", fg="black", bg="whitesmoke", font=('times new roman', 13, 'bold'))
    lbl_name2.grid(row=2, column=0, pady=10, padx=30, sticky="W")
    txt_name2 = ttk.Combobox(Manage_frame1, font=('times new roman', 13), width=20)
    txt_name2['values'] = ('Home_Loan', 'Gold_Loan', 'Cash_Loan')
   # txt_name2.insert(0, '1. Home_Loan')
    txt_name2.grid(row=2, column=1, pady=10, padx=30, sticky="W")


    lbl_name3 = Label(Manage_frame1, text="Client", fg="black", bg="whitesmoke", font=('times new roman', 13, 'bold'))
    lbl_name3.grid(row=3, column=0, pady=10, padx=30, sticky="W")
    txt_name3 = ttk.Combobox(Manage_frame1, font=('times new roman', 13), width=20)
    txt_name3['values'] = ('Shreya', 'Shivangi', 'Simran', 'Surbhi','Sonal','Sunita')
    txt_name3.insert(0, 'Shivangi')
    txt_name3.grid(row=3, column=1, pady=10, padx=30, sticky="W")


    lbl_name4 = Label(Manage_frame1, text="Loan Amount", fg="black", bg="whitesmoke", font=('times new roman', 13, 'bold'))
    lbl_name4.grid(row=4, column=0, pady=10, padx=30, sticky="W")
    txt_name4 = Entry(Manage_frame1, font=('times new roman', 13), bd=2,width=20,
                     relief=GROOVE)
    txt_name4.grid(row=4, column=1, pady=10, padx=30, sticky="W")

    lbl_name5 = Label(Manage_frame1, text="ID Proof", fg="black", bg="whitesmoke", font=('times new roman', 13, 'bold'))
    lbl_name5.grid(row=5, column=0, pady=10, padx=30, sticky="W")
    txt_name5 = tk.Checkbutton(Manage_frame1, font=('times new roman',0), bd=1,variable=v1,
                      relief=GROOVE)
    txt_name5.grid(row=5, pady=10, padx=30, column=1,sticky="W")

    lbl_name6 = Label(Manage_frame1, text="Residence Proof", fg="black", bg="whitesmoke", font=('times new roman', 13, 'bold'))
    lbl_name6.grid(row=6, column=0, pady=10, padx=30, sticky="W")
    txt_name6 =  tk.Checkbutton(Manage_frame1, font=('times new roman',0), bd=1,
                      relief=GROOVE)
    txt_name6.grid(row=6, column=1, pady=10, padx=30, sticky="W")

    lbl_name7 = Label(Manage_frame1, text="Income Proof", fg="black", bg="whitesmoke",
                      font=('times new roman', 13, 'bold'))
    lbl_name7.grid(row=7, column=0, pady=10, padx=30, sticky="W")
    txt_name7 =  tk.Checkbutton(Manage_frame1, font=('times new roman',0), bd=1,variable=v3,
                      relief=GROOVE)
    txt_name7.grid(row=7, column=1, pady=10, padx=30, sticky="W")

    lbl_name8 = Label(Manage_frame1, text="Bank Statement", fg="black", bg="whitesmoke",
                      font=('times new roman', 13, 'bold'))
    lbl_name8.grid(row=8, column=0, pady=10, padx=30, sticky="W")
    txt_name8 = tk.Checkbutton(Manage_frame1, font=('times new roman',0), bd=1,variable=v4,
                      relief=GROOVE)
    txt_name8.grid(row=8, column=1, pady=10, padx=30, sticky="W")

    lbl_name9 = Label(Manage_frame1, text="Remarks", fg="black", bg="whitesmoke",
                      font=('times new roman', 13, 'bold'))
    lbl_name9.grid(row=9, column=0, pady=10, padx=30, sticky="W")

    txt_name9 = Entry(Manage_frame1, relief=RIDGE, bg="white", bd=6)
    txt_name9.place(x=210, y=440, width=200, height=70)

    lbl_name10 = Label(Manage_frame1, text="Status", fg="black", bg="whitesmoke",
                      font=('times new roman', 13, 'bold'))
    lbl_name10.grid(row=10, column=0, pady=30, padx=30, sticky="W")
    txt_name10 = Entry(Manage_frame1, font=('times new roman', 13), bd=2, width=13,
                      relief=GROOVE)
    txt_name10.insert(0,'Approved')
    txt_name10.grid(row=10, column=1, pady=45, padx=30, sticky="W")



   # ===============================Manage_frame4========================================

    lbl_name1 = Label(Manage_frame4, text="Loan Amount", fg="black", bg="whitesmoke",
                      font=('times new roman', 15, 'bold'))
    lbl_name1.place(x=20,y=30)
    name1 = Entry(Manage_frame4, font=('times new roman', 15, 'bold'), bd=2, width=18,
                      relief=GROOVE)
    name1.place(x=230,y=30)

    lbl_name1 = Label(Manage_frame4, text="Rate Of Interest", fg="black", bg="whitesmoke",
                      font=('times new roman', 15, 'bold'))
    lbl_name1.place(x=430,y=30)
    name2 = Entry(Manage_frame4, font=('times new roman', 15, 'bold'), bd=2, width=18,
                      relief=GROOVE)
    name2.place(x=660,y=30)

    lbl_name1 = Label(Manage_frame4, text="Client Monthly Income", fg="black", bg="whitesmoke",
                     font=('times new roman', 15, 'bold'))
    lbl_name1.place(x=20,y=80)
    name3 = Entry(Manage_frame4, font=('times new roman', 15, 'bold'), bd=2, width=18,
                      relief=GROOVE)
    name3.place(x=230,y=80)

    lbl_name1 = Label(Manage_frame4, text="Client Monthly Expenses", fg="black", bg="whitesmoke",
                      font=('times new roman', 15, 'bold'))
    lbl_name1.place(x=430,y=80)
    name4 = Entry(Manage_frame4, font=('times new roman', 15, 'bold'), bd=2, width=18,
                      relief=GROOVE)
    name4.place(x=660,y=80)

    lbl_name1 = Label(Manage_frame4, text="Number Of years", fg="black", bg="whitesmoke",
                     font=('times new roman', 15, 'bold'))
    lbl_name1.place(x=20,y=130)
    name5 = Entry(Manage_frame4, font=('times new roman', 15, 'bold'), bd=2, width=18,
                      relief=GROOVE)
    name5.place(x=230,y=130)

    evaluate_btn = Button(Manage_frame4, text="Evaluate", width=18, pady=5, bg="lightcyan", fg="black", bd=5,
                       font=('times new roman', 8, 'bold'),command=evaluate)
    evaluate_btn.place(x=480, y=125)

    issue_btn = Button(Manage_frame4, text="Issue", width=18, pady=5, bg="lightcyan", fg="black", bd=5,
                          font=('times new roman', 8, 'bold'),command=issue)
    issue_btn.place(x=700, y=125)

    lbl_name1 = Label(Manage_frame4, text="Loan Evaluation Result :", fg="black", bg="whitesmoke",
                      font=('times new roman', 15, 'bold'))
    lbl_name1.place(x=20, y=170)


    first_btn = Button(Manage_frame3, text="First", width=13, pady=5, bg="lightcyan", fg="black", bd=5,
                        font=('times new roman', 10, 'bold'),command=first)
    first_btn.place(x=20, y=10)

    previous_btn=Button(Manage_frame3,text="Previous",width=13, pady=5,bg="lightcyan",fg="black",
                        bd=5, font=('times new roman', 10, 'bold'),command=previous)
    previous_btn.place(x=140,y=10)

    next_btn = Button(Manage_frame3, text="Save", width=13, pady=5,bg="lightcyan",fg="black",bd=5,
                      font=('times new roman', 10, 'bold'),command=save)
    next_btn.place(x=260, y=10)

    last_btn = Button(Manage_frame3, text="Last", width=13, pady=5, bg="lightcyan", fg="black", bd=5,
                        font=('times new roman', 10, 'bold'),command=last)
    last_btn.place(x=380, y=10)


    add_btn = Button(Manage_frame3, text="Add", width=13, pady=5, bg="lightcyan", fg="black", bd=5,
                     font=('times new roman', 10, 'bold'),command=add)
    add_btn.place(x=20, y=60)

    update_btn = Button(Manage_frame3, text="Update", width=13, pady=5, bg="lightcyan", fg="black", bd=5,
                        font=('times new roman', 10, 'bold'),command=update)
    update_btn.place(x=140, y=60)

    save_btn = Button(Manage_frame3, text="Next", width=13, pady=5, bg="lightcyan", fg="black", bd=5,
                      font=('times new roman', 10, 'bold'))
    save_btn.place(x=260, y=60)

    cancel_btn = Button(Manage_frame3, text="Cancel", width=13, pady=5, bg="lightcyan", fg="black", bd=5,
                        font=('times new roman', 10, 'bold'),command=cancel)
    cancel_btn.place(x=380, y=60)
    search_btn = Button(Manage_frame1, text="Search", width=9, pady=3, bg="whitesmoke", fg="black", bd=3,command=search,
                      font=('times new roman', 11, 'bold'))
    search_btn.place(x=400, y=15)


    mainloop()