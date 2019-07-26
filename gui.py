from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
import time
import mysql.connector

mydb = mysql.connector.connect(host=' 127.0.0.1',
                               user='root',
                               passwd='Vagabondbrains696@',
                               database="db1")
class main():
    def __init__(self, name, startupidea, area, technology, marketibilty ,scalabilty,founders):
        self.name = name
        self.startupidea = startupidea
        self.area = area
        self.technology = technology
        self.marketibilty = marketibilty
        self.scalabilty= scalabilty
        self.founders = founders

        mycursor = mydb.cursor()

        sql = "INSERT INTO final1 (name,startupidea,area,technology,marketibilty,scalabilty,founders) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        val = (self.name, self.startupidea, self.area, self.technology,self.marketibilty,self.scalabilty,self.founders)
        mycursor.execute(sql, val)
        mydb.commit()

root = Tk()
root.geometry('1600x800+0+0')
root.title('startup evaluation')





def show_entry_fields():
    main(entry1.get(),entry2.get(),entry3.get(),entry4.get(), entry5.get(),entry6.get(),entry7.get())


def submit_entry_fields():
    f1 = Frame(root, bg='#50A7C2', relief=SUNKEN)
    f1.place(relx=0.1, rely=0.1, relwidth=0.7, relheight=0.6)
    Label(f1, text='Thankyou for the response',font="-weight bold", bg='#50A7C2', fg='black').grid(row=1, column=1)
    Button(f1, text='Next', command=proceed, bg='white', fg='black').grid(row=20, column=10)


def proceed():
    f2 = Frame(root, bg='#50A7C2', relief=SUNKEN)
    f2.place(relx=0.1, rely=0.1, relwidth=0.7, relheight=0.6)
    Label(f2, text='Processing the Data Now', font="-weight bold", bg='#50A7C2', fg='black').grid(row=5, column=5)
    Button(f2, text='Next', command=final11, bg='white', fg='black').grid(row=6, column=5)
    progressbar()


def progressbar():
        f3 = Frame(root, bg='#50A7C2', relief=SUNKEN)
        f3.place(relx=0.5, rely=0.2, relwidth=0.1, relheight=0.1)
        pb = ttk.Progressbar(f3, orient='horizontal', mode='determinate')
        pb.pack(expand=True, fill=BOTH, side=TOP)
        time.sleep(1)
        pb.start(50)


def test():
    return Label(tops, text='As you have only one cofounder you are less likely to succeed', bg='#50A7C2', font="-weight bold", fg='black').grid(row=4, column=2)



def final11():
    f4 = Frame(root, bg='#50A7C2', relief=SUNKEN)
    f4.place(relx=0.1, rely=0.1, relwidth=0.7, relheight=0.6)
    Label(f4, text='Hello %s' % entry1.get(), bg='#50A7C2',font = "-weight bold" , fg='black').grid(row=2, column=2)
    Label(f4, text='here are your results', bg='#50A7C2', font='-weight bold', fg='black').grid(row=3, column=2)
    if len(entry7.get()) == 1:
        test()
    else:
        Label(f4, text="you have  more than 1 cofounder" ,bg='#50A7C2', font='bold', fg = 'black').grid(row=4, column=2)
    Label(f4, text='your Idea that is %s' % entry2.get(), bg='#50A7C2', font="-weight bold", fg='black').grid(row=5, column=2)
    Label(f4, text='The Idea sounds interesting and also has a potential but you need to tell me more for better calculation', bg='#50A7C2', font="-weight bold", fg='black').grid(row=6,column=2)
    Label(f4, text='Now %s coming to the area, so  you are working in %s' % (entry1.get() ,entry3.get()), bg='#50A7C2', font="-weight bold", fg='black').grid(row=7,column=2)
    Label(f4, text='%s , so you are using %s' % (entry1.get(),entry4.get()), bg='#50A7C2',font="-weight bold", fg='black').grid(row=8, column=2)
    if len(entry5.get()) == 65:
        Label(f4, text='you have an ideal marketing threshold' % (entry5.get()), bg='#50A7C2',font="-weight bold", fg='black').grid(row=9, column=2)
    elif len(entry5.get()) == 'less than 65':
        Label(f4, text='Not an ideal threshold,ideal marketibilty threshold is 65' , bg='#50A7C2', font="-weight bold",fg='black').grid(row=9, column=2)
    elif len(entry5.get()) == 'more than 65':
        Label(f4, text='ideal marketibilty threshold is 65', bg='#50A7C2', font="-weight bold", fg='black').grid(row=9, column=2)
    else:
        Label(f4, text='you have put an invalid entry of marketibilty ', bg='#50A7C2', font="-weight bold", fg='black').grid(row=9,column=2)







def do_something():
    return Label(tops, text='Warning! Please fill all the details', bg='#ff7eb3', fg='black').grid(row=22, column=13)



def search():
    if len(entry1.get()) == 0:
        do_something()
    elif len(entry2.get()) == 0:
        do_something()
    elif len(entry3.get()) == 0:
        do_something()
    elif len(entry4.get()) == 0:
        do_something()
    elif len(entry5.get()) == 0:
        do_something()
    elif len(entry6.get()) == 0:
        do_something()
    elif len(entry7.get()) == 0:
        do_something()
    else:
        return submit_entry_fields()

value = ['0','1','2','3','4','5','more than 5']
value1 = lista = ['AI', 'IT', 'Healthcare', 'Food', 'Digital Marketing', 'Media' ,'Agriculture']


tops = Frame(root, bg='#ff7eb3', relief=SUNKEN)
tops.place(relx=0.1, rely=0.1, relwidth=0.7, relheight=0.6)
top1 = Frame(root, bg='#764ba2', relief=SUNKEN)
top1.place(relx=0.7, rely=0.1, relwidth=0.2, relheight=0.6)
Label(top1, text='Steps to Follow',font="-weight bold", bg='#764ba2', fg='white').grid(row=1, column=1)
labelA = Label(tops, text='CHECK YOUR SUCCESS',font="-weight bold", bg='#ff7eb3', fg='BLACK').grid(row=1, column=1)
label1 = Label(tops, text='Enter name', bg='#ff7eb3',font="-weight bold", fg='BLACK').grid(row=4, column=1)
label2 = Label(tops, text='Startup Idea', bg='#ff7eb3',font="-weight bold", fg='BLACK').grid(row=6, column=1)
label3 = Label(tops, text='Area', bg='#ff7eb3',font="-weight bold", fg='BLACK').grid(row=10, column=1)
label4 = Label(tops, text='Technology', bg='#ff7eb3',font="-weight bold", fg='BLACK').grid(row=12, column=1)
label5 = Label(tops, text='Marketibilty', bg='#ff7eb3',font="-weight bold", fg='BLACK').grid(row=16, column=1)
label6 = Label(tops, text='Scalabilty', bg='#ff7eb3',font="-weight bold", fg='BLACK').grid(row=18, column=1)
label7 = Label(tops, text='founders', bg='#ff7eb3',font="-weight bold", fg='BLACK').grid(row=20, column=1)
entry1 = Entry(tops, bg='white') #name
entry1.grid(row=4, column=2,sticky=N+S+E+W)
entry2 = Entry(tops, bg='white',width="20") #startup idea
entry2.grid(row=6, column=2,sticky=N+S+E+W)
entry3 = Combobox(tops, values= value1, height = 5)#area
entry3.grid(row=10, column=2,sticky=N+S+E+W)
entry4 = Entry(tops, bg='white')#technology
entry4.grid(row=12, column=2,sticky=N+S+E+W)
entry5 = Entry(tops, bg='white')#marketibilty
entry5.grid(row=16, column=2,sticky=N+S+E+W)
entry6 = Entry(tops, bg='white') #scalabilty
entry6.grid(row=18, column=2,sticky=N+S+E+W)
entry7 = Combobox(tops,values=value)#founders
entry7.grid(row=20, column=2,sticky=N+S+E+W)



button1 = Button(tops, text='Submit', command=lambda: [search(), show_entry_fields()], bg='WHITE', fg='black').grid(
        row=30, column=10)




if __name__ == '__main__':
    root.mainloop()
