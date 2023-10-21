from tkinter import *
#from tkFileDialog import askopenfilename
import pyodbc

class firstform:

    def __init__(self,name,color):
        self.name=name
        self.color=color

    def admission_top_level():
        admission_page=Toplevel()
        admission_page.title("BLW ADMISSION")
        admission_page.geometry('850x430')
        admission_page.configure(background="lightblue")

        def clear_text():
            firstname_entry.delete(0, END)
            middlename_entry.delete(0, END)
            lastname_entry.delete(0, END)
            gender_entry.delete(0, END)
            date_of_birth_entry.delete(0, END)
            contact_entry.delete(0, END)
            emailaddress_entry.delete(0, END)
            contactaddress_entry.delete(0, END)

        def window_close():
            admission_page.destroy()

        def datasubmit():
            firstnamedata = firstname_entry.get()
            middlenamedata = middlename_entry.get()
            lastnamedata = lastname_entry.get()
            genderdata = gender_entry.get()
            dateofbirthdata = date_of_birth_entry.get()
            contactdata = contact_entry.get()
            emailaddressdata = emailaddress_entry.get()
            contactaddressdata = contactaddress_entry.get()

            conn = pyodbc.connect('driver={sql server};'
                               'server=DESKTOP-6TT9F9L\JOSEPHMASSAQUOI;' 
	     		               'database=FIRSTFORM;'
			                   'Trusted_Connection=yes;')
    
            process = "execute firstform_data_entry '"+firstnamedata+"','"+middlenamedata+"','"+lastnamedata+"','"+genderdata+"','"+dateofbirthdata+"',"+contactdata+",'"+emailaddressdata+"','"+contactaddressdata+"'"
    
            firstname_entry.delete(0, END)
            middlename_entry.delete(0, END)
            lastname_entry.delete(0, END)
            gender_entry.delete(0, END)
            date_of_birth_entry.delete(0, END)
            contact_entry.delete(0, END)
            emailaddress_entry.delete(0, END)
            contactaddress_entry.delete(0, END)

            cursor=conn.cursor()
            cursor.execute(process)
            conn.commit()

        def selectpic():
            name=askopenfilename()
            print(name)
        


        #CREATING TITLE

        title=Label(admission_page,text='BLUE LIGHT WAVES ADMISSION',font='times 20 bold',bg='lightblue')
        title.place(x=75,y=5)

        #creating picture frame

        picframe=Frame(admission_page,width='170px',height='170px')
        picframe.place(x=580,y=20)

        #CREATING FRAME 1
        frame1=Frame(admission_page, width='200px',height='200px',bg='lightblue')
        frame1.place(x=70,y=50)

        firstname=Label(frame1,text="        First Name :",font='times 20 bold ',bg='lightblue')
        firstname.grid(row=1,column=0)

        firstname_entry=Entry(frame1, font='times 17 bold ' )
        firstname_entry.grid(row=1,column=1)

        middlename=Label(frame1,text="    Middle Name :",font='times 20 bold ',bg='lightblue')
        middlename.grid(row=2,column=0)

        middlename_entry=Entry(frame1, font='times 17 bold ' )
        middlename_entry.grid(row=2,column=1)

        lastname=Label(frame1,text="         Last Name :",font='times 20 bold ',bg='lightblue')
        lastname.grid(row=3,column=0)

        lastname_entry=Entry(frame1, font='times 17 bold ' )
        lastname_entry.grid(row=3,column=1)

        gender=Label(frame1,text="               Gender :",font='times 20 bold ',bg='lightblue')
        gender.grid(row=4,column=0)

        gender_entry=Entry(frame1, font='times 17 bold ' )
        gender_entry.grid(row=4,column=1)

        date_of_birth=Label(frame1,text="    Date Of Birth :",font='times 20 bold ',bg='lightblue')
        date_of_birth.grid(row=5,column=0)

        date_of_birth_entry=Entry(frame1, font='times 17 bold ' )
        date_of_birth_entry.grid(row=5,column=1)

        contact=Label(frame1,text="              Contact :",font='times 20 bold ',bg='lightblue')
        contact.grid(row=6,column=0)

        contact_entry=Entry(frame1, font='times 17 bold ' )
        contact_entry.grid(row=6,column=1)

        emailaddress=Label(frame1,text="    EmailAddress :",font='times 20 bold ',bg='lightblue')
        emailaddress.grid(row=7,column=0)

        emailaddress_entry=Entry(frame1, font='times 17 bold ' )
        emailaddress_entry.grid(row=7,column=1)

        contactaddress=Label(frame1,text="Contact Address :",font='times 20 bold ',bg='lightblue')
        contactaddress.grid(row=8,column=0)

        contactaddress_entry=Entry(frame1, font='times 17 bold ' )
        contactaddress_entry.grid(row=8,column=1)
    
        #creation of buttons

        submit=Button(admission_page,text='SUBMIT',height=2,width=15, font='times 10 bold ',bg='white',command=datasubmit)
        submit.place(x=90,y=360)

        close=Button(admission_page,text='CLOSE',height=2,width=15 ,font='times 10 bold ',bg='red',command=window_close)
        close.place(x=240,y=360)

        refresh=Button(admission_page,text='REFRESH',height=2,width=15 ,font='times 10 bold ',bg='white',command=clear_text)
        refresh.place(x=390,y=360)

        openfile=Button(admission_page,text='FILE',height=2,width=15 ,font='times 10 bold ',bg='white',command=selectpic)
        openfile.place(x=640,y=270)

        admission_page.mainloop

    def checkdata_top_level():
        checkdata_page=Toplevel()
        checkdata_page.title("BLW ADMISSION")
        checkdata_page.geometry('750x470')
        checkdata_page.configure(background="lightblue")

        def window_close():
            checkdata_page.destroy()

        def data_fetch():
            searching=Label(checkdata_page,text='Searching Please Wait...',font='times 30 bold',bg='grey')
            searching.place(x=170,y=180)
            

        #CREATING TITLE
    
        title=Label(checkdata_page,text='BLUE LIGHT WAVES CHECK DATA',font='times 20 bold',bg='lightblue')
        title.place(x=140,y=5)

        frame2=Frame(checkdata_page,height='250px',width='700', bg='grey')
        frame2.place(x=25,y=60)

        id_number2=Label(checkdata_page,text="         ID Number :",font='times 20 bold ',bg='lightblue')
        id_number2.place(x=-40,y=405)

        id_number2_entry=Entry(checkdata_page, font='times 20 bold ' )
        id_number2_entry.place(x=180,y=410)

        #CREATING BUTTONS

        check=Button(checkdata_page,text='CHECK',height=2,width=15, font='times 10 bold ',bg='lightblue',command=data_fetch)
        check.place(x=475,y=410)

        close=Button(checkdata_page,text='CLOSE',height=2,width=15, font='times 10 bold ',bg='red',command=window_close)
        close.place(x=610,y=410)

        checkdata_page.mainloop()

    def home_page(h):
        h.window=Tk()
        h.window.geometry('1150x550')
        h.window.title(h.name)
        h.window.resizable(False,False)
        h.window.configure(background=h.color)
        h.window.iconbitmap("")
        
        def window_close():
            h.window.destroy()

        #creating title
        
        #CREATING TITLE
    
        title=Label(h.window,text='BLUE LIGHT WAVES HOME PAGE',font='times 20 bold',bg='lightblue')
        title.place(x=330,y=5)
        
        #creating left frame

        leftframe=Frame(h.window,width='540px',height='250px',bg='grey')
        leftframe.place(x=10,y=50)

        #creation right frame

        rightframe=Frame(h.window,width='300px',height='250px',bg='grey')
        rightframe.place(x=740,y=50)

        #creating bottom frame

        bottomframe=Frame(h.window,width='848px',height='110px',bg='grey')
        bottomframe.place(x=10,y=393)


        #creation of buttons

        h.admission=Button(h.window,text='ADMISSION',height=2,width=15, font='times 10 bold ',bg='lightblue',command=firstform.admission_top_level)
        h.admission.place(x=600,y=475)

        h.close=Button(h.window,text='CLOSE',height=2,width=15, font='times 10 bold ',bg='red',command=window_close)
        h.close.place(x=728,y=475)

        h.refresh=Button(h.window,text='REFRESH',height=2,width=15 ,font='times 10 bold ',bg='lightblue')
        h.refresh.place(x=856,y=475)

        h.checkdata=Button(h.window,text='CHECK DATA',height=2,width=15, font='times 10 bold ',bg='lightblue',command=firstform.checkdata_top_level)
        h.checkdata.place(x=985,y=475)
        h.window.mainloop()

homepage=firstform('BLUE LIGHT WAVES FIRST FORM','lightblue')
homepage.home_page()