from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine
from be.setings import Setting

con=Setting().GetConectionStrinh()
engine=create_engine(str(con))
Session=sessionmaker(bind=engine)
session=Session()

class Repository():
    def Add(self, obj):
        try:
            session.add(obj)
            session.commit()
            return True
        except Exception as e:
            print(e)
            return False
    def Read(self,obj):
        return session.query(obj).all()

    def Delete(self,obj):
        session.delete(obj)
        session.commit()

    def Update(self,obj,id,newobj):
        result=self.ReabById(obj,id)
        result.prsl_Namepatient=newobj.prsl_Namepatient
        result.prsl_Family = newobj.prsl_Family
        result.prsl_NationalCode=newobj.prsl_NationalCode
        result.prsl_diseasebackground = newobj.prsl_diseasebackground
        result.prsl_Consumabledrugs = newobj.prsl_Consumabledrugs
        result.prsl_Age = newobj.prsl_Age
        session.commit()

    def Update_1(self,obj,id,newobj):
        result = self.ReabById(obj,id)
        result.prsl_Name=newobj.prsl_Name
        result.prsl_Name_E=newobj.prsl_Name_E
        result.prsl_Alternativemedicine=newobj.prsl_Alternativemedicine
        result.prsl_Drugform=newobj.prsl_Drugform
        session.commit()

    def Update_2(self,obj,id,newobj):
        result = self.ReabById(obj,id)
        result.prsl_Name=newobj.prsl_Name
        result.prsl_interference=newobj.prsl_interference
        result.prsl_AlternativeMedizin=newobj.prsl_AlternativeMedizin
        result.prsl_Theintensityoftheinterference=newobj.prsl_Theintensityoftheinterference
        session.commit()

    def Update_3(self,obj,id,newobj):
        result = self.ReabById(obj,id)
        result.prsl_Namepatientturn=newobj.prsl_Namepatientturn
        result.prsl_Famylipatientturn=newobj.prsl_Famylipatientturn
        result.prsl_NationalCodeturn=newobj.prsl_NationalCodeturn
        result.prsl_appointmentdate =newobj.prsl_appointmentdate
        result.prsl_turntime =newobj.prsl_turntime
        session.commit()

    def Update_4(self,obj,id,newobj):
        result= self.ReabById(obj,id)
        result.prsl_DoctorName=newobj.prsl_DoctorName
        result.prsl_FamilyDoctor=newobj.prsl_FamilyDoctor
        result.prsl_DoctorSpecialty=newobj.prsl_DoctorSpecialty
        result.prsl_DoctorPersonnelCode=newobj.prsl_DoctorPersonnelCode
        session.commit()


    def ReabById(self,obj,id):
        return session.query(obj).filter(obj.prsl_id == id).first()

    def ReadByUsernamePasword(self,obj,username,pasword):
        try:
            return session.query(obj).filter(obj.prsl_username == username and obj.prsl_password == pasword).first()
        except Exception as e:
            print(e)
            return False


    def Search_Date(self,obj,text_Name):
        return session.query(obj).filter(obj.prsl_Namepatient== text_Name).all()

    def Search_Date_1(self,obj,text_Name_1):
        return session.query(obj).filter(obj.prsl_Name== text_Name_1).all()

    def Search_Date_2(self, obj, text_Name_1):
        return session.query(obj).filter(obj.prsl_Name == text_Name_1).all()

    def Search_Date_3(self, obj, text_Name_1):
        return session.query(obj).filter(obj.prsl_Namepatientturn  == text_Name_1).all()

    def Search_Date_4(self, obj, text_Name_1):
        return session.query(obj).filter(obj.prsl_DoctorName == text_Name_1).all()

    def Search_Datefrm1(self, obj, text_Name_5):
        return session.query(obj).filter(obj.prsl_NationalCode == text_Name_5).all()





