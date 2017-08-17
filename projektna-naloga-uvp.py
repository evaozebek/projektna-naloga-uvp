import tkinter as tk
okno = tk.Tk()
import math

#################


# VSI GUMBI - RAZPOREJENI V GRID
gumb0 = tk.Button(okno, text = "0")
gumb0.grid(row = 5, column = 0)

gumb1 = tk.Button(okno, text = "1")
gumb1.grid(row = 4, column = 0)

gumb2 = tk.Button(okno, text = "2")
gumb2.grid(row = 4, column = 1)

gumb3 = tk.Button(okno, text = "3")
gumb3.grid(row = 4, column = 2)

gumb4 = tk.Button(okno, text = "4")
gumb4.grid(row = 3, column = 0)

gumb5 = tk.Button(okno, text = "5")
gumb5.grid(row = 3, column = 1)

gumb6 = tk.Button(okno, text = "6")
gumb6.grid(row = 3, column = 2)

gumb7 = tk.Button(okno, text = "7")
gumb7.grid(row = 2, column = 0)

gumb8 = tk.Button(okno, text = "8")
gumb8.grid(row = 2, column = 1)

gumb9 = tk.Button(okno, text = "9")
gumb9.grid(row = 2, column = 2)

gumbplus = tk.Button(okno, text = "+")
gumbplus.grid(row = 5, column = 3)

gumbminus = tk.Button(okno, text = "-")
gumbminus.grid(row = 4, column = 3)

gumbkrat = tk.Button(okno, text = "x")
gumbkrat.grid(row = 3, column = 3)

gumbdeljeno = tk.Button(okno, text = "/")
gumbdeljeno.grid(row = 2, column = 3)

gumboklepajl = tk.Button(okno, text = "(")
gumboklepajl.grid(row = 5, column = 1)

gumboklepajd = tk.Button(okno, text = ")")
gumboklepajd.grid(row = 5, column = 2)

gumbjeenako = tk.Button(okno, text = "=")
gumbjeenako.grid(row = 6, column = 3)

gumbpika = tk. Button(okno, text = ".")
gumbpika.grid(row = 6, column = 0)

gumbc = tk.Button(okno, text = "C")
gumbc.grid(row = 6, column = 1)

gumbac = tk.Button(okno, text = "AC")
gumbac.grid(row = 6, column = 2)
                         
 #VNOSNO POLJE

vhod = tk.Entry(okno)
vhod.grid(row = 0, columnspan = 4)








####################
okno.mainloop()
