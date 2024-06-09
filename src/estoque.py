# Part of Stoquee. See LICENSE file for full copyright and licensing details.
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import QDate
from PyQt6.QtGui import QIcon
import mysql.connector
# A classe Estoque é a janela principal da aplicação.
class Estoque(object):

    # O método abrir_estoque tem a função de criar uma tela.
    # É um método de interface gráfica. Este método cria frames, labels e botões, e conecta esses widgets às suas respectivas funções.

    def abrir_estoque(self,Form=None,tela=None) -> None:
        self.tela = tela
        self.frame = self.tela.frame_estoque
        self.frame_new =  self.tela.frame_new_item
        self.frame.show()
        self.frame_new.hide()
        self.tela.label.setText("Estoque")
        self.pesquisar_estoque = QtWidgets.QLineEdit(parent=self.frame)
        self.pesquisar_estoque.setGeometry(QtCore.QRect(320, 70, 431, 21))
        self.pesquisar_estoque.setStyleSheet("border: 2px solid #737373; border-radius: 10px; background-color: white;")
        self.pesquisar_estoque.setObjectName("pesquisar_estoque")
        self.pesquisar_estoque.show()
        icon = QtGui.QIcon('resources/assets/a_lupa.png')
        self.pesquisar_estoque.setPlaceholderText("Pesquisar Item")
        self.pesquisar_estoque.addAction(icon, QtWidgets.QLineEdit.ActionPosition.LeadingPosition)
        self.pesquisar_estoque.textChanged.connect(self.pesquisar)

        self.editable = False

        self.tabela_estoque = QtWidgets.QTableWidget(parent=self.frame)
        self.tabela_estoque.setGeometry(QtCore.QRect(250, 130, 991, 541))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tabela_estoque.show()

        self.tabela_alt = QtWidgets.QTableWidget()
        self.tabela_alt2 = QtWidgets.QTableWidget()

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
        self.tabela_estoque.setEditTriggers(QtWidgets.QTableWidget.EditTrigger.NoEditTriggers)

        self.analise_edit_tabela = 'Nenhum'
        self.tabela_estoque.doubleClicked.connect(lambda: self.altera_table('Tabela'))

    def analise(self) -> None:
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

    # Método increase_column_width define o tamanho das colunas de acordo com a quantidade de caracteres da coluna.
    # Assim a coluna fica com o tamanho correto.
    def increase_column_width(self, column=int, width=int):
        self.tabela_estoque.setColumnWidth(column, width)

    # O método criar_item é um método gráfico que abre a parte de criar um item novo no estoque.
    def criar_item(self) -> None:

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

    # Método altera_table usado alterar a tabela e salvar as alterações.
    def altera_table(self,nivel=str)-> None:
        if self.analise_edit_tabela != nivel :
            colum_item = 0
            colum_preco_unitario = 0
            colum_ultima_aqui = 0
            colum_quantidade = 0
            colum_marca = 0
            colum_unidade = 0
            colum_desc = 0

            for colum in range(self.tabela_estoque.columnCount()):
                item_pac = self.tabela_estoque.horizontalHeaderItem(colum)

                if item_pac.text() == 'Descrição do Item':
                    colum_desc = colum
                if item_pac.text() == 'Unidade do Item':
                    colum_unidade = colum
                if item_pac.text() == "Item":
                    colum_item = colum
                if item_pac.text() == "Quantidade no Estoque":
                    colum_quantidade = colum
                if item_pac.text() == 'Marca':
                    colum_marca = colum
                if item_pac.text() == 'Preço Unitário':
                    colum_preco_unitario = colum
                if item_pac.text() == 'Ultima Aquisição':
                    colum_ultima_aqui = colum

            self.lista_modificacoes = []
            if self.tabela_estoque.rowCount() > 0:
                self.editable = not self.editable
                self.tabela_estoque.setEditTriggers(
                    QtWidgets.QTableWidget.EditTrigger.AllEditTriggers if self.editable else QtWidgets.QTableWidget.EditTrigger.NoEditTriggers)

                if self.editable:
                    self.analise_edit_tabela = "Tabela"
                    self.copiadora()

                    self.pushButton_confirmar_alteracao.show()
                    self.pushButton_new_item.hide()

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
                                id = self.tabela_estoque.verticalHeaderItem(row)
                                item = self.tabela_estoque.item(row, colum_item)
                                descricao = self.tabela_estoque.item(row, colum_desc)
                                preco_unitario = self.tabela_estoque.item(row, colum_preco_unitario)
                                ultima_aqui = self.tabela_estoque.item(row, colum_ultima_aqui)
                                marca = self.tabela_estoque.item(row, colum_marca)
                                quantidade = self.tabela_estoque.item(row, colum_quantidade)
                                unidade = self.tabela_estoque.item(row, colum_unidade)
                                self.alt_banco(item, descricao, unidade, quantidade, marca, preco_unitario, ultima_aqui, id)
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
                    self.pushButton_new_item.show()

    # Método generar_numero usado para gerar um número aleatório.
    def generar_numero(self)-> None:
        data = QDate.currentDate()
        dia = data.day()
        mes = data.month()
        import random
        random_numbers = ''.join(str(random.randint(0, 9)) for _ in range(4))
        generated_number = f"{dia:02}{mes:02}{random_numbers}"
        self.id = int(generated_number)

    # O método atualiza_estoque faz conexão e lê o database e atualiza a tabela de estoque.

    def atualiza_estoque(self)-> None:
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

    # Método add_estoque usado para adicionar novos itens ao dabase de estoque.
    def add_estoque(self)-> None:
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

    # Método copiadora copia a tabela de estoque.
    def copiadora(self)-> None:
        conta_linha = self.tabela_estoque.rowCount()
        conta_coluna = self.tabela_estoque.columnCount()
        self.tabela_alt.setColumnCount(conta_coluna)
        self.tabela_alt.setRowCount(conta_linha)
        for analisa_linha in range(conta_linha):
            for analisa_coluna in range(conta_coluna - 1):
                item = self.tabela_estoque.item(analisa_linha, analisa_coluna + 1)
                if item is not None:
                    item_text = item.text()
                    item_copy = QtWidgets.QTableWidgetItem(item_text)
                    self.tabela_alt.setItem(analisa_linha, analisa_coluna + 1, item_copy)

    # Método copiadora2 copia a tabela do estoque para uma segunda tabela.
    def copiadora2(self)-> None:
        conta_linha = self.tabela_estoque.rowCount()
        conta_coluna = self.tabela_estoque.columnCount()
        self.tabela_alt2.setColumnCount(conta_coluna)
        self.tabela_alt2.setRowCount(conta_linha)
        for analisa_linha in range(conta_linha):
            for analisa_coluna in range(conta_coluna - 1):
                item = self.tabela_estoque.item(analisa_linha, analisa_coluna + 1)
                if item is not None:
                    item_text = item.text()
                    item_copy = QtWidgets.QTableWidgetItem(item_text)
                    self.tabela_alt2.setItem(analisa_linha, analisa_coluna + 1, item_copy)

    # Método moficacao verifica se ouve alguma modificação na tabela. E pega qual o item alterado.
    def modificao(self)-> None:
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
    def alt_banco(self,item=str,descricao=str,unidade=str,quantidade=int,marca=str,precounico=int,ultima_aqui=str,id=int)-> None:

        try:
            conexao = mysql.connector.connect(
                host="monorail.proxy.rlwy.net",
                port=30980,
                user="root",
                password="RXlnFIuFEKMvnYsMaPWvDimjLdGyoJVv",
                database="railway"
            )
            cursor = conexao.cursor()
            comando = f'UPDATE estoque SET item = "{item.text()}",descricao = "{descricao.text()}",unidade = "{unidade.text()}", quantidade = "{quantidade.text()}", ultima_aqui = "{ultima_aqui.text()}", precounico = "{precounico.text()}", marca = "{marca.text()}"  WHERE id = "{id.text()}"'

            cursor.execute(comando)
            conexao.commit()
            cursor.close()
            conexao.close()
        except mysql.connector.Error as error:
            print("Erro ao conectar ao MySQL:", error)

    # Método pesquisar usado para fazer pesquisa na tabela.
    def pesquisar(self, pesquisa=str)-> None:
        for row in range(self.tabela_estoque.rowCount()):
            item = self.tabela_estoque.item(row, 0)
            item2 = self.tabela_estoque.item(row, 1)
            if item is not None:
                if pesquisa.lower() in item.text().lower() or pesquisa.lower() in item2.text().lower():
                    self.tabela_estoque.showRow(row)
                else:
                    self.tabela_estoque.hideRow(row)
