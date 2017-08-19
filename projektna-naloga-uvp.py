from tkinter import *
okno = Tk()
okno.title("Kalkulator")   #naslov okna

#========================================================================

#========================================================================
#VSE FUNKCIJE

def gumbKlik(numbers):    #da deluje klik gumba
    global operacija
    operacija = operacija + str(numbers)
    text_input.set(operacija)

def gumbClearAll():     #izbriše vse
    global operacija
    operacija = ""
    text_input.set("")

def gumbEnako():
    global operacija
    sumup = str(eval(operacija))
    text_input.set(sumup)
    operacija = ""

operacija = ""
text_input = StringVar()              

   
#========================================================================
#VNOSNO POLJE

rezultat = Entry(textvariable = text_input)
rezultat.grid(row = 0, columnspan = 4)


# VSI GUMBI - RAZPOREJENI V GRID
gumb0 = Button(okno, text = "0", command = lambda: gumbKlik(0))
gumb0.grid(row = 5, column = 0)

gumb1 = Button(okno, text = "1", command = lambda: gumbKlik(1))
gumb1.grid(row = 4, column = 0)

gumb2 = Button(okno, text = "2", command = lambda: gumbKlik(2))
gumb2.grid(row = 4, column = 1)

gumb3 = Button(okno, text = "3", command = lambda: gumbKlik(3))
gumb3.grid(row = 4, column = 2)

gumb4 = Button(okno, text = "4", command = lambda: gumbKlik(4))
gumb4.grid(row = 3, column = 0)

gumb5 = Button(okno, text = "5", command = lambda: gumbKlik(5))
gumb5.grid(row = 3, column = 1)

gumb6 = Button(okno, text = "6", command = lambda: gumbKlik(6))
gumb6.grid(row = 3, column = 2)

gumb7 = Button(okno, text = "7", command = lambda: gumbKlik(7))
gumb7.grid(row = 2, column = 0)

gumb8 = Button(okno, text = "8", command = lambda: gumbKlik(8))
gumb8.grid(row = 2, column = 1)

gumb9 = Button(okno, text = "9", command = lambda: gumbKlik(9))
gumb9.grid(row = 2, column = 2)

gumbplus = Button(okno, text = "+", command = lambda: gumbKlik("+"))
gumbplus.grid(row = 5, column = 3)

gumbminus = Button(okno, text = "-", command = lambda: gumbKlik("-"))
gumbminus.grid(row = 4, column = 3)

gumbkrat = Button(okno, text = "x", command = lambda: gumbKlik("*"))
gumbkrat.grid(row = 3, column = 3)


gumbdeljeno = Button(okno, text = "/", command = lambda: gumbKlik("/"))
gumbdeljeno.grid(row = 2, column = 3)

gumboklepajl = Button(okno, text = "(", command = lambda: gumbKlik("("))
gumboklepajl.grid(row = 5, column = 1)

gumboklepajd = Button(okno, text = ")", command = lambda: gumbKlik(")"))
gumboklepajd.grid(row = 5, column = 2)

gumbjeenako = Button(okno, text = "=", command = gumbEnako)
gumbjeenako.grid(row = 6, column = 3)

gumbpika = Button(okno, text = ".", command = lambda: gumbKlik("."))
gumbpika.grid(row = 6, column = 0)

gumbc = Button(okno, text = "C")
gumbc.grid(row = 6, column = 1)

gumbac = Button(okno, text = "AC", command = gumbClearAll)
gumbac.grid(row = 6, column = 2)
                         
#========================================================================
okno.mainloop()
