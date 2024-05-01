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

def codificar_cesar(frase, corrimiento):
    resultado_codificado = ""
    for caracter in frase:
        if caracter.isalpha():
            base = ord('a') if caracter.islower() else ord('A')
            codificado = chr((ord(caracter) - base + corrimiento) % 26 + base)
            resultado_codificado += codificado
        else:
            resultado_codificado += caracter
    return resultado_codificado

def decodificar_cesar(resultado_codificado, corrimiento):
    resultado_decodificado = ""
    for caracter in resultado_codificado:
        if caracter.isalpha():
            base = ord('a') if caracter.islower() else ord('A')
            decodificado = chr((ord(caracter) - base - corrimiento + 26) % 26 + base)
            resultado_decodificado += decodificado
        else:
            resultado_decodificado += caracter
    return resultado_decodificado

def generar_codificacion():
    frase = frase_field.get()
    corrimiento = int(corrimiento_field.get())
    resultado_codificado = codificar_cesar(frase, corrimiento)
    resultado_area.delete('1.0', tk.END)
    resultado_area.insert(tk.END, resultado_codificado)

def generar_decodificacion():
    resultado_codificado = resultado_area.get('1.0', tk.END)
    corrimiento = int(corrimiento_field.get())
    resultado_decodificado = decodificar_cesar(resultado_codificado, corrimiento)
    resultado_area.delete('1.0', tk.END)
    resultado_area.insert(tk.END, resultado_decodificado)

# Crear la ventana principal
root = tk.Tk()
root.title("Cifrado César")

longitud_label = tk.Label(root, text="Introduce la longitud de la clave:")
longitud_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

entry_longitud = tk.Entry(root)
entry_longitud.grid(row=0, column=1, padx=10, pady=5)

boton_generar = tk.Button(root, text="Generar Clave", command=generar_clave_y_mostrar)
boton_generar.grid(row=1, column=0, padx=10, pady=5)

label_clave = tk.Label(root, text="")
label_clave.grid(row=1, column=1, padx=10, pady=5)

frase_label = tk.Label(root, text="Frase:")
frase_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")

frase_field = tk.Entry(root)
frase_field.grid(row=3, column=1, padx=10, pady=5)

corrimiento_label = tk.Label(root, text="Corrimiento:")
corrimiento_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")

corrimiento_field = tk.Entry(root)
corrimiento_field.grid(row=4, column=1, padx=10, pady=5)

codificar_button = tk.Button(root, text="Codificar", command=generar_codificacion)
codificar_button.grid(row=5, column=0, padx=10, pady=5)

decodificar_button = tk.Button(root, text="Decodificar", command=generar_decodificacion)
decodificar_button.grid(row=5, column=1, padx=10, pady=5)

resultado_label = tk.Label(root, text="Resultado:")
resultado_label.grid(row=6, column=0, padx=10, pady=5, sticky="w")

resultado_area = tk.Text(root, height=5, width=40)
resultado_area.grid(row=7, column=0, columnspan=2, padx=10, pady=5)




# Iniciar el bucle de eventos
root.mainloop()
