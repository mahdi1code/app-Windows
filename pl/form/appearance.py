from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from dal.Repository import *
from be.clinic import *
from bll.operationsRPS import operations
from datetime import datetime

class App(Frame):
    def __init__(self,screen):
        super().__init__(screen)
        self.master = screen

        self.CreateWidgets()

    def CreateWidgets(self):

        self.frm_1=Frame(self.master,width=900,height=400)
        self.frm_1.place(x=0,y=0)

        self.frm_2 = Frame(self.master, width=900, height=400)
        self.frm_2.place(x=0,y=0)

        self.frm_3 = Frame(self.master, width=900, height=400)
        self.frm_3.place(x=0,y=0)

        self.frm_4 = Frame(self.master, width=900, height=400)
        self.frm_4.place(x=0,y=0)

        self.frm_5 = Frame(self.master, width=900, height=400, background="#575151")
        self.frm_5.place(x=0, y=0)

        self.frm_6 = Frame(self.master, width=900, height=400)
        self.frm_6.place(x=0, y=0)

        self.frm_7=Frame(self.master, width=900, height=400)
        self.frm_7.place(x=0,y=0)

        self.Hidefrm_All()
        self.Showfrm_1()

        self.Picturebg=PhotoImage(file="IMG/Picturebg.png")
        self.Picturebg_1=PhotoImage(file="IMG/Picturebg_1.png")
        self.Picturebg_2=PhotoImage(file="IMG/Picturebg_2.png")
        self.Picturebg_3=PhotoImage(file="IMG/Picturebg_3.png")
        self.Picturebg_4=PhotoImage(file="IMG/Picturebg_4.png")
        self.Picturebg_5 = PhotoImage(file="IMG/Picturebg_5.png")

        self.Menubar=Menu(self.master)
        self.UserMenu=Menu(self.Menubar, tearoff=0, background="Black")
        self.UserMenu.add_command(label="ثبت بیماران", command=self.OnClick)
        self.UserMenu.add_separator()
        self.UserMenu.add_command(label="تجویزدارو", command=self.OnClick_1)
        self.UserMenu.add_separator()
        self.UserMenu.add_command(label="ثبت تداخلات دارویی", command=self.OnClick_2)
        self.UserMenu.add_separator()
        self.UserMenu.add_command(label="نوبت دهی", command=self.OnClick_3)
        self.UserMenu.add_separator()
        self.UserMenu.add_command(label="سرپرست", command=self.OnClick_4)
        self.Menubar.add_cascade(label="منو", menu=self.UserMenu)
        self.UserMenu.configure(background="Black",foreground="white")
        self.master.config(menu=self.Menubar)




        self.lblbg = Label(self.frm_1, text="*", image=self.Picturebg).place(x=0, y=0)
        self.lblbg_1 = Label(self.frm_2, text="*", image=self.Picturebg_1).place(x=0, y=0)
        self.lblbg_2 = Label(self.frm_3, text="*", image=self.Picturebg_2).place(x=0, y=0)
        self.lblbg_3 = Label(self.frm_4, text="*", image=self.Picturebg_3).place(x=0, y=0)
        self.lblbg_4 = Label(self.frm_6, text="*", image=self.Picturebg_4).place(x=0, y=0)
        self.lblbg_5= Label(self.frm_7, text="*", image=self.Picturebg_5).place(x=0,y=0)

#############################################################frm_1
        self.jun=IntVar()
        self.textIDfrm1= IntVar()
        self.Codenationalfrm1 = StringVar()

        self.textIDfrm1=Entry(self.frm_1, textvariable=self.textIDfrm1)
        self.lbl = Label(self.frm_1, text="آیا بیمار قبلا ثبت نام شده؟", bg="#87a7dc" ,font="nazanin 15 bold ").place(x=400, y=50)
        self.RED_1=Radiobutton(self.frm_1, text="آره", variable=self.jun, value=1, command=self.toshow)
        self.RED_1.place(x=400,y=100)
        self.RED_2 = Radiobutton(self.frm_1, text="نه", variable=self.jun, value=2, command=self.toshow)
        self.RED_2.place(x=450, y=100)
        self.btnSearch_1=ttk.Button(self.frm_1, text="جستجو",command=self.Searchfrm1)
        self.btnSearch_1.place_forget()
        self.textSearch1=Entry(self.frm_1, bg="#87a7dc", textvariable=self.Codenationalfrm1)
        self.textSearch1.place_forget()
        self.tbl_3 = ttk.Treeview(self.frm_1, columns=("c1", "c2", "c3", "c4", "c5", "c6", "c7"), show="headings")
        self.tbl_3.heading("# 7", text="شماره")
        self.tbl_3.column("# 7", width=50)
        self.tbl_3.heading("# 6", text="نام")
        self.tbl_3.column("# 6", width=100)
        self.tbl_3.heading("# 5", text="فامیل")
        self.tbl_3.column("# 5", width=100)
        self.tbl_3.heading("# 4", text="کدملی")
        self.tbl_3.column("# 4", width=100)
        self.tbl_3.heading("# 3", text="سابقه بیماری")
        self.tbl_3.column("# 3", width=100)
        self.tbl_3.heading("# 2", text="سن")
        self.tbl_3.column("# 2", width=50)
        self.tbl_3.heading("# 1", text="دارو مصرفی")
        self.tbl_3.column("# 1", width=100)
        #self.tbl.bind("<Button-1>", self.GetSelction)
        self.tbl_3.place_forget()

##############################################################################frm_2
        self.Id = IntVar()
        self.Namepatient = StringVar()
        self.Famyli = StringVar()
        self.Codenational= StringVar()
        self.diseasebackground = StringVar()
        self.Age = StringVar()
        self.Consumabledrugs = StringVar()
        self.que = StringVar()


        self.textId=Entry(self.frm_2,textvariable=self.Id, justify="center").place_forget()
        self.btn_1 = ttk.Button(self.frm_2, text="ثبت بیمار", command=self.SavePatient).place(x=825, y=0)
        self.btn_Search =ttk.Button(self.frm_2, text="جستجو", command=self.Search)
        self.btn_Search.place_forget()
        self.text_NameSearch = Entry(self.frm_2, bg="#5f6368", fg="#f1f3f4", justify="center", textvariable=self.que).place(x=700, y=220)
        self.btn_Delet=ttk.Button(self.frm_2, text="حذف", command=self.DeleteLine)
        self.btn_Delet.place_forget()
        self.btn_Edit=ttk.Button(self.frm_2, text="ویرایش", command=self.EDIT)
        self.btn_Edit.place_forget()
        self.lbl_text = Label(self.frm_2, text="نام", bg="#0ecac9")
        self.lbl_text.place(x=875, y=40)
        self.text_Name= Entry(self.frm_2, bg="#5f6368", justify="center", fg="#f1f3f4", textvariable=self.Namepatient)
        self.text_Name.place(x=700, y=40)
        self.lbl_text = Label(self.frm_2, text="فامیل", bg="#0ecac9" ).place(x=860, y=70)
        self.text_Famyli = Entry(self.frm_2, bg="#5f6368", justify="center", fg="#f1f3f4", textvariable=self.Famyli)
        self.text_Famyli.place(x=700, y=70)
        self.lbl_text = Label(self.frm_2, text="ثابقه بیماری", bg="#0ecac9").place(x=830, y=100)
        self.text_diseasebackground = Entry(self.frm_2, bg="#5f6368", justify="center", fg="#f1f3f4", textvariable=self.diseasebackground)
        self.text_diseasebackground.place(x=700, y=100)
        self.lbl_text = Label(self.frm_2, text="سن", bg="#0ecac9").place(x=870, y=130)
        self.text_Age = Entry(self.frm_2, bg="#5f6368", justify="center", fg="#f1f3f4", textvariable=self.Age)
        self.text_Age.place(x=700, y=130)
        self.lbl_text = Label(self.frm_2, text="دارو مصرفی", bg="#0ecac9").place(x=830, y=160)
        self.text_Consumabledrugs=Entry(self.frm_2, bg="#5f6368", justify="center", fg="#f1f3f4",textvariable=self.Consumabledrugs)
        self.text_Consumabledrugs.place(x=700, y=160)
        self.NationalCode=Label(self.frm_2, text="کدملی", bg="#0ecac9").place(x=860,y=190)
        self.text_NationalCode=Entry(self.frm_2, bg="#5f6368", justify="center", fg="#f1f3f4", textvariable=self.Codenational)
        self.text_NationalCode.place(x=700,y=190)
        self.tbl = ttk.Treeview(self.frm_2, columns=("c1", "c2", "c3", "c4", "c5", "c6", "c7"), show="headings", height=9)
        self.tbl.heading("# 7", text="شماره")
        self.tbl.column("# 7", width=50)
        self.tbl.heading("# 6", text="نام")
        self.tbl.column("# 6", width=100)
        self.tbl.heading("# 5", text="فامیل")
        self.tbl.column("# 5", width=100)
        self.tbl.heading("# 4", text="کدملی")
        self.tbl.column("# 4", width=100)
        self.tbl.heading("# 3", text="سابقه بیماری")
        self.tbl.column("# 3", width=100)
        self.tbl.heading("# 2", text="سن")
        self.tbl.column("# 2", width=50)
        self.tbl.heading("# 1", text="دارو مصرفی")
        self.tbl.column("# 1", width=100)
        self.tbl.bind("<Button-1>", self.GetSelction)
        self.tbl.place(x=0, y=0)

#####################################################################################frm_3
        self.jens=IntVar()
        self.Id_1=IntVar()
        self.Name = StringVar()
        self.medicinename = StringVar()
        self.Alternativemedicine = StringVar()
        self.Drugform = StringVar()
        self.que_1 = StringVar()

        self.textid_1 = Entry(self.frm_3, textvariable=self.Id_1, justify="center").place_forget()
        self.btn_2 = ttk.Button(self.frm_3, text="ثبت نسخه", command=self.Saveprescription).place(x=820, y=0)
        self.btn_Search_1 = ttk.Button(self.frm_3, text="جستجو", command= self.Search_1)
        self.btn_Search_1.place_forget()
        self.text_NameSearch_1 = Entry(self.frm_3, bg="#5f6368", fg="#f1f3f4", justify="center", textvariable=self.que_1).place(x=680, y=160)
        self.btn_Delet_1 = ttk.Button(self.frm_3, text="حذف", command=self.DeleteLine_1)
        self.btn_Delet_1.place_forget()
        self.btn_Edit_1 = ttk.Button(self.frm_3, text="ویرایش", command=self.EDIT_1)
        self.btn_Edit_1.place_forget()
        self.lbl_1 = Label(self.frm_3, text="نام دارو (فارسی)" ).place(x=820, y=40)
        self.text_Name1 = Entry(self.frm_3, bg="#5f6368", justify="center", fg="#f1f3f4", textvariable=self.Name)
        self.text_Name1.place(x=680, y=40)
        self.lbl_2 = Label(self.frm_3, text="نام دارو (انگلیسی)").place(x=810, y=70)
        self.text_medicinename= Entry(self.frm_3, bg="#5f6368", justify="center", fg="#f1f3f4", textvariable=self.medicinename)
        self.text_medicinename.place(x=680, y=70)
        self.lbl_3 = Label(self.frm_3, text="داروی جایگزین").place(x=820, y=100)
        self.text_Alternativemedicine = Entry(self.frm_3, bg="#5f6368", justify="center", fg="#f1f3f4", textvariable=self.Alternativemedicine )
        self.text_Alternativemedicine.place(x=680,y=100)
        self.lbl_4 = Label(self.frm_3, text="شکل دارو").place(x=840, y=130)
        self.text_Drugform = ttk.Combobox(self.frm_3, values=["قرص", "کپسول", "شربت", "سرم", "آمپول", "شیافت"],state="readonly",justify="center", textvariable=self.Drugform)
        self.text_Drugform.place(x=660, y=130)
        #self.lbl_5 = Label(self.frm_3, text="آیا ثابقه مصرف دارو دارید").place(x=700, y=180)
        #self.redo_5=Radiobutton(self.frm_3, text="بله", variable=self.jens, value=1).place(x=650,y=180)
        #self.redo_5=Radiobutton(self.frm_3, text="خیر", variable=self.jens, value=2).place(x=600,y=180)
        #self.text_Age = Entry(self.frm_3, bg="#5f6368", justify="center", fg="#f1f3f4").place(x=740, y=130)
        #self.lbl_text = Label(self.frm_3, text="دارو مصرفی").place(x=830, y=160)
        #self.text_Consumabledrugs = Entry(self.frm_3, bg="#5f6368", justify="center", fg="#f1f3f4").place(x=700, y=160)
        self.tbl_1 = ttk.Treeview(self.frm_3, columns=("c1", "c2", "c3", "c4", "c5"), show="headings")
        self.tbl_1.heading("# 5", text="شماره")
        self.tbl_1.column("# 5", width=50)
        self.tbl_1.heading("# 4", text="نام دارو (فارسی)")
        self.tbl_1.column("# 4", width=100)
        self.tbl_1.heading("# 3", text="نام دارو (انگلیسی)")
        self.tbl_1.column("# 3", width=100)
        self.tbl_1.heading("# 2", text="داروی جایگزین")
        self.tbl_1.column("# 2", width=100)
        self.tbl_1.heading("# 1", text="شکل دارو")
        self.tbl_1.column("# 1", width=100)
        self.tbl_1.bind("<Button-1>", self.GetSelction_1)
        self.tbl_1.place(x=0, y=0)



######################################################################frm_4
        self.Id_2 = IntVar()
        self.nomdumédicament = StringVar()
        self.Itinterfereswith = StringVar()
        self.AlternativeMedizin = StringVar()
        self.Theintensityoftheinterference = StringVar()
        self.que_2 = StringVar()


        self.textId_2=Entry(self.frm_4, textvariable=self.Id_2, justify="center").place_forget()
        self.btn_2 = ttk.Button(self.frm_4, text="ثبت تداخلات", command=self.SaveInterferences)
        self.btn_2.place(x=825, y=0)
        self.btn_Search_2 = ttk.Button(self.frm_4, text="جستجو", command=self.Search_2)
        self.btn_Search_2.place_forget()
        self.text_NameSearch_2 = ttk.Entry(self.frm_4, justify="center", textvariable=self.que_2).place(x=690, y=160)
        self.btn_Delet_2 = ttk.Button(self.frm_4, text="حذف", command=self.DeleteLine_2)
        self.btn_Delet_2.place_forget()
        self.btn_Edit_2 = ttk.Button(self.frm_4, text="ویرایش", command=self.EDIT_2)
        self.btn_Edit_2.place_forget()
        self.lbl_1 = ttk.Label(self.frm_4, text=": نام دارو (فارسی) ").place(x=810, y=40)
        self.text_nomdumédicament = ttk.Entry(self.frm_4, justify="center", textvariable= self.nomdumédicament)
        self.text_nomdumédicament.place(x=690, y=40)
        self.lbl_2 = ttk.Label(self.frm_4, text=": تداخل داردبا").place(x=830, y=70)
        self.text_Itinterfereswith = ttk.Entry(self.frm_4, justify="center", textvariable=self.Itinterfereswith)
        self.text_Itinterfereswith.place(x=690, y=70)
        self.lbl_3 = ttk.Label(self.frm_4, text=": داروی جایگزین").place(x=820, y=100)
        self.text_AlternativeMedizin = ttk.Entry(self.frm_4, justify="center" , textvariable=self.AlternativeMedizin)
        self.text_AlternativeMedizin.place(x=690, y=100)
        self.lbl_4 = ttk.Label(self.frm_4, text=": شدت تداخل").place(x=830, y=130)
        self.text_Theintensityoftheinterference = ttk.Combobox(self.frm_4, values=["کم", "متوسط", "زیاد"], state="readonly", justify="center", textvariable=self.Theintensityoftheinterference)
        self.text_Theintensityoftheinterference.place(x=680, y=130)
        self.tbl_2 = ttk.Treeview(self.frm_4, columns=("c1", "c2", "c3", "c4", "c5"), show="headings")
        self.tbl_2.heading("# 5", text="شماره")
        self.tbl_2.column("# 5", width=100)
        self.tbl_2.heading("# 4", text="نام دارو (فارسی)")
        self.tbl_2.column("# 4", width=100)
        self.tbl_2.heading("# 3", text="تداخل داردبا")
        self.tbl_2.column("# 3", width=100)
        self.tbl_2.heading("# 2", text="داروی جایگزین")
        self.tbl_2.column("# 2", width=100)
        self.tbl_2.heading("# 1", text="شدت تداخل")
        self.tbl_2.column("# 1", width=100)
        self.tbl_2.bind("<Button-1>", self.GetSelction_2)
        self.tbl_2.place(x=0, y=0)
        self.btnclos = ttk.Button(self.master, text="بستن", command=self.Close).place(x=820, y=375)
        self.btnReturn = ttk.Button(self.master, text="برگشت", command=self.Return).place(x=750, y=375)
#####################################################################################################################################frm_5

        self.Codenational_turn = StringVar()
        self.patientname_turn = StringVar()
        self.patientFamyli_turn = StringVar()
        self.appointmentdate= StringVar()
        self.turntime= StringVar()
        self.textSearch= StringVar()
        self.textId3_turn= IntVar()

        self.textId_3=Entry(self.frm_5, textvariable=self.textId3_turn).place_forget()
        self.lbl_turn1=Label(self.frm_5, text="نام بیمار", bg="#575151", fg="#fff").place(x=800,y=50)
        self.text_turn1=Entry(self.frm_5, bg="#5f6368", fg="#000", justify="center", textvariable=self.patientname_turn)
        self.text_turn1.place(x=670,y=50)
        self.lbl_turn2=Label(self.frm_5, text="فامیل بیمار", bg="#575151", fg="#fff").place(x=800,y=80)
        self.text_turn2 = Entry(self.frm_5, bg="#5f6368", fg="#000", justify="center", textvariable=self.patientFamyli_turn )
        self.text_turn2.place(x=670, y=80)
        self.lbl_turn3 = (Label(self.frm_5, text="کدملی بیمار", bg="#575151", fg="#fff").place(x=800, y=110))
        self.text_turn3 = Entry(self.frm_5, bg="#5f6368", fg="#000", justify="center", textvariable=self.Codenational_turn)
        self.text_turn3.place(x=670, y=110)
        self.lbl_turn4 = Label(self.frm_5, text="تاریخ توبت", bg="#575151", fg="#fff").place(x=800, y=140)
        self.text_turn4 =Entry(self.frm_5, bg="#5f6368", fg="#000", justify="center", textvariable=self.appointmentdate)
        self.text_turn4.place(x=670, y=140)
        self.lbl_turn5 = Label(self.frm_5, text="ساعت نوبت", bg="#575151", fg="#fff").place(x=800, y=170)
        self.text_turn5 =Entry(self.frm_5, bg="#5f6368", fg="#000", justify="center", textvariable=self.turntime)
        self.text_turn5.place(x=670, y=170)
        self.btn_turn1=Button(self.frm_5, text="ثبت نوبت", bg="#5f6368", command=self.SaveTurn)
        self.btn_turn1.place(x=300, y=250)
        self.btn_turn2=Button(self.frm_5, text="حذف", bg="#5f6368", command=self.DeleTurn)
        self.btn_turn2.place(x=260,y=250)
        self.btn_turn3=Button(self.frm_5, text="ویرایش", bg="#5f6368", command=self.EditTrun)
        self.btn_turn3.place(x=210,y=250)
        self.btn_turn4=Button(self.frm_5, text="جستجو", bg="#5f6368", command=self.SearchTrun)
        self.btn_turn4.place(x=300,y=280)
        self.text_turn6=Entry(self.frm_5, bg="#5f6368", fg="#000", justify="center", textvariable= self.textSearch)
        self.text_turn6.place(x=170,y=280)
        self.tbl_4=ttk.Treeview(self.frm_5, columns=("c1","c2","c3","c4","c5","c6") ,show="headings")
        self.tbl_4.heading("# 6", text="شماره")
        self.tbl_4.column("# 6", width=50)
        self.tbl_4.heading("# 5", text="نام بیمار")
        self.tbl_4.column("# 5", width=50)
        self.tbl_4.heading("# 4", text="فامیل بیمار")
        self.tbl_4.column("# 4", width=70)
        self.tbl_4.heading("# 3", text="کدملی")
        self.tbl_4.column("# 3", width=100)
        self.tbl_4.heading("# 2", text="تاریخ نوبت")
        self.tbl_4.column("# 2", width=100)
        self.tbl_4.heading("# 1", text="ساعت نوبت")
        self.tbl_4.column("# 1", width=100)
        self.tbl_4.bind("<Button-1>", self.GetSelction_turn)
        self.tbl_4.place(x=100,y=10)

##############################################################################################frm_6

        self.DoctorName= StringVar()
        self.FamilyDoctor=StringVar()
        self.DoctorExpertise=StringVar()
        self.PersonnelCode=StringVar()
        self.textDserch= StringVar()
        self.ID_D=IntVar()

        self.textDID=Entry(self.frm_6, textvariable=self.ID_D).place_forget()
        self.lblD_1=Label(self.frm_6, text="نام پزشک", fg="#575151").place(x=850,y=0)
        self.textD_1=Entry(self.frm_6, bg="#5f6368", justify="center", textvariable=self.DoctorName)
        self.textD_1.place(x=670,y=0)
        self.lblD_2 = Label(self.frm_6, text="فامیل پزشک", fg="#575151").place(x=830, y=40)
        self.textD_2 = Entry(self.frm_6, bg="#5f6368", justify="center", textvariable=self.FamilyDoctor)
        self.textD_2.place(x=670, y=40)
        self.lbl_3=Label(self.frm_6, text="تخصص پزشک", fg="#575151").place(x=820,y=80)
        self.textD_3=Entry(self.frm_6, bg="#5f6368", justify="center", textvariable=self.DoctorExpertise)
        self.textD_3.place(x=670,y=80)
        self.lbl_4=Label(self.frm_6, text="کدپرسنلی پزشک", fg="#575151").place(x=810,y=120)
        self.textD_4=Entry(self.frm_6, bg="#5f6368", justify="center", textvariable=self.PersonnelCode)
        self.textD_4.place(x=670,y=120)
        self.btnD=ttk.Button(self.frm_6, text="ثبت پزشک", command=self.SaveDoctor)
        self.btnD.place(x=580,y=0)
        self.btnD_1=ttk.Button(self.frm_6, text="حذف", command=self.DeleteLine_Doctor)
        self.btnD_1.place_forget()
        self.btnD_2=ttk.Button(self.frm_6, text="ویرایش", command=self.EDIT_Doctor)
        self.btnD_2.place_forget()
        self.btnD_3=ttk.Button(self.frm_6, text="جستجو", command=self.search_D)
        self.btnD_3.place(x=580,y=111)
        self.textD_5=Entry(self.frm_6, bg="#5f6368", justify="center", textvariable=self.textDserch)
        self.textD_5.place(x=450,y=115)
        self.tbl_D=ttk.Treeview(self.frm_6, columns=("c1","c2","c3","c4","c5") ,show="headings")
        self.tbl_D.heading("# 5", text="شماره")
        self.tbl_D.column("# 5", width=50)
        self.tbl_D.heading("# 4", text="نام پزشک")
        self.tbl_D.column("# 4", width=100)
        self.tbl_D.heading("# 3", text="فامیل پزشک")
        self.tbl_D.column("# 3", width=100)
        self.tbl_D.heading("# 2", text="تخصص پزشک")
        self.tbl_D.column("# 2", width=100)
        self.tbl_D.heading("# 1", text="کدپرسنلی")
        self.tbl_D.column("# 1", width=100)
        self.tbl_D.bind("<Button-1>", self.GetSelction_D)
        self.tbl_D.place(x=450,y=140)
######################################################################frm_7

        self.username= StringVar()
        self.password= StringVar()

        self.lblSRP=Label(self.frm_7, text="ورود به پنل سرپرست", font=("Helvetica", 30)).place(x=500,y=50)
        self.textSRPL=Label(self.frm_7, text="نام کاربری").place(x=730,y=150)
        self.textSRP=Entry(self.frm_7, justify="right", textvariable=self.username)
        self.textSRP.place(x=600,y=150)
        self.textSRPL1 =Label(self.frm_7, text="رمزعبور").place(x=730,y=200)
        self.textSRP_1=Entry(self.frm_7, justify="right", textvariable=self.password)
        self.textSRP_1.place(x=600,y=200)
        self.btnSRP=ttk.Button(self.frm_7, text="واردشدن", command=self.SeveEnter)
        self.btnSRP.place(x=630,y=250)

    def Hidefrm_1(self):
        self.frm_1.place_forget()

    def Showfrm_1(self):
        self.Hidefrm_All()
        self.frm_1.place(x=0, y=0)

    def Hidefrm_2(self):
        self.frm_2.place_forget()

    def Showfrm_2(self):
        self.Hidefrm_All()
        self.frm_2.place(x=0, y=0)

    def Hidefrm_3(self):
        self.frm_3.place_forget()

    def Showfrm_3(self):
        self.Hidefrm_All()
        self.frm_3.place(x=0, y=0)

    def Hidefrm_4(self):
        self.frm_4.place_forget()

    def Showfrm_4(self):
        self.Hidefrm_All()
        self.frm_4.place(x=0, y=0)

    def Hidefrm_5(self):
        self.frm_5.place_forget()

    def Showfrm_5(self):
        self.Hidefrm_All()
        self.frm_5.place(x=0, y=0)

    def Hidefrm_6(self):
        self.frm_5.place_forget()

    def Showfrm_6(self):
        self.Hidefrm_All()
        self.frm_6.place(x=0, y=0)

    def Hidefrm_7(self):
        self.frm_7.place_forget()

    def Showfrm_7(self):
        self.Hidefrm_All()
        self.frm_7.place(x=0, y=0)


    def Hidefrm_All(self):
        self.frm_1.place_forget()
        self.frm_2.place_forget()
        self.frm_3.place_forget()
        self.frm_4.place_forget()
        self.frm_5.place_forget()
        self.frm_6.place_forget()
        self.frm_7.place_forget()
    def OnClick(self):
        self.Showfrm_2()
        self.Delet()
        self.Lod()
        self.btn_Search.place(x=830, y=220)

    def OnClick_1(self):
        self.Showfrm_3()
        self.Delet_1()
        self.Lod_1()
        self.btn_Search_1.place(x=820, y=160)

    def OnClick_2(self):
        self.Showfrm_4()
        self.Delet_2()
        self.Lod_2()
        self.btn_Search_2.place(x=830, y=160)
    def OnClick_3(self):
        self.Showfrm_5()
        self.Delet_3()
        self.Lod_3()

    def OnClick_4(self):
        self.Showfrm_7()
        self.Delet_4()
        self.Lod_4()

    def GetSelction(self,e=[]):
        self.selection_row = self.tbl.selection()
        self.btn_Edit.place(x=200, y=230)
        self.btn_Delet.place(x=300, y=230)
        if self.selection_row != ():
            self.Namepatient.set(self.tbl.item(self.selection_row)["values"][5])
            self.Famyli.set(self.tbl.item(self.selection_row)["values"][4])
            (self.Codenational.set(self.tbl.item(self.selection_row)["values"][3]))
            self.diseasebackground.set(self.tbl.item(self.selection_row)["values"][2])
            self.Age.set(self.tbl.item(self.selection_row)["values"][1])
            self.Consumabledrugs.set(self.tbl.item(self.selection_row)["values"][0])
            self.Id.set(self.tbl.item(self.selection_row)["values"][6])

    def GetSelction_1(self, e=[]):
        self.selection_row = self.tbl_1.selection()
        self.btn_Edit_1.place(x=200, y=230)
        self.btn_Delet_1.place(x=300, y=230)
        if self.selection_row != ():
            self.Name.set(self.tbl_1.item(self.selection_row)["values"][3])
            self.medicinename.set(self.tbl_1.item(self.selection_row)["values"][2])
            self.Alternativemedicine.set(self.tbl_1.item(self.selection_row)["values"][1])
            self.Drugform.set(self.tbl_1.item(self.selection_row)["values"][0])
            self.Id_1.set(self.tbl_1.item(self.selection_row)["values"][4])

    def GetSelction_2(self, e=[]):
        self.selection_row = self.tbl_2.selection()
        self.btn_Edit_2.place(x=200, y=230)
        self.btn_Delet_2.place(x=300, y=230)
        if self.selection_row != ():
            self.nomdumédicament.set(self.tbl_2.item(self.selection_row)["values"][3])
            self.Itinterfereswith.set(self.tbl_2.item(self.selection_row)["values"][2])
            self.AlternativeMedizin.set(self.tbl_2.item(self.selection_row)["values"][1])
            self.Theintensityoftheinterference.set(self.tbl_2.item(self.selection_row)["values"][0])
            self.Id_2.set(self.tbl_2.item(self.selection_row)["values"][4])

    def GetSelction_turn(self, e=[]):
        self.selection_row = self.tbl_4.selection()
        if self.selection_row !=():
            self.patientname_turn.set(self.tbl_4.item(self.selection_row)["values"][4])
            self.patientFamyli_turn.set(self.tbl_4.item(self.selection_row)["values"][3])
            self.Codenational_turn.set(self.tbl_4.item(self.selection_row)["values"][2])
            self.appointmentdate.set(self.tbl_4.item(self.selection_row)["values"][1])
            self.turntime.set(self.tbl_4.item(self.selection_row)["values"][0])
            self.textId3_turn.set(self.tbl_4.item(self.selection_row)["values"][5])


    def GetSelction_D(self, e=[]):
        self.selection_row = self.tbl_D.selection()
        self.btnD_1.place(x=510,y=0)
        self.btnD_2.place(x=440,y=0)
        if self.selection_row !=():
            self.DoctorName.set(self.tbl_D.item(self.selection_row)["values"][3])
            self.FamilyDoctor.set(self.tbl_D.item( self.selection_row)["values"][2])
            self.DoctorExpertise.set(self.tbl_D.item(self.selection_row)["values"][1])
            self.PersonnelCode.set(self.tbl_D.item(self.selection_row)["values"][0])
            self.ID_D.set(self.tbl_D.item(self.selection_row)["values"][4])
    def SavePatient(self):
        if self.Namepatient.get() =="":
            self.text_Name.focus_set()
            messagebox.showerror("خطا","نام را پر کنید")
        elif self.Famyli.get() =="":
            self.text_Famyli.focus_set()
            messagebox.showerror("توجه"," لطفا فامیل را پر کنید")
        elif self.diseasebackground.get()=="":
            self.text_diseasebackground.focus_set()
            messagebox.showerror("توجه","ثابقه بیماری را پر کنید")
        elif self.Age.get().isdigit()==FALSE :
            self.text_Age.focus_set()
            messagebox.showerror("توجه","لطفا سن راعددی پر کنید")
        elif self.Consumabledrugs.get()=="":
            self.text_Consumabledrugs.focus_set()
            messagebox.showerror("توجه","لطفا داروی مصرفی را پر کنید")
        elif self.Codenational.get().isdigit()==FALSE:
            self.text_NationalCode.focus_set()
            messagebox.showerror("توجه","لطفا کدملی راعددی پر کنید")

        else:
            self.tbl.insert('',"end", values=(self.Consumabledrugs.get(), self.Age.get(), self.diseasebackground.get(), self.Codenational.get(),self.Famyli.get(), self.Namepatient.get()))
            self.obj=patients(self.Namepatient.get(), self.Famyli.get(), self.diseasebackground.get(), self.Consumabledrugs.get(), self.Age.get(), self.Codenational.get())
            self.oprts=operations()
            self.oprts.Add(self.obj)
            self.Delet()
            self.Lod()


           # self.quest.set("")

    def Saveprescription(self):
        if self.Name.get() == "":
            self.text_Name1.focus_set()
            messagebox.showerror("توجه","لطفا نام را پر کنید")
        elif self.medicinename.get() == "":
            self.text_medicinename.focus_set()
            messagebox.showerror("توجه","لطفا نام رابه انگلیسی پر کنید")
        elif self.Alternativemedicine.get() == "":
            self.text_Alternativemedicine.focus_set()
            messagebox.showerror("توجه","لطفا دارو جایگزین را پر کنید")
        elif self.Drugform.get() =="":
            self.text_Drugform.focus_set()
            messagebox.showerror("توجه","لطفا شکل دارو رو انتخاب کنید")

        else:
            self.tbl_1.insert('', 'end', values=(self.Drugform.get(), self.Alternativemedicine.get(), self.medicinename.get(), self.Name.get()))
            self.obj_1 = prescription(self.Name.get(), self.medicinename.get(), self.Alternativemedicine.get(),self.Drugform.get())
            self.oprts = operations()
            self.oprts.Add(self.obj_1)
            self.Delet_1()
            self.Lod_1()

    def SaveInterferences(self):
        if self.nomdumédicament.get() =="":
            self.text_nomdumédicament.focus_set()
            messagebox.showerror("توجه","نام را پر کنید")
        elif self.Itinterfereswith.get() =="":
            self.text_Itinterfereswith.focus_set()
            messagebox.showerror("توجه","تداخل رو پر کنید")
        elif self.AlternativeMedizin.get() =="":
            self.text_AlternativeMedizin.focus_set()
            messagebox.showerror("توجه","داروی جایگزین راپر کنید")
        elif self.Theintensityoftheinterference.get() =="":
            self.text_Theintensityoftheinterference.focus_set()
            messagebox.showinfo("توجه","لطفا فیلد را پر کنید")

        else:
            self.tbl_2.insert('', "end", values=(self.Theintensityoftheinterference.get(), self.AlternativeMedizin.get(), self.Itinterfereswith.get(),self.nomdumédicament.get()))
            obj_2 = Druginteractions(self.nomdumédicament.get(), self.Itinterfereswith.get(),self.AlternativeMedizin.get(), self.Theintensityoftheinterference.get())
            self.oprts = operations()
            self.oprts.Add(obj_2)
            self.Delet_2()
            self.Lod_2()

    def SaveTurn(self):
        if self.patientname_turn.get() == "":
            self.text_turn1.focus_set()
            messagebox.showerror("توجه","نام بیمار را پر کنید")
        elif self.patientFamyli_turn.get() == "":
            self.text_turn2.focus_set()
            messagebox.showerror("توجه","فامیل بیمار را پر کنید")
        elif self.Codenational_turn.get().isdigit() == FALSE:
            self.text_turn3.focus_set()
            messagebox.showerror("توجه","کد ملی را به صورت عددی پر کنید")
        elif self.appointmentdate.get() == "":
            self.text_turn4.focus_set()
            messagebox.showerror("توجه","تاریخ را وارد کنید")
        elif self.turntime.get() == "":
            self.text_turn5.focus_set()
            messagebox.showerror("توجه","ساعت را وارد کنید")
        else:
            self.tbl_4.insert('',"end",values=(self.turntime.get(),self.appointmentdate.get(),self.Codenational_turn.get(),self.patientFamyli_turn.get(),self.patientname_turn.get(),self.textId3_turn.get()))
            self.obj_3=patientsturn(self.patientname_turn.get(),self.patientFamyli_turn.get(),self.Codenational_turn.get(),self.appointmentdate.get(),self.turntime.get())
            self.oprts=operations()
            self.oprts.Add(self.obj_3)
            self.Delet_3()
            self.Lod_3()
    def SaveDoctor(self):
        if self.DoctorName.get() == "":
            self.textD_1.focus_set()
            messagebox.showerror("توجه","نام را پر کنید")
        elif self.FamilyDoctor.get() =="":
            self.textD_2.focus_set()
            messagebox.showerror("توجه","فامیل را پر کنید")
        elif self.DoctorExpertise.get() == "":
            self.textD_3.focus_set()
            messagebox.showerror("توجه","تخصص را پر کنید")
        elif self.PersonnelCode.get().isdigit() == FALSE:
            self.textD_4.focus_set()
            messagebox.showerror("توجه","کد پرسنلی را به صورت عددی وارد کنید")
        else:
            self.tbl_D.insert('',"end", values=(self.PersonnelCode.get(),self.DoctorExpertise.get(),self.FamilyDoctor.get(),self.DoctorName.get(),self.ID_D.get()))
            self.obj_4=Doctor(self.DoctorName.get(), self.FamilyDoctor.get(), self.DoctorExpertise.get(), self.PersonnelCode.get())
            self.obj_6=Enter(self.DoctorName.get(), self.PersonnelCode.get())
            self.oprts=operations()
            self.oprts.Add(self.obj_4)
            self.oprts.Add(self.obj_6)
            self.Delet_4()
            self.Lod_4()

    def SeveEnter(self):
        self.oprts=operations()
        if self.username.get() == "":
            self.textSRP.focus_set()
            messagebox.showerror("توجه", "نام کاربری را وارد کنید")
        elif self.password.get().isdigit() == FALSE:
            self.textSRP_1.focus_set()
            messagebox.showerror("توجه", "رمز عبور را عددی وارد کنید")
        else:
            #self.Showfrm_6()
            self.x()



    def x(self):
        self.optrs=operations()
        mac=self.username.get()
        mak=self.password.get()
        result= self.oprts.Raed(Enter)
        for item in result:
            print(item.prsl_username)
            print(item.prsl_password)
        result1=self.oprts.ReadByUsernamePasword(Enter,mac,mak)
        if result1 == None :
            messagebox.showerror("توجه","این نام کاربری وجود ندارد")
        else:
            self.Showfrm_6()
            self.username.set("")
            self.password.set("")

    def Lod(self):
        oprts = operations()
        result = oprts.Raed(patients)
        for item in result:
            self.tbl.insert('', "end",values=[item.prsl_Consumabledrugs,item.prsl_Age,item.prsl_diseasebackground,item.prsl_NationalCode,item.prsl_Family,item.prsl_Namepatient,item.prsl_id])

    def Lod_1(self):
        oprts = operations()
        result = oprts.Raed(prescription)
        for item in result:
            self.tbl_1.insert('', "end",values=[item.prsl_Drugform, item.prsl_Alternativemedicine, item.prsl_Name_E,item.prsl_Name, item.prsl_id])

    def Lod_2(self):
        oprts = operations()
        result = oprts.Raed(Druginteractions)
        for item in result:
            self.tbl_2.insert('', "end",values=[item.prsl_Theintensityoftheinterference, item.prsl_AlternativeMedizin,item.prsl_interference, item.prsl_Name, item.prsl_id])

    def Lod_3(self):
        oprts = operations()
        result = oprts.Raed(patientsturn)
        for item in result:
            self.tbl_4.insert('',"end", values=[item.prsl_turntime, item.prsl_appointmentdate, item.prsl_NationalCodeturn, item.prsl_Famylipatientturn, item.prsl_Namepatientturn, item.prsl_id])

    def Lod_4(self):
        oprts = operations()
        result = oprts.Raed(Doctor)
        for item in result:
            self.tbl_D.insert('',"end", values=[item.prsl_DoctorPersonnelCode,item.prsl_DoctorSpecialty,item.prsl_FamilyDoctor,item.prsl_DoctorName,item.prsl_id])

    def Delet(self):
        for item in self.tbl.get_children():
                print(item)
                sel = (str(item),)
                self.tbl.delete(sel)
                self.Namepatient.set("")
                self.Famyli.set("")
                self.diseasebackground.set("")
                self.Age.set("")
                self.Consumabledrugs.set("")
                self.Codenational.set("")

            #            self.quest.set("")

            # self.oprts = operations()
            # self.result = self.oprts.Raed(prescription)
            # self.tbl_1.delete(*self.tbl_1.get_children())

    def Delet_1(self):
        for item in self.tbl_1.get_children():
            print(item)
            sel = (str(item),)
            self.tbl_1.delete(sel)
            self.Name.set("")
            self.medicinename.set("")
            self.Alternativemedicine.set("")
            self.Drugform.set("")

    def Delet_2(self):
        for item in self.tbl_2.get_children():
            print(item)
            sel = (str(item),)
            self.tbl_2.delete(sel)
            self.nomdumédicament.set("")
            self.Itinterfereswith.set("")
            self.AlternativeMedizin.set("")
            self.Theintensityoftheinterference.set("")

    def Delet_3(self):
        for item in self.tbl_4.get_children():
            print(item)
            sel= (str(item))
            self.tbl_4.delete(sel)
            self.patientname_turn.set("")
            self.patientFamyli_turn.set("")
            self.Codenational_turn.set("")
            self.turntime.set("")
            self.appointmentdate.set("")

    def Delet_4(self):
        for item in self.tbl_D.get_children():
            print(item)
            sel=(str(item))
            self.tbl_D.delete(sel)
            self.DoctorName.set("")
            self.FamilyDoctor.set("")
            self.DoctorExpertise.set("")
            self.PersonnelCode.set("")
    def Search(self):
        self.oprts = operations()
        NAME = self.que.get()
        result = self.oprts.Search_Date(patients, NAME)
        self.Delet()
        for item in result:
            self.tbl.insert('', "end", values=[item.prsl_Consumabledrugs, item.prsl_Age, item.prsl_diseasebackground,item.prsl_NationalCode,item.prsl_Family, item.prsl_Namepatient,item.prsl_id])
            self.que.set("")
            self.selection_row = self.tbl.selection()
            # self.btn_Edit.place(x=680, y=0)
            # self.btn_Deleteline.place(x=745, y=0)
            if self.selection_row != ():
                self.Namepatient.set(self.tbl.item(self.selection_row)["values"][5])
                self.Famyli.set(self.tbl.item(self.selection_row)["values"][4])
                self.Codenational.set(self.tbl.item(self.selection_row)["values"][3])
                self.diseasebackground.set(self.tbl.item(self.selection_row)["values"][2])
                self.Age.set(self.tbl.item(self.selection_row)["values"][1])
                self.Consumabledrugs.set(self.tbl.item(self.selection_row)["values"][0])
                self.Id.set(self.tbl.item(self.selection_row)["values"][6])


    def Search_1(self):
        self.oprts = operations()
        NAME_1 = self.que_1.get()
        result = self.oprts.Search_Date_1(prescription, NAME_1)
        self.Delet_1()
        for item in result:
            self.tbl_1.insert('', "end", values=[item.prsl_Drugform, item.prsl_Alternativemedicine, item.prsl_Name_E,item.prsl_Name,item.prsl_id])
            self.que_1.set("")
            self.selection_row = self.tbl_1.selection()
            if self.selection_row != ():
                self.Name.set(self.tbl_1.item(self.selection_row)["values"][4])
                self.medicinename.set(self.tbl_1.item(self.selection_row)["values"][3])
                self.Alternativemedicine.set(self.tbl_1.item(self.selection_row)["values"][2])
                self.Drugform.set(self.tbl_1.item(self.selection_row)["values"][1])
                self.Id_1.set(self.tbl_1.item(self.selection_row)["values"][0])

    def Search_2(self):
        self.oprts = operations()
        NAME_2 = self.que_2.get()
        result = self.oprts.Search_Date_2(Druginteractions, NAME_2)
        self.Delet_2()
        for item in result:
            self.tbl_2.insert('', "end", values=[item.prsl_Theintensityoftheinterference, item.prsl_AlternativeMedizin,item.prsl_interference, item.prsl_Name,item.prsl_id])
            self.que_2.set("")
            self.selection_row = self.tbl_2.selection()
            if self.selection_row != ():
                self.nomdumédicament.set(self.tbl_2.item(self.selection_row)["values"][4])
                self.Itinterfereswith.set(self.tbl_2.item(self.selection_row)["values"][3])
                self.AlternativeMedizin.set(self.tbl_2.item(self.selection_row)["values"][2])
                self.Theintensityoftheinterference.set(self.tbl_2.item(self.selection_row)["values"][1])
                self.Id_2.set(self.tbl_2.item(self.selection_row)["values"][0])

    def SearchTrun(self):
        self.oprts=operations()
        NAME_3=self.textSearch.get()
        result = self.oprts.Search_Date_3(patientsturn,NAME_3)
        self.Delet_3()
        for item in result :
            self.tbl_4.insert('',"end",values=[item.prsl_turntime,item.prsl_appointmentdate,item.prsl_NationalCodeturn,item.prsl_Famylipatientturn,item.prsl_Namepatientturn,item.prsl_id])
            self.textSearch.set("")
            self.selection_row=self.tbl_4.selection()
            if self.selection_row != ():
                self.patientname_turn.set(self.tbl_4.item( self.selection_row)["values"][4])
                self.patientFamyli_turn.set(self.tbl_4.item( self.selection_row)["values"][3])
                self.Codenational_turn.set(self.tbl_4.item( self.selection_row)["values"][2])
                self.appointmentdate.set(self.tbl_4.item( self.selection_row)["values"][1])
                self.turntime.set(self.tbl_4.item( self.selection_row)["values"][0])
                self.textId3_turn.set(self.tbl_4.item( self.selection_row)["values"][5])


    def search_D(self):
        self.oprts=operations()
        NAME_4=self.textDserch.get()
        result= self.oprts.Search_Date_4(Doctor,NAME_4)
        self.Delet_4()
        for item in result:
            self.tbl_D.insert('',"end", values=[item.prsl_DoctorPersonnelCode,item.prsl_DoctorSpecialty,item.prsl_FamilyDoctor,item.prsl_DoctorName,item.prsl_id])
            self.textDserch.set("")
            self.selection_row=self.tbl_D.selection()
            if self.selection_row !=():
                self.DoctorName.set(self.tbl_D.item(self.selection_row)["values"][3])
                self.FamilyDoctor.set(self.tbl_D.item(self.selection_row)["values"][2])
                self.DoctorExpertise.set(self.tbl_D.item(self.selection_row)["values"][1])
                self.PersonnelCode.set(self.tbl_D.item(self.selection_row)["values"][0])
                self.ID_D.set(self.tbl_D.item(self.selection_row)["values"][4])

    def Searchfrm1(self):

        self.oprts=operations()
        NAME_5=self.Codenationalfrm1.get()
        result = self.oprts.Search_Datefrm1(patients,NAME_5)
        self.Delet()
        if result == []:
            messagebox.showerror("توجه","این کدملی وجود ندارد")
            self.Codenationalfrm1.set("")
        else:
            self.tbl_3.place(x=0, y=200)
            for item in result:
                self.tbl_3.insert('',"end", values=[item.prsl_Consumabledrugs,item.prsl_Age,item.prsl_diseasebackground,item.prsl_NationalCode,item.prsl_Family,item.prsl_Namepatient,item.prsl_id])
                self.Codenationalfrm1.set("")




    def DeleteLine(self):
        self.oprts = operations()
        self.qu= self.Id.get()
        self.oprts.DeleteRow(patients, self.qu)
        self.btn_Delet.place_forget()
        self.Delet()
        self.Lod()
    def DeleteLine_1(self):
        self.oprts = operations()
        self.qury=self.Id_1.get()
        self.oprts.DeleteRow(prescription, self.qury)
        self.btn_Delet_1.place_forget()
        self.Delet_1()
        self.Lod_1()


    def DeleteLine_2(self):
        self.oprts = operations()
        self.tyu=self.Id_2.get()
        self.oprts.DeleteRow(Druginteractions,self.tyu)
        self.btn_Delet_2.place_forget()
        self.Delet_2()
        self.Lod_2()

    def DeleTurn(self):
        self.oprts=operations()
        man=self.textId3_turn.get()
        self.oprts.DeleteRow(patientsturn,man)
        self.Delet_3()
        self.Lod_3()


    def DeleteLine_Doctor(self):
        self.oprts = operations()
        self.ope=self.ID_D.get()
        self.oprts.DeleteRow(Doctor,self.ope)
        self.Delet_4()
        self.Lod_4()

    def EDIT(self):
        self.oprts = operations()
        que=self.Id.get()
        data=patients(self.Namepatient.get(),self.Famyli.get(),self.diseasebackground.get(),self.Consumabledrugs.get(),self.Age.get(),self.Codenational.get())
        self.oprts.Update(patients,que,data)
        self.Delet()
        self.Lod()
    def EDIT_1(self):
        self.oprts = operations()
        qury=self.Id_1.get()
        data_1=prescription(self.Name.get(),self.medicinename.get(),self.Alternativemedicine.get(),self.Drugform.get())
        self.oprts.Update_1(prescription,qury,data_1)
        self.Delet_1()
        self.Lod_1()
    def EDIT_2(self):
        self.oprts = operations()
        que_2 = self.Id_2.get()
        data_2=Druginteractions(self.nomdumédicament.get(),self.Itinterfereswith.get(),self.AlternativeMedizin.get(),self.Theintensityoftheinterference.get())
        self.oprts.Update_2(Druginteractions,que_2,data_2)
        self.Delet_2()
        self.Lod_2()

    def EditTrun(self):
        self.oprts=operations()
        cut=self.textId3_turn.get()
        data_3=patientsturn(self.patientname_turn.get(),self.patientFamyli_turn.get(),self.Codenational_turn.get(),self.appointmentdate.get(),self.turntime.get())
        self.oprts.Update_3(patientsturn,cut,data_3)
        self.Delet_3()
        self.Lod_3()


    def EDIT_Doctor(self):
        self.oprts = operations()
        self.ope=self.ID_D.get()
        self.data_D=Doctor(self.DoctorName.get(),self.FamilyDoctor.get(),self.DoctorExpertise.get(),self.PersonnelCode.get())
        self.oprts.Update_4(Doctor,self.ope,self.data_D)
        self.Delet_4()
        self.Lod_4()
    def toshow(self):
        if self.jun.get() == 1:
            self.textSearch1.place(x=340,y=150)
            self.btnSearch_1.place(x=470,y=145)
            #self.tbl_3.place(x=0,y=200)
            '''self.oprts=operations()
            result= self.oprts.Raed(patients)
            for item in result:
                self.tbl_3.insert('',"end", values=[item.prsl_Consumabledrugs, item.prsl_Age, item.prsl_diseasebackground,item.prsl_NationalCode,item.prsl_Family, item.prsl_Namepatient, item.prsl_id])'''
        else:
            return messagebox.showinfo("سلام","از منوی تنظیمات بیمار را ثبت نام کن")

    def Close(self):
        self.master.destroy()
    def Return(self):
        self.tbl_3.place_forget()
        self.btnSearch_1.place_forget()
        self.textSearch1.place_forget()
        self.jun.set(0)
        self.Showfrm_1()



    '''def Enter(self):
        #self.x()
        self.oprts=operations()
        if self.username.get() =="":
            self.textSRP.focus_set()
            messagebox.showerror("توجه","نام کاربری را وارد کنید")
        elif self.password.get().isdigit() == FALSE:
            self.textSRP_1.focus_set()
            messagebox.showerror("توجه","رمز عبور را به صورت عددی وارد کنید")
        else:
            self.Showfrm_6()'''





















































































































