import tkinter as tk
import string
import random
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Generador de Contraseñas")

tk.Label(ventana, text="Introduce un sitio web").pack()
entrada_sitio = tk.Entry(ventana)
entrada_sitio.pack()

tk.Label(ventana, text="Longitud de la contraseña").pack()
longitud=tk.Entry(ventana)
longitud.pack()

def generar_contraseña():
    long_contraseña = int(longitud.get())
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(long_contraseña))
    entry_resultado.delete(0, tk.END)
    entry_resultado.insert(0, contraseña)
tk.Button(ventana, text="Generar contraseña", command=generar_contraseña).pack()

entry_resultado = tk.Entry(ventana, width=30)
entry_resultado.pack()

def guardar_contraseña():
    sitio = entrada_sitio.get()
    contraseña = entry_resultado.get()
    if sitio and contraseña:
        with open("contraseñas.txt", "a") as f:
            f.write(f"{sitio}:{contraseña}\n")
        messagebox.showinfo("Guardado", "Contraseña guardada con éxito.")
    else:
        messagebox.showwarning("Error", "Introduce un sitio y genera una contraseña.")

tk.Button(ventana, text="Guardar contraseña", command=guardar_contraseña).pack()

ventana.mainloop()
