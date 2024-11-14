#1.Creating Quiz Application
from tkinter import*
from tkinter import ttk
import tkinter.font as font
from tkinter import messagebox
import time
hour=14
minute=50
data = {}
data_with_roll={}
s1_file=open("Score.txt","r")
sc={}
file=open("Quiz_username.txt","r")
p_file=open("Quiz_password.txt","r")
a=file.read()
b=p_file.read()
e=s1_file.read()
timer_hour=0
timer_minute=1-1
timer_ss=10-1
def dashboard():
    d_board=Tk()
    Pass_dict = {}
    w = 1000
    h = 500
    sw = d_board.winfo_screenwidth()
    sh = d_board.winfo_screenheight()
    x = (sw / 2) - (w / 2)
    y = (sh / 2) - (h / 2)
    d_board.geometry("%dx%d+%d+%d" % (w, h, x, y))
    d_board.title("SCOREBOARD")
    d_board.resizable(False, False)
    value = list(sc.values())
    key = list(sc.keys())
    Pass=0
    for k in range(len(value)):
        if (int(value[k])>5):
            Pass+=1
            Pass_dict.update({key[k]:value[k]})
    label_attended= Label(d_board, text="Total No.of.students Attended: "+str(len(value)),font=("Bodoni MT Black",20))
    label_attended.place(x=100,y=150)
    label_pass = Label(d_board, text="Total No.of.students passed: " + str(Pass),
                           font=("Bodoni MT Black", 20))
    def sb():
        scoredisp = Tk()
        scoredisp.geometry("700x300")
        scoredisp.title("SCORE BOARD")
        label = Label(scoredisp, text="Score board", font=("Bodoni MT Black", 20))
        label.pack()
        tree = ttk.Treeview(scoredisp, columns=("c1", "c2", "c3"), show='headings')
        tree.column("#1", anchor=CENTER)
        tree.heading("#1", text="S.No")
        tree.column("#2", anchor=CENTER)
        tree.heading("#2", text="Name")
        tree.column("#3", anchor=CENTER)
        tree.heading("#3", text="Score")
        pass_key = list(Pass_dict.keys())
        pass_value = list(Pass_dict.values())
        for i in range(len(pass_value)):
            tree.insert('', 'end', text="1", values=(i + 1, pass_key[i], pass_value[i]))
            tree.pack()
        scoredisp.mainloop()
    label_pass.place(x=100, y=250)
    det=ttk.Button(d_board,text="Details",command=sb)
    det.place(x=550,y=260)
    d_board.mainloop()
if a!="" and b!="":
    c=b.split(",")
    c.pop()
    d=a.split(",")
    d.pop()
    f=e.split(",")
    f.pop()
    file.close()
    Value=""
    s_value=0
    for i in range(len(d)):
        data.update({d[i]:c[i]})
    for j in range(len(f)):
        if(j%2==0):
            Value=f[j]
        elif(j%2!=0):
            s_value=f[j]
        sc.update({Value:s_value})
    p_file.close()
def file():
    value = list(data.values())
    key = list(data.keys())
    file_u = open("Quiz_username.txt", "w")
    file_p = open("Quiz_password.txt", "w")
    for i in range(len(key)):
        file_u.write(key[i])
        file_u.write(",")
        file_p.write(value[i])
        file_p.write(",")
    file_u.close()
    file_p.close()
admin_login={"Admin":"admin"}
#New_Registration
def N_reg():
    new= Tk()
    w = 1000
    h = 500
    sw = new.winfo_screenwidth()
    sh = new.winfo_screenheight()
    x = (sw / 2) - (w / 2)
    y = (sh / 2) - (h / 2)
    new.geometry("%dx%d+%d+%d" % (w, h, x, y))
    new.title("REGISTRATION PAGE")
    new.resizable(False, False)
    logo = Label(new, text="NEW REGISTRATION", font=("Arial black", 18), width=20, fg="purple")
    logo.place(x=350)
    name = Label(new, text="username", fg="black", font=("Ariel bold", 10), bg="light grey")
    name.place(x=400, y=200)
    user_input = ttk.Entry(new)
    user_input.place(x=470, y=200)
    roll= Label(new, text="roll.no", fg="black", font=("Ariel bold", 10), bg="light grey")
    roll.place(y=240, x=400)
    roll_no = ttk.Entry(new)
    roll_no.place(x=470, y=240)
    def entry():
        a=user_input.get()
        b=roll_no.get()
        data.update({a:"hello123"})
        data_with_roll.update({a:b})
        file()
        def show():
            u_msg.destroy()
        u_msg = Label(new, text="Updated successfully!!..", font=("GoudyStout",30),fg="green")
        u_msg.place(x=350, y=400)
        new.after(2000,show)
    enter=ttk.Button(new,text="Register",width=10,command=entry)
    enter.place(x=400,y=300)
    value = list(data.values())
    key = list(data.keys())
    file_u = open("Quiz_username.txt", "w")
    file_p = open("Quiz_password.txt", "w")
    for i in range(len(key)):
        file_u.write(key[i])
        file_u.write(",")
        file_p.write(value[i])
        file_p.write(",")
    file_u.close()
    file_p.close()
    def clear():
        user_input.delete(0,END)
        roll_no.delete(0,END)
    new_user=ttk.Button(new,text="Next",command=clear)
    new_user.place(x=500,y=300)
    new.mainloop()
#Admin first_page
def A_F():
    admin_first = Tk()
    w = 1000
    h = 500
    sw = admin_first.winfo_screenwidth()
    sh = admin_first.winfo_screenheight()
    x = (sw / 2) - (w / 2)
    y = (sh / 2) - (h / 2)
    admin_first.geometry("%dx%d+%d+%d" % (w, h, x, y))
    admin_first.title("Admin")
    admin_first.resizable(False, False)
    lbl=Label(admin_first,text="WELCOME  QUIZ-\nADMINISTRATOR",font=("Arial black",20),fg="green")
    lbl.place(x=330,y=150)
    menu_bar=Menu(admin_first)
    def close():
        admin_first.destroy()
    menu_bar.add_command(label="Home",command=close)
    menu_bar.add_command(label="New Registration",command=N_reg)
    menu_bar.add_command(label="Score Board",command=dashboard)
    admin_first.configure(menu=menu_bar)
    admin_first.mainloop()
SCORE=0
score = 0
question = 1
#instruction
def instr():
    ins=Tk()
    w = 1000
    h = 500
    sw = ins.winfo_screenwidth()
    sh = ins.winfo_screenheight()
    x = (sw / 2) - (w / 2)
    y = (sh / 2) - (h / 2)
    ins.geometry("%dx%d+%d+%d" % (w, h, x, y))
    ins.title("Admin")
    ins.resizable(False, False)
    label=Label(ins,text="INSTRUCTIONS:\n1.Each Question carries 2 marks\n2.Only 90 Minutes time alloted\n3.If you want to continue click'START' \nelse click 'LEAVE'",font=('Helvatical bold', 20),bg="light green")
    label.place(x=300,y=180)
    global SCORE
    def leave_page():
        ins.destroy()
    SCORE=0
    def quiz():
        ins.destroy()
        global timer_ss,timer_hour,timer_minute
        test1 = Tk()
        test1.title("For Testing")
        w = 1000
        h = 500
        sw = test1.winfo_screenwidth()
        sh = test1.winfo_screenheight()
        x = (sw / 2) - (w / 2)
        y = (sh / 2) - (h / 2)
        test1.geometry("%dx%d+%d+%d" % (w, h, x, y))
        menu_bar = Menu(test1)
        menu_bar.add_command(label="Home",command=instr)
        test1.configure(menu=menu_bar)
        file = open("question.txt", "r")
        topic = Label(test1, text="Python Quiz", fg="Black", bg="White", font=("Ariel", 30))
        topic.pack(fill=X)
        SCORE=0
        score=0
        question=1
        var = StringVar(test1,0)
        TIMER = Label(test1, text=str(timer_hour) + ":" + str(timer_minute) + ":" + str(timer_ss), font=("Arial", 20),bg="White")
        TIMER.place(x=900,y=10)
        def Time():
            global timer_ss, timer_minute, timer_hour,question
            if (timer_hour == 0 and timer_minute == 0 and timer_ss == 0):
                TIMER.config(text=str(timer_hour) + ":" + str(timer_minute) + ":" + str(timer_ss))
                question=5
            elif (timer_minute== 0 and timer_ss == 0):
                TIMER.config(text=str(timer_hour) + ":" + str(timer_minute) + ":" + str(timer_ss))
                timer_hour = timer_hour - 1
                timer_minute = 59
                timer_ss = 59
                test1.after(1000, Time)
            elif (timer_ss == 0):
                TIMER.config(text=str(timer_hour) + ":" + str(timer_minute) + ":" + str(timer_ss))
                timer_ss = 59
                timer_minute = timer_minute - 1
                test1.after(1000, Time)
            else:
                TIMER.config(text=str(timer_hour) + ":" + str(timer_minute) + ":" + str(timer_ss))
                timer_ss= timer_ss - 1
                test1.after(1000, Time)
        test1.after(1000, Time)
        def next():
            global ss,mm,timer_hour,timer_minute,timer_ss
            global score,question
            answers= ["1", "4", "2", "2", "4"]
            ans=var.get()
            Font = font.Font(family="Castellar")
            for widgets in test1.winfo_children():
                if(widgets!=topic and widgets!=TIMER):
                        widgets.destroy()
            if question < 5:
                menu_bar = Menu(test1)
                menu_bar.add_command(label="Home", command=instr)
                test1.configure(menu=menu_bar)
                if ans == answers[question - 1]:
                    score += 2
                for i in range(1):
                    for j in range(1):
                        a = ttk.Label(test1, text=file.readline(),font=("Castellar",20,"bold"))
                        a.pack()
                        b = Radiobutton(test1, text=file.readline(), variable=var, value=1)
                        b['font']=Font
                        b.pack()
                        c = Radiobutton(test1, text=file.readline(), variable=var, value=2)
                        c['font'] = Font
                        c.pack()
                        d = Radiobutton(test1, text=file.readline(), variable=var, value=3)
                        d['font'] = Font
                        d.pack()
                        e =Radiobutton(test1, text=file.readline(), variable=var, value=4)
                        e['font'] = Font
                        e.pack()
                    nxt_que = ttk.Button(test1, text="NEXT", command=next)
                    nxt_que.pack()
                    question += 1
            else:
                def close_t():
                    TIMER.destroy()
                    test1.destroy()
                c2=ttk.Button(test1,text= "Back to home page",command=close_t)
                c2.place(x=450,y=200)
                if(timer_hour==0 and timer_ss==0 and timer_minute==0):
                    time_out_msg=Label(test1,text="Time Out!!..",fg="Red",font=("Bodoni MT Black", 30))
                    time_out_msg.pack(anchor=CENTER)
                inf=Label(test1,text="Your Response were Submitted\nThanks for supporting us!!",font=("Bodoni MT Black", 20),fg="green")
                inf.pack(anchor=CENTER)
                global SCORE
                SCORE=str(score)
                s_file = open("Score.txt", "a")
                s_file.write(uinput)
                s_file.write(",")
                s_file.write(str(score))
                s_file.write(",")
                #Reset for the next player
                score=0
                question=1
        myFont = font.Font(family="Castellar")
        for i in range(1):
            for j in range(1):
                a = ttk.Label(test1, text=file.readline(),font=("Castellar",20,"bold"))
                a.pack()
                b = Radiobutton(test1, text=file.readline(), variable=var, value=1)
                b['font']=myFont
                b.pack(anchor=CENTER)
                c = Radiobutton(test1, text=file.readline(), variable=var, value=2)
                c['font'] = myFont
                c.pack(anchor=CENTER)
                d = Radiobutton(test1, text=file.readline(), variable=var, value=3)
                d['font'] = myFont
                d.pack(anchor=CENTER)
                e = Radiobutton(test1, text=file.readline(), variable=var, value=4)
                e['font'] = myFont
                e.pack(anchor=CENTER)
            nxt_que = ttk.Button(test1, text="NEXT", command=next)
            nxt_que.pack()
        test1.mainloop()
        file.close()
    start=ttk.Button(ins,text="START",width=20,command=quiz)
    start.place(x=350,y=350)
    leave=ttk.Button(ins,text="LEAVE",width=20,command=leave_page)
    leave.place(x=550,y=350)
    ins.mainloop()
#Admin Login
def Ad_Login():
    admin=Tk()
    admin.configure(bg="light grey")
    w=1000
    h=500
    sw=admin.winfo_screenwidth()
    sh=admin.winfo_screenheight()
    x=(sw/2)-(w/2)
    y=(sh/2)-(h/2)
    admin.geometry("%dx%d+%d+%d"%(w,h,x,y))
    admin.title("Admin")
    admin.resizable(False,False)
    logo=Label(admin,text="ADMIN LOGIN PAGE", font=("Arial black", 18), width=20, fg="purple")
    logo.place(x=350)
    name = Label(admin, text="username", fg="black", font=("Ariel bold", 10), bg="light grey")
    name.place(x=400, y=200)
    user_input = ttk.Entry(admin)
    user_input.place(x=470, y=200)
    pas = Label(admin, text="password", fg="black", font=("Ariel bold", 10), bg="light grey")
    pas.place(y=240, x=400)
    pass_word = ttk.Entry(admin, show=".")
    pass_word.place(x=470, y=240)
    def submit():
        uname = user_input.get()
        password = pass_word.get()
        if uname in admin_login:
            if password==admin_login[uname]:
                admin.destroy()
                A_F()
            else:
                messagebox.showerror("SORRY!!...", "Incorrect Password")
        elif uname =="":
            messagebox.showerror("404", "Kindly,Fill the username")
            admin.destroy()
        elif password == "":
            messagebox.showerror("404", "Kindly,Fill the password")
            admin.destroy()
        else:
             messagebox.showerror("Alert", "OOPS!....Username is not found")
             admin.destroy()
    login=ttk.Button(admin,text="Login",command=submit)
    login.place(x=500,y=300)
    admin.mainloop()
#User login page
def student():
    test1=Tk()
    test1.configure(bg="light grey")
    w = 1000
    h = 500
    sw = test1.winfo_screenwidth()
    sh = test1.winfo_screenheight()
    x = (sw / 2) - (w / 2)
    y = (sh / 2) - (h / 2)
    test1.geometry("%dx%d+%d+%d" % (w, h, x, y))
    test1.resizable(False,False)
    test1.title("LOGIN PAGE")
    Title = Label(test1, text="USER LOGIN PAGE", font=("Arial black", 18), width=20, fg="purple")
    Title.place(x=350)
    name = Label(test1, text="username", fg="black", font=("Ariel bold", 10), bg="light grey")
    name.place(x=400, y=200)
    user_input = ttk.Entry(test1)
    user_input.place(x=470, y=200)
    pas = Label(test1, text="password", fg="black", font=("Ariel bold", 10), bg="light grey")
    pas.place(y=240, x=400)
    pass_word = ttk.Entry(test1, show=".")
    pass_word.place(x=470, y=240)
    def change_p():
        password=Tk()
        password.title("Security")
        w = 400
        h = 200
        sw = password.winfo_screenwidth()
        sh = test1.winfo_screenheight()
        x = (sw / 2) - (w / 2)
        y = (sh / 2) - (h / 2)
        password.geometry("%dx%d+%d+%d" % (w, h, x, y))
        v=Label(password,text="Username")
        v.place(x=50,y=30)
        v_entry=Entry(password)
        v_entry.place(x=110,y=30)
        u=Label(password,text="Old password")
        u.place(x=30,y=60)
        u_entry=Entry(password)
        u_entry.place(x=110,y=60)
        m=Label(password,text="New password")
        m.place(x=30,y=90)
        m_entry=Entry(password)
        m_entry.place(x=110,y=90)
        def check():
            a=v_entry.get()
            b=u_entry.get()
            c=m_entry.get()
            if a in data.keys() and data[a]==b:
                    data.update({a:c})
                    file()
                    def show():
                        u_msg.destroy()
                    u_msg = Label(password, text="Updated successfully!!..",fg="green",font=10)
                    u_msg.place(x=100, y=150)
                    password.after(2000, show)
                    v_entry.delete(0, END)
                    u_entry.delete(0, END)
                    m_entry.delete(0,END)
            else:
                def err():
                    err_msg.destroy()
                err_msg=Label(password,text="Username or Password not found*",fg="red")
                err_msg.place(x=80,y=150)
                password.after(2000,err)
                v_entry.delete(0, END)
                u_entry.delete(0, END)
                m_entry.delete(0,END)
        s_button=ttk.Button(password,text="Confirm",command=check)
        s_button.place(x=200,y=120)
        password.mainloop()
    pass_info=Label(test1,text="NOTE:\n1.If You Are a New User Kindly \nChange Your Password For Your Security purpose \n2.Other user can also change password",fg="red")
    pass_info.place(x=700,y=100)
    change_pass=ttk.Button(test1,text="Change Password",command=change_p)
    change_pass.place(y=80,x=880)
    def submit():
        global uinput
        uinput = user_input.get()
        pass1 = pass_word.get()
        if uinput in data.keys():
            if pass1 == data[uinput]:
                test1.destroy()
                instr()
            else:
                messagebox.showerror("SORRY!!...", "Incorrect Password")
                test1.destroy()
        elif uinput=="":
            messagebox.showerror("404","Kindly,Fill the username")
            test1.destroy()
        elif pass1=="":
            messagebox.showerror("404","Kindly,Fill the password")
            test1.destroy()
        else:
            messagebox.showerror("Alert", "OOPS!....Username is not found")
            test1.destroy()
    def time_checker():
        hr = time.strftime("%H")
        mm = time.strftime("%M")
        if hour == int(hr) and minute == int(mm):
            submit()
        else:
            messagebox.showinfo("Remainder","Be on time!!\nTry again later..")
    last_line = ttk.Button(test1, text="Login", command=time_checker)
    last_line.place(x=500, y=300)
    test1.mainloop()
#creating Main  page
first_page=Tk()
first_page.configure(bg="light grey")
w=1000
h=500
sw=first_page.winfo_screenwidth()
sh=first_page.winfo_screenheight()
x=(sw/2)-(w/2)
y=(sh/2)-(h/2)
first_page.geometry("%dx%d+%d+%d"%(w,h,x,y))
first_page.resizable(False,False)
first_page.title("QUIZ")
heading=Label(first_page,text="WELCOME TO QUIZ",width=30,font=("Bodoni MT Black",30),bg="sky Blue")
heading.pack(fill=X)
login_instr=Label(first_page,text="WELCOME!! To Quiz Game...\nif you are a player kindly press STUDENT LOGIN before kindly \nconform that you have register by the admin..",font=("Copperplate Gothic Bold",17))
login_instr.place(x=70,y=55)
a=ttk.Button(first_page,text="STUDENT LOGIN",command=student,width=20)#calling user_login page
a.place(x=450,y=150)
gap_msg=Label(first_page,text="OR",bg="light grey")
gap_msg.place(x=500,y=180)
b=ttk.Button(first_page,text="ADMIN LOGIN",width=20,command=Ad_Login)#calling admin_login page
b.place(x=450,y=195)
first_page.mainloop()
