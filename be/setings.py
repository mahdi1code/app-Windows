class Setting:
    def GetConectionStrinh(self):
        with open("constr.txt") as F:
            return str(F.read())
