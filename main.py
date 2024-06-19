import sys
from PyQt6.QtWidgets import QApplication, QWidget
from src.Login import Login

def main():
    app = QApplication(sys.argv)
    form = QWidget()
    ui = Login()
    ui.login(Form)
    form.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
