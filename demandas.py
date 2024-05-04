from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QMessageBox
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from PyQt6.QtCore import Qt
class Demandas(object):
    def demandas(self, Form,dema,tela):
        self.tela = tela
        self.frame = self.tela.frame_demandas
        if dema == 1:

            self.radioButton_Estoque = QtWidgets.QRadioButton(parent=self.frame)
            self.radioButton_Estoque.setGeometry(QtCore.QRect(250, 80, 82, 17))
            self.radioButton_Estoque.setObjectName("radioButton_Estoque")

            self.radioButton_Demandas = QtWidgets.QRadioButton(parent=self.frame)
            self.radioButton_Demandas.setGeometry(QtCore.QRect(370, 80, 82, 17))
            self.radioButton_Demandas.setObjectName("radioButton_Demandas")

            self.tabela_demandas = QtWidgets.QTableWidget(parent=self.frame)
            self.tabela_demandas.setGeometry(QtCore.QRect(250, 120, 1091, 541))
            font = QtGui.QFont()
            font.setPointSize(12)
            font.setBold(True)
            font.setWeight(75)
            self.tabela_demandas.setFont(font)
            self.tabela_demandas.setStyleSheet("background-color: transparent;\n"
                                               " border-radius: 10px;\n"
                                               "")
            self.tabela_demandas.setShowGrid(False)
            self.tabela_demandas.setObjectName("tableWidget")
            self.tabela_demandas.setColumnCount(10)
            self.tabela_demandas.setRowCount(6)
            item = QtWidgets.QTableWidgetItem()
            self.tabela_demandas.setHorizontalHeaderItem(0, item)
            item = QtWidgets.QTableWidgetItem()
            self.tabela_demandas.setHorizontalHeaderItem(1, item)
            item = QtWidgets.QTableWidgetItem()
            self.tabela_demandas.setHorizontalHeaderItem(2, item)
            item = QtWidgets.QTableWidgetItem()
            self.tabela_demandas.setHorizontalHeaderItem(3, item)
            item = QtWidgets.QTableWidgetItem()
            self.tabela_demandas.setHorizontalHeaderItem(4, item)
            item = QtWidgets.QTableWidgetItem()
            self.tabela_demandas.setHorizontalHeaderItem(5, item)
            item = QtWidgets.QTableWidgetItem()
            self.tabela_demandas.setHorizontalHeaderItem(6, item)
            item = QtWidgets.QTableWidgetItem()
            self.tabela_demandas.setHorizontalHeaderItem(7, item)
            item = QtWidgets.QTableWidgetItem()
            self.tabela_demandas.setHorizontalHeaderItem(8, item)
            item = QtWidgets.QTableWidgetItem()
            self.tabela_demandas.setHorizontalHeaderItem(9, item)
            self.tabela_demandas.horizontalHeader().setDefaultSectionSize(114)

            self.pesquisar_demandas = QtWidgets.QLineEdit(parent=self.frame)
            self.pesquisar_demandas.setGeometry(QtCore.QRect(250, 50, 431, 21))
            self.pesquisar_demandas.setStyleSheet(
                "border: 2px solid #737373; border-radius: 10px; background-color: white;")
            self.pesquisar_demandas.setObjectName("pesquisar_demandas")

            self.radioButton_Estoque.setText("Estoque")
            self.radioButton_Demandas.setText("Funcionario")

            item = self.tabela_demandas.horizontalHeaderItem(0)
            item.setText("Item")
            item = self.tabela_demandas.horizontalHeaderItem(1)
            item.setText("Descrição do Item")
            item = self.tabela_demandas.horizontalHeaderItem(2)
            item.setText("Unidade do Item")
            item = self.tabela_demandas.horizontalHeaderItem(3)
            item.setText("Quantidade")
            item = self.tabela_demandas.horizontalHeaderItem(4)
            item.setText("Marca")
            item = self.tabela_demandas.horizontalHeaderItem(5)
            item.setText("Preço Unitário")
            item = self.tabela_demandas.horizontalHeaderItem(6)
            item.setText("Preço Total")
            item = self.tabela_demandas.horizontalHeaderItem(7)
            item.setText("Status")
            item = self.tabela_demandas.horizontalHeaderItem(8)
            item.setText("Data do Pedido")
            item = self.tabela_demandas.horizontalHeaderItem(9)
            item.setText("")

            self.pesquisar_demandas.setPlaceholderText("Pesquisar Item")

            self.radioButton_Estoque.show()
            self.pesquisar_demandas.show()
            self.radioButton_Demandas.show()
            self.tabela_demandas.show()
            self.ler_database()

            self.frame_scrol  = QtWidgets.QFrame(parent=self.frame)
            self.frame_scrol.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            self.frame_scrol.setGeometry(QtCore.QRect(450, 50, 505, 610))
            self.frame_scrol.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
            self.frame_scrol.setObjectName("frame")
            self.frame_scrol.hide()
            self.frame_scrol.setCursor(QtCore.Qt.CursorShape.OpenHandCursor)
            self.frame_scrol.mousePressEvent = lambda event, centralwidget=self.frame_scrol: self.mousePressEvent(event, centralwidget)
            self.frame_scrol.mouseReleaseEvent = lambda event,centralwidget=self.frame_scrol: self.mouseReleaseEvent(event, centralwidget)
            self.frame_scrol.mouseMoveEvent = lambda event, centralwidget=self.frame_scrol: self.mouseMoveEvent(event, centralwidget)
            self.frame_scrol.setStyleSheet(f'background-color: rgb(212, 212, 212);'
                                             f'color: black;'
                                             f'font: arial 12px;'
                                             f'border: 2px solid #2E3D48;'
                                             f'border-radius: 10px;')

        if dema == 2:
            self.nome_item_label = QtWidgets.QLabel('Nome do Item:', self.frame)
            self.nome_item_label.setGeometry(QtCore.QRect(290, 72, 80, 21))

            self.nome_item = QtWidgets.QLineEdit(parent=self.frame)
            self.nome_item.setGeometry(QtCore.QRect(290, 100, 331, 20))
            self.nome_item.setStyleSheet("border: 2px solid #737373; border-radius: 10px; background-color: white;")
            self.nome_item.setObjectName("nome_item")
            self.nome_item.setPlaceholderText("Nome do Item")

            self.descricao_label = QtWidgets.QLabel('Descrição:', self.frame)
            self.descricao_label.setGeometry(QtCore.QRect(290, 210, 80, 21))

            self.descricao = QtWidgets.QTextEdit(parent=self.frame)
            self.descricao.setGeometry(QtCore.QRect(290, 240, 481, 181))
            self.descricao.setObjectName("descricao")
            self.descricao.setStyleSheet("border: 2px solid #2E3D48; border-radius: 10px; background-color: white;")

            self.unidade_label = QtWidgets.QLabel('Unidade do Item:', self.frame)
            self.unidade_label.setGeometry(QtCore.QRect(290, 140, 100, 21))
            self.Combounidade = QtWidgets.QComboBox(parent=self.frame)
            self.Combounidade.setGeometry(QtCore.QRect(290, 160, 180, 31))
            self.Combounidade.setObjectName("Combounidade")
            self.Combounidade.addItem("Metros - m")
            self.Combounidade.addItem("Unidade - qt")
            self.Combounidade.addItem("Peso - Kg")
            self.Combounidade.addItem("Volume - L")
            self.Combounidade.addItem("Área - m2")
            self.Combounidade.setStyleSheet("background-color: rgb(255, 255, 255);"
                                            "border: none;")

            self.marca_label = QtWidgets.QLabel('Marca do Item:', self.frame)
            self.marca_label.setGeometry(QtCore.QRect(900, 72, 80, 21))

            self.marca_item = QtWidgets.QLineEdit(parent=self.frame)
            self.marca_item.setGeometry(QtCore.QRect(900, 100, 331, 20))
            self.marca_item.setStyleSheet("border: 2px solid #737373; border-radius: 10px; background-color: white;")
            self.marca_item.setObjectName("marca_item")
            self.marca_item.setPlaceholderText("Marca do Item")

            self.Qt_label = QtWidgets.QLabel('Quantidade do Item:', self.frame)
            self.Qt_label.setGeometry(QtCore.QRect(900, 150, 110, 21))

            self.Quantidade_item = QtWidgets.QSpinBox(parent=self.frame)
            self.Quantidade_item.setGeometry(QtCore.QRect(900, 170, 331, 20))
            self.Quantidade_item.setStyleSheet("border: 2px solid #737373; border-radius: 10px; background-color: white;")
            self.Quantidade_item.setObjectName("Quantidade_item")

            self.nome_item.show()
            self.nome_item_label.show()
            self.descricao_label.show()
            self.descricao.show()
            self.Combounidade.show()
            self.unidade_label.show()
            self.marca_item.show()
            self.marca_label.show()
            self.Quantidade_item.show()
            self.Qt_label.show()
        if dema == 3:
            self.nome_item_label = QtWidgets.QLabel('Nome do Item:', self.frame)
            self.nome_item_label.setGeometry(QtCore.QRect(290, 72, 80, 21))

            self.nome_item = QtWidgets.QComboBox(parent=self.frame)
            self.nome_item.setGeometry(QtCore.QRect(290, 100, 331, 20))
            self.nome_item.setStyleSheet("background-color: rgb(255, 255, 255);"
                                            "border: none;")

            self.unidade_label = QtWidgets.QLabel('Unidade do Item:', self.frame)
            self.unidade_label.setGeometry(QtCore.QRect(290, 140, 100, 21))

            self.Combounidade = QtWidgets.QComboBox(parent=self.frame)
            self.Combounidade.setGeometry(QtCore.QRect(290, 160, 180, 31))
            self.Combounidade.setObjectName("Combounidade")
            self.Combounidade.addItem("Metros - m")
            self.Combounidade.addItem("Peso - Kg")
            self.Combounidade.addItem("Volume - L")
            self.Combounidade.addItem("Área - m2")
            self.Combounidade.setStyleSheet("background-color: rgb(255, 255, 255);"
                                            "border: none;")

            self.marca_label = QtWidgets.QLabel('Marca do Item:', self.frame)
            self.marca_label.setGeometry(QtCore.QRect(900, 72, 80, 21))

            self.marca_item = QtWidgets.QComboBox(parent=self.frame)
            self.marca_item.setGeometry(QtCore.QRect(900, 100, 331, 20))
            self.marca_item.setStyleSheet("background-color: rgb(255, 255, 255);"
                                            "border: none;")

            self.Qt_label = QtWidgets.QLabel('Quantidade do Item:', self.frame)
            self.Qt_label.setGeometry(QtCore.QRect(900, 150, 110, 21))

            self.Quantidade_item = QtWidgets.QSpinBox(parent=self.frame)
            self.Quantidade_item.setGeometry(QtCore.QRect(900, 170, 70, 20))
            self.Quantidade_item.setStyleSheet("border: 2px solid #737373; border-radius: 10px; background-color: white;")
            self.Quantidade_item.setObjectName("Quantidade_item")

            self.nome_item.show()
            self.nome_item_label.show()
            self.Combounidade.show()
            self.unidade_label.show()
            self.marca_item.show()
            self.marca_label.show()
            self.Quantidade_item.show()
            self.Qt_label.show()

        self.pushButton_confirmar_new_demanda = QtWidgets.QPushButton('Confirmar', parent=self.frame)
        self.pushButton_confirmar_new_demanda.setGeometry(QtCore.QRect(1200, 420, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_confirmar_new_demanda.setFont(font)
        self.pushButton_confirmar_new_demanda.setStyleSheet("QPushButton {\n"
                                               "                    border: 2px solid #2E3D48 ;\n"
                                               "                    border-radius: 10px;\n"
                                               "                    background-color: (131, 131, 131);\n"
                                               "                    color: #2E3D48;\n"
                                               "                }\n"
                                               "\n"
                                               "                QPushButton:hover {\n"
                                               "                    background-color: #DDDDDD;  /* Change this to your desired hover color */\n"
                                               "                    color: rgb(0, 0, 0);\n"
                                               "                }\n"
                                               "\n"
                                               "                QPushButton:pressed {\n"
                                               "                    background-color: white;  /* Change this to your desired pressed color */\n"
                                               "                    color: black;\n"
                                               "                }")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("botao-adicionar.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_confirmar_new_demanda.setIcon(icon6)
        self.pushButton_confirmar_new_demanda.setIconSize(QtCore.QSize(23, 23))
        self.pushButton_confirmar_new_demanda.setObjectName("pushButton_7")
        self.pushButton_confirmar_new_demanda.clicked.connect(self.add_demandas)
        if dema != 1:
            self.pushButton_confirmar_new_demanda.show()
        else:
            self.pushButton_confirmar_new_demanda.hide()
    def add_demandas(self):
        import mysql.connector
        host = "monorail.proxy.rlwy.net"
        port = 30980
        user = "root"
        password = "RXlnFIuFEKMvnYsMaPWvDimjLdGyoJVv"
        database = "railway"

        try:
            connection = mysql.connector.connect(
                host="monorail.proxy.rlwy.net",
                port=30980,
                user="root",
                password="RXlnFIuFEKMvnYsMaPWvDimjLdGyoJVv",
                database="railway"
            )

            if connection.is_connected():
                print("Conexão ao MySQL bem-sucedida.")

                print(self.nome_item.text(),self.descricao.toPlainText(),self.marca_item.text())

                unidade = self.Combounidade.currentText()
                value = self.Quantidade_item.value()
                value_str = str(value)
                cursor = connection.cursor()
                data_hoje = QDate.currentDate()
                self.id = 0
                self.generar_numero()
                data_formatada = data_hoje.toString('dd/MM/yyyy')
                query = "INSERT INTO demanda (id,item, descricao,unidade,quantidade, marca,precounico,precototal,status,data) VALUES (%s,%s, %s, %s,%s,%s, %s, %s,%s,%s)"
                values = (f"{self.id}",f"{self.nome_item.text()}", f"{self.descricao.toPlainText()}",f"{unidade}",f"{value_str}", f"{self.marca_item.text()}","",'','Aguardando',f'{data_formatada}')
                cursor.execute(query, values)

                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Icon.Information)
                msg_box.setWindowTitle("AVISO")
                msg_box.setText("Demanda Cadastrada!")
                msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
                reply = msg_box.exec()

                connection.commit()


        except mysql.connector.Error as e:
            print("Erro ao conectar ao MySQL:", e)

        finally:
            if 'connection' in locals() and connection.is_connected():
                cursor.close()
                connection.close()
                print("Conexão ao MySQL encerrada.")

    def generar_numero(self):
        data = QDate.currentDate()
        dia = data.day()
        mes = data.month()
        import random
        random_numbers = ''.join(str(random.randint(0, 9)) for _ in range(4))
        generated_number = f"{dia:02}{mes:02}{random_numbers}"
        self.id = int(generated_number)
    def ler_database(self):
        import mysql.connector
        host = "monorail.proxy.rlwy.net"
        port = 30980
        user = "root"
        password = "RXlnFIuFEKMvnYsMaPWvDimjLdGyoJVv"
        database = "railway"

        try:
            connection = mysql.connector.connect(
                host=host,
                port=port,
                user=user,
                password=password,
                database=database
            )

            if connection.is_connected():
                print("Conexão ao MySQL bem-sucedida.")

                cursor = connection.cursor()

                query = "SELECT * FROM demanda"
                cursor.execute(query)
                leitura = cursor.fetchall()
                self.tabela_demandas.clearContents()
                self.tabela_demandas.setRowCount(0)
                for linha in leitura:

                    row = self.tabela_demandas.rowCount()
                    self.tabela_demandas.insertRow(row)

                    for column, valor in enumerate(linha):
                        item = QtWidgets.QTableWidgetItem(str(valor))
                        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                        if item is None:
                            item = QtWidgets.QTableWidgetItem(str(""))
                        if column!= 9:
                            self.tabela_demandas.setItem(row, column, item)
                        button_widget = QtWidgets.QPushButton("Comprar Item")
                        button_widget.clicked.connect(lambda state, row=row: self.comprar(row))
                        self.tabela_demandas.setCellWidget(row, 9, button_widget)



        except mysql.connector.Error as e:
            print("Erro ao conectar ao MySQL:", e)

        finally:
            # Fechando a conexão com o banco de dados
            if 'connection' in locals() and connection.is_connected():
                cursor.close()
                connection.close()
                print("Conexão ao MySQL encerrada.")
    def comprar(self,row):
        item_name = self.tabela_demandas.item(row, 0).text()
        item_marca = self.tabela_demandas.item(row, 4).text()
        self.buscar_google(f'{item_name} da marca {item_marca}')

    def buscar_google(self,query):
        self.lista_de_url = []
        url = f"https://www.google.com/search?q={query}"

        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            search_results = soup.find_all('a')

            for result in search_results:
                title = result.get_text()
                url = result.get('href')
                if url.startswith('/url?q='):
                    url = url[7:]
                    url = url.split('&')[0]
                    print(f"{title}: {url}")
                    self.lista_de_url.append(f"{title}: {url}")
            self.baixar_imagens(query)
            self.criar_scrol(query)

        else:
            print("Falha ao fazer a solicitação.")

    def baixar_imagens(self,query):
        url = f"https://www.google.com/search?q={query}&tbm=isch"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        img_tags = soup.find_all('img')

        img_urls = [img['src'] for img in img_tags]
        import os

        if not os.path.exists(query):
            os.makedirs(query)

        for i, img_url in enumerate(img_urls):
            if i == 10:
                break
            try:
                img_data = requests.get(img_url).content
                with open(f"{query}/image_{i + 1}.jpg", 'wb') as f:
                    f.write(img_data)
                print(f"Imagem {i + 1} baixada com sucesso.")
            except Exception as e:
                print(f"Erro ao baixar imagem {i + 1}: {str(e)}")

    def criar_scrol(self,query):
        print(1)
        self.frame_scrol.show()
        h_layout_scrol = QtWidgets.QHBoxLayout()
        self.frame_scrol.setLayout(h_layout_scrol)
        layout = QtWidgets.QVBoxLayout()
        scroll_area = QtWidgets.QScrollArea()
        scroll_area.setWidgetResizable(True)
        print(2)

        content_widget = QtWidgets.QWidget()
        scroll_layout = QtWidgets.QVBoxLayout(content_widget)
        import os
        print(3)
        cont = 0
        for file_name in os.listdir(query):
            if file_name.endswith('.jpg') or file_name.endswith('.png'):
                image_path = os.path.join(query, file_name)
                name = self.lista_de_url[cont]
                print(name)
                frame = self.criar_frame_scrol(image_path,name,cont)
                scroll_layout.addWidget(frame)
                cont += 1
        print(4)

        scroll_area.setWidget(content_widget)
        fechar_frame_scroll = QtWidgets.QPushButton('Fechar')
        fechar_frame_scroll.setStyleSheet("QPushButton {\n"
"                    border: none ;\n"
"                    border-radius: 10px;\n"
"                    background-color: (131, 131, 131);\n"
"                    color:black;\n"
"                }\n"
"\n"
"                QPushButton:hover {\n"
"                    background-color: #DDDDDD;  /* Change this to your desired hover color */\n"
"                    color: rgb(0, 0, 0);\n"
"                }\n"
"\n"
"                QPushButton:pressed {\n"
"                    background-color: white;  /* Change this to your desired pressed color */\n"
"                    color: black;\n"
"                }")
        fechar_frame_scroll.clicked.connect(self.fechar_frame_scrol)
        h_layout_scrol.addWidget(fechar_frame_scroll)

        h_layout_scrol.addWidget(scroll_area)
        for widget in scroll_area.findChildren(QtWidgets.QWidget):
            widget.show()

    def fechar_frame_scrol(self):

        self.frame_scrol.hide()

    def criar_frame_scrol(self, image_path,name,cont):

        frame = QtWidgets.QFrame()
        frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        frame.setStyleSheet('border:none;background-color: white;')
        layout = QtWidgets.QHBoxLayout(frame)

        file_label = QtWidgets.QPushButton(name)

        image_label = QtWidgets.QLabel()
        pixmap = QtGui.QPixmap(image_path)
        image_label.setPixmap(pixmap)

        layout.addWidget(image_label)
        h_layout_image_label = QtWidgets.QHBoxLayout()
        frame.setLayout(h_layout_image_label)
        layout.addWidget(file_label)

        return frame

    def mousePressEvent(self, event, centralwidget):
        if event.button() == Qt.MouseButton.LeftButton:
            centralwidget.setCursor(Qt.CursorShape.ClosedHandCursor)
        centralwidget.mouse_offset = event.pos()
    def mouseReleaseEvent(self, event,centralwidget):
            if event.button() == Qt.MouseButton.LeftButton:
                    centralwidget.setCursor(Qt.CursorShape.OpenHandCursor)
    def mouseMoveEvent(self, event, centralwidget):
            if event.buttons() == Qt.MouseButton.LeftButton:
                    new_pos = centralwidget.mapToParent(event.pos() - centralwidget.mouse_offset)
                    centralwidget.move(new_pos)
                    x, y = new_pos.x(), new_pos.y()
