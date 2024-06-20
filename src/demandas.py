# Part of Stoquee. See LICENSE file for full copyright and licensing details.
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QMessageBox,QCompleter,QWidget,QVBoxLayout
import webbrowser
import requests
from bs4 import BeautifulSoup
from PyQt6.QtCore import Qt
import mysql.connector
from PyQt6.QtGui import QIcon
import mysql.connector
import os
from Interface import Interface



# A classe ClickableLabel é uma subclasse personalizada de QLabel que emite um sinal quando clicada.
class ClickableLabel(QtWidgets.QLabel):
    # Sinal personalizado emitido quando o label é clicado
    clicked = QtCore.pyqtSignal()

    # Método que captura o evento de clique do mouse

    def mousePressEvent(self, event):
        '''
        
        :param event: A função é chamdad quando o certo evento acontece
        :return: Nao retorna nada 
        '''
        self.clicked.emit()

# A classe Demandas é a janela principal da aplicação.
class Demandas(Interface):

    # O método Tela tem a função de criar uma tela.
    # É um método de interface gráfica. Este método cria frames, labels e botões, e conecta esses widgets às suas respectivas funções.

    def Tela(self, Form=None,dema=int,tela=None) -> None:
        '''
        :param Form: Tela
        :param dema: Atributo escolhido pelo usuário entre 1, 2 e 3
        :param tela: Atributo recebido do arquivo tela_inicial, ele representa todos os
        :return: Não retorna nada
        '''
        self.tela = tela
        self.frame = self.tela.frame_demandas

        #Dema é um inteiro utilizado para definir qual tela sera aberta.
        # A tela de tabela de demandas ou de criação de demandas funcionarios ou estoque.
        if dema == 1:
            self.pushButton_confirmar_alteracao = QtWidgets.QPushButton('Confirmar', parent=self.frame)
            self.pushButton_confirmar_alteracao.setGeometry(QtCore.QRect(1200, 50, 111, 31))
            font = QtGui.QFont()
            font.setPointSize(11)
            font.setBold(True)
            font.setWeight(75)
            self.pushButton_confirmar_alteracao.setFont(font)
            self.pushButton_confirmar_alteracao.setStyleSheet("QPushButton {\n"
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
            icon6.addPixmap(QtGui.QPixmap("resources/assets/a_botao_adicionar.png"), QtGui.QIcon.Mode.Normal,
                            QtGui.QIcon.State.Off)  # Icone do botão
            self.pushButton_confirmar_alteracao.setIcon(icon6)
            self.pushButton_confirmar_alteracao.setIconSize(QtCore.QSize(23, 23))
            self.pushButton_confirmar_alteracao.setObjectName("pushButton_7")
            self.pushButton_confirmar_alteracao.clicked.connect(lambda: self.altera_table('Não Tabela'))
            self.pushButton_confirmar_alteracao.hide()

            self.editable = False

            self.enter_pressed = False

            self.radioButton_Estoque = QtWidgets.QRadioButton(parent=self.frame)
            self.radioButton_Estoque.setGeometry(QtCore.QRect(250, 80, 82, 17))
            self.radioButton_Estoque.setObjectName("radioButton_Estoque")

            self.radioButton_Demandas = QtWidgets.QRadioButton(parent=self.frame)
            self.radioButton_Demandas.setGeometry(QtCore.QRect(370, 80, 82, 17))
            self.radioButton_Demandas.setObjectName("radioButton_Demandas")

            self.tabela_alt = QtWidgets.QTableWidget()
            self.tabela_alt2 = QtWidgets.QTableWidget()

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

            self.tabela_apoio = QtWidgets.QTableWidget()

            conta_linha = self.tabela_demandas.rowCount()
            conta_coluna = self.tabela_demandas.columnCount()
            self.tabela_apoio.setColumnCount(conta_coluna)
            self.tabela_apoio.setRowCount(conta_linha)

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
            self.pesquisar_demandas.textChanged.connect(self.pesquisar)

            self.radioButton_Estoque.show()
            self.pesquisar_demandas.show()
            self.radioButton_Demandas.show()
            self.tabela_demandas.show()

            self.radioButton_Demandas.setChecked(True)
            self.radioButton_Estoque.setChecked(False)

            self.radioButton_Demandas.toggled.connect(self.atualizar_tabela)
            self.radioButton_Estoque.toggled.connect(self.atualizar_tabela)

            self.ler_database()

            self.atualizar_tabela()

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

            self.frame_foto = QtWidgets.QFrame(self.frame)
            self.frame_foto.hide()
            self.frame_foto.setGeometry(QtCore.QRect(450, 50, 505, 610))
            self.frame_foto.setFrameShape(QtWidgets.QFrame.Shape.Box)
            self.frame_foto.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
            self.frame_foto.setStyleSheet(f'background-color: rgb(212, 212, 212);'
                                             f'color: black;'
                                             f'font: arial 12px;'
                                             f'border: 2px solid #2E3D48;'
                                             f'border-radius: 10px;')

            self.tabela_demandas.setEditTriggers(QtWidgets.QTableWidget.EditTrigger.NoEditTriggers)

            self.analise_edit_tabela = 'Nenhum'
            self.tabela_demandas.doubleClicked.connect(lambda: self.altera_table('Tabela'))

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

            self.nome_item = QtWidgets.QLineEdit(parent=self.frame)
            self.nome_item.setGeometry(QtCore.QRect(290, 100, 331, 20))
            self.nome_item.setStyleSheet("border: 2px solid #737373; border-radius: 10px; background-color: white;")

            self.nome_item.textChanged.connect( self.procurar_nome_data)

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

            self.marca_item = QtWidgets.QLineEdit(parent=self.frame)
            self.marca_item.setGeometry(QtCore.QRect(900, 100, 331, 20))
            self.marca_item.setStyleSheet("border: 2px solid #737373; border-radius: 10px; background-color: white;")

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
        icon6.addPixmap(QtGui.QPixmap("resources/assets/a_botao_adicionar.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off) # Icone do botão
        self.pushButton_confirmar_new_demanda.setIcon(icon6)
        self.pushButton_confirmar_new_demanda.setIconSize(QtCore.QSize(23, 23))
        self.pushButton_confirmar_new_demanda.setObjectName("pushButton_7")
        self.pushButton_confirmar_new_demanda.clicked.connect(lambda: self.add_demandas(dema))


        if dema != 1:
            self.pushButton_confirmar_new_demanda.show()
        else:
            self.pushButton_confirmar_new_demanda.hide()
        self.lista_nome = []

    # Método procurar_nome_data usado para fazer pesquisa no database.
    # A pesquisa tem objetico de achar os itens cadastrados no estoque.
    # Esse método abre o data base e procura se o Item do estoque existe no banco de dados e coloca em uma lista
    def procurar_nome_data(self,pesquisa:str) -> None:
        '''
        
        :param pesquisa: Atribuido pelo usuário quando fez a pesquisa no line edit. Es
        :return: Não retorna nada 
        '''
        if pesquisa != '':
            try:
                if len(self.lista_nome) == 0:
                    conexao = mysql.connector.connect(
                        host="monorail.proxy.rlwy.net",
                        port=30980,
                        user="root",
                        password="RXlnFIuFEKMvnYsMaPWvDimjLdGyoJVv",
                        database="railway"
                    )
                    cursor = conexao.cursor()
                    comando = f'SELECT * FROM estoque'
                    cursor.execute(comando)
                    leitura = cursor.fetchall()
                    self.analise_leitura = leitura
                    self.lista_nome = [str(valor[1]) for valor in leitura if valor[1] is not None]

                    conexao.commit()
                    cursor.close()
                    conexao.close()

                completer = QCompleter(self.lista_nome, self.frame)
                completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
                self.nome_item.setCompleter(completer)
                if self.lista_nome:
                    if pesquisa in self.lista_nome:
                        posicao = self.lista_nome.index(pesquisa)
                        nome = str(self.analise_leitura[posicao][1]) if self.analise_leitura[posicao][
                                                                            1] is not None else "N/A"
                        marca = str(self.analise_leitura[posicao][6]) if self.analise_leitura[posicao][
                                                                             6] is not None else "N/A"
                        unidade = str(self.analise_leitura[posicao][3]) if self.analise_leitura[posicao][
                                                                               3] is not None else "N/A"

                        self.nome_item.setText(nome)
                        self.marca_item.setText(marca)
                        self.Combounidade.setItemText(0, f"{unidade}")



            except mysql.connector.Error as e:
                print("Erro ao conectar ao MySQL:", e)

    # Método add_demandas usado para adicionar novas demandas ao dabase.
    def add_demandas(self,dema:int) -> None:
        '''
         
        :param dema: inteiro definido pelo usuário quando o mesmo escolhe entre demandas, criar demanda de funcionário ou de estoque 
        :return: Não retorna nada
        '''
        import mysql.connector
        host = "monorail.proxy.rlwy.net"
        port = 30980
        user = "root"
        password = "RXlnFIuFEKMvnYsMaPWvDimjLdGyoJVv"
        database = "railway"

        if len(self.marca_item.text()) == 0:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Icon.Information)
            msg_box.setWindowTitle("AVISO")
            msg_box.setText(f"A marca deve ser informada.")
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            reply = msg_box.exec()

        elif dema == 3 and not self.nome_item.text() in self.lista_nome:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Icon.Information)
            msg_box.setWindowTitle("AVISO")
            msg_box.setText(f"O item {self.nome_item.text()} não existe no Estoque.\nCadastre primeiro.")
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            reply = msg_box.exec()


        elif dema == 2 and len(self.descricao.toPlainText()) == 0:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Icon.Information)
            msg_box.setWindowTitle("AVISO")
            msg_box.setText(f"A descrição deve ser preenchida.")
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            reply = msg_box.exec()
        else:
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
                    value = self.Quantidade_item.value()
                    value_str = str(value)
                    cursor = connection.cursor()
                    data_hoje = QDate.currentDate()
                    self.id = 0
                    self.generar_numero(dema)
                    if dema == 3:
                        descricao = ''
                    if dema == 2:
                        descricao = self.descricao.toPlainText()
                    data_formatada = data_hoje.toString('dd/MM/yyyy')
                    query = "INSERT INTO demanda (id,item, descricao,unidade,quantidade, marca,precounico,precototal,status,data) VALUES (%s,%s, %s, %s,%s,%s, %s, %s,%s,%s)"
                    values = (f"{self.id}", f"{self.nome_item.text()}", f"{descricao}", f"{unidade}",
                              f"{value_str}", f"{self.marca_item.text()}", "", '', 'Aguardando', f'{data_formatada}')
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

    # Método generar_numero usado para gerar um número aleatório.
    # O numero deve ser par para demandas dos funcionarios e ímpar para demandas do Estoque.
    def generar_numero(self,type:int) -> None:
        '''
        
        :param type: inteiro para saber se é um número par ou impar que deve ser gerado
        :return:NÃO RETORNA NADA 
        '''
        data = QDate.currentDate()
        dia = data.day()
        mes = data.month()
        import random
        random_numbers = ''.join(str(random.randint(0, 9)) for _ in range(3))

        if type == 2:
            last_digit = random.choice([2, 4, 6, 8])
        if type == 3:
            last_digit = random.choice([1, 3, 5, 7, 9])

        random_numbers += str(last_digit)
        generated_number = f"{dia:02}{mes:02}{random_numbers}"
        self.id = int(generated_number)

    # O método ler_dabase faz conexão e lê o database chamando o método de atualizar a tabela.
    def ler_database(self)-> None:
        self.lista_linhas_par = []
        self.lista_linhas_impar = []
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
                self.tabela_apoio.clearContents()
                self.tabela_apoio.setRowCount(0)
                for linha in leitura:

                    row = self.tabela_apoio.rowCount()
                    self.tabela_apoio.insertRow(row)

                    for column, valor in enumerate(linha):
                        item = QtWidgets.QTableWidgetItem(str(valor))
                        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                        if item is None:
                            item = QtWidgets.QTableWidgetItem(str(""))

                        if column == 9:
                            if int(item.text()) % 2 == 0:
                                self.lista_linhas_par.append((row,item.text()))
                            if int(item.text()) % 2 == 1:
                                self.lista_linhas_impar.append((row,item.text()))
                        self.tabela_apoio.setItem(row, column, item)


        except mysql.connector.Error as e:
            print("Erro ao conectar ao MySQL:", e)

        finally:
            # Fechando a conexão com o banco de dados
            if 'connection' in locals() and connection.is_connected():
                cursor.close()
                connection.close()
                print("Conexão ao MySQL encerrada.")

    # O método atualizar_tabela atualiza a tabela_demandas de acordo com qual tipo de demanda o usuário deseja.
    # Demanda de estoque ou dos funcionários
    def atualizar_tabela(self)-> None:
        '''
        
        :return: Não retorna nada
        '''
        if self.radioButton_Demandas.isChecked() or self.radioButton_Estoque.isChecked():
            analise = []
            if self.radioButton_Demandas.isChecked():
                analise = self.lista_linhas_par
            if self.radioButton_Estoque.isChecked():
                analise = self.lista_linhas_impar

            self.tabela_demandas.clearContents()
            self.tabela_demandas.setRowCount(0)
            conta_coluna = self.tabela_apoio.columnCount()

            for linha,id in analise:
                row = self.tabela_demandas.rowCount()

                self.tabela_demandas.insertRow(row)

                for analisa_coluna in range(conta_coluna):
                    if analisa_coluna != 9:
                        item = self.tabela_apoio.item(linha, analisa_coluna)
                        item_text = QtWidgets.QTableWidgetItem(str(""))
                        if item is not None:
                            item_text = item.text()
                        item_copy = QtWidgets.QTableWidgetItem(item_text)
                        item_copy.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                        self.tabela_demandas.setItem(row, analisa_coluna, item_copy)

                    if analisa_coluna == 9:
                        item_text = ""
                        if id is not None:
                            item_text = id
                        item_copy = QtWidgets.QTableWidgetItem(item_text)
                        item_copy.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

                        self.tabela_demandas.setVerticalHeaderItem(row, item_copy)
                if self.tabela_demandas.item(row,7).text() == 'Aguardando':
                    button_widget = QtWidgets.QPushButton("Comprar Item")
                    button_widget.clicked.connect(lambda state, row=row: self.comprar(row))
                    self.tabela_demandas.setCellWidget(row, 9, button_widget)
                if self.tabela_demandas.item(row,7).text() == 'Compra Realizada':
                    button_widget = QtWidgets.QPushButton("Confirmar Item")
                    button_widget.clicked.connect(lambda state, row=row: self.confirmar_item(row))
                    self.tabela_demandas.setCellWidget(row, 9, button_widget)

    # Método comprar pega o item na tabela para uma busca no google.
    def comprar(self,row:int)-> None:
        '''
        
        :param row: linha em qual se encontra o item que será comprado
        :return: Não retorna nada
        '''
        self.linha_ = row
        item_name = self.tabela_demandas.item(row, 0).text()
        item_marca = self.tabela_demandas.item(row, 4).text()
        self.buscar_google(f'{item_name} da marca {item_marca}')


    # Método buscar_google faz uma busca no google do item escolhido.
    def buscar_google(self,query: str)-> None:
        '''
        
        :param query: str que é o link de onde foi tirado o item
        :return: Não retorna nada
        '''
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
                    self.lista_de_url.append((title,url))
            self.baixar_imagens(query)
            self.criar_scrol(query)

        else:
            print("Falha ao fazer a solicitação.")

    # Método baixar_imagens baixa as imagens do google
    def baixar_imagens(self,query:str) -> None:
        '''
            :param query: str que é o link de onde foi tirado o item
            :return: Não retorna nada        
        '''
        url = f"https://www.google.com/search?q={query}&tbm=isch"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        img_tags = soup.find_all('img')

        img_urls = [img['src'] for img in img_tags]

        if not os.path.exists(f"resources/assets/{query}"):
            os.makedirs(f"resources/assets/{query}")

        for i, img_url in enumerate(img_urls):
            if i == 10:
                break
            try:
                img_data = requests.get(img_url).content
                with open(f"resources/assets/{query}/image_{i + 1}.jpg", 'wb') as f: # Salvando a imagem, acho que deve ser em resources/products ou algo assim
                    f.write(img_data)
                print(f"Imagem {i + 1} baixada com sucesso.")
            except Exception as e:
                print(f"Erro ao baixar imagem {i + 1}: {str(e)}")

    # Método criar_scrol é um método gráfico que cria um scrol onde fica as imagens.
    # Scrol é diferente do frame, o scrol possui a barra de rolagem.
    def criar_scrol(self,query:str) -> None:
        '''
            :param query: str que é o link de onde foi tirado o item
            :return: Não retorna nada
        '''
        self.frame_scrol.show()

        h_layout_scrol = QtWidgets.QHBoxLayout()
        self.frame_scrol.setLayout(h_layout_scrol)
        layout = QtWidgets.QVBoxLayout()
        scroll_area = QtWidgets.QScrollArea()
        scroll_area.setWidgetResizable(True)

        content_widget_painel = QWidget()
        main_layout_painel = QVBoxLayout(content_widget_painel)
        scroll_area.setWidget(content_widget_painel)
        cont = 0

        fechar_frame_scroll = QtWidgets.QPushButton('Fechar')
        fechar_frame_scroll.setFixedSize(111, 30)
        fechar_frame_scroll.setStyleSheet("QPushButton {\n"
                                          "                    border: 1px solid black ;\n"
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
        main_layout_painel.addWidget(fechar_frame_scroll)

        for file_name in os.listdir(f"resources/assets/{query}"):
            if file_name.endswith('.jpg') or file_name.endswith('.png'):
                image_path = os.path.join(query, file_name)
                name = self.lista_de_url[cont][0]
                link = self.lista_de_url[cont][1]
                frame = self.criar_frame_scrol(image_path,name,cont,link)

                file_label = QtWidgets.QPushButton(name)
                file_label.clicked.connect(
                    lambda _, name_2=name, image_path_2=image_path, link_2=link: self.abrir_tela_foto(name_2,image_path_2,link_2))
                file_label.setStyleSheet("""
                                QPushButton {
                                    border: 2px solid #2E3D48;
                                    border-radius: 10px;
                                    background-color: #FFFFFF;
                                    color: #2E3D48;
                                }

                                QPushButton:hover {
                                    background-color: #DDDDDD;  /* Change this to your desired hover color */
                                    color: rgb(0, 0, 0);
                                }

                                QPushButton:pressed {
                                    background-color: #2E3D48;  /* Change this to your desired pressed color */
                                    color: #FFFFFF;
                                }
                            """)

                main_layout_painel.addWidget(file_label)
                main_layout_painel.addWidget(frame)
                cont += 1

        h_layout_scrol.addWidget(scroll_area)
        for widget in scroll_area.findChildren(QtWidgets.QWidget):
            widget.show()

    # Método fechar_frame_scrol fecha o scrol quando solicitado.
    def fechar_frame_scrol(self) -> None:
        '''
        
        :return: Não retorna nada
        '''

        self.frame_scrol.deleteLater()

        self.frame_scrol = QtWidgets.QFrame(parent=self.frame)
        self.frame_scrol.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_scrol.setGeometry(QtCore.QRect(450, 50, 505, 610))
        self.frame_scrol.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_scrol.setObjectName("frame")
        self.frame_scrol.hide()
        self.frame_scrol.setCursor(QtCore.Qt.CursorShape.OpenHandCursor)
        self.frame_scrol.mousePressEvent = lambda event, centralwidget=self.frame_scrol: self.mousePressEvent(event,
                                                                                                              centralwidget)
        self.frame_scrol.mouseReleaseEvent = lambda event, centralwidget=self.frame_scrol: self.mouseReleaseEvent(event,
                                                                                                                  centralwidget)
        self.frame_scrol.mouseMoveEvent = lambda event, centralwidget=self.frame_scrol: self.mouseMoveEvent(event,
                                                                                                            centralwidget)
        self.frame_scrol.setStyleSheet(f'background-color: rgb(212, 212, 212);'
                                       f'color: black;'
                                       f'font: arial 12px;'
                                       f'border: 2px solid #2E3D48;'
                                       f'border-radius: 10px;')
        self.frame_foto.deleteLater()

        self.frame_foto = QtWidgets.QFrame(self.frame)
        self.frame_foto.hide()
        self.frame_foto.setGeometry(QtCore.QRect(450, 50, 505, 610))
        self.frame_foto.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_foto.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_foto.setStyleSheet(f'background-color: rgb(212, 212, 212);'
                                      f'color: black;'
                                      f'font: arial 12px;'
                                      f'border: 2px solid #2E3D48;'
                                      f'border-radius: 10px;')
    # O método criar_frame_scrol cria um frame que será anexado ao scrol. Existe um frame para cada imagem.
    def criar_frame_scrol(self, image_path:str,name:str,cont:int,link:str) -> QtWidgets.QFrame:

        '''

        :param image_path: str que é o nome ao qual foi atribuido a imagem na máquina
        :param name: str do nome do item
        :param cont: int que representa uma posicao na lista de imagens
        :param link: str do link da imagem
        :return: retorna um frame que é usado em cada imagem. Cada imagem tem um frame
        '''

        frame = QtWidgets.QFrame()
        frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        frame.setStyleSheet('border:none;background-color: white;')


        layout = QtWidgets.QHBoxLayout(frame)

        image_label = QtWidgets.QLabel()
        image_label.setFixedSize(300,300)
        pixmap = QtGui.QPixmap(f"resources/assets/{image_path}")
        scaled_pixmap = pixmap.scaled(image_label.size(), Qt.AspectRatioMode.KeepAspectRatio,
                                      Qt.TransformationMode.SmoothTransformation)

        image_label.setPixmap(scaled_pixmap)

        image_label.setScaledContents(True)

        layout.addWidget(image_label)
        h_layout_image_label = QtWidgets.QHBoxLayout()
        frame.setLayout(h_layout_image_label)

        return frame

    # O método fechar_frame_foto fecha o frame da foto.
    def fechar_frame_foto(self) -> None:
        '''

        :return: Não retorna nada
        '''
        self.frame_foto.deleteLater()

        self.frame_foto = QtWidgets.QFrame(self.frame)
        self.frame_foto.hide()
        self.frame_foto.setGeometry(QtCore.QRect(450, 50, 505, 610))
        self.frame_foto.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_foto.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_foto.setStyleSheet(f'background-color: rgb(212, 212, 212);'
                                      f'color: black;'
                                      f'font: arial 12px;'
                                      f'border: 2px solid #2E3D48;'
                                      f'border-radius: 10px;')

        self.frame_scrol.show()

    # O método abrir_tela_foto a bre um frame somente com a foto e o link para efetuar a compra.
    def abrir_tela_foto(self,name:str,image_path:str,link:str) -> None:
        '''

        param image_path: str que é o nome ao qual foi atribuido a imagem na máquina
        :param name: str do nome do item
        :param link: str do link da imagem
        :return: Não retorna nada
        '''
        self.frame_foto.show()
        self.frame_scrol.hide()

        self.atualizar_compra()

        self.ler_database()

        fechar_frame_scroll = QtWidgets.QPushButton('Fechar',self.frame_foto)
        fechar_frame_scroll.clicked.connect(self.fechar_frame_foto)
        fechar_frame_scroll.setGeometry(QtCore.QRect(5, 5, 110, 30))
        fechar_frame_scroll.show()
        fechar_frame_scroll.setStyleSheet("QPushButton {\n"
                                          "                    border: 1px solid black ;\n"
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
        text = f"Clique <span style='color: blue;'>aqui</span> para seguir para o site."
        label_link = ClickableLabel(text, self.frame_foto)
        label_link.setGeometry(QtCore.QRect(5, 550, 500, 30))
        label_link.clicked.connect(lambda: self.open_link(link))
        label_link.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_link.setStyleSheet(
            "font-size: 12px; margin: 0; padding: 0;border: none;")
        label_link.show()
        label_link.setWordWrap(True)

        image_label = QtWidgets.QLabel(self.frame_foto)
        image_label.setGeometry(QtCore.QRect(100, 80, 300, 300))
        pixmap = QtGui.QPixmap(f"resources/assets/{image_path}")  # Carregando a imagem
        image_label.show()
        image_label.setStyleSheet("border: none;")
        label = QtWidgets.QLabel(name,self.frame_foto)
        label.setGeometry(QtCore.QRect(100, 40, 100, 30))
        label.setStyleSheet("border: none;")
        label.show()

        scaled_pixmap = pixmap.scaled(image_label.size(), Qt.AspectRatioMode.KeepAspectRatio,
                                      Qt.TransformationMode.SmoothTransformation)

        image_label.setPixmap(scaled_pixmap)

        image_label.setScaledContents(True)

    # Método open_link abre o link do google. Algumas maquinas por questão de segurança não vão permitir que isso aconteça.
    def open_link(self,url:str) -> None:
        '''

        :param url: str do link da imagem
        :return: Não retorna nada
        '''
        webbrowser.open(url)

    # Métodos mousePressEvent, mouseMoveEvent e mouseReleaseEvent.
    # Usados para movimentar as telas que contem as imagens geradas pelo google.
    def mousePressEvent(self, event: None, centralwidget:None)-> None:
        '''
        :param event: evento que acontece para a funcão ser chamada
        :param centralwidget: frame
        :return: Não retorna nada
        '''
        if event.button() == Qt.MouseButton.LeftButton:
            centralwidget.setCursor(Qt.CursorShape.ClosedHandCursor)
        centralwidget.mouse_offset = event.pos()
    def mouseReleaseEvent(self, event: None, centralwidget:None)-> None:
        '''
        :param event: evento que acontece para a funcão ser chamada
        :param centralwidget: frame
        :return: Não retorna nada
        '''
        if event.button() == Qt.MouseButton.LeftButton:
            centralwidget.setCursor(Qt.CursorShape.OpenHandCursor)
    def mouseMoveEvent(self,  event: None, centralwidget:None)-> None:
        '''
        :param event: evento que acontece para a funcão ser chamada
        :param centralwidget: frame
        :return: Não retorna nada
        '''

        if event.buttons() == Qt.MouseButton.LeftButton:
            new_pos = centralwidget.mapToParent(event.pos() - centralwidget.mouse_offset)
            centralwidget.move(new_pos)
            x, y = new_pos.x(), new_pos.y()

    # Método pesquisar usado para fazer pesquisa na tabela.
    def pesquisar(self, pesquisa:str)->None:

        '''

        :param pesquisa: str da pesquisa feita pelo usuário ao digitar no line edit
        :return: Não retorna nada
        '''
        for row in range(self.tabela_demandas.rowCount()):
            item = self.tabela_demandas.item(row, 0)
            item2 = self.tabela_demandas.item(row, 1)
            if item is not None:
                if pesquisa.lower() in item.text().lower() or pesquisa.lower() in item2.text().lower():
                    self.tabela_demandas.showRow(row)
                else:
                    self.tabela_demandas.hideRow(row)

    # Método altera_table usado alterar a tabela e salvar as alterações.
    def altera_table(self,nivel:str) -> None:

        '''

        :param nivel: nivel é um str que india se a tabela está em estado de alteração ou não
        :return: Não retorna nada
        '''
        if self.analise_edit_tabela != nivel :
            colum_item = 0
            colum_status = 0
            colum_preco_total = 0
            colum_preco_unitario = 0
            colum_data = 0
            colum_quantidade = 0
            colum_marca = 0
            colum_unidade = 0
            colum_desc = 0

            for colum in range(self.tabela_demandas.columnCount()):
                item_pac = self.tabela_demandas.horizontalHeaderItem(colum)

                if item_pac.text() == 'Descrição do Item':
                    colum_desc = colum
                if item_pac.text() == 'Unidade do Item':
                    colum_unidade = colum
                if item_pac.text() == "Item":
                    colum_item = colum
                if item_pac.text() == "Quantidade":
                    colum_quantidade = colum
                if item_pac.text() == 'Marca':
                    colum_marca = colum
                if item_pac.text() == 'Preço Unitário':
                    colum_preco_unitario = colum
                if item_pac.text() == 'Preço Total':
                    colum_preco_total = colum
                if item_pac.text() == 'Status':
                    colum_status = colum
                if item_pac.text() == 'Data do Pedido':
                    colum_data = colum

            self.lista_modificacoes = []
            if self.tabela_demandas.rowCount() > 0:
                self.editable = not self.editable
                self.tabela_demandas.setEditTriggers(
                    QtWidgets.QTableWidget.EditTrigger.AllEditTriggers if self.editable else QtWidgets.QTableWidget.EditTrigger.NoEditTriggers)

                if self.editable:
                    self.analise_edit_tabela = "Tabela"
                    self.copiadora()

                    self.pushButton_confirmar_alteracao.show()

                    msg_box = QMessageBox()
                    msg_box.setIcon(QMessageBox.Icon.Information)
                    msg_box.setWindowTitle("AVISO")
                    msg_box.setText("A tabela está habilitada para edição")
                    icon = QIcon('resources/assets/warning.ico')
                    msg_box.setWindowIcon(icon)
                    msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
                    msg_box.exec()
                else:

                    self.analise_edit_tabela = 'Nenhum'
                    self.modificao()
                    if len(self.lista_modificacoes) != 0:
                        msg_box = QMessageBox()
                        msg_box.setIcon(QMessageBox.Icon.Information)
                        msg_box.setWindowTitle("AVISO")
                        msg_box.setText("Confirmar Alteração ?")
                        icon = QIcon('warning.ico')
                        msg_box.setWindowIcon(icon)
                        msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                        reply = msg_box.exec()
                        if reply == QMessageBox.StandardButton.Yes:
                            msg_box = QMessageBox()
                            msg_box.setIcon(QMessageBox.Icon.Information)
                            msg_box.setWindowTitle("AVISO")
                            msg_box.setText("Alteração Concluída com Sucesso!")
                            icon = QIcon(
                                'resources/assets/warning.ico')
                            msg_box.setWindowIcon(icon)
                            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
                            reply = msg_box.exec()

                            for row in self.lista_modificacoes:
                                id = self.tabela_demandas.verticalHeaderItem(row)
                                item = self.tabela_demandas.item(row, colum_item)
                                descricao = self.tabela_demandas.item(row, colum_desc)
                                status = self.tabela_demandas.item(row, colum_status)
                                preco_total = self.tabela_demandas.item(row, colum_preco_total)
                                preco_unitario = self.tabela_demandas.item(row, colum_preco_unitario)
                                data = self.tabela_demandas.item(row, colum_data)
                                marca = self.tabela_demandas.item(row, colum_marca)
                                quantidade = self.tabela_demandas.item(row, colum_quantidade)
                                unidade = self.tabela_demandas.item(row, colum_unidade)
                                self.alt_banco(item, descricao, unidade, quantidade, marca, preco_unitario, preco_total,
                                               status, data, id)

                            self.ler_database()
                    else:
                        msg_box = QMessageBox()
                        msg_box.setIcon(QMessageBox.Icon.Information)
                        msg_box.setWindowTitle("AVISO")
                        msg_box.setText("Nenhuma Alteração Realizada")
                        icon = QIcon('resources/assets/warning.ico')
                        msg_box.setWindowIcon(icon)
                        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
                        msg_box.exec()

                    self.pushButton_confirmar_alteracao.hide()

    # Método copiadora copia a tabela de demandas.
    def copiadora(self) -> None:
        '''

        :return: Não retorna nada
        '''
        conta_linha = self.tabela_demandas.rowCount()
        conta_coluna = self.tabela_demandas.columnCount()
        self.tabela_alt.setColumnCount(conta_coluna)
        self.tabela_alt.setRowCount(conta_linha)
        for analisa_linha in range(conta_linha):
            for analisa_coluna in range(conta_coluna - 1):
                item = self.tabela_demandas.item(analisa_linha, analisa_coluna + 1)
                if item is not None:
                    item_text = item.text()
                    item_copy = QtWidgets.QTableWidgetItem(item_text)
                    self.tabela_alt.setItem(analisa_linha, analisa_coluna + 1, item_copy)

    # Método copiadora2 copia a tabela de demandas para uma segunda tabela.
    def copiadora2(self) -> None:
        '''

        :return: Não retorna nada
        '''
        conta_linha = self.tabela_demandas.rowCount()
        conta_coluna = self.tabela_demandas.columnCount()
        self.tabela_alt2.setColumnCount(conta_coluna)
        self.tabela_alt2.setRowCount(conta_linha)
        for analisa_linha in range(conta_linha):
            for analisa_coluna in range(conta_coluna - 1):
                item = self.tabela_demandas.item(analisa_linha, analisa_coluna + 1)
                if item is not None:
                    item_text = item.text()
                    item_copy = QtWidgets.QTableWidgetItem(item_text)
                    self.tabela_alt2.setItem(analisa_linha, analisa_coluna + 1, item_copy)

    # Método moficacao verifica se ouve alguma modificação na tabela. E pega qual o item alterado.
    def modificao(self) -> None:
        '''

        :return: Não retorna nada
        '''
        self.copiadora2()

        conta_linha = self.tabela_alt2.rowCount()
        conta_coluna = self.tabela_alt2.columnCount()
        for analisa_linha in range(conta_linha):
            for analisa_coluna in range(conta_coluna - 1):
                item = self.tabela_alt2.item(analisa_linha, analisa_coluna + 1)
                item2 = self.tabela_alt.item(analisa_linha, analisa_coluna + 1)
                if item is not None and item2 is not None:
                    if item.text() != item2.text():
                        self.lista_modificacoes.append(analisa_linha)

    # Método alt_banco altera o database no respectivo item alterado na tabela.
    def alt_banco(self,item:str,descricao:str,unidade:str,quantidade:int,marca:str,precounico:str,precototal:str,status:str,data:str,id:int) -> None:
        '''

        :param item: str que representa o nome do item
        :param descricao: str que representa a descrição do item
        :param unidade: str que representa a unidade do item
        :param quantidade: int que rerpresenta a quantidade de itens
        :param marca: str que representa a marca do item
        :param precounico: str que representa o preço unitário do item
        :param precototal: str que representa o preço total do item
        :param status: str que representa o status do item
        :param data: str que representa a data do item
        :param id: int que representa o id no banco de dados
        :return:
        '''
        try:
            conexao = mysql.connector.connect(
                host="monorail.proxy.rlwy.net",
                port=30980,
                user="root",
                password="RXlnFIuFEKMvnYsMaPWvDimjLdGyoJVv",
                database="railway"
            )
            cursor = conexao.cursor()
            comando = f'UPDATE demanda SET item = "{item.text()}",descricao = "{descricao.text()}",unidade = "{unidade.text()}", quantidade = "{quantidade.text()}", marca = "{marca.text()}", precounico = "{precounico.text()}", precototal = "{precototal.text()}",status =  "{status.text()}",data = "{data.text()}"  WHERE id = "{id.text()}"'

            cursor.execute(comando)
            conexao.commit()
            cursor.close()
            conexao.close()
        except mysql.connector.Error as error:
            print("Erro ao conectar ao MySQL:", error)

    # O método atualizar_compra confirma a compra e atualiza o database
    def atualizar_compra(self)->None:
        '''

        :return: Não retorna nada
        '''
        try:
            conexao = mysql.connector.connect(
                host="monorail.proxy.rlwy.net",
                port=30980,
                user="root",
                password="RXlnFIuFEKMvnYsMaPWvDimjLdGyoJVv",
                database="railway"
            )
            cursor = conexao.cursor()
            id = self.tabela_demandas.verticalHeaderItem(self.linha_)

            comando = f'UPDATE demanda SET status =  "Compra Realizada"  WHERE id = "{id.text()}"'

            cursor.execute(comando)
            conexao.commit()
            cursor.close()
            conexao.close()
        except mysql.connector.Error as error:
            print("Erro ao conectar ao MySQL:", error)

    # O método confirmar_item confirma que o item foi recebido e atualiza o database
    def confirmar_item(self,row:int) -> None:
        '''

        :param row: int que representa a linha que se encontra o item
        :return: Não retorna nada
        '''
        print('e')
        try:
            conexao = mysql.connector.connect(
                host="monorail.proxy.rlwy.net",
                port=30980,
                user="root",
                password="RXlnFIuFEKMvnYsMaPWvDimjLdGyoJVv",
                database="railway"
            )
            cursor = conexao.cursor()
            id = self.tabela_demandas.verticalHeaderItem(row)
            print(id)
            comando = f'DELETE FROM demanda WHERE id = "{id.text()}"'
            print('e')

            cursor.execute(comando)
            conexao.commit()
            cursor.close()
            conexao.close()
            if not self.radioButton_Estoque.isChecked():
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Icon.Information)
                msg_box.setWindowTitle("AVISO")
                msg_box.setText(f"Item deve ser entregue ao funcionário.")
                msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
                reply = msg_box.exec()
        except mysql.connector.Error as error:
            print("Erro ao conectar ao MySQL:", error)

        if self.radioButton_Estoque.isChecked():
            print('e')
            quantidade_inicial = 0
            try:
                conexao = mysql.connector.connect(
                    host="monorail.proxy.rlwy.net",
                    port=30980,
                    user="root",
                    password="RXlnFIuFEKMvnYsMaPWvDimjLdGyoJVv",
                    database="railway"
                )
                cursor = conexao.cursor()

                id = self.tabela_demandas.item(row, 0).text()

                print('eww')
                comando = "SELECT quantidade FROM estoque WHERE item = %s"
                print('eww')
                valores = (id,)
                print('eww')
                cursor.execute(comando, valores)
                print('e')
                resultado = cursor.fetchone()
                print(id)

                if resultado:
                    print(quantidade_inicial)
                    print(int(resultado[0]))
                    quantidade_inicial += int(resultado[0])
                    print(quantidade_inicial)
                conexao.commit()
                cursor.close()
                conexao.close()

            except mysql.connector.Error as error:
                print("Erro ao conectar ao MySQL:", error)

            try:
                conexao = mysql.connector.connect(
                    host="monorail.proxy.rlwy.net",
                    port=30980,
                    user="root",
                    password="RXlnFIuFEKMvnYsMaPWvDimjLdGyoJVv",
                    database="railway"
                )
                cursor = conexao.cursor()
                quantidade = int(self.tabela_demandas.item(row, 3).text())
                id = self.tabela_demandas.item(row, 0)
                quantidade += quantidade_inicial
                comando = f'UPDATE estoque SET  quantidade = "{str(quantidade)}" WHERE item = "{id.text()}"'

                cursor.execute(comando)
                conexao.commit()
                cursor.close()
                conexao.close()
            except mysql.connector.Error as error:
                print("Erro ao conectar ao MySQL:", error)

            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Icon.Information)
            msg_box.setWindowTitle("AVISO")
            msg_box.setText(f"Compra Confirmada.")
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            reply = msg_box.exec()
            self.ler_database()
