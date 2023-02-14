import tkinter as tk
from tkinter import *
import os
from PIL import ImageTk, Image

ventana = tk.Tk()
ventana.geometry("350x800")
ventana.config(bd=10, background="White")


framePrincipal = Frame(ventana)
framePrincipal.grid(column=0,row=0)
framePrincipal.config(bg="white", width=350, height=790)

logo = ImageTk.PhotoImage(Image.open(os.path.join("images","logo_wheels.png")).resize((150,44)))
logoUnisabana = Label(framePrincipal, image=logo)
logoUnisabana.grid(column=0, row=0, columnspan=2)
logoUnisabana.config(background="white")

usuario = tk.Label(framePrincipal, text="Juan G.")
usuario.grid(column=3, row=0)
usuario.config(background="White", font=("Verdana", 10))

frameUno = Frame(framePrincipal)
frameUno.grid(column=0, row=1, columnspan=4)
frameUno.config(bd=5, relief="sunken", background="White")

nombreUno = tk.Label(frameUno, text="Joaquin Villamizar", width=15)
nombreUno.grid(column=0, row=0, columnspan=3)
nombreUno.config(fg="Blue",    # Foreground
             bg="White",   # Background
             font=("Verdana",25))


calificacionUno = tk.Label(frameUno, text="4.8 ☆")
calificacionUno.grid(column=0, row=1, columnspan=1)
calificacionUno.config(background="White", font=("Verdana", 10))

placaUno = tk.Label(frameUno, text="FBO538")
placaUno.grid(column=2, row=1, columnspan=1)
placaUno.config(background="White", font=("Verdana", 10))

RutaUno = tk.Label(frameUno, text="Ruta: Unisabana - Boyaca")
RutaUno.grid(column=0, row=2, columnspan=3)
RutaUno.config(background="White", font=("Verdana", 10))

linkUno = tk.Label(frameUno, text="Link: https://goo.gl/maps/dgme9x5cc6CZLr6K9")
linkUno.grid(column=0, row=3, columnspan=3)
linkUno.config(background="White", font=("Verdana", 10))

horaUno = tk.Label(frameUno, text="Hora: 14:00")
horaUno.grid(column=0, row=4, columnspan=1)
horaUno.config(background="White", font=("Verdana", 10))

fechaUno = tk.Label(frameUno, text="14/02/2023")
fechaUno.grid(column=1, row=4, columnspan=1)
fechaUno.config(background="White", font=("Verdana", 10))

precioUno = tk.Label(frameUno, text="$5.000")
precioUno.grid(column=2, row=4, columnspan=1)
precioUno.config(background="White", font=("Verdana", 10))

ReservarUno = tk.Button(frameUno, text="Reservar")
ReservarUno.grid(column=0, row=5, columnspan=3)
ReservarUno.config(background="White", font=("Verdana", 10))


frameDos = Frame(framePrincipal)
frameDos.grid(column=0, row=2, columnspan=4)
frameDos.config(bd=5, relief="sunken", background="White")

nombreDos = tk.Label(frameDos, text="Juana Alamenda", width=15)
nombreDos.grid(column=0, row=0, columnspan=3)
nombreDos.config(fg="blue",    # Foreground
             bg="White",   # Background
             font=("Verdana",25))


calificacionDos = tk.Label(frameDos, text="3.9 ☆")
calificacionDos.grid(column=0, row=1, columnspan=1)
calificacionDos.config(background="White", font=("Verdana", 10))

placaDos = tk.Label(frameDos, text="HBO392")
placaDos.grid(column=2, row=1, columnspan=1)
placaDos.config(background="White", font=("Verdana", 10))

rutaDos = tk.Label(frameDos, text="Ruta: Autopista - Unisabana")
rutaDos.grid(column=0, row=2, columnspan=3)
rutaDos.config(background="White", font=("Verdana", 10))

linkDos = tk.Label(frameDos, text="Link: https://goo.gl/maps/LDQu3P6Fg9LoXNaNA")
linkDos.grid(column=0, row=3, columnspan=3)
linkDos.config(background="White", font=("Verdana", 10))

horaDos = tk.Label(frameDos, text="Hora: 9:00")
horaDos.grid(column=0, row=4, columnspan=1)
horaDos.config(background="White", font=("Verdana", 10))

fechaDos = tk.Label(frameDos, text="14/02/2023")
fechaDos.grid(column=1, row=4, columnspan=1)
fechaDos.config(background="White", font=("Verdana", 10))

precioDos = tk.Label(frameDos, text="$5.000")
precioDos.grid(column=2, row=4, columnspan=1)
precioDos.config(background="White", font=("Verdana", 10))

ReservarDos = tk.Button(frameDos, text="Reservar")
ReservarDos.grid(column=0, row=5, columnspan=3)
ReservarDos.config(background="White", font=("Verdana", 10))



frameTres = Frame(framePrincipal)
frameTres.grid(column=0, row=3, columnspan=4)
frameTres.config(bd=5, relief="sunken", background="White")

nombreTres = tk.Label(frameTres, text="Hernan Fuentes", width=15)
nombreTres.grid(column=0, row=0, columnspan=3)
nombreTres.config(fg="blue",    # Foreground
             bg="White",   # Background
             font=("Verdana",25))


calificacionTres = tk.Label(frameTres, text="5.0 ☆")
calificacionTres.grid(column=0, row=1, columnspan=1)
calificacionTres.config(background="White", font=("Verdana", 10))

placaTres = tk.Label(frameTres, text="SGC941")
placaTres.grid(column=2, row=1, columnspan=1)
placaTres.config(background="White", font=("Verdana", 10))

RutaTres = tk.Label(frameTres, text="Ruta: Chia Variante - Unisabana")
RutaTres.grid(column=0, row=2, columnspan=3)
RutaTres.config(background="White", font=("Verdana", 10))

linkTres = tk.Label(frameTres, text="Link: https://goo.gl/maps/47diZBhFFt3vSieJ8")
linkTres.grid(column=0, row=3, columnspan=3)
linkTres.config(background="White", font=("Verdana", 10))

horaTres = tk.Label(frameTres, text="Hora: 7:00")
horaTres.grid(column=0, row=4, columnspan=1)
horaTres.config(background="White", font=("Verdana", 10))

fechaTres = tk.Label(frameTres, text="14/02/2023")
fechaTres.grid(column=1, row=4, columnspan=1)
fechaTres.config(background="White", font=("Verdana", 10))

precioTres = tk.Label(frameTres, text="$4.000")
precioTres.grid(column=2, row=4, columnspan=1)
precioTres.config(background="White", font=("Verdana", 10))

ReservarTres = tk.Button(frameTres, text="Reservar")
ReservarTres.grid(column=0, row=5, columnspan=3)
ReservarTres.config(background="White", font=("Verdana", 10))
tk.mainloop()
