import tkinter as tk
from tkinter import messagebox
import string
from tkinter import font

class WinAlineamiento:

    def __init__(self, win, title, frame, alineaciones, see = False, add = False, dele = False):
        self.see = see
        self.add = add
        self.dele = dele
        self.alis = alineaciones
        self.win = win
        self.frame = frame
        self.title = title

        def insert():
            self.num = ["1","2","3","4","5","6","7","8","9"]
            plys = 1
            for q in self.d.get():
                if q in self.num:
                    plys += int(q)
            l = len(self.d.get())
            c = 0
            for q in self.d.get():
                if q in string.punctuation and q != "-":
                    c += 1
            if c != 0:
                messagebox.showwarning("Error", "Ingrese una alineacion valida")
            else:
                if 3 > l or 4 < l or plys != 11:
                    messagebox.showwarning("Error", "Ingrese una alineacion valida")
                    self.d.delete(0,tk.END)
                else:
                    for q in range(1,l + 2,2):
                        self.d.insert(q, "-")
                    a = ask()
                    if a == False:
                        self.d.delete(0, tk.END)
                    else:
                        if self.d.get() not in self.alis:
                            self.alis += [self.d.get()]
                            print(self.alis)
                            win.destroy()
                        #else:
                        #    messagebox.showwarning("Error", "Esta alineacion ya existe")
                        #    self.d.delete(0, tk.END)

        def ask():
            x = messagebox.askyesno(title = "Guardar", message = "¿Guardar "+ self.d.get() + "?")
            return x

        if self.add == True:
            win = self.win
            win.title(self.title)
            win.resizable(False,False)
            frame = self.frame

            self.var = tk.StringVar()

            tk.Label(frame, text = "Nueva alineacion: ").grid(padx = 10, pady = 10, sticky = "e")
            self.d = tk.Entry(frame, textvariable = self.var)
            self.d.grid(row = 0, column = 1, padx = 3, pady = 10)
            tk.Label(frame, text = 'Ej: "442", "4231"').grid(row = 0, column = 2)
            tk.Button(win, text = "guardar", command = insert).pack()

        else:
            if len(self.alis) == 0:
                win = self.win
                win.withdraw()
                msj = "No tiene alineaciones"
                messagebox.showinfo("Alineaciones", msj)
                win.destroy()
            else:
                if self.see == True:
                    win = self.win
                    win.withdraw()
                    msj = ""
                    for q in range(0, len(self.alis)):
                        n = q + 1
                        msj += f"{n}~  [" + self.alis[q] + "]\n\n"
                    m = messagebox.showinfo("alis", msj )

                elif self.dele == True:
                    win = self.win
                    win.title(title)
                    self.frame.pack_forget()

                    def rm():
                        for q in range(0, len(self.alis)):
                            if self.d.get() == q:
                                msg = "¿Desea eliminar la alinleacion " + self.alis[q] + "?"
                                r = messagebox.askyesno(message = msg, title = "Eliminar")
                                if r == True:
                                    msg2 = "La alineacion " + self.alis[q] +" se ha eliminado"
                                    self.alis.pop(q)
                                    messagebox.showinfo(title = "Hecho", message = msg2)
                                    win.destroy()

                    self.d = tk.IntVar()

                    self.font = font.Font(size = 12, weight = "bold")
                    tk.Label(win, text= "Alineaciones", font = self.font).pack(side = "top")

                    c = 0
                    for q in self.alis:
                        x = tk.Radiobutton(self.frame, text = q, variable = self.d, value = c).grid(row = c, column = 0, sticky= "w")
                        c += 1

                    self.frame.pack()
                    delete = tk.Button(win, text = "Eliminar", command = rm).pack()

class ChooseAl():

    def __init__(self, win, bg, bgim, list):
        self.bgim = bgim
        self.bg = bg
        self.window = win
        self.als = list
        self.num = ["1","2","3","4","5","6","7","8","9"]

        self.win = tk.Tk()
        self.frame = tk.Frame(self.win)
        self.frame.pack()

        self.al = tk.IntVar(self.frame)

        tk.Label(self.frame, text = "Alineacion: ").grid(sticky = "nw")

        c = 0
        for q in self.als:
            tk.Radiobutton(self.frame, text = q, variable = self.al, value = c).grid(row = c, column = 1)
            c += 1

        self.font = font.Font(size = 12, weight = "bold", family = "DejaVu Sans")

        def change(al):
            if al == "4-2-3-1":
                self.bg.pack_forget()
                self.label = tk.Label(win, image = self.bgim)
                self.label.pack()
                # Arquero
                tk.Button(win).place(x = 660, y = 200, height = 50, width = 50)
                # Lateral D Central D Central I Lateral I
                tk.Button(win).place(x = 530, y = 20, height = 50, width = 50)
                tk.Button(win).place(x = 580, y = 140, height = 50, width = 50)
                tk.Button(win).place(x = 580, y = 260, height = 50, width = 50)
                tk.Button(win).place(x = 530, y = 375, height = 50, width = 50)
                # 6 D 6 I
                tk.Button(win).place(x = 450, y = 140, height = 50, width = 50)
                tk.Button(win).place(x = 450, y = 260, height = 50, width = 50)
                # extremo D Mediapunta extremo I delantero
                tk.Button(win).place(x = 360, y = 45, height = 50, width = 50)
                tk.Button(win).place(x = 360, y = 200, height = 50, width = 50)
                tk.Button(win).place(x = 360, y = 355, height = 50, width = 50)
                tk.Button(win).place(x = 260, y = 200, height = 50, width = 50)

                def change2(al):
                    if al == "4-2-3-1":
                        self.label.pack_forget()

                tk.Button(win, text = "Invertir", height = 3, width = 12, bg = "lightgreen", command = lambda: change2(al)).place(x = 80, y = 200)


        def ordenar(win):
            a = self.als[self.al.get()]
            # Arquero
            tk.Button(win).place(x = 40, y = 200, height = 50, width = 50)
            if a == "4-2-3-1":
                #Defensa de 4
                # Lateral I, Central I, Central D, Lateral D
                tk.Button(win).place(x = 180, y = 20, height = 50, width = 50)
                tk.Button(win).place(x = 122, y = 140, height = 50, width = 50)
                tk.Button(win).place(x = 122, y = 260, height = 50, width = 50)
                tk.Button(win).place(x = 180, y = 375, height = 50, width = 50)
                # mediocampo
                # 6 I, 6 D
                tk.Button(win).place(x = 252, y = 140, height = 50, width = 50)
                tk.Button(win).place(x = 252, y = 260, height = 50, width = 50)
                # mediocampo 2
                #Extremo I, Mediapunta, Extremo D
                tk.Button(win).place(x = 335, y = 45, height = 50, width = 50)
                tk.Button(win).place(x = 335, y = 200, height = 50, width = 50)
                tk.Button(win).place(x = 335, y = 350, height = 50, width = 50)
                # Delanteros
                tk.Button(win).place(x = 435, y = 200, height = 50, width = 50)
                # Cambio de cancha
                tk.Button(win, text = "Invertir", height = 3, width = 12, bg = "lightgreen", command = lambda: change(a)).place(x = 600, y = 180)
                self.win.destroy()

        tk.Button(self.win, text = "Empezar", command = lambda: ordenar(self.window)).pack()

        self.win.mainloop()



"""win = tk.Tk()
frame = tk.Frame(win)
al = []
frame.pack()
x = WinAlineamiento(win, "Agregar Alineacion", frame, al, add = True)
win.mainloop()"""
