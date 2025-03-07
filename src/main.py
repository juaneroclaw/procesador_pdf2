import tkinter as tk
from src.gui import ProcesadorPDFApp

def main():
    root = tk.Tk()
    app = ProcesadorPDFApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
