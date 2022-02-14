from tkinter import*
from tkinter import ttk
from turtle import width
# from typing_extensions import Self
from PIL import Image,ImageTk 
import mysql.connector
from tkinter import messagebox



class Student :
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title('MANAGE.OI')
        
        # Variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()  
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()        
        self.var_div=StringVar()
        self.var_roll=StringVar()        
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        
        
        
        img=Image.open(r"C:\Users\DELL\Desktop\demo1\sk blue.jfif")
        img=img.resize((1530,120),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        self.btn_1=Button(self.root,image=self.photoimg,cursor="hand2")
        self.btn_1.place(x=0,y=0,width=1530,height=120)
        
        Manage_frame=Frame(bd=0,relief=RIDGE,bg="#F9F9F8")
        Manage_frame.place(x=0,y=120,width=1530,height=750)
        
        lbl_title=Label(Manage_frame,text="Manage Database",font=("Helvetica",30),fg="black",bg="#F9F9F8")
        lbl_title.place(x=0,y=0,width=1400,height=50)
        
        # manage Frame
        
        secondManage_frame=Frame(Manage_frame,bd=2,relief=RIDGE,bg="#95C0A3")
        secondManage_frame.place(x=23,y=55,width=1320,height=550)
        
        # left frame
        DataLeftFrame=LabelFrame(secondManage_frame,bd=4,relief=RIDGE,padx=2,text="Student Information",font=('times new roman',12,"bold"),fg="#45955B",bg="#F9F9F8")
        DataLeftFrame.place(x=10,y=10,width=660,height=510)  
        
        # img
        img_1=Image.open(r"C:\\Users\\DELL\\Desktop\\demo1\\info 1.jpg")
        img_1=img_1.resize((450,120),Image.ANTIALIAS)
        self.photoimg_1=ImageTk.PhotoImage(img_1)
        
        
        my_img=Label(DataLeftFrame,image=self.photoimg_1,bd=2,relief=RIDGE)
        my_img.place(x=100,y=0,width=450,height=120)
        
        # Current course LabelFrame Information
        std_lbl_info_frame=LabelFrame(DataLeftFrame,bd=4,relief=RIDGE,padx=2,text="Current Course Information",font=('times new roman',12,"bold"),fg="#45955B",bg="#F9F9F8")
        std_lbl_info_frame.place(x=10,y=120,width=630,height=115)  
        
        # labels and combobox
        # department
        
        lbl_dep=Label(std_lbl_info_frame,text="Department",font=("arial",12,"bold"),bg="#F9F9F8")
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W)
        
        combo_dep=ttk.Combobox(std_lbl_info_frame,textvariable=self.var_dep,font=("arial",10,"bold"),width=17,state="readonly")
        combo_dep["value"]=("Select Department","Computer","IT","Civil")
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        # course
        
        course_std=Label(std_lbl_info_frame,font=("arial",12,"bold"),text="Courses:",bg="#F9F9F8")
        course_std.grid(row=0,column=2,sticky=W,padx=2,pady=10)
        
        com_txtcourse_std=ttk.Combobox(std_lbl_info_frame,textvariable=self.var_course,state="readonly",font=("arial",10,"bold"),width=17)
        com_txtcourse_std["value"]=("Select Course","FE","SE","TE","BE")
        com_txtcourse_std.current(0)
        com_txtcourse_std.grid(row=0,column=3,sticky=W,padx=2,pady=10)
        
        # year
        current_year=Label(std_lbl_info_frame,font=("arial",12,"bold"),text="Year:",bg="#F9F9F8")
        current_year.grid(row=1,column=0,sticky=W,padx=2,pady=10)
        
        com_txt_current_year=ttk.Combobox(std_lbl_info_frame,textvariable=self.var_year,state="readonly",font=("arial",10,"bold"),width=17)
        com_txt_current_year["value"]=("Select Year","2020-2021","2021-2022","2022-2023","2023-2024")
        com_txt_current_year.current(0)
        com_txt_current_year.grid(row=1,column=1,sticky=W,padx=2)
        
        #semester
        label_semester=Label(std_lbl_info_frame,font=("arial",12,"bold"),text="Semester:",bg="white")
        label_semester.grid(row=1,column=2,sticky=W,padx=2,pady=10)
        
        comSemester=ttk.Combobox(std_lbl_info_frame,textvariable=self.var_semester,state="readonly",font=("arial",10,"bold"),width=17)
        comSemester["value"]=("Select Semester","Semester-1","Semester-2")
        comSemester.current(0)
        comSemester.grid(row=1,column=3,sticky=W,padx=2,pady=10)
        
        # Student class LabelFrame Information
        std_lbl_class_frame=LabelFrame(DataLeftFrame,bd=4,relief=RIDGE,padx=2,text="Class Course Information",font=('times new roman',12,"bold"),fg="#45955B",bg="#F9F9F8")
        std_lbl_class_frame.place(x=10,y=235,width=630,height=215) 
        
        # labels entry
        #ID
        lbl_id=Label(std_lbl_class_frame,font=("arial",12,"bold"),text="Student ID:",bg="#F9F9F8")
        lbl_id.grid(row=0,column=0,sticky=W,padx=2,pady=7)
        
        id_entry=ttk.Entry(std_lbl_class_frame,textvariable=self.var_std_id,font=("arial",10,"bold"),width=18)
        id_entry.grid(row=0,column=1,sticky=W,padx=2,pady=7)
        
        # Name
        lbl_Name=Label(std_lbl_class_frame,font=("arial",12,"bold"),text="Student Name:",bg="#F9F9F8")
        lbl_Name.grid(row=0,column=2,sticky=W,padx=2,pady=7)
        
        txt_name=ttk.Entry(std_lbl_class_frame,textvariable=self.var_std_name,font=("arial",10,"bold"),width=18)
        txt_name.grid(row=0,column=3,sticky=W,padx=2,pady=7)
        
        #Division
        lbl_div=Label(std_lbl_class_frame,font=("arial",12,"bold"),text="Class Division:",bg="#F9F9F8")
        lbl_div.grid(row=1,column=0,sticky=W,padx=2,pady=7)
        
        com_txt_div=ttk.Combobox(std_lbl_class_frame,textvariable=self.var_div,state="readonly",font=("arial",10,"bold"),width=15)
        com_txt_div["value"]=("Select Division","A","B","C")
        com_txt_div.current(0)
        com_txt_div.grid(row=1,column=1,sticky=W,padx=2,pady=7)   
        
        # Roll
        lbl_roll=Label(std_lbl_class_frame,font=("arial",12,"bold"),text="Roll No:",bg="#F9F9F8")
        lbl_roll.grid(row=1,column=2,sticky=W,padx=2,pady=7)
        
        txt_roll=ttk.Entry(std_lbl_class_frame,textvariable=self.var_roll,width=18,font=("arial",10,"bold"))
        txt_roll.grid(row=1,column=3,padx=2,pady=7)
        
        #gender
        lbl_gender=Label(std_lbl_class_frame,font=("arial",12,"bold"),text="Gender:",bg="#F9F9F8")
        lbl_gender.grid(row=2,column=0,sticky=W,padx=2,pady=7)
        
        com_txt_gender=ttk.Combobox(std_lbl_class_frame,textvariable=self.var_gender,state="readonly",font=("arial",10,"bold"),width=15)
        com_txt_gender["value"]=("Male","Female","Other")
        com_txt_gender.current(0)
        com_txt_gender.grid(row=2,column=1,sticky=W,padx=2,pady=7)  
        
        # DOB
        lbl_dob=Label(std_lbl_class_frame,font=("arial",12,"bold"),text="DOB:",bg="#F9F9F8")
        lbl_dob.grid(row=2,column=2,sticky=W,padx=2,pady=7)
        
        txt_dob=ttk.Entry(std_lbl_class_frame,textvariable=self.var_dob,width=18,font=("arial",10,"bold"))
        txt_dob.grid(row=2,column=3,padx=2,pady=7)
        
        # Email
        lbl_email=Label(std_lbl_class_frame,font=("arial",12,"bold"),text="Email:",bg="#F9F9F8")
        lbl_email.grid(row=3,column=0,sticky=W,padx=2,pady=7)
        
        txt_email=ttk.Entry(std_lbl_class_frame,textvariable=self.var_email,width=18,font=("arial",10,"bold"))
        txt_email.grid(row=3,column=1,padx=2,pady=7)
        
        # phone
        lbl_phone=Label(std_lbl_class_frame,font=("arial",12,"bold"),text="Phone No:",bg="#F9F9F8")
        lbl_phone.grid(row=3,column=2,sticky=W,padx=2,pady=7)
        
        txt_phone=ttk.Entry(std_lbl_class_frame,textvariable=self.var_phone,width=18,font=("arial",10,"bold"))
        txt_phone.grid(row=3,column=3,padx=2,pady=7)
        
        
        # Address
        lbl_address=Label(std_lbl_class_frame,font=("arial",12,"bold"),text="Address:",bg="#F9F9F8")
        lbl_address.grid(row=4,column=0,sticky=W,padx=2,pady=7)
        
        txt_address=ttk.Entry(std_lbl_class_frame,textvariable=self.var_address,width=18,font=("arial",10,"bold"))
        txt_address.grid(row=4,column=1,padx=2,pady=7)    
        
        
        # Teacher
        lbl_teacher=Label(std_lbl_class_frame,font=("arial",12,"bold"),text="Teacher Name:",bg="#F9F9F8")
        lbl_teacher.grid(row=4,column=2,sticky=W,padx=2,pady=7)
        
        txt_teacher=ttk.Entry(std_lbl_class_frame,textvariable=self.var_teacher,width=18,font=("arial",10,"bold"))
        txt_teacher.grid(row=4,column=3,padx=2,pady=7)   
        
        # Button Frame
        btn_frame=Frame(DataLeftFrame,bd=2,relief=RIDGE,bg="#F9F9F8")
        btn_frame.place(x=10,y=455,width=630,height=30) 
        
        btn_Add=Button(btn_frame,text="Save",command=self.add_data,font=("arial",10,"bold"),width=17,bg="#5e9abc",fg="black")
        btn_Add.grid(row=0,column=0,padx=5)
        
        btn_update=Button(btn_frame,text="Update",command=self.update_data,font=("arial",10,"bold"),width=17,bg="#5e9abc",fg="black")
        btn_update.grid(row=0,column=1,padx=5)
        
        btn_Delete=Button(btn_frame,text="Delete",command=self.delete_data,font=("arial",10,"bold"),width=17,bg="#5e9abc",fg="black")
        btn_Delete.grid(row=0,column=2,padx=5)
        
        btn_reset=Button(btn_frame,text="Reset",command=self.reset_data,font=("arial",10,"bold"),width=17,bg="#5e9abc",fg="black")
        btn_reset.grid(row=0,column=3,padx=5)

        
        # right frame
        DataRightFrame=LabelFrame(secondManage_frame,bd=4,relief=RIDGE,padx=2,text="Student Information",font=('times new roman',12,"bold"),fg="#45955B",bg="#F9F9F8")
        DataRightFrame.place(x=680,y=10,width=625,height=510)       
        
        # img
        img_2=Image.open(r"C:\Users\DELL\Desktop\demo1\details.jpg")
        img_2=img_2.resize((450,180),Image.ANTIALIAS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)
        
        my_img=Label(DataRightFrame,image=self.photoimg_2,bd=2,relief=RIDGE)
        my_img.place(x=100,y=0,width=450,height=180)
        
        
        # right frame
        Search_Frame=LabelFrame(DataRightFrame,bd=4,relief=RIDGE,padx=2,text="Serach Student Information",font=('times new roman',12,"bold"),fg="#45955B",bg="#F9F9F8")
        Search_Frame.place(x=0,y=180,width=610,height=70)  
        
        search_by=Label(Search_Frame,font=("arial",12,"bold"),text="Search By:",bg="#F9F9F8")
        search_by.grid(row=0,column=0,sticky=W,padx=2,pady=7)
    
        # search
        self.var_com_search=StringVar()
        com_txt_search=ttk.Combobox(Search_Frame,textvariable=self.var_com_search,state="readonly",font=("arial",10,"bold"),width=15)
        com_txt_search["value"]=("Select Option","Roll","Phone","Student_id")
        com_txt_search.current(0)
        com_txt_search.grid(row=0,column=1,sticky=W,padx=2)
        
        
        
        
        self.var_search=StringVar()
        txt_search=ttk.Entry(Search_Frame,textvariable=self.var_search,width=15,font=("arial",10,"bold"))
        txt_search.grid(row=0,column=2,padx=2)
        
        btn_search=Button(Search_Frame,command=self.search_data,text="Search",font=("arial",10,"bold"),width=14,bg="#5e9abc",fg="black")
        btn_search.grid(row=0,column=3,padx=2)
        
        btn_ShowAll=Button(Search_Frame,command=self.fetch_data,text="Show All",font=("arial",10,"bold"),width=14,bg="#5e9abc",fg="black")
        btn_ShowAll.grid(row=0,column=4,padx=2)

        
        
        # ================================Student Table and Scroll bar =====================================
        table_frame=Frame(DataRightFrame,bd=4,relief=RIDGE)
        table_frame.place(x=0,y=250,width=610,height=235)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Student Name")
        self.student_table.heading("div",text="Class Div")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone No")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher Name")
        
        self.student_table["show"]="headings"
        
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
    def add_data(self):
        if (self.var_dep.get()==""or self.var_email.get()==""or self.var_std_id.get()==""):
            messagebox.showerror("Error","All Fields Are required")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",passwd="abhishekom26",database="mydata")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_semester.get(),
                                                                                                            self.var_std_id.get(),
                                                                                                            self.var_std_name.get(),
                                                                                                            self.var_div.get(),
                                                                                                            self.var_roll.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_teacher.get(),
                                                                                                  ))
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student has been added!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
        
    
    # fetch function
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",passwd="abhishekom26",database="mydata")    
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()    
        
    # get cursor
    
    def get_cursor(self,event=""):
        cursor_row=self.student_table.focus()
        content=self.student_table.item(cursor_row)
        data=content["values"]
        
        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2]) 
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4]) 
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])  
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])        
        
    def update_data(self):
        if (self.var_dep.get()==" or self.var_email.get()==" or self.var_std_id.get()==""):
            messagebox.showerror("Error", "All Fields Are required")
        else:
            try:
                update=messagebox.askyesno("Update","Are you sure update this student data",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",user="root",passwd="abhishekom26",database="mydata")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s where student_id=%s",(
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_semester.get(),
                                                                                                            
                                                                                                            self.var_std_name.get(),
                                                                                                            self.var_div.get(),
                                                                                                            self.var_roll.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_teacher.get(),
                                                                                                            self.var_std_id.get()
        
                                                                                                            ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                
                messagebox.showinfo("Success","Student successfully updated",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
        
    # Delete
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields Are required")
        else:
            try:
                Delete=messagebox.askyesno("Delete","Are you sure delete this student")
                if Delete>0:
                    conn=mysql.connector.connect(host="localhost",user="root",passwd="abhishekom26",database="mydata")
                    my_cursor=conn.cursor()
                    sql="delete from student where student_id=%s"
                    value=(self.var_std_id.get(),)       
                    my_cursor.execute(sql,value)
                else:
                    if not Delete:
                        return
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Your Student data has been Deleted",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                
    # reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        
        
        
        
    # search data
    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","Please select option")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",passwd="abhishekom26",database="mydata")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student where " +str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                data=my_cursor.fetchall()
                if len(data)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("",END,values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                
                

                       

        
if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
    
    
     
