import sys
from PyQt6.QtWidgets import QApplication, QWidget
from src.tela_inicial import Tela_Inicio

def main():
    app = QApplication(sys.argv)
    form = QWidget()
    ui = Tela_Inicio()
    ui.setupUi(form)
    form.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
