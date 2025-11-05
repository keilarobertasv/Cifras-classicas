import sys
from PyQt6.QtWidgets import QApplication
from gui import CriptoApp

def load_stylesheet(file_name):
    with open(file_name, "r") as f:
        return f.read()

def main():
    app = QApplication(sys.argv)    
    
    try:
        stylesheet = load_stylesheet("style.qss")
        app.setStyleSheet(stylesheet)
    except FileNotFoundError:
        print("AVISO: Arquivo 'style.qss' não encontrado. Usando estilo padrão.")
        pass
    
    window = CriptoApp()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()