from tkinter import *
janela = Tk()

rotulo = Label(janela, text="Que legal!")
rotulo.grid(row=0, column=0)
rotulo["font"] = ("Arial","18","bold", "italic")
rotulo["fg"] = "red"
rotulo["bg"] = "white"

outro_rot = Label(janela, text ="Gostei disso!")
outro_rot.grid(row=1, column=1)
outro_rot["font"] = ("Verdana","14")
outro_rot["fg"] = "blue"
outro_rot["bg"] = "yellow"
                 
janela.mainloop()