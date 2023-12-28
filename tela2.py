import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("Meu Programa")
        #setting window size
        width=400
        height=300
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_465=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_465["font"] = ft
        GLabel_465["fg"] = "#333333"
        GLabel_465["justify"] = "center"
        GLabel_465["text"] = "Nome:"
        GLabel_465.place(x=30,y=30,width=70,height=25)

        GLineEdit_617=tk.Entry(root)
        GLineEdit_617["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_617["font"] = ft
        GLineEdit_617["fg"] = "#333333"
        GLineEdit_617["justify"] = "center"
        GLineEdit_617["text"] = ""
        GLineEdit_617.place(x=120,y=30,width=247,height=30)

        GButton_771=tk.Button(root)
        GButton_771["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_771["font"] = ft
        GButton_771["fg"] = "#000000"
        GButton_771["justify"] = "center"
        GButton_771["text"] = "Salvar"
        GButton_771.place(x=300,y=80,width=70,height=25)
        GButton_771["command"] = self.GButton_771_command

    def GButton_771_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
