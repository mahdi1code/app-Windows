from be.clinic import *
from dal.Repository import Repository

class operations():

    def Add(self, obj):

            rps=Repository()
            return rps.Add(obj)

        #else:
        #return False


    def Raed(self,obj):
        rps = Repository()
        return rps.Read(obj)

    def Update(self,obj,id,newobj):
        rps = Repository()
        rps.Update(obj,id,newobj)

    def Update_1(self,obj,id,newobj):
        rps = Repository()
        rps.Update_1(obj, id, newobj)

    def Update_2(self,obj,id,newobj):
        rps = Repository()
        rps.Update_2(obj, id, newobj)

    def Update_3(self,obj,id,newobj):
        rps= Repository()
        rps.Update_3(obj, id, newobj)

    def Update_4(self,obj,id,newobj):
        rps = Repository()
        rps.Update_4(obj, id, newobj)


    def Delete(self,obj):
        rps = Repository()
        rps.Delete(obj)

    def ReadById(self,obj,id):
        rps = Repository()
        return rps.ReabById(obj,id)

    def ReadByUsernamePasword(self,obj,username,pasword):
        rps= Repository()
        return rps.ReadByUsernamePasword(obj,username,pasword)
    def DeleteRow(self,obj,id):
        rps = Repository()
        object = rps.ReabById(obj,id)
        return rps.Delete(object)

    def Search_Date(self,obj,text_Name):
        rps = Repository()
        return rps.Search_Date(obj,text_Name)

    def Search_Date_1(self, obj, text_Name_1):
        rps = Repository()
        return rps.Search_Date_1(obj, text_Name_1)


    def Search_Date_2(self, obj, text_Name_2):
        rps = Repository()
        return rps.Search_Date_2(obj, text_Name_2)

    def Search_Date_3(self, obj, text_Name_3):
        rps = Repository()
        return rps.Search_Date_3(obj, text_Name_3)

    def Search_Date_4(self, obj, text_Name_4):
        rps= Repository()
        return rps.Search_Date_4(obj, text_Name_4)

    def Search_Datefrm1(self, obj, text_Name_5):
        rps= Repository()
        return rps.Search_Datefrm1(obj, text_Name_5)




