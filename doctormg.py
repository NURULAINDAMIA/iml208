import time
import random
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

class Doctor():
    def __init__(self,root):
        self.root = root
        self.root.title("Doctor Management system")
        self.root.geometry("1700x900+0+0")
        self.root.configure(background = "black")

        # Declare all functions 
        Date_of_Registration = StringVar()
        Date_of_Registration.set(time.strftime("%d/%m/%y")) 
        DrId  = StringVar()
        Drname = StringVar()
        DateofBirth = StringVar()
        Spes = StringVar()
        GovtPri = StringVar()
        Surgeries = StringVar()
        Experience = StringVar()
        Nurses = StringVar()
        DrMobile = StringVar()
        PtName = StringVar()
        Apptime = StringVar()
        PtAge  = StringVar()
        PatientAddress = StringVar()
        PtMobile = StringVar()
        Disease = StringVar() 
        Case = StringVar()
        BenefitCard = StringVar()

        def exitbtn():
            exitbtn = tkinter.messagebox.askyesno("Doctor Management System", "Are you sure you want to exit ?")
            if exitbtn > 0:
                root.destroy()
                return
        
        def deletefunc():
            DrId.set("")
            Drname.set("")
            DateofBirth.set("")
            Spes.set("")
            GovtPri.set("")
            Surgeries.set("")
            Experience.set("")
            Nurses.set("")
            DrMobile.set("")
            PtName.set("")
            Apptime.set("")
            PtAge.set("")
            PatientAddress.set("")
            PtMobile.set("")
            Disease.set("")
            Case.set("")
            BenefitCard.set("")
            TextPrescription.delete("1.0",END)
            TextPrescriptionData.delete("1.0",END)
            return
        
        def resetfunc():
            DrId.set("")
            Drname.set("")
            DateofBirth.set("")
            Spes.set("")
            GovtPri.set("")
            Surgeries.set("")
            Experience.set("")
            Nurses.set("")
            DrMobile.set("")
            PtName.set("")
            Apptime.set("")
            PtAge.set("")
            PatientAddress.set("")
            PtMobile.set("")
            Disease.set("") 
            Case.set("")
            BenefitCard.set("")
            TextPrescription.delete("1.0",END)
            return
        
        
        def Patient_idFunc():
            ranumber = random.randint(1000,9999)
            randomnumber = str(ranumber)
            DrId.set(randomnumber)
        
        def prescriptiondatafunc():
            Patient_idFunc()
            TextPrescriptionData.insert(END,Date_of_Registration.get()+"\t"+DrId.get()+"\t"
            +DrName.get()+"\t"+DateofBirth.get()+"\t\t"+ Spes.get()+"\t\t"+GovtPri.get()+"\t\t"+
            Surgeries.get()+"\t"+Experience.get()+"\t"+Nurses.get()+"\t"+DrMobile.get()+"\t\t"+
            PtName.get()+"\t\t"+Case.get()+"\t\t"+PtAge.get()+"\n")
            return
        
        def prescriptionfunc():
            Patient_idFunc()
            TextPrescription.insert(END,"Date: \t\t"+Date_of_Registration.get()+"\n")
            TextPrescription.insert(END,"Patient Name: \t\t"+PtName.get()+"\n")
            TextPrescription.insert(END,"Appoinment Time: \t\t"+Apptime.get()+"\n")
            TextPrescription.insert(END,"Age: \t\t"+PtAge.get()+"\n")
            TextPrescription.insert(END,"Address: \t\t"+PatientAddress.get()+"\n")
            TextPrescription.insert(END,"Disease: \t\t"+Disease.get()+"\n")
            TextPrescription.insert(END,"Case: \t\t"+Case.get()+"\n")
            TextPrescription.insert(END,"Benefit Card: \t\t"+BenefitCard.get()+"\n")
            TextPrescription.insert(END,"To meet Dr: \t\t"+DrName.get()+"\n")
            TextPrescription.insert(END,"Dr. Mobile No.: \t\t"+DrMobile.get()+"\n")
            return


        #Title Label
        title = Label(self.root , text = "Doctor Management System", font =("monotype corsiva",42,"bold"),bd = 5,
            relief = GROOVE,bg = "#b7d8d6", fg = "black")
        title.pack(side=TOP , fill = X)

        #Frame
        Manage_Frame = Frame(self.root , width = 1510 , height = 400 , bd = 5 , relief = RIDGE , bg = "#789e9e")
        Manage_Frame.place(x=10,y=80)

        Buttons_Frame = Frame(self.root , width = 1510 , height = 55 , bd = 4 , relief = RIDGE , bg = "#eef3db")
        Buttons_Frame.place(x=10,y=460)

        Data_Frame = LabelFrame(self.root,width = 1510 , height = 270 , bd = 4 , relief = RIDGE , bg = "#266E73")
        Data_Frame.place(x=10,y=510)

        Data_FrameLeft = LabelFrame(Manage_Frame,width = 1050,text = "General Information",
        font =("arial",20,"italic bold"), height = 390 , bd = 7 , pady = 1,relief = RIDGE , bg = "#789e9e")
        Data_FrameLeft.pack(side = LEFT)

        Data_FrameRight = LabelFrame(Manage_Frame, width = 450, text = "Patient's Information",font=("arial",15,"italic bold"), 
        height = 390 , bd = 7 , relief = RIDGE , bg = "#789e9e")
        Data_FrameRight.pack(side = RIGHT)

        Data_Framedata = LabelFrame(Data_Frame,width = 1050,text = "Doctor's Details",
        font =("arial",12,"italic bold") ,height = 360 , bd = 4 , relief = RIDGE , bg = "#4d6466",fg = "#b7d8d6")
        Data_Framedata.pack(side = LEFT)

        # Doctor's ID

        DrId1b1 = Label(Data_FrameLeft , font =("arial",12,"bold"),width =20,text = "Doctor ID",bg = "#789e9e")
        DrId1b1.grid(row = 0 , column = 0 , padx = 10 , pady = 5 , sticky = W)
        DrIdtxt = Entry(Data_FrameLeft , font=("arial",12,"bold"),width =27, state = DISABLED,textvariable = DrId)
        DrIdtxt.grid(row = 0 , column = 1 , padx = 10 , pady = 5 , sticky = E)

        DrName1b1 = Label(Data_FrameLeft , font =("arial",12,"bold"),width =20,text = "Doctor Name",bg = "#789e9e")
        DrName1b1.grid(row = 1 , column = 0 , padx = 10 , pady = 5 , sticky = W)
        DrName = Entry(Data_FrameLeft , font=("arial",12,"bold"),width =27,textvariable = Drname)
        DrName.grid(row = 1 , column = 1 , padx = 10 , pady = 5 , sticky = E)

        DateofBirth1b1 = Label(Data_FrameLeft , font =("arial",12,"bold"),width =20,text = "Date of Birth",bg = "#789e9e")
        DateofBirth1b1.grid(row = 2 , column = 0 , padx = 10 , pady = 5 , sticky = W)
        DateofBirthtxt = Entry(Data_FrameLeft , font=("arial",12,"bold"),width =27,textvariable = DateofBirth)
        DateofBirthtxt.grid(row = 2 , column = 1 , padx = 10 , pady = 5 , sticky = E)

        Spes1b1 = Label(Data_FrameLeft , font =("arial",12,"bold"),width =20,text = "Specialization",bg = "#789e9e")
        Spes1b1.grid(row = 3 , column = 0 , padx = 10 , pady = 5 , sticky = W)
        Spestxt = Entry(Data_FrameLeft , font=("arial",12,"bold"),width =27,textvariable = Spes)
        Spestxt.grid(row = 3 , column = 1 , padx = 10 , pady = 5 , sticky = E)

        GovtPri1b1 = Label(Data_FrameLeft , font =("arial",12,"bold"),width =20,text = "Govt/Private",padx=2,
        bg = "#789e9e")
        GovtPri1b1.grid(row = 4 ,column = 0 , padx = 10 , pady = 5 , sticky = W)
        GovtPricmb= ttk.Combobox(Data_FrameLeft , textvariable = GovtPri , width = 25 ,state = "readonly",
        font=("arial",12,"bold"))
        GovtPricmb['values'] = ("", "Government","Private")
        GovtPricmb.current(0)
        GovtPricmb.grid(row = 4 , column = 1 , padx = 10 , pady = 5 , sticky =E)

        Surgeries1b1 = Label(Data_FrameLeft , font =("arial",12,"bold"),width =20,text = "Total Surgeries",bg = "#789e9e")
        Surgeries1b1.grid(row = 5 , column = 0 , padx = 10 , pady = 5 , sticky = W)
        Surgeriestxt = Entry(Data_FrameLeft , font=("arial",12,"bold"),width =27,textvariable = Surgeries)
        Surgeriestxt.grid(row = 5 , column = 1 , padx = 10 , pady = 5 , sticky = E)

        Experience1b1 = Label(Data_FrameLeft , font =("arial",12,"bold"),width =20,text = "Experience in years",bg = "#789e9e")
        Experience1b1.grid(row = 6 , column = 0 , padx = 10 , pady = 5 , sticky = W)
        Experiencetxt = Entry(Data_FrameLeft , font=("arial",12,"bold"),width =27,textvariable = Experience)
        Experiencetxt.grid(row = 6 , column = 1 , padx = 10 , pady = 5 , sticky = E)

        Nurses1b1 = Label(Data_FrameLeft , font =("arial",12,"bold"),width =20,text = "Nurses under Dr",bg = "#789e9e")
        Nurses1b1.grid(row = 7 , column = 0 , padx = 10 , pady = 5 , sticky = W)
        Nursestxt = Entry(Data_FrameLeft , font=("arial",12,"bold"),width =27,textvariable = Nurses)
        Nursestxt.grid(row = 7 , column = 1 , padx = 10 , pady = 5 , sticky = E)

        DrMobile1b1 = Label(Data_FrameLeft , font =("arial",12,"bold"),width =20,text = "Doctor Mobile No.",bg = "#789e9e")
        DrMobile1b1.grid(row = 8 , column = 0 , padx = 10 , pady = 5 , sticky = W)
        DrMobiletxt = Entry(Data_FrameLeft , font=("arial",12,"bold"),width =27,textvariable = DrMobile)
        DrMobiletxt.grid(row = 8 , column = 1 , padx = 10 , pady = 5 , sticky = E)

        Date1b1 = Label(Data_FrameLeft ,font=("arial",12,"bold"),width = 20,text = "Date",bg = "#789e9e")
        Date1b1.grid(row = 0 , column = 2, padx = 10 , pady = 5 , sticky = W)
        Datetxt = Entry(Data_FrameLeft, font=("arial",12,"bold"), width = 27, textvariable = Date_of_Registration)
        Datetxt.grid(row = 0 , column = 3,padx = 10 , pady = 5, sticky = E)

        PtName1b1 = Label(Data_FrameLeft,font=("arial",12,"bold"),width = 20,text = "Patient Name",padx=2, 
        bg="#789e9e")
        PtName1b1.grid(row = 1 , column = 2,padx = 10 , pady = 5 , sticky = W)
        PtNametxt = Entry(Data_FrameLeft, font=("arial",12,"bold"),width = 27,textvariable = PtName)
        PtNametxt.grid(row = 1 , column = 3,padx = 10 , pady = 5, sticky = E)

        Apptime1b1 = Label(Data_FrameLeft,font=("arial",12,"bold"),width = 20,text = "Appointment Time",padx=2, 
        bg="#789e9e")
        Apptime1b1.grid(row = 2 , column = 2,padx = 10 , pady = 5 , sticky = W)
        Apptimetxt = Entry(Data_FrameLeft, font=("arial",12,"bold"),width = 27,textvariable = Apptime)
        Apptimetxt.grid(row = 2 , column = 3,padx = 10 , pady = 5, sticky = E)

        PtAge1b1 = Label(Data_FrameLeft,font=("arial",12,"bold"),width = 20,text = "Patient Age",padx=2, 
        bg="#789e9e")
        PtAge1b1.grid(row = 3 , column = 2,padx = 10 , pady = 5 , sticky = W)
        PtAgetxt = Entry(Data_FrameLeft, font=("arial",12,"bold"),width = 27,textvariable = PtAge)
        PtAgetxt.grid(row = 3 , column = 3,padx = 10 , pady = 5, sticky = E)
        
        PtAddress1b1 = Label(Data_FrameLeft,font=("arial",12,"bold"),width = 20,text = "Patient Address",padx=2, 
        bg="#789e9e")
        PtAddress1b1.grid(row = 4 , column = 2,padx = 10 , pady = 5 , sticky = W)
        PtAddresstxt = Entry(Data_FrameLeft, font=("arial",12,"bold"),width = 27,textvariable = PatientAddress)
        PtAddresstxt.grid(row = 4 , column = 3,padx = 10 , pady = 5, sticky = E)

        PtMobile1b1 = Label(Data_FrameLeft,font=("arial",12,"bold"),width = 20,text = "Patient Mobile No.",padx=2, 
        bg="#789e9e")
        PtMobile1b1.grid(row = 5 , column = 2,padx = 10 , pady = 5 , sticky = W)
        PtMobiletxt = Entry(Data_FrameLeft, font=("arial",12,"bold"),width = 27,textvariable = PtMobile)
        PtMobiletxt.grid(row = 5 , column = 3,padx = 10 , pady = 5, sticky = E)

        Disease1b1 = Label(Data_FrameLeft,font=("arial",12,"bold"),width = 20,text = "Patient Disease",padx=2, 
        bg="#789e9e")
        Disease1b1.grid(row = 6 , column = 2,padx = 10 , pady = 5 , sticky = W)
        Diseasetxt = Entry(Data_FrameLeft, font=("arial",12,"bold"),width = 27,textvariable = Disease)
        Diseasetxt.grid(row = 6 , column = 3,padx = 10 , pady = 5, sticky = E)

        Case1b1 = Label(Data_FrameLeft,font=("arial",12,"bold"),width = 20,text = "Case",padx=2, 
        bg="#789e9e")
        Case1b1.grid(row = 7 , column = 2,padx = 10 , pady = 5 , sticky = W)
        Casecmb = ttk.Combobox(Data_FrameLeft, textvariable = Case,width = 25,state = "readonly",
        font = ("arial", 12,"bold"))
        Casecmb['values'] = ("", "New Case", "Old Case")
        Casecmb.current(0)
        Casecmb.grid(row = 7 , column = 3,padx = 10 , pady = 5, sticky = E)

        BenefitCard1b1 = Label(Data_FrameLeft,font=("arial",12,"bold"),text = "Benefit Card",width = 20, padx=10, 
        bg="#789e9e")
        BenefitCard1b1.grid(row = 8 , column = 2 , sticky = W)

        BenefitCardcmb = ttk.Combobox(Data_FrameLeft, textvariable = BenefitCard,width = 25, state = "readonly",
        font = ("arial", 12,"bold"))
        BenefitCardcmb['values'] = ("", "Ayushman Card", "Health Insurance", "Senior Citizen","Army Card")
        BenefitCardcmb.current(0)
        BenefitCardcmb.grid(row = 8 , column = 3, padx = 10 , sticky = E)

        # Text Prescription

        TextPrescription = Text(Data_FrameRight , font = ("arial",12,"bold"), width = 55 , height = 17 , padx = 3 , 
        pady = 5)
        TextPrescription.grid(row = 0 , column = 0)
        TextPrescriptionData =Text(Data_Framedata, font =("arial",12,"bold"),width = 150 , height = 12)
        TextPrescriptionData.grid(row=1 , column = 0)

        # Buttons
        Prescriptionbtn = Button(Buttons_Frame, text = "Patient Information", bg = "#fe615a",activebackground = "#cc6686",
        font = ("arial",13,"bold"),width = 22, command = prescriptionfunc)
        Prescriptionbtn.grid(row = 0 , column = 0 , padx = 13)

        DoctorDetailbtn = Button(Buttons_Frame, text = "Doctor's Details", bg = "#fe615a",activebackground = "#cc6686",
        font = ("arial",13,"bold"),width = 22, command = prescriptiondatafunc)
        DoctorDetailbtn.grid(row = 0 , column = 1 , padx = 13)

        Resetbtn = Button(Buttons_Frame, text = "Reset", bg = "#fe615a",activebackground = "#cc6686",
        font = ("arial",13,"bold"),width = 22, command = resetfunc)
        Resetbtn.grid(row = 0 , column = 2 , padx =13)

        Deletebtn = Button(Buttons_Frame, text = "Delete", bg = "#fe615a",activebackground = "#cc6686",
        font = ("arial",13,"bold"),width = 22, command = deletefunc)
        Deletebtn.grid(row = 0 , column = 3 , padx = 13)

        Exitbtn = Button(Buttons_Frame, text = "Exit", bg = "#fe615a",activebackground = "#cc6686",
        font = ("arial",13,"bold"),width = 22, command = exitbtn)
        Exitbtn.grid(row = 0 , column = 4 , padx = 13)

        prescriptiondatarow = Label(Data_Framedata , bg = "pink", font =("arial",10,"bold"),
        text = "Date\t   Doctor ID    Dr.Name    Date of Birth\tSpecialisation\t\tGovt/Private               Surgeries   Y.Exp\tNurses         Dr Mobile No.\t\tPatient Name              Case\t\tPt. Age")
        prescriptiondatarow.grid(row =0 , column = 0 , sticky = W)


if __name__ == "__main__":
    root = Tk()
    app = Doctor(root)
    root.mainloop()  