from tkinter import *
from para_apagar_pc import apagar_sistema as apagar

window = Tk()
window.geometry("400x200")
window.title("temporizador apagado pc")

minutos = IntVar(value=None)


lbl = Label(window, text="Apagar el pc", font=("comic sans",15))
lbl.place(relx=0.5, rely=0.1, anchor=CENTER)

label_minutos = Label(window, text="Ingrese los minutos para apagar la Pc")
label_minutos.place(relx=0.5, rely=0.25, anchor=CENTER)

minutos = Entry(window, exportselection = 0, textvariable=minutos)
minutos.place(relx=0.5, rely=0.4, anchor=CENTER)

button_shutdown = Button(window, text="Apagar",width=10, command=lambda: apagar(int(minutos.get())))
button_shutdown.place(relx=0.39, rely=0.8, anchor=CENTER)
button_cancel = Button(window, text="Salir", width=10, command=lambda:window.destroy())
button_cancel.place(relx=0.65, rely=0.8, anchor=CENTER)

window.mainloop()

