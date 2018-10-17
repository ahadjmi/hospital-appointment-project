
from tkinter import *
import sqlite3
import tkinter.messagebox




conn = sqlite3.connect('hospital.db')

c = conn.cursor()



class app:

    def __init__(self,master):
        self.master = master

        master.title('Hospital Appointment')

        self.top = Frame(master, height=50, width=1100, bg='pink')
        self.top.place(x=0, y=0)


        self.left = Frame(master,height = 650 , width = 500, bg = 'light blue')
        self.left.place(x=600,y=50)

        self.right = Frame(master, height = 650, width = 600, bg = 'light green')
        self.right.place(x= 0 ,y=50)

        self.log = Label(self.left,text = '    Logs',fg = 'Black',font = 'arial 20 bold',bg= 'light blue')
        self.log.place(x=180, y =10)

        self.box = Text(self.left, width= 40, height = 30, font = 'Arial 12')
        self.box.place(x = 70 ,y = 70)

        #labels#############################################################################################

        self.head = Label(self.top, text='Jamia Hospital Appointments',font = 'arial 20 bold',bg='pink',fg = 'Black')
        self.head.place(x=300, y=5)

        self.name = Label(self.right,text='    Patient Name :',bg = 'light green',font = 'courier 15 bold')
        self.name.place(x=50,y=100)

        self.age = Label(self.right, text='             Age :', bg='light green', font='courier 15 bold')
        self.age.place(x=50, y=150)

        self.gender = Label(self.right, text='          Gender :', bg='light green', font='courier 15 bold')
        self.gender.place(x=50, y=200)

        self.address = Label(self.right, text='         Address :', bg='light green', font='courier 15 bold')
        self.address.place(x=50, y=250)

        self.time = Label(self.right, text='Appointment Time :', bg='light green', font='courier 15 bold')
        self.time.place(x=50, y=300)

        self.date = Label(self.right, text='Appointment Date :', bg='light green', font='courier 15 bold')
        self.date.place(x=50, y=350)

        self.mobile = Label(self.right, text='       Mobile no :', bg='light green', font='courier 15 bold')
        self.mobile.place(x=50, y=400)

        self.email = Label(self.right, text='           Email :', bg='light green', font='courier 15 bold')
        self.email.place(x=50, y=450)

        #entry##############################################################################

        self.ename = Entry(self.right,font='arial 15')
        self.ename.place(x=280,y=100)

        self.eage = Entry(self.right, font='arial 15')
        self.eage.place(x=280, y=150)

        self.egender = Entry(self.right, font='arial 15')
        self.egender.place(x=280, y=200)
        self.eaddress = Entry(self.right, font='arial 15')
        self.eaddress.place(x=280, y=250)

        self.etime = Entry(self.right, font='arial 15')
        self.etime.place(x=280, y=300)

        self.edate = Entry(self.right, font='arial 15')
        self.edate.place(x=280, y=350)

        self.emobile = Entry(self.right, font='arial 15')
        self.emobile.place(x=280, y=400)

        self.eemail = Entry(self.right, font='arial 15 ')
        self.eemail.place(x=280, y=450)

        self.add = Button(self.right,text='Submit',font ='arial 12 ',fg='black',bg='green',height =1, width = 10 , command=self.add_button)
        self.add.place(x=250, y= 530)

        self.show = Button(self.right, text='Show me', font='arial 12', fg='black',height =1,width =10, bg='grey',command=self.show_button)
        self.show.place(x=200, y=30)


        self.show = Button(self.right, text='Search', font='arial 12', fg='black', height=1, width=10, bg='blue',
                           command=self.show_search)
        self.show.place(x=50, y=30)


    def add_button(self):

        self.var1 = self.ename.get()
        self.var2 = self.eage.get()
        self.var3 = self.egender.get()
        self.var4 = self.eaddress.get()
        self.var5 = self.etime.get()
        self.var6 = self.edate.get()
        self.var7 = self.emobile.get()
        self.var8 = self.eemail.get()

        if self.var1 == '' or self.var2 == '' or self.var3 == '' or self.var4 == '' or self.var5 == '' or self.var6 == '' or self.var7 == '' or self.var8 == '':
            tkinter.messagebox.showinfo('Warning','Please fill all the entries')

        else:

            sql = "INSERT INTO Appointments (Name, Age, Gender, Address, Time, Date, Mobile, Email ) values(?,?,?,?,?,?,?,?);"
            c.execute(sql,(self.var1, self.var2, self.var3, self.var4,self.var5,self.var6,self.var7,self.var8))
            conn.commit()
            tkinter.messagebox.showinfo('Success','Appointment for ' + str(self.var1) + ' has been created')




    def show_button(self):

        self.list1=[]
        self.list2=[]
        self.list3=[]
        self.list4=[]
        self.n = 0

        sql3 = 'select Name, Mobile,Date,Time from appointments;'
        self.command = c.execute(sql3)

        for self.row in self.command:
            self.list1.append(self.row[0])
            self.list2.append(self.row[1])
            self.list3.append(self.row[2])
            self.list4.append(self.row[3])
            self.n = self.n + 1

        self.box.insert('end',f'                           Total Appointments : {self.n}' + '\n')
        for self.i in range(len(self.list1)):
            self.box.insert('end','\n' + f'     {self.i + 1}.   Name : ' + str(self.list1[self.i]) + '\n')
            self.box.insert('end', '            Time : ' + str(self.list4[self.i]) + '\n')
            self.box.insert('end', '            Date : ' + str(self.list3[self.i]) + '\n')
            self.box.insert('end', '            Mobile : ' + str(self.list2[self.i]) + '\n')
            self.box.insert('end','________________________________________' + '\n')




    def show_search(self):
        self.new=Toplevel(self.top)
        self.new.geometry('700x750')
        self.new.resizable(FALSE, FALSE)

        self.frame = Frame(self.new, bg='light blue', height=700, width=700)
        self.frame.place(x=0, y=0)

        self.heading = Label(self.frame, text='Search', font='arial 25 bold', fg='blue', bg='light blue')
        self.heading.place(x=300, y=20)

        self.pname = Label(self.frame, text='Patient Name:', font='courier 15 bold', bg='light blue')
        self.pname.place(x=80, y=80)

        self.ename2 = Entry(self.frame, font='courier 15 bold', fg='green')
        self.ename2.place(x=260, y=80)

        self.button1 = Button(self.frame, text='Search', font='arial 12 ', bg='grey', height=1, width=10,
                              command=self.search_button)
        self.button1.place(x=330, y=120)

        self.button2 = Button(self.frame, text='Exit', font='arial 12 ', bg='red', height=1, width=10,
                              command=self.exit_button)
        self.button2.place(x=50, y=20)

    def search_button(self):
        try:
            self.naam = self.ename2.get()

            sql = 'select * from appointments where Name LIKE ?'
            self.cursor = c.execute(sql, (self.naam,))

            for self.row in self.cursor:
                self.uname = self.row[0]
                self.uage = self.row[1]
                self.ugender = self.row[2]
                self.uaddress = self.row[3]
                self.utime = self.row[4]
                self.udate = self.row[5]
                self.umobile = self.row[6]
                self.uemail = self.row[7]

            self.patient = Label(self.frame, text='    Patient Name :', font='courier 15 bold', bg='light blue')
            self.patient.place(x=100, y=200)

            self.age1 = Label(self.frame, text='             Age :', font='courier 15 bold', bg='light blue')
            self.age1.place(x=100, y=250)

            self.gender1 = Label(self.frame, text='          Gender :', font='courier 15 bold', bg='light blue')
            self.gender1.place(x=100, y=300)

            self.address1 = Label(self.frame, text='         Address :', font='courier 15 bold', bg='light blue')
            self.address1.place(x=100, y=350)

            self.time1 = Label(self.frame, text='Appointment Time :', font='courier 15 bold', bg='light blue')
            self.time1.place(x=100, y=400)

            self.date1 = Label(self.frame, text='Appointment Date :', font='courier 15 bold', bg='light blue')
            self.date1.place(x=100, y=450)

            self.mobile1 = Label(self.frame, text='       Mobile no :', font='courier 15 bold', bg='light blue')
            self.mobile1.place(x=100, y=500)

            self.email1 = Label(self.frame, text='           Email :', font='courier 15 bold', bg='light blue')
            self.email1.place(x=100, y=550)

            # Entries=====================================================================================
            self.ename1 = Entry(self.frame, font='courier 15 bold', fg='green')
            self.ename1.place(x=330, y=200)
            self.ename1.insert(END, str(self.uname))

            self.eage1 = Entry(self.frame, font='courier 15 bold', fg='green')
            self.eage1.place(x=330, y=250)
            self.eage1.insert(END, str(self.uage))

            self.egender1 = Entry(self.frame, font='courier 15 bold', fg='green')
            self.egender1.place(x=330, y=300)
            self.egender1.insert(END, str(self.ugender))

            self.eaddress1 = Entry(self.frame, font='courier 15 bold', fg='green')
            self.eaddress1.place(x=330, y=350)
            self.eaddress1.insert(END, str(self.uaddress))

            self.etime1 = Entry(self.frame, font='courier 15 bold', fg='green')
            self.etime1.place(x=330, y=400)
            self.etime1.insert(END, str(self.utime))

            self.edate1 = Entry(self.frame, font='courier 15 bold', fg='green')
            self.edate1.place(x=330, y=450)
            self.edate1.insert(END, str(self.udate))

            self.emobile1 = Entry(self.frame, font='courier 15 bold', fg='green')
            self.emobile1.place(x=330, y=500)
            self.emobile1.insert(END, str(self.umobile))

            self.eemail1 = Entry(self.frame, font='courier 15 bold', fg='green')
            self.eemail1.place(x=330, y=550)
            self.eemail1.insert(END, str(self.uemail))

            self.button2 = Button(self.frame, text='Update', font='arial 12', bg='green', width=10, height=1,
                                  command=self.update_button)
            self.button2.place(x=350, y=610)

            self.button3 = Button(self.frame, text='Delete', font='arial 12', bg='orange', width=10, height=1,
                                  command=self.delete_button)
            self.button3.place(x=200, y=610)

            self.view = Button(self.frame, text='Print', font='arial 12', fg='black', height=1, width=10, bg='yellow',
                               command=self.view_button)
            self.view.place(x=50, y=610)

        except AttributeError:
            tkinter.messagebox.showinfo('Not Found', 'This patient appointment does not exist. ')

    def update_button(self):
        self.var1 = self.ename1.get()
        self.var2 = self.eage1.get()
        self.var3 = self.egender1.get()
        self.var4 = self.eaddress1.get()
        self.var5 = self.etime1.get()
        self.var6 = self.edate1.get()
        self.var7 = self.emobile1.get()
        self.var8 = self.eemail1.get()

        sql1 = 'UPDATE appointments SET Name =?, Age =?, Gender =?, Address =?, Time=?, Date=?, Mobile=?, Email=? Where Name LIKE ?'
        self.run = c.execute(sql1, (
            self.var1, self.var2, self.var3, self.var4, self.var5, self.var6, self.var7, self.var8, self.naam))
        conn.commit()
        tkinter.messagebox.showinfo('Updated', str(self.var1) + ' Appointment Successfully updated')

    def delete_button(self):
        sql2 = 'Delete from appointments where Name like ?;'

        c.execute(sql2, (self.ename2.get(),))
        conn.commit()

        self.ename1.destroy()
        self.eage1.destroy()
        self.egender1.destroy()
        self.eaddress1.destroy()
        self.etime1.destroy()
        self.edate1.destroy()
        self.emobile1.destroy()
        self.eemail1.destroy()
        tkinter.messagebox.showinfo('Deleted', str(self.ename2.get()) + ' Appointment successfully deleted.')

    def view_button(self):
        self.new2 = Toplevel(self.master)
        self.new2.geometry('700x750')

        self.box1 = Text(self.new2, width=63, height=30, font='Arial 15')
        self.box1.place(x=0, y=0)

        self.nam = self.ename2.get()

        sql4 = 'select * from appointments where Name LIKE ?'
        self.cursor1 = c.execute(sql4, (self.nam,))

        for self.row in self.cursor1:
            self.sname = self.row[0]
            self.sage = self.row[1]
            self.sgender = self.row[2]
            self.saddress = self.row[3]
            self.stime = self.row[4]
            self.sdate = self.row[5]
            self.smobile = self.row[6]
            self.semail = self.row[7]

        self.box1.insert(END, '\n                                          Appointment Letter \n \n ')
        self.box1.insert(END, '\n \n        ' + str(self.sname))
        self.box1.insert(END,
                         '\n\n        ' + str(self.saddress) + '\n        ' + str(self.smobile) + '\n        ' + str(
                             self.semail))

        if self.sgender == 'Male':
            self.box1.insert(END, '\n \n \n       Dear Mr ' + str(self.sname))

        else:
            self.box1.insert(END, '\n \n \n       Dear Mrs ' + str(self.sname))
        self.box1.insert(END,
                         '\n \n             Your Appointment has been confirmed on date ' + str(self.sdate) + ' at '
                         + str(self.stime))
        self.box1.insert('end',
                         '\n             Please visit at hospital before one hour from the time given by doctor \n '
                         '            and also visit  with at least one family member for support.')
        self.box1.insert('end', '\n             for any query feel free to contact us.  \n\n             Thank you  \n')
        self.box1.insert('end', '\n             Appointment Time : ' + str(self.stime))
        self.box1.insert('end', '\n             Appointment Date : ' + str(self.sdate))
        self.box1.insert('end', '\n             Contact Number : 02262345672')
        self.box1.insert('end',
                         '\n             Email ID : jamiahospital@hotmail.com \n\n          your sincerely \n          ......................')

    def exit_button(self):
        self.new.destroy()






room = Tk()

app(room)
room.geometry('1100x750')
room.resizable(FALSE, FALSE)

room.mainloop()