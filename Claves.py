import tkinter as tk
import random
import string

def generar_clave(longitud):
    letras = string.ascii_letters
    clave = ''.join(random.choice(letras) for _ in range(longitud))
    return clave

def generar_clave_y_mostrar():
    longitud = int(entry_longitud.get())
    clave_generada = generar_clave(longitud)
    label_clave.config(text=clave_generada)

# Crear la ventana principal
root = tk.Tk()
root.title("Generador de Claves")

# Crear y posicionar los elementos de la interfaz
label_instruccion = tk.Label(root, text="Introduce la longitud de la clave:")
label_instruccion.pack()

entry_longitud = tk.Entry(root)
entry_longitud.pack()

boton_generar = tk.Button(root, text="Generar Clave", command=generar_clave_y_mostrar)
boton_generar.pack()

label_clave = tk.Label(root, text="")
label_clave.pack()

# Iniciar el bucle de eventos
root.mainloop()


