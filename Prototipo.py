import tkinter as tk
from tkinter import *
import os
from PIL import ImageTk, Image
from tkinter import messagebox as mb


def cancelar():
    mb.showerror("Cancelada", "Su proceso ha sido cancelado")
    ventana.destroy()
    ventanaCupo.destroy()


def confirmar():
    mb.showinfo("Reserva Exitosa", "Su reserva se ha realizado correctamente")
    ventana.destroy()
    ventanaCupo.destroy()


def publicarCompletado():
    mb.showinfo("Publicacion Exitosa",
                "Su publicacion se ha realizado correctamente")
    ventanaPublicar.destroy()


def cancelaReserva():
    mb.showerror("Cancelada", "Su reserva ha sido cancelado")
    ventanaReservas.destroy()


def reservas():
    global ventanaReservas
    ventanaReservas = tk.Toplevel()
    ventanaReservas.title("Reservas activas")
    ventanaReservas.config(width=330, height=300, bg="white")

    wCupoVentana = 330
    hCupoVentana = 300

    pCupoWidth = round(wTotal/2-wCupoVentana/2)
    pCupoHeight = round(hTotal/2-hCupoVentana/2)
    ventanaReservas.geometry(str(wCupoVentana)+"x"+str(hCupoVentana) +
                             "+"+str(pCupoWidth)+"+"+str(pCupoHeight))

    frameUno = Frame(ventanaReservas)
    frameUno.grid(column=0, row=1, columnspan=4)
    frameUno.config(bd=5, relief="sunken", background="White")

    nombreUno = tk.Label(frameUno, text="Joaquin Villamizar", width=15)
    nombreUno.grid(column=0, row=0, columnspan=3)
    nombreUno.config(fg="Blue",    # Foreground
                     bg="White",   # Background
                     font=("Verdana", 25))

    calificacionUno = tk.Label(frameUno, text="4.8 ☆")
    calificacionUno.grid(column=0, row=1, columnspan=1)
    calificacionUno.config(background="White", font=("Verdana", 10))

    placaUno = tk.Label(frameUno, text="FBO538")
    placaUno.grid(column=2, row=1, columnspan=1)
    placaUno.config(background="White", font=("Verdana", 10))

    RutaUno = tk.Label(frameUno, text="Ruta: Unisabana - Boyaca")
    RutaUno.grid(column=0, row=2, columnspan=3)
    RutaUno.config(background="White", font=("Verdana", 10))

    linkUno = tk.Label(
        frameUno, text="Link: https://goo.gl/maps/dgme9x5cc6CZLr6K9")
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

    cancelarReserva = tk.Button(
        frameUno, text="Cancelar Reserva", command=cancelaReserva)
    cancelarReserva.grid(column=0, row=5, columnspan=3)
    cancelarReserva.config(background="White", font=("Verdana", 10))


def cuposUno():
    global ventanaCupo
    ventanaCupo = tk.Toplevel()
    ventanaCupo.title("Cupos disponibles")
    ventanaCupo.config(width=330, height=300, bg="white")

    wCupoVentana = 330
    hCupoVentana = 300

    pCupoWidth = round(wTotal/2-wCupoVentana/2)
    pCupoHeight = round(hTotal/2-hCupoVentana/2)
    ventanaCupo.geometry(str(wCupoVentana)+"x"+str(hCupoVentana) +
                         "+"+str(pCupoWidth)+"+"+str(pCupoHeight))

    circulo = Canvas(ventanaCupo, width=330, height=90, bg='white')
    circulo.grid(column=0, row=0, columnspan=2)
    circulo.create_oval(10, 10, 80, 80, width=5, fill='Green')
    circulo.create_oval(90, 10, 160, 80, width=5, fill='Green')
    circulo.create_oval(170, 10, 240, 80, width=5, fill='Green')
    circulo.create_oval(250, 10, 320, 80, width=5, fill='Red')

    textoCupo = tk.Label(
        ventanaCupo, text="Haga click en la cantidad de puestos que" + "\n" + "necesita")
    textoCupo.grid(column=0, row=1, columnspan=2)
    textoCupo.config(background="White", font=("Verdana", 10))

    cancelarCupo = tk.Button(ventanaCupo, text="Cancelar", command=cancelar)
    cancelarCupo.grid(column=1, row=2)
    cancelarCupo.config(background="White", font=("Verdana", 10))

    confirmarCupo = tk.Button(ventanaCupo, text="Confirmar", command=confirmar)
    confirmarCupo.grid(column=0, row=2)
    confirmarCupo.config(background="White", font=("Verdana", 10))


def publicar():
    global ventanaPublicar
    ventanaPublicar = tk.Toplevel()
    ventanaPublicar.title("Publicar")
    ventanaPublicar.config(width=330, height=300, bg="white")

    wCupoVentana = 330
    hCupoVentana = 300

    pCupoWidth = round(wTotal/2-wCupoVentana/2)
    pCupoHeight = round(hTotal/2-hCupoVentana/2)
    ventanaPublicar.geometry(
        str(wCupoVentana)+"x"+str(hCupoVentana)+"+"+str(pCupoWidth)+"+"+str(pCupoHeight))

    titulo = tk.Label(ventanaPublicar, text="Publicar Wheels", width=15)
    titulo.grid(column=0, row=0, columnspan=2)
    titulo.config(fg="Blue",    # Foreground
                  bg="White",   # Background
                  font=("Verdana", 25))

    nombreUno = tk.Label(ventanaPublicar, text="Nombre:", width=20, height=2)
    nombreUno.grid(column=0, row=1, columnspan=1)
    nombreUno.config(background="White", font=("Verdana", 10))

    calificacionUno = tk.Label(ventanaPublicar, text="Precio:")
    calificacionUno.grid(column=0, row=2, columnspan=1)
    calificacionUno.config(background="White", font=("Verdana", 10))

    placaUno = tk.Label(ventanaPublicar, text="Placa:", height=2)
    placaUno.grid(column=0, row=3, columnspan=1)
    placaUno.config(background="White", font=("Verdana", 10))

    RutaUno = tk.Label(ventanaPublicar, text="Ruta:")
    RutaUno.grid(column=0, row=4, columnspan=1)
    RutaUno.config(background="White", font=("Verdana", 10))

    linkUno = tk.Label(ventanaPublicar, text="Maps:", height=2)
    linkUno.grid(column=0, row=5, columnspan=1)
    linkUno.config(background="White", font=("Verdana", 10))

    horaUno = tk.Label(ventanaPublicar, text="Hora:")
    horaUno.grid(column=0, row=6, columnspan=1)
    horaUno.config(background="White", font=("Verdana", 10))

    fechaUno = tk.Label(ventanaPublicar, text="Fecha:", height=2)
    fechaUno.grid(column=0, row=7, columnspan=1)
    fechaUno.config(background="White", font=("Verdana", 10))

    entryDos = tk.Entry(ventanaPublicar, highlightcolor="blue",
                        highlightbackground="black",
                        highlightthickness=2)
    entryDos.grid(column=1, row=1)

    entryTres = tk.Entry(ventanaPublicar, highlightcolor="blue",
                         highlightbackground="black",
                         highlightthickness=2)
    entryTres.grid(column=1, row=2)

    entryCuatro = tk.Entry(ventanaPublicar, highlightcolor="blue",
                           highlightbackground="black",
                           highlightthickness=2)
    entryCuatro.grid(column=1, row=3)

    entryCinco = tk.Entry(ventanaPublicar, highlightcolor="blue",
                          highlightbackground="black",
                          highlightthickness=2)
    entryCinco.grid(column=1, row=4)

    entrySeis = tk.Entry(ventanaPublicar, highlightcolor="blue",
                         highlightbackground="black",
                         highlightthickness=2)
    entrySeis.grid(column=1, row=5)

    entrySiete = tk.Entry(ventanaPublicar, highlightcolor="blue",
                          highlightbackground="black",
                          highlightthickness=2)
    entrySiete.grid(column=1, row=6)

    entryUno = tk.Entry(ventanaPublicar, highlightcolor="blue",
                        highlightbackground="black",
                        highlightthickness=2)
    entryUno.grid(column=1, row=7)

    buttonPublicar = tk.Button(
        ventanaPublicar, text="Publicar", command=publicarCompletado)
    buttonPublicar.grid(column=0, row=8, columnspan=2)
    buttonPublicar.config(background="White", font=("Verdana", 10))


def ventanaBusqueda():

    global logo
    global logoUnisabanaz
    global ventana
    ventana = tk.Toplevel()
    ventana.config(bd=10, background="White")

    ventana.geometry(str(wVentana)+"x"+str(hVentana) +
                     "+"+str(pWidth)+"+"+str(pHeight))

    framePrincipal = Frame(ventana)
    framePrincipal.grid(column=0, row=0)
    framePrincipal.config(bg="white", width=350, height=790)

    logo = ImageTk.PhotoImage(Image.open(os.path.join(
        "images", "logo_wheels.png")).resize((150, 44)))
    logoUnisabana = Label(framePrincipal, image=logo)
    logoUnisabana.grid(column=0, row=0, columnspan=2)
    logoUnisabana.config(background="white")

    usuario = tk.Label(framePrincipal, text="Juan G.")
    usuario.grid(column=3, row=0)
    usuario.config(background="White", font=("Verdana", 10))

    # Primer Frame
    frameUno = Frame(framePrincipal)
    frameUno.grid(column=0, row=1, columnspan=4)
    frameUno.config(bd=5, relief="sunken", background="White")

    nombreUno = tk.Label(frameUno, text="Joaquin Villamizar", width=15)
    nombreUno.grid(column=0, row=0, columnspan=3)
    nombreUno.config(fg="Blue",    # Foreground
                     bg="White",   # Background
                     font=("Verdana", 25))

    calificacionUno = tk.Label(frameUno, text="4.8 ☆")
    calificacionUno.grid(column=0, row=1, columnspan=1)
    calificacionUno.config(background="White", font=("Verdana", 10))

    placaUno = tk.Label(frameUno, text="FBO538")
    placaUno.grid(column=2, row=1, columnspan=1)
    placaUno.config(background="White", font=("Verdana", 10))

    RutaUno = tk.Label(frameUno, text="Ruta: Unisabana - Boyaca")
    RutaUno.grid(column=0, row=2, columnspan=3)
    RutaUno.config(background="White", font=("Verdana", 10))

    linkUno = tk.Label(
        frameUno, text="Link: https://goo.gl/maps/dgme9x5cc6CZLr6K9")
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

    ReservarUno = tk.Button(frameUno, text="Reservar", command=cuposUno)
    ReservarUno.grid(column=0, row=5, columnspan=3)
    ReservarUno.config(background="White", font=("Verdana", 10))

    # Segundo Frame
    frameDos = Frame(framePrincipal)
    frameDos.grid(column=0, row=2, columnspan=4)
    frameDos.config(bd=5, relief="sunken", background="White")

    nombreDos = tk.Label(frameDos, text="Juana Alamenda", width=15)
    nombreDos.grid(column=0, row=0, columnspan=3)
    nombreDos.config(fg="blue",    # Foreground
                     bg="White",   # Background
                     font=("Verdana", 25))

    calificacionDos = tk.Label(frameDos, text="3.9 ☆")
    calificacionDos.grid(column=0, row=1, columnspan=1)
    calificacionDos.config(background="White", font=("Verdana", 10))

    placaDos = tk.Label(frameDos, text="HBO392")
    placaDos.grid(column=2, row=1, columnspan=1)
    placaDos.config(background="White", font=("Verdana", 10))

    rutaDos = tk.Label(frameDos, text="Ruta: Autopista - Unisabana")
    rutaDos.grid(column=0, row=2, columnspan=3)
    rutaDos.config(background="White", font=("Verdana", 10))

    linkDos = tk.Label(
        frameDos, text="Link: https://goo.gl/maps/LDQu3P6Fg9LoXNaNA")
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

    ReservarDos = tk.Button(frameDos, text="Reservar", command=cuposUno)
    ReservarDos.grid(column=0, row=5, columnspan=3)
    ReservarDos.config(background="White", font=("Verdana", 10))

    # Tercer Frame
    frameTres = Frame(framePrincipal)
    frameTres.grid(column=0, row=3, columnspan=4)
    frameTres.config(bd=5, relief="sunken", background="White")

    nombreTres = tk.Label(frameTres, text="Hernan Fuentes", width=15)
    nombreTres.grid(column=0, row=0, columnspan=3)
    nombreTres.config(fg="blue",    # Foreground
                      bg="White",   # Background
                      font=("Verdana", 25))

    calificacionTres = tk.Label(frameTres, text="5.0 ☆")
    calificacionTres.grid(column=0, row=1, columnspan=1)
    calificacionTres.config(background="White", font=("Verdana", 10))

    placaTres = tk.Label(frameTres, text="SGC941")
    placaTres.grid(column=2, row=1, columnspan=1)
    placaTres.config(background="White", font=("Verdana", 10))

    RutaTres = tk.Label(frameTres, text="Ruta: Chia Variante - Unisabana")
    RutaTres.grid(column=0, row=2, columnspan=3)
    RutaTres.config(background="White", font=("Verdana", 10))

    linkTres = tk.Label(
        frameTres, text="Link: https://goo.gl/maps/47diZBhFFt3vSieJ8")
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

    ReservarTres = tk.Button(frameTres, text="Reservar", command=cuposUno)
    ReservarTres.grid(column=0, row=5, columnspan=3)
    ReservarTres.config(background="White", font=("Verdana", 10))


ventanaPrincipal = tk.Tk()
ventanaPrincipal.config(bd=10, background="White")
wTotal = ventanaPrincipal.winfo_screenwidth()
hTotal = ventanaPrincipal.winfo_screenheight()

wVentana = 350
hVentana = 790

pWidth = round(wTotal/2-wVentana/2)
pHeight = round(hTotal/2-hVentana/2)
ventanaPrincipal.geometry(
    str(wVentana)+"x"+str(hVentana)+"+"+str(pWidth)+"+"+str(pHeight))

logoPrincipal = ImageTk.PhotoImage(Image.open(
    os.path.join("images", "logo_wheels.png")).resize((150, 44)))
logoUnisabanaP = Label(ventanaPrincipal, image=logoPrincipal)
logoUnisabanaP.grid(column=0, row=0, columnspan=1)
logoUnisabanaP.config(background="white")

usuarioPrincipal = tk.Label(ventanaPrincipal, text="Juan G.")
usuarioPrincipal.grid(column=1, row=0)
usuarioPrincipal.config(background="White", font=("Verdana", 10))

labelTitulo = tk.Label(
    ventanaPrincipal, text="¿Que ruta necesitas el dia de hoy?", width=29)
labelTitulo.grid(column=0, row=2, columnspan=2)
labelTitulo.config(fg="blue",    # Foreground
                   bg="White",   # Background
                   font=("Verdana", 13))

labelSeguridad = tk.Label(ventanaPrincipal, text="Como universidad queremos asegurarnos de que" + "\n" +
                          "llegues a tu casa de manera comoda y segura")
labelSeguridad.grid(column=0, row=3, columnspan=2)
labelSeguridad.config(background="White", font=("Verdana", 10))

frameEscoger = Frame(ventanaPrincipal)
frameEscoger.grid(column=0, row=4, columnspan=2)
frameEscoger.config(bd=5, relief="sunken", background="White")

recogerBusqueda = tk.Label(frameEscoger, text="Ruta a escoger:")
recogerBusqueda.grid(column=0, row=0, columnspan=2)
recogerBusqueda.config(background="White", font=("Verdana", 10))

casaIcono = ImageTk.PhotoImage(Image.open(
    os.path.join("images", "casa_icono.png")).resize((30, 30)))
casaUnisabana = Label(frameEscoger, image=casaIcono)
casaUnisabana.grid(column=0, row=1, columnspan=1)
casaUnisabana.config(background="white")

entryCasa = tk.Entry(frameEscoger, width=20, font="Verdana, 10", highlightcolor="blue",
                     highlightbackground="black",
                     highlightthickness=2)
entryCasa.grid(column=1, row=1)

calendarioIcono = ImageTk.PhotoImage(Image.open(
    os.path.join("images", "calendario_icono.png")).resize((30, 30)))
calendarioUnisabana = Label(frameEscoger, image=calendarioIcono)
calendarioUnisabana.grid(column=0, row=2, columnspan=1)
calendarioUnisabana.config(background="white")

entryReserva = tk.Entry(frameEscoger, width=20, font="Verdana, 10", highlightcolor="blue",
                        highlightbackground="black",
                        highlightthickness=2)
entryReserva.grid(column=1, row=2)

buttonBuscar = tk.Button(frameEscoger, text="Buscar", command=ventanaBusqueda)
buttonBuscar.grid(column=0, row=3, columnspan=2)
buttonBuscar.config(background="White", font=("Verdana", 10))


labelTrayectos = tk.Label(
    ventanaPrincipal, text="Rutas o trayectos preferidos")
labelTrayectos.grid(column=0, row=5, columnspan=2)
labelTrayectos.config(fg="blue",    # Foreground
                      bg="White",   # Background
                      font=("Verdana", 13))

ReservarUno = Frame(ventanaPrincipal)
ReservarUno.grid(column=0, row=6)
ReservarUno.config(bd=5, relief="sunken", background="White")

labelInformacion = tk.Label(ReservarUno, text="Nombre: Juan Perez" + "\n" +
                            "Telefono: 3213456676" + "\n" +
                            "Unisabana - Boyaca" + "\n" +
                            "Hora salida: 17:30" + "\n" +
                            "Precio : $5000" + "\n" +
                            "Placa: RIL945")

labelInformacion.grid(column=0, row=0)
labelInformacion.config(background="White", font=("Verdana", 10))

ReservarDos = Frame(ventanaPrincipal)
ReservarDos.grid(column=1, row=6)
ReservarDos.config(bd=5, relief="sunken", background="White")

labelInformacion = tk.Label(ReservarDos, text="Nombre: Juan Perez" + "\n" +
                            "Telefono: 3213456676" + "\n" +
                            "Boyaca - Unisabana" + "\n" +
                            "Hora llegada: 7:00" + "\n" +
                            "Precio : $5000" + "\n" +
                            "Placa: RIL945")

labelInformacion.grid(column=0, row=0)
labelInformacion.config(background="White", font=("Verdana", 10))

ReservarTres = Frame(ventanaPrincipal)
ReservarTres.grid(column=0, row=7)
ReservarTres.config(bd=5, relief="sunken", background="White")

labelInformacion = tk.Label(ReservarTres, text="Nombre: Ana Estrada" + "\n" +
                            "Telefono: 3145672344" + "\n" +
                            "Unisabana - Heroes" + "\n" +
                            "Hora salida: 14:00" + "\n" +
                            "Precio : $5000" + "\n" +
                            "Placa: GHB765")

labelInformacion.grid(column=0, row=0)
labelInformacion.config(background="White", font=("Verdana", 10))

ReservarCuatro = Frame(ventanaPrincipal)
ReservarCuatro.grid(column=1, row=7)
ReservarCuatro.config(bd=5, relief="sunken", background="White")

labelInformacion = tk.Label(ReservarCuatro, text="Nombre: Ana Estrada" + "\n" +
                            "Telefono: 3145672344" + "\n" +
                            "Heroes - Unisabana" + "\n" +
                            "Hora llegada: 10:00" + "\n" +
                            "Precio : $5000" + "\n" +
                            "Placa: GHB765")

labelInformacion.grid(column=0, row=0)
labelInformacion.config(background="White", font=("Verdana", 10))

nuevaRuta = tk.Button(ventanaPrincipal, text="Publicar ruta", command=publicar)
nuevaRuta.grid(column=0, row=8, columnspan=2)
nuevaRuta.config(background="White", font=("Verdana", 10))

reservaActiva = tk.Button(
    ventanaPrincipal, text="Reservas Activas", command=reservas)
reservaActiva.grid(column=0, row=9, columnspan=2)
reservaActiva.config(background="White", font=("Verdana", 10))


tk.mainloop()
