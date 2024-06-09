# Part of Stoquee. See LICENSE file for full copyright and licensing details.
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMenu
from PyQt6.QtGui import QAction,QIcon

# A classe Tela_Inicio representa a Tela inicial do software e todas as suas conexões o seguimento do estoque.
class Tela_Inicio(object):

    # O método setup tem a função de criar a tela principal.
    # É um método de interface gráfica. Este método cria frames, labels e botões, e conecta esses widgets às suas respectivas funções.
    def setup(self, Form = None, user = str,nome_user = str) -> None:
        self.config_Aberta = False

        icon = QIcon('resources/assets/bender.jfif')
        Form.setWindowIcon(icon)
        Form.setObjectName("Form")
        Form.showMaximized()
        self.Form = Form

        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.frame = QtWidgets.QFrame(parent=Form)
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.frame.mousePressEvent = lambda event: self.toggle_frame_visibility(self.frame)
        self.frame.show()

        self.frame.setGeometry(QtCore.QRect(0, 0, 1366, 768))

        self.frame_demandas = QtWidgets.QFrame(parent=Form)
        self.frame_demandas.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_demandas.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_demandas.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_demandas.setObjectName("frame_demandas")
        self.frame_demandas.hide()
        self.frame_demandas.setGeometry(QtCore.QRect(0, 0, 2000, 1000))

        self.frame_estoque = QtWidgets.QFrame(parent=Form)
        self.frame_estoque.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_estoque.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_estoque.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_estoque.setObjectName("frame_estoque")
        self.frame_estoque.hide()
        self.frame_estoque.setGeometry(QtCore.QRect(0, 0, 2000, 1000))

        self.frame_new_item = QtWidgets.QFrame(parent=Form)
        self.frame_new_item.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_new_item.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_new_item.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_new_item.setObjectName("frame_new_item")
        self.frame_new_item.hide()
        self.frame_new_item.setGeometry(QtCore.QRect(0, 0, 2000, 1000))

        self.frame_2 = QtWidgets.QFrame(parent=self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 241, 541))
        self.frame_2.setStyleSheet("\n"
"background-color: #737373;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")

        self.pushButton_estoque = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButton_estoque.setGeometry(QtCore.QRect(20, 240, 201, 35))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_estoque.setFont(font)
        self.pushButton_estoque.setStyleSheet("QPushButton {\n"
"                    border: none ;\n"
"                    border-radius: 10px;\n"
"                    background-color: (131, 131, 131);\n"
"                    color: white;\n"
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/assets/a_cubo_3d.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_estoque.setIcon(icon)
        self.pushButton_estoque.setIconSize(QtCore.QSize(34, 35))
        self.pushButton_estoque.setObjectName("pushButton")
        self.new_item_aberto = False
        self.pushButton_estoque.clicked.connect( self.abrir_estoque)

        self.pushButton_demandas = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButton_demandas.setGeometry(QtCore.QRect(20, 290, 201, 35))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_demandas.setFont(font)
        self.pushButton_demandas.setStyleSheet("QPushButton {\n"
"                    border: none ;\n"
"                    border-radius: 10px;\n"
"                    background-color: (131, 131, 131);\n"
"                    color: white;\n"
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resources/assets/a_carrinho_de_compras.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_demandas.setIcon(icon1)
        self.pushButton_demandas.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_demandas.setObjectName("pushButton_demandas")

        self.pushButton_demandas.setMouseTracking(True)
        self.pushButton_demandas.enterEvent = self.showOptions
        self.pushButton_demandas.leaveEvent = self.hideOptions

        self.menu = QMenu(self.frame_2)
        self.action1 = QAction('Demandas', self.frame_2)
        self.action2 = QAction('Registrar Demanda Funcionario', self.frame_2)
        self.action3 = QAction('Registrar Demanda Estoque', self.frame_2)

        self.action3.triggered.connect(lambda: self.abrir_demandas(3))
        self.action1.triggered.connect(lambda: self.abrir_demandas(1))
        self.action2.triggered.connect(lambda: self.abrir_demandas(2))

        self.menu.addAction(self.action1)
        self.menu.addAction(self.action2)
        self.menu.addAction(self.action3)

        self.menu.setStyleSheet("""
                    QMenu {
                        background-color: #DDDDDD;  /* Cor de fundo */
                        border: 1px solid black;   /* Borda */
                    }
                    QMenu::item {
                        background-color: transparent;
                        padding: 8px 16px;  /* Espaçamento interno */
                    }
                    QMenu::item:selected {
                        background-color: #a8a8a8;  /* Cor de fundo do item selecionado */
                    }
                """)

        self.pushButton_config = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButton_config.setGeometry(QtCore.QRect(20, 340, 201, 35))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_config.setFont(font)
        self.pushButton_config.setStyleSheet("QPushButton {\n"
"                    border: none ;\n"
"                    border-radius: 10px;\n"
"                    background-color: (131, 131, 131);\n"
"                    color: white;\n"
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("resources/assets/a_engrenagens.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_config.setIcon(icon2)
        self.pushButton_config.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_config.setObjectName("pushButton_config")
        self.pushButton_config.clicked.connect(lambda: self.abrir_configuracoes(Form))

        self.pushButton_fechar_frame_options = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButton_fechar_frame_options.setGeometry(QtCore.QRect(100, 470, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_fechar_frame_options.setFont(font)
        self.pushButton_fechar_frame_options.setStyleSheet("QPushButton {\n"
                                             "                    border: 2px solid black ;\n"
                                             "                    border-radius: 10px;\n"
                                             "                    background-color: (131, 131, 131);\n"
                                             "                    color: white;\n"
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("resources/assets/a_remover.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_fechar_frame_options.setIcon(icon2)
        self.pushButton_fechar_frame_options.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_fechar_frame_options.setObjectName("pushButton_fechar_frame_options")
        self.pushButton_fechar_frame_options.clicked.connect( self.fechar_options)

        self.pushButton_funcionario = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButton_funcionario.setGeometry(QtCore.QRect(20, 390, 201, 35))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_funcionario.setFont(font)
        self.pushButton_funcionario.setStyleSheet("QPushButton {\n"
"                    border: none ;\n"
"                    border-radius: 10px;\n"
"                    background-color: (131, 131, 131);\n"
"                    color: white;\n"
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("resources/assets/a_grupo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_funcionario.setIcon(icon3)
        self.pushButton_funcionario.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_funcionario.setObjectName("pushButton_funcionario")

        self.label_3 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(70, 30, 101, 101))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("resources/assets/a_capturar.png"))
        self.label_3.setObjectName("label_3")
        name = self.abreviar_nome(nome_user)
        self.label_4 = QtWidgets.QLabel(name,parent=self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(40, 150, 110, 20))

        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")

        self.pushButton_6 = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 10, 41, 31))
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"                    border: none ;\n"
"                    border-radius: 10px;\n"
"                    background-color: (131, 131, 131);\n"
"                    color: white;\n"
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
        self.pushButton_6.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("resources/assets/a_sair.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_6.setIcon(icon4)
        self.pushButton_6.setIconSize(QtCore.QSize(28, 28))
        self.pushButton_6.setObjectName("pushButton_6")

        self.abrir_options = QtWidgets.QPushButton(parent=self.frame)
        self.abrir_options.setGeometry(QtCore.QRect(-2, -6, 101, 101))
        self.abrir_options.setStyleSheet("QPushButton {\n"
                                        "                    border: none ;\n"
                                        "                    border-radius: 15px;\n"
                                        "                    background-color: #737373;\n"
                                        "                    color: white;\n"
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
        self.abrir_options.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("resources/assets/a_usuario-de-perfil.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.abrir_options.setIcon(icon4)
        self.abrir_options.setIconSize(QtCore.QSize(35, 35))
        self.abrir_options.setObjectName("abrir_options")
        self.abrir_options.clicked.connect( self.fechar_options)
        self.abrir_options.hide()

        self.frame_3 = QtWidgets.QFrame(parent=self.frame)
        self.frame_3.setGeometry(QtCore.QRect(241, 0, 1141, 41))
        self.frame_3.setStyleSheet("background-color: rgb(212, 212, 212);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label = QtWidgets.QLabel(parent=self.frame_3)
        self.label.setGeometry(QtCore.QRect(7, 5, 204, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_Início = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushButton_Início.setGeometry(QtCore.QRect(1030, 10, 91, 23))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Início.setFont(font)
        self.pushButton_Início.setStyleSheet("QPushButton {\n"
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
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("resources/assets/a_casa.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_Início.setIcon(icon5)
        self.pushButton_Início.setIconSize(QtCore.QSize(23, 23))
        self.pushButton_Início.setObjectName("pushButton_Início")
        self.pushButton_Início.clicked.connect(self.voltar_inicio)

        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setGeometry(QtCore.QRect(400, 180, 231, 231))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("resources/assets/S.jpeg"))
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(parent=self.frame)
        self.label_5.setGeometry(QtCore.QRect(720, 210, 261, 221))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("resources/assets/a_UF.png"))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.frame)

        self.Definir_Nomes(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        for widget in self.frame.findChildren(QtWidgets.QWidget):
            if widget == self.abrir_options:
                continue
            else:
                widget.show()

    # Esse método Definir_Nomes tem a função gráfica de definir os nomes de alguns labels e botões fixos.
    # Ou seja, que não mudam os nomes.
    def Definir_Nomes(self, Form=None) -> None:

        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_estoque.setText(_translate("Form", "Estoque             "))
        self.pushButton_demandas.setText(_translate("Form", "Demandas       "))
        self.pushButton_config.setText(_translate("Form", "Configurações   "))
        self.pushButton_funcionario.setText(_translate("Form", "Funcionarios    "))
        self.label.setText(_translate("Form", "Controle de Estoque"))
        self.pushButton_Início.setText(_translate("Form", "Início"))

    # O método fechar_options tem a função gráfica de abrir e fechar o menu com as opções de Demanda, Estoque e Configurações.
    def fechar_options(self) -> None:
        if self.frame_2.isVisible():
            self.frame_2.hide()
            self.abrir_options.show()
            self.frame_3.setGeometry(QtCore.QRect(97, 0, 1285, 41))
            self.pushButton_Início.setGeometry(QtCore.QRect(1174, 10, 91, 23))

        else:
            self.frame_2.show()
            self.abrir_options.hide()
            self.frame_3.setGeometry(QtCore.QRect(241, 0, 1141, 41))
            self.pushButton_Início.setGeometry(QtCore.QRect(1030, 10, 91, 23))

    # O método abrir_estoque tem a função de abrir o arquivo 'estoque.py' e mudar para a parte de estoque do software.
    def abrir_estoque(self) -> None:
        from estoque import Estoque
        if self.new_item_aberto == True:
            self.estoq.analise()
        else:
            self.frame_demandas.hide()
            self.frame_2.setParent(self.frame_estoque)
            self.abrir_options.setParent(self.frame_estoque)
            self.frame_3.setParent(self.frame_estoque)
            self.estoq = Estoque()
            self.estoq.abrir_estoque(self.Form, self)
        for widget in self.frame_demandas.findChildren(QtWidgets.QWidget):
            widget.deleteLater()

    # O método showOptions mostra as opções do menu, que incluem Criar Demandas para o Estoque ou Funcionários, e ver a tabela de demandas.
    def showOptions(self, event=None) -> None:
        self.menu.popup(self.pushButton_demandas.mapToGlobal(self.pushButton_demandas.rect().bottomLeft()))

    # O método hideOptions esconde as opções do menu, que incluem Criar Demandas para o Estoque ou Funcionários, e ver a tabela de demandas.
    def hideOptions(self, event=None) -> None:
        self.menu.close()

    # O método abrir_demandas  tem a função de abrir o arquivo 'demandas.py' e mudar para a parte de demandas do software.
    def abrir_demandas(self,dema=int) -> None:
        self.frame_2.setParent(self.frame_estoque)
        self.abrir_options.setParent(self.frame_estoque)
        self.frame_3.setParent(self.frame_estoque)

        for widget in self.frame_demandas.findChildren(QtWidgets.QWidget):
            widget.deleteLater()

        from demandas import Demandas
        self.frame_2.setParent(self.frame_demandas)
        self.abrir_options.setParent(self.frame_demandas)
        self.frame_3.setParent(self.frame_demandas)

        for widget in self.frame_estoque.findChildren(QtWidgets.QWidget):
            widget.deleteLater()
        self.frame_estoque.hide()

        self.frame_3.show()
        self.frame_2.show()

        self.demanda = Demandas()
        self.demanda.demandas(self.Form, dema, self)
        self.frame_demandas.show()
        self.new_item_aberto = False

    # O método voltar_inicio tem a função de limpar a tela do software e mostrar a mesma tela que aparece quando o código é iniciado.
    # Ou seja, a tela inicial.
    def voltar_inicio(self) -> None:
        self.frame_2.setParent(self.frame)
        self.abrir_options.setParent(self.frame)
        self.frame_3.setParent(self.frame)

        self.frame_3.show()
        self.frame_2.show()

        for widget in self.frame_estoque.findChildren(QtWidgets.QWidget):
            widget.deleteLater()
        for widget in self.frame_demandas.findChildren(QtWidgets.QWidget):
            widget.deleteLater()
        self.frame_estoque.hide()
        self.frame_demandas.hide()

    # O método toggle_frame_visibility tem a função de fechar a janela_config do software.
    # A janela_config só existe quando as configurções são abertas por isso se usa a condição config_Aberta.
    def toggle_frame_visibility(self,frame=None) -> None:

        if self.config_Aberta == True:
            self.janela_config.close()
            self.config_Aberta = False

    # O método abrir_configuracoes abre a tela de configurações do software
    def abrir_configuracoes(self,Form=None) -> None:

        from config import Config

        self.config = Config()
        self.config.Tela_configuracao(Form, self)
        self.config_Aberta = True

    # O método abreviar_nome apenas pega o nome do usuário e abrevia e retorna o nome abreviado.
    def abreviar_nome(self, nome = str) -> str:
        item = nome
        tamnaho = len(item)
        login = ''
        i = 0
        space_atual = 0
        quantidade_space = 0
        for j in range(tamnaho):
            if item[j] == ' ':
                quantidade_space += 1
        for i in range(tamnaho):
            if item[i] != ' ' and space_atual == 0 or space_atual == quantidade_space:
                login += item[i]
            if space_atual != 0 and space_atual != quantidade_space and item[i] != ' ' and analise == 0:
                login += item[i]
                analise = 1
            if item[i] == ' ':
                login += ' '
                space_atual += 1
                analise = 0
        return login
