# PDF Procesador 📄🔧

## Descripción General
PDF Procesador es una aplicación de escritorio desarrollada en Python que permite manipular y procesar archivos PDF de manera sencilla e intuitiva. Ofrece funcionalidades avanzadas de conversión y extracción de documentos PDF.

## Características Principales ✨
- 📄 División de archivos PDF en partes más pequeñas
- 🖼️ Conversión de páginas PDF a imágenes (formatos webp y jpg)
- 📝 Extracción de texto a documentos Word
- 🎨 Personalización de resolución de imágenes
- 🔧 Interfaz gráfica intuitiva y fácil de usar

## Tecnologías Utilizadas 💻
- **Lenguaje**: Python 3.8+
- **Interfaz Gráfica**: Tkinter
- **Bibliotecas Principales**:
  - PyPDF2 (manipulación de PDFs)
  - pdf2image (conversión a imágenes)
  - pdfplumber (extracción de texto)
  - python-docx (generación de documentos Word)

## Requisitos del Sistema 🖥️
- Python 3.8 o superior
- Sistema operativo: Linux, macOS, Windows
- Dependencias listadas en `requirements.txt`

## Instalación 🚀

### Clonar el Repositorio
```bash
git clone https://github.com/tu_usuario/pdf-procesador.git
cd pdf-procesador
```

### Configurar Entorno Virtual
```bash
python3 -m venv venv
source venv/bin/activate
```

### Instalar Dependencias
```bash
pip install -r requirements.txt
```

## Estructura del Proyecto 📂
```
procesador_pdf/
│
├── src/                    # Código fuente
│   ├── __init__.py         # Inicializador del paquete
│   ├── main.py             # Punto de entrada principal
│   ├── gui.py              # Interfaz gráfica
│   └── procesador.py       # Lógica de procesamiento de PDFs
│
├── run.py                  # Script de ejecución
├── requirements.txt        # Dependencias del proyecto
└── README.md               # Documentación del proyecto
```

## Uso 🖱️
1. Ejecutar la aplicación:
```bash
python run.py
```

2. Interfaz de Usuario:
- Seleccionar archivo PDF
- Elegir formato de imagen
- Configurar resolución
- Definir número de páginas por archivo
- Seleccionar directorio de salida
- Hacer clic en "Procesar PDF"

## Funcionalidades Detalladas 🔍

### División de PDFs
- Divide documentos PDF en archivos más pequeños
- Configurable por número de páginas
- Mantiene la integridad del documento original

### Conversión de Imágenes
- Convierte páginas PDF a imágenes
- Soporta formatos webp y jpg
- Control de resolución (50-300 DPI)

### Extracción de Texto
- Extrae texto de documentos PDF
- Genera archivos Word (.docx)
- Limpieza y formateo automático de texto

## Contribuciones 🤝
¡Las contribuciones son bienvenidas! Por favor, lee las pautas de contribución antes de enviar un pull request.

## Licencia 📄
[Especificar Licencia, por ejemplo MIT]

## Contacto 📧
- Nombre del Desarrollador
- Correo electrónico
- Perfil de GitHub
