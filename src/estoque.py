# Part of Stoquee. See LICENSE file for full copyright and licensing details.
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import QDate

class Estoque(object):
    def abrir_estoque(self,Form,tela):
        self.tela = tela
        self.frame = self.tela.frame_estoque
        self.frame.show()
        self.tela.label.setText("Estoque")
        self.pesquisar_estoque = QtWidgets.QLineEdit(parent=self.frame)
        self.pesquisar_estoque.setGeometry(QtCore.QRect(320, 70, 431, 21))
        self.pesquisar_estoque.setStyleSheet("border: 2px solid #737373; border-radius: 10px; background-color: white;")
        self.pesquisar_estoque.setObjectName("pesquisar_estoque")
        self.pesquisar_estoque.show()
        icon = QtGui.QIcon('resources/assets/a_lupa.png')
        self.pesquisar_estoque.setPlaceholderText("Pesquisar Item")
        self.pesquisar_estoque.addAction(icon, QtWidgets.QLineEdit.ActionPosition.LeadingPosition)

        self.tabela_estoque = QtWidgets.QTableWidget(parent=self.frame)
        self.tabela_estoque.setGeometry(QtCore.QRect(250, 130, 991, 541))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tabela_estoque.show()

        self.tabela_estoque.setFont(font)
        self.tabela_estoque.setStyleSheet("background-color: transparent;\n"
                                          " border-radius: 10px;\n"
                                          "")
        self.tabela_estoque.setShowGrid(False)
        self.tabela_estoque.setObjectName("tabela_estoque")
        self.tabela_estoque.setColumnCount(7)
        self.tabela_estoque.setRowCount(6)

        item = QtWidgets.QTableWidgetItem()
        self.tabela_estoque.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_estoque.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_estoque.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_estoque.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_estoque.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_estoque.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_estoque.setHorizontalHeaderItem(6, item)

        self.pushButton_new_item = QtWidgets.QPushButton('New Item', parent=self.frame)
        self.pushButton_new_item.setGeometry(QtCore.QRect(1250, 50, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_new_item.setFont(font)
        self.pushButton_new_item.setStyleSheet("QPushButton {\n"
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
        icon6.addPixmap(QtGui.QPixmap("resources/assets/a_botao_adicionar.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_new_item.setIcon(icon6)
        self.pushButton_new_item.setIconSize(QtCore.QSize(23, 23))
        self.pushButton_new_item.setObjectName("pushButton_7")
        self.pushButton_new_item.show()
        self.pushButton_new_item.clicked.connect(self.criar_item)

        self.pushButton_confirmar_new_item = QtWidgets.QPushButton('Confirmar', parent=self.frame)
        self.pushButton_confirmar_new_item.setGeometry(QtCore.QRect(1200, 420, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_confirmar_new_item.setFont(font)
        self.pushButton_confirmar_new_item.setStyleSheet("QPushButton {\n"
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
        icon6.addPixmap(QtGui.QPixmap("resources/assets/a_botao_adicionar.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_confirmar_new_item.setIcon(icon6)
        self.pushButton_confirmar_new_item.setIconSize(QtCore.QSize(23, 23))
        self.pushButton_confirmar_new_item.setObjectName("pushButton_7")
        self.pushButton_confirmar_new_item.hide()
        self.pushButton_confirmar_new_item.clicked.connect(self.add_estoque)

        item = self.tabela_estoque.horizontalHeaderItem(0)
        item.setText("Item")
        item = self.tabela_estoque.horizontalHeaderItem(1)
        item.setText("Descrição do Item")
        item = self.tabela_estoque.horizontalHeaderItem(2)
        item.setText("Unidade do Item")
        item = self.tabela_estoque.horizontalHeaderItem(3)
        item.setText("Quantidade no Estoque")
        item = self.tabela_estoque.horizontalHeaderItem(4)
        item.setText("Ultima Aquisição")
        item = self.tabela_estoque.horizontalHeaderItem(5)
        item.setText("Marca")
        item = self.tabela_estoque.horizontalHeaderItem(6)
        item.setText("Preço Unitário")

        for colum in range(1, self.tabela_estoque.columnCount()):
            self.increase_column_width(colum, 135)
        self.atualiza_estoque()

    def analise(self):
        if self.tela.new_item_aberto == True:
            self.nome_item.hide()
            self.nome_item_label.hide()
            self.descricao_label.hide()
            self.descricao.hide()
            self.Combounidade.hide()
            self.unidade_label.hide()
            self.marca_item.hide()
            self.marca_label.hide()
            self.pushButton_confirmar_new_item.hide()


            self.pesquisar_estoque.show()
            self.pushButton_new_item.show()
            self.tabela_estoque.show()
            self.tela.new_item_aberto = False

    def increase_column_width(self, column, width):
        self.tabela_estoque.setColumnWidth(column, width)

    def criar_item(self):

        if self.tela.new_item_aberto == False:
            self.tela.label.setText("Cadastrar Item")
            self.pushButton_confirmar_new_item.show()

            self.tela.new_item_aberto = True


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
            self.Combounidade.addItem("Unidade - qt")
            self.Combounidade.addItem("Metros - m")
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

            self.nome_item.show()
            self.nome_item_label.show()
            self.descricao_label.show()
            self.descricao.show()
            self.Combounidade.show()
            self.unidade_label.show()
            self.marca_item.show()
            self.marca_label.show()

            self.pesquisar_estoque.hide()
            self.pushButton_new_item.hide()
            self.tabela_estoque.hide()
    def generar_numero(self):
        data = QDate.currentDate()
        dia = data.day()
        mes = data.month()
        import random
        random_numbers = ''.join(str(random.randint(0, 9)) for _ in range(4))
        generated_number = f"{dia:02}{mes:02}{random_numbers}"
        self.id = int(generated_number)
    def atualiza_estoque(self):
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

                query = "SELECT * FROM estoque"
                cursor.execute(query)
                leitura = cursor.fetchall()
                self.tabela_estoque.clearContents()
                self.tabela_estoque.setRowCount(0)
                for linha in leitura:

                    row = self.tabela_estoque.rowCount()
                    self.tabela_estoque.insertRow(row)

                    for column, valor in enumerate(linha):
                        item = QtWidgets.QTableWidgetItem(str(valor))
                        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                        if item is None:
                            item = QtWidgets.QTableWidgetItem(str(""))
                        if column == 0:
                            self.tabela_estoque.setVerticalHeaderItem(row, item)
                            continue
                        if column!= 9:
                            self.tabela_estoque.setItem(row, column-1, item)
                        button_widget = QtWidgets.QPushButton("Comprar Item")
                        #button_widget.clicked.connect(lambda state, row=row: self.comprar(row))
                        self.tabela_estoque.setCellWidget(row, 9, button_widget)



        except mysql.connector.Error as e:
            print("Erro ao conectar ao MySQL:", e)

        finally:
            # Fechando a conexão com o banco de dados
            if 'connection' in locals() and connection.is_connected():
                cursor.close()
                connection.close()
                print("Conexão ao MySQL encerrada.")
    def add_estoque(self):
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

                unidade = self.Combounidade.currentText()
                value = 0
                value_str = str(value)
                cursor = connection.cursor()
                data_hoje = QDate.currentDate()

                self.id = 0
                self.generar_numero()
                data_formatada = data_hoje.toString('dd/MM/yyyy')
                query = "INSERT INTO estoque (id,item, descricao,unidade,quantidade,ultima_aqui, marca,precounico) VALUES (%s,%s,%s, %s, %s,%s,%s, %s)"
                values = (f"{self.id}",f"{self.nome_item.text()}", f"{self.descricao.toPlainText()}",f"{unidade}",f"{value_str}",' / / /',f"{self.marca_item.text()}","",)
                cursor.execute(query, values)

                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Icon.Information)
                msg_box.setWindowTitle("AVISO")
                msg_box.setText("Item Cadastrado!")
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
