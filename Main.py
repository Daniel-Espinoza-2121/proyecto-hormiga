from tkinter import Tk, Button, Label, Canvas, IntVar, Radiobutton, Scale
from laberinto import Laberinto  # Asegúrate de que la clase Laberinto esté importada correctamente
from hormiga import hormiga
import numpy as np

root = Tk()
root.title("Hormiga")
root.geometry("500x500")
root.resizable(width=False, height=False)
root.configure(bg="green")
fuente = ("Arial", 12)

editable = False

def mostrar_inicio():
    label_size_tablero.pack(anchor="center")
    scale_size_tablero.pack(anchor="center")
    boton_crear.pack(anchor="center")

def ocultar_inicio():
    label_size_tablero.forget()
    scale_size_tablero.forget()
    boton_crear.forget()

def crear_tablero():
    global canva, tablero, HORMIGA
    size = scale_size_tablero.get()
    # Configurar el Canvas y el tablero
    canva = Canvas(root, width=size * 30, height=size * 30, bg="green")
    tablero = Laberinto(canva, size)  # Crear el laberinto con el tamaño ingresado
    HORMIGA = hormiga(canva, -60, -60)
    canva.bind("<Button-1>", editar)

def mostrar_edit():
    global editable, canva
    editable = True
    canva.pack(anchor="nw")  # Muestra el Canvas en la ventana
    for boton in [boton_hierba, boton_azucar, boton_vino, boton_veneno, boton_roca, boton_hormiga]:
        boton.pack(anchor="ne")
    boton_simulacion.pack(anchor="s")

def editar(event):
    global tablero, obj, editable, HORMIGA
    if editable:
        # Convertir coordenadas de clic a coordenadas de la matriz
        celda_x = event.x // 30
        celda_y = event.y // 30
        if obj.get() != 5:
            # Verificar que las coordenadas estén dentro de los límites del tablero
            tablero.reemplazar(obj.get(), celda_x, celda_y)
        else:
            canva.coords(HORMIGA.id, celda_x*30+15, celda_y*30+15)
            HORMIGA.posicion = np.array([[celda_x//30], [celda_y//30]])
        canva.update()

def simulacion():
    global HORMIGA, editable
    editable = False
    HORMIGA.algoritmo_genetico_adaptativo(100, tablero.matriz)
    boton_simulacion.forget()
    for boton in [boton_hierba, boton_azucar, boton_vino, boton_veneno, boton_roca, boton_hormiga]:
        boton.forget()

# Crear un Label y Entry para el tamaño del tablero
label_size_tablero = Label(root, text="Dimensiones del tablero:", font=fuente)
var_size = IntVar(value=3)
scale_size_tablero = Scale(root, from_=3, to=10, showvalue=False, tickinterval=1, orient="horizontal", variable=var_size)

# Botón para crear el tablero
boton_crear = Button(text="Crear", font=fuente, command=lambda: [crear_tablero(), ocultar_inicio(), mostrar_edit()])

# Botones de opción para seleccionar el tipo de ítem
obj = IntVar(value=0)
boton_hierba = Radiobutton(text="Hierba", font=fuente, variable=obj, value=0)
boton_azucar = Radiobutton(text="Azúcar", font=fuente, variable=obj, value=1)
boton_vino = Radiobutton(text="Vino", font=fuente, variable=obj, value=2)
boton_veneno = Radiobutton(text="Veneno", font=fuente, variable=obj, value=3)
boton_roca = Radiobutton(text="Roca", font=fuente, variable=obj, value=4)
boton_hormiga = Radiobutton(text="Hormiga", font=fuente, variable=obj, value=5)
boton_simulacion = Button(text="Iniciar simulación", font=fuente, command=simulacion)

# Muestra el inicio
mostrar_inicio()
root.mainloop()
