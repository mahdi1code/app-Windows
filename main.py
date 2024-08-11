from tkinter import *
from pl.form import appearance
#from be.setings import *
import pyodbc
if __name__ == "__main__":
    screen= Tk()
    screen.geometry("%dx%d+%d+%d" % (900, 400, 100, 100))
    PageMe=appearance.App(screen)
    screen.mainloop()