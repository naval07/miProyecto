import tkinter as tk

def crearData():
    print(data.get())

win = tk.Tk()
win.title("Crear plantilla")
#win.geometry("300x50")
frame = tk.Frame(win)
frame.pack()
tk.Label(frame, text = "Ingrese el nombre").grid(row = 0, column = 0)
tk.Label(frame, text = "de su plantilla: ").grid(row = 1, column = 0)
data = tk.StringVar()
d = tk.Entry(frame, textvariable = data)
d.grid(row = 1, column = 1)
imprimir = tk.Button(frame, text = "Crear", command = crearData).grid(row = 2, column = 0)
win.mainloop()
