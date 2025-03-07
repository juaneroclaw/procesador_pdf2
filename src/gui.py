import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import threading
import gc
from src.procesador import ProcesadorPDFOptimizado

class ProcesadorPDFApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Procesador de PDFs")
        self.root.geometry("600x500")
        self.root.configure(bg='#f0f0f0')

        # Estilo
        self.style = ttk.Style()
        self.style.configure('TButton', font=('Arial', 10))
        self.style.configure('TLabel', font=('Arial', 10), background='#f0f0f0')

        # Variables
        self.ruta_pdf = tk.StringVar()
        self.formato_imagen = tk.StringVar(value='webp')
        self.resolucion = tk.IntVar(value=100)
        self.paginas_por_archivo = tk.IntVar(value=10)
        self.directorio_salida = tk.StringVar(value='salida')  # Valor por defecto

        # Crear interfaz
        self.crear_interfaz()

    def crear_interfaz(self):
        # Marco principal
        marco = ttk.Frame(self.root, padding="20")
        marco.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Título
        ttk.Label(marco, text="Procesador de PDFs", font=('Arial', 16, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)

        # Selección de PDF
        ttk.Label(marco, text="Seleccionar PDF:").grid(row=1, column=0, sticky=tk.W, pady=5)
        ttk.Entry(marco, textvariable=self.ruta_pdf, width=50).grid(row=1, column=1, pady=5)
        ttk.Button(marco, text="Examinar", command=self.seleccionar_pdf).grid(row=1, column=2, padx=5)

        # Opciones de formato
        ttk.Label(marco, text="Formato de Imagen:").grid(row=2, column=0, sticky=tk.W, pady=5)
        formatos = ['webp', 'jpg']
        ttk.Combobox(marco, textvariable=self.formato_imagen, values=formatos, state="readonly", width=20).grid(row=2, column=1, sticky=tk.W, pady=5)

        # Resolución
        ttk.Label(marco, text="Resolución (DPI):").grid(row=3, column=0, sticky=tk.W, pady=5)
        ttk.Scale(marco, from_=50, to=300, variable=self.resolucion, orient=tk.HORIZONTAL, length=200).grid(row=3, column=1, sticky=tk.W, pady=5)
        ttk.Label(marco, textvariable=self.resolucion).grid(row=3, column=2, sticky=tk.W)

        # Páginas por archivo
        ttk.Label(marco, text="Páginas por Archivo:").grid(row=4, column=0, sticky=tk.W, pady=5)
        ttk.Spinbox(marco, from_=1, to=50, textvariable=self.paginas_por_archivo, width=10).grid(row=4, column=1, sticky=tk.W, pady=5)

        # Directorio de Salida
        ttk.Label(marco, text="Directorio de Salida:").grid(row=5, column=0, sticky=tk.W, pady=5)
        ttk.Entry(marco, textvariable=self.directorio_salida, width=50).grid(row=5, column=1, pady=5)
        ttk.Button(marco, text="Examinar", command=self.seleccionar_directorio_salida).grid(row=5, column=2, padx=5)

        # Botón de procesamiento
        ttk.Button(marco, text="Procesar PDF", command=self.iniciar_procesamiento).grid(row=6, column=0, columnspan=3, pady=20)

        # Barra de progreso
        self.barra_progreso = ttk.Progressbar(marco, orient="horizontal", length=300, mode="determinate")
        self.barra_progreso.grid(row=7, column=0, columnspan=3, pady=10)

        # Área de log
        self.log_texto = tk.Text(marco, height=10, width=70, state='disabled')
        self.log_texto.grid(row=8, column=0, columnspan=3, pady=10)

    def seleccionar_pdf(self):
        """Permite al usuario seleccionar un archivo PDF"""
        archivo = filedialog.askopenfilename(
            title="Seleccionar archivo PDF", 
            filetypes=[("Archivos PDF", "*.pdf")]
        )
        if archivo:
            self.ruta_pdf.set(archivo)

    def seleccionar_directorio_salida(self):
        """Permite al usuario seleccionar el directorio de salida"""
        directorio = filedialog.askdirectory(
            title="Seleccionar directorio de salida"
        )
        if directorio:
            self.directorio_salida.set(directorio)

    def log(self, mensaje):
        """Agrega un mensaje al área de log"""
        self.log_texto.configure(state='normal')
        self.log_texto.insert(tk.END, mensaje + "\n")
        self.log_texto.configure(state='disabled')
        self.log_texto.see(tk.END)
        # Actualizar la interfaz gráfica
        self.root.update_idletasks()

    def iniciar_procesamiento(self):
        """Inicia el procesamiento del PDF en un hilo separado"""
        # Validar que se haya seleccionado un PDF
        if not self.ruta_pdf.get():
            messagebox.showerror("Error", "Seleccione un archivo PDF")
            return

        # Limpiar log anterior
        self.log_texto.configure(state='normal')
        self.log_texto.delete('1.0', tk.END)
        self.log_texto.configure(state='disabled')

        # Reiniciar barra de progreso
        self.barra_progreso['value'] = 0

        # Iniciar procesamiento en un hilo separado
        threading.Thread(target=self.procesar_pdf, daemon=True).start()

    def procesar_pdf(self):
        """Procesa el PDF con las opciones seleccionadas"""
        try:
            # Crear procesador
            procesador = ProcesadorPDFOptimizado(
                self.ruta_pdf.get(), 
                directorio_salida=self.directorio_salida.get()
            )
            
            # Dividir PDF
            self.log("Dividiendo PDF...")
            pdfs_divididos = procesador.dividir_pdf(paginas_por_archivo=self.paginas_por_archivo.get())
            
            # Procesar cada parte
            total_partes = len(pdfs_divididos)
            for i, pdf_parte in enumerate(pdfs_divididos, start=1):
                # Actualizar barra de progreso
                progreso = int((i / total_partes) * 100)
                self.root.after(0, self.barra_progreso.configure, {'value': progreso})

                # Convertir a imágenes
                self.log(f"Procesando parte {i}: Convirtiendo a imágenes...")
                rutas_imagenes = procesador.convertir_a_imagenes(
                    pdf_parte, 
                    parte_numero=i,
                    formato=self.formato_imagen.get(), 
                    resolucion=self.resolucion.get()
                )
                self.log(f"Imágenes guardadas: {rutas_imagenes}")
                
                # Extraer texto
                self.log(f"Procesando parte {i}: Extrayendo texto...")
                ruta_word = procesador.extraer_texto_a_word(pdf_parte, parte_numero=i)
                self.log(f"Texto guardado: {ruta_word}")
                
                # Liberar memoria
                gc.collect()
            
            # Finalizar
            self.root.after(0, self.barra_progreso.configure, {'value': 100})
            messagebox.showinfo("Éxito", "Procesamiento completado")

        except Exception as e:
            self.log(f"Error: {str(e)}")
            messagebox.showerror("Error", str(e))
