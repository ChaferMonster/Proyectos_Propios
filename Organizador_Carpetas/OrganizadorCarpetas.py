import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime

fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
carpeta = ""
carpeta_destino = ""
i = 0

def elegirCarpeta():
    global carpeta
    carpeta = filedialog.askdirectory()
    if carpeta:
        etiqueta_entrada.config(text=f"📁 Origen:\n{carpeta}")

def elegirDestino():
    global carpeta_destino
    carpeta_destino = filedialog.askdirectory()
    if carpeta_destino:
        etiqueta_salida.config(text=f"📂 Destino:\n{carpeta_destino}")
        analizarContenido()


#carpeta = "C:\\Users\\alvar\\Desktop\\Proyectos Varios\\Organizador_Carpetas\\test_descargas"



tipos = {
    'imagenes': ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    'documentos': ['.pdf', '.docx', '.txt'],
    'videos': ['.mp4', '.mkv', '.avi'],
    'comprimidos': ['.zip', '.rar'],
}



def ejecutarOrden():
    global imagenes, documentos, videos, comprimidos, otros
    imagenes = 0
    documentos = 0
    videos = 0
    comprimidos = 0
    otros = 0



    if not carpeta_destino:
        messagebox.showwarning("Atención", "Primero selecciona una carpeta.")
        return
    
    # Se crea un txt de forma que se añade la info al final cada vez
    log_path = os.path.abspath("log.txt")
    log = open(log_path, "a", encoding="utf-8")

    estado_label.config(text="Organizando archivos...")

    #Cuenta la cantidad de archivos
    total_archivos = 0
    for _, _, archivos in os.walk(carpeta):
        total_archivos += len(archivos)

    barra_progreso["maximum"] = total_archivos
    barra_progreso["value"] = 0
    ventana.update_idletasks()

    for raiz, subcarpetas, archivos in os.walk(carpeta):
        for archivo in archivos:
            if archivo == "log.txt":
                continue

            # Construye la ruta completa del archivo
            ruta_archivo = os.path.join(raiz, archivo)

            # Solo continuamos si es un archivo (evitamos subcarpetas)
            if os.path.isfile(ruta_archivo):

                # Divide el nombre del archivo en nombre y extensión
                nombre, extension = os.path.splitext(archivo)

                # Posteriormente se usa para comprobar si es de la carpeta otros
                clasificado = False

                # Recorre cada categoría del diccionario de tipos
                for tipo, extensiones in tipos.items():
                    if extension.lower() in extensiones:
                        clasificado = True

                        # Crea la ruta de la carpeta de destino (por ejemplo: "carpeta/imagenes")
                        mod_time = os.path.getmtime(ruta_archivo)
                        fecha_archivo = datetime.fromtimestamp(mod_time).strftime("%Y-%m")
                        ruta_destino = os.path.join(carpeta_destino, tipo, fecha_archivo)

                        # Crea la carpeta si no existe todavía
                        os.makedirs(ruta_destino, exist_ok=True)
                        nuevo_nombre = archivo

                        # Crea la ruta completa a donde moveremos el archivo
                        nueva_ruta = os.path.join(ruta_destino, nuevo_nombre)
                        contador = 1

                        # Evitar sobrescribir: si ya existe un archivo con el mismo nombre, añadir _1, _2, etc.
                        while os.path.exists(nueva_ruta):
                            nuevo_nombre = (f"{nombre}_{contador}{extension}")
                            nueva_ruta = os.path.join(ruta_destino, nuevo_nombre)
                            contador+=1


                        # Mueve el archivo desde su ruta original a la nueva ruta o muestra la simulación
                        if not modo_simulacion.get():
                            os.rename(ruta_archivo, nueva_ruta)
                        else:
                            print(f"[SIMULACUIÓN] Movería: {ruta_archivo} → {nueva_ruta}")

                        barra_progreso["value"] +=1
                        ventana.update_idletasks()

                        # Para hacer el control del log
                        fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                        if not modo_simulacion.get():
                            log.write(f"[{fecha}] {ruta_archivo} → {nueva_ruta}\n")
                            print(f"{nuevo_nombre} > {nueva_ruta}")

                        if tipo == "imagenes":
                            imagenes+=1
                        elif tipo == "documentos":
                            documentos+=1
                        elif tipo == "videos":
                            videos+=1
                        elif tipo == "comprimidos":
                            comprimidos+=1
                            

                        break

                if not clasificado: # En caso de no pertenecer a ningún tipo de los anteriores se traspasa a 'otros'

                    ruta_destino = os.path.join(carpeta_destino, "otros")
                    os.makedirs(ruta_destino, exist_ok=True)
                    nuevo_nombre = archivo
                    nueva_ruta = os.path.join(ruta_destino, nuevo_nombre)
                    contador = 1

                    # Evitar sobrescribir: si ya existe un archivo con el mismo nombre, añadir _1, _2, etc.
                    while os.path.exists(nueva_ruta):
                        nuevo_nombre = (f"{nombre}_{contador}{extension}")
                        nueva_ruta = os.path.join(ruta_destino, nuevo_nombre)
                        contador+=1

                    if not modo_simulacion.get():
                        os.rename(ruta_archivo, nueva_ruta)
                    else:
                        print(f"[SIMULACUIÓN] Movería: {ruta_archivo} → {nueva_ruta}")

                    # Aumenta la barra de progreso archivo a archivo
                    barra_progreso["value"] += 1
                    ventana.update_idletasks()

                    fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                    if not modo_simulacion.get():
                        log.write(f"[{fecha}] {ruta_archivo} → {nueva_ruta}\n")

                        print(f"{nuevo_nombre} > {nueva_ruta}")
                    
                    # Conteo de archivos que van a 'otros'
                    otros+=1

    barra_progreso["value"] = total_archivos
    estado_label.config(text="✔ Organización completada")

    log.close()
    if not modo_simulacion.get():
        if imagenes != 0:
            print(f"Se han movido a la carpeta imagenes {imagenes} archivo/s.")
        if documentos != 0:
            print(f"Se han movido a la carpeta documentos {documentos} archivo/s.")
        if videos != 0:
            print(f"Se han movido a la carpeta videos {videos} archivo/s.")
        if comprimidos != 0:
            print(f"Se han movido a la carpeta comprimidos {comprimidos} archivo/s.")
        if otros != 0:
            print(f"Se han movido a la carpeta otros {otros} archivo/s.")

        messagebox.showinfo("Organizado", f"Se han movido:\n\n"
        f"📷 Imágenes: {imagenes}\n"
        f"📄 Documentos: {documentos}\n"
        f"🎥 Videos: {videos}\n"
        f"🗜️ Comprimidos: {comprimidos}\n"
        f"📦 Otros: {otros}")
    else:
        messagebox.showinfo("Simulación realizada", f"Se han simulado los siguientes movimientos:\n\n"
        f"📷 Imágenes: {imagenes}\n"
        f"📄 Documentos: {documentos}\n"
        f"🎥 Videos: {videos}\n"
        f"🗜️ Comprimidos: {comprimidos}\n"
        f"📦 Otros: {otros}")

def deshacer():
# Leemos el log linea por linea de atras a delante        
    with open("log.txt", "r", encoding="utf-8") as log:
        lineas = log.readlines()

        for linea in reversed(lineas):
            #Elimina espacios y saltos de línea
            linea = linea.strip()

            if not linea:
                continue
            
            #Elimina la parte de la fecha
            try:
                _, movimiento = linea.split("]", 1) #Divide en dos a partir de ]
                ruta_origen, ruta_destino = [r.strip() for r in movimiento.split(" → ")]

                if os.path.exists(ruta_destino):
                    os.makedirs(os.path.dirname(ruta_origen), exist_ok=True)
                    os.rename(ruta_destino, ruta_origen)
                    print(f"Deshecho: {ruta_destino} → {ruta_origen}")

                else: 
                    print(f"Archivo no encontrado: {ruta_destino}")

            except ValueError:
                        print(f"Línea inválida en el log: {linea}")


def analizarContenido():
    if not carpeta or not carpeta_destino:
        return
    
    conteo = {"imagenes":0, "documentos":0, "videos":0, "comprimidos":0, "otros":0}

    for raiz, _, archivos in os.walk(carpeta):
        for archivo in archivos:
            nombre, extension = os.path.splitext(archivo)
            extension = extension.lower()
            clasificado = False

            for tipo, extensiones in tipos.items():
                if extension in extensiones:
                    conteo[tipo] += 1
                    clasificado = True
                    break

            if not clasificado:
                conteo["otros"] +=1

    resumen = (
        f"Se moverán:\n"
        f"📷 Imágenes: {conteo['imagenes']}\n"
        f"📄 Documentos: {conteo['documentos']}\n"
        f"🎥 Videos: {conteo['videos']}\n"
        f"🗜️ Comprimidos: {conteo['comprimidos']}\n"
        f"📦 Otros: {conteo['otros']}"
    )
    etiquetaResumen.config(text=resumen)

ventana = tk.Tk()
ventana.title("Organizador de carpetas")
ventana.geometry("500x480")

boton_entrada = tk.Button(ventana, text="Seleccionar carpeta", command=elegirCarpeta)
boton_entrada.pack(pady=10)

boton_destino = tk.Button(ventana, text="Seleccionar destino", command=elegirDestino)
boton_destino.pack(pady=10)

modo_simulacion = tk.BooleanVar()

simular_check = tk.Checkbutton(ventana, text="Simular organización (no mover archivos)", variable=modo_simulacion)
simular_check.pack()


etiquetaResumen = tk.Label(ventana, text="", justify="left")
etiquetaResumen.pack(pady=10)

etiqueta_entrada = tk.Label(ventana, text="No se ha seleccionado ninguna carpeta")
etiqueta_entrada.pack()

etiqueta_salida = tk.Label(ventana, text="No se ha seleccionado ninguna carpeta")
etiqueta_salida.pack()

barra_progreso = ttk.Progressbar(ventana, orient="horizontal", length=300, mode="determinate")
barra_progreso.pack(pady=10)

estado_label = tk.Label(ventana, text="")
estado_label.pack(pady=5)

boton_ejecutar = tk.Button(ventana, text="Ejecutar organizacion de archivos", command=ejecutarOrden)
boton_ejecutar.pack(pady=20)

boton_deshacer = tk.Button(ventana, text="Deshacer último movimiento", command=deshacer)
boton_deshacer.pack(pady=10)

ventana.mainloop()