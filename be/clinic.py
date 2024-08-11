from sqlalchemy import Column, Integer, String,Text,create_engine,NVARCHAR,ForeignKey,BigInteger,DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base,relationship
from be.setings import Setting



con=Setting().GetConectionStrinh()
engine=create_engine(str(con))
Base = declarative_base()


class Doctor(Base):
    __tablename__ = 'doctor'
    prsl_id=Column(Integer, primary_key=True)
    prsl_DoctorName=Column(NVARCHAR)
    prsl_FamilyDoctor=Column(NVARCHAR)
    prsl_DoctorSpecialty=Column(NVARCHAR)
    prsl_DoctorPersonnelCode=Column(BigInteger)
    #PTTS=relationship("patients",back_populates="doctor")
    #PTTS_id = Column(Integer, ForeignKey(patients.id), unique=True)

    def __init__(self,prsl_DoctorName,prsl_FamilyDoctor,prsl_DoctorSpecialty,prsl_DoctorPersonnelCode):
        self.prsl_DoctorName=prsl_DoctorName
        self.prsl_FamilyDoctor=prsl_FamilyDoctor
        self.prsl_DoctorSpecialty=prsl_DoctorSpecialty
        self.prsl_DoctorPersonnelCode=prsl_DoctorPersonnelCode
class patients(Base):
    __tablename__ = 'patients'
    prsl_id=Column(Integer, primary_key=True)
    prsl_Namepatient=Column(NVARCHAR)
    prsl_Family=Column(NVARCHAR)
    prsl_diseasebackground=Column(NVARCHAR)
    prsl_Consumabledrugs=Column(NVARCHAR)
    prsl_Age=Column(Integer)
    prsl_NationalCode=Column(BigInteger)
   #DR_id = Column(Integer, ForeignKey(doctor.prsl_id))
    #DR=relationship("doctor", back_populates="patients")

    def __init__(self,prsl_Namepatient,prsl_Family,prsl_diseasebackground,prsl_Consumabledrugs,prsl_Age,prsl_NationalCode):
        self.prsl_Namepatient=prsl_Namepatient
        self.prsl_Family=prsl_Family
        self.prsl_diseasebackground=prsl_diseasebackground
        self.prsl_Consumabledrugs=prsl_Consumabledrugs
        self.prsl_Age=prsl_Age
        self.prsl_NationalCode=prsl_NationalCode





class prescription(Base):
    __tablename__ = 'prescription'
    prsl_id=Column(Integer,primary_key=True)
    prsl_Name=Column(NVARCHAR)
    prsl_Name_E =Column(NVARCHAR)
    prsl_Alternativemedicine=Column(NVARCHAR)
    prsl_Drugform=Column(NVARCHAR)
    #DR_id = Column(Integer, ForeignKey(doctor.prsl_id))prsl_Drugform
    #DR = relationship("doctor", back_populates="prescription")

    def __init__(self,prsl_Name,prsl_Name_E,prsl_Alternativemedicine,prsl_Drugform):
        #self.prsl_id=prsl_id
        self.prsl_Name=prsl_Name
        self.prsl_Name_E=prsl_Name_E
        self.prsl_Alternativemedicine=prsl_Alternativemedicine
        self.prsl_Drugform=prsl_Drugform


class Druginteractions(Base):
    __tablename__ = 'Druginteractions'
    prsl_id=Column(Integer,primary_key=True)
    prsl_Name=Column(NVARCHAR)
    prsl_interference=Column(NVARCHAR)
    prsl_AlternativeMedizin=Column(NVARCHAR)
    prsl_Theintensityoftheinterference=Column(NVARCHAR)
    #DR_id = Column(Integer, ForeignKey(doctor.prsl_id))
    #DR = relationship("doctor", back_populates=" Druginteractions")

    def __init__(self,prsl_Name,prsl_interference,prsl_AlternativeMedizin,prsl_Theintensityoftheinterference):
        #self.prsl_id=prsl_id
        self.prsl_Name=prsl_Name
        self.prsl_interference=prsl_interference
        self.prsl_AlternativeMedizin=prsl_AlternativeMedizin
        self.prsl_Theintensityoftheinterference=prsl_Theintensityoftheinterference

class patientsturn(Base):
    __tablename__ = 'patientsturn'
    prsl_id = Column(Integer, primary_key=True)
    prsl_Namepatientturn = Column(NVARCHAR)
    prsl_Famylipatientturn = Column(NVARCHAR)
    prsl_NationalCodeturn = Column(BigInteger)
    prsl_appointmentdate = Column(NVARCHAR)
    prsl_turntime = Column(NVARCHAR)

    def __init__(self,prsl_Namepatientturn, prsl_Famylipatientturn, prsl_NationalCodeturn, prsl_appointmentdate, prsl_turntime):
        self.prsl_Namepatientturn= prsl_Namepatientturn
        self.prsl_Famylipatientturn= prsl_Famylipatientturn
        self.prsl_NationalCodeturn= prsl_NationalCodeturn
        self.prsl_appointmentdate = prsl_appointmentdate
        self.prsl_turntime = prsl_turntime

class Enter(Base):
    __tablename__ = 'Enter'
    prsl_id = Column(Integer, primary_key=True)
    prsl_username = Column(NVARCHAR)
    prsl_password = Column(BigInteger)

    def __init__(self,prsl_username,prsl_password):
        self.prsl_username = prsl_username
        self.prsl_password = prsl_password

Base.metadata.create_all(engine)

