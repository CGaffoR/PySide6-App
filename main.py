import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel

class MainJanela(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('My App with Pyside6')
        self.setGeometry(100, 100, 400, 400)

        self.label = QLabel('Digite seu nome:', self)
        self.label.move(20, 20)

        self.textbox = QLineEdit(self)
        self.textbox.move(150, 20)
        self.textbox.resize(200, 30)

        self.button = QPushButton('confirmar', self)
        self.button.move(150, 60)
        self.button.clicked.connect(self.lambda1)

        self.result_label = QLabel('', self)
        self.result_label.move(150, 100)

    def lambda1(self):
        nome = self.textbox.text()
        if nome:
            mensagem = f"Ola, {nome}!"
            self.result_label.setText(mensagem)
        else:
            self.result_label.setText('Digite seu nome!.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = MainJanela()
    janela.show()
    sys.exit(app.exec_())
