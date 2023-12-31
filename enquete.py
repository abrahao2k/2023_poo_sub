# Form implementation generated from reading ui file 'enquete.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox     # janela de diálogo

class Ui_Janela(object):
    
    # Contadores de votos
    dubai = 0
    paris = 0
    tibau = 0
    casa  = 0
    
    def setupUi(self, Janela):
        Janela.setObjectName("Janela")
        Janela.resize(270, 152)
        self.centralwidget = QtWidgets.QWidget(parent=Janela)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_pergunta = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_pergunta.setObjectName("label_pergunta")
        self.gridLayout.addWidget(self.label_pergunta, 0, 0, 1, 2)
        self.radioButton_dubai = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_dubai.setObjectName("radioButton_dubai")
        self.gridLayout.addWidget(self.radioButton_dubai, 1, 0, 1, 1)
        self.radioButton_paris = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_paris.setObjectName("radioButton_paris")
        self.gridLayout.addWidget(self.radioButton_paris, 2, 0, 1, 1)
        self.radioButton_tibau = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_tibau.setObjectName("radioButton_tibau")
        self.gridLayout.addWidget(self.radioButton_tibau, 3, 0, 1, 1)
        self.radioButton_casa = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_casa.setObjectName("radioButton_casa")
        self.gridLayout.addWidget(self.radioButton_casa, 4, 0, 1, 1)
        self.pushButton_votar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_votar.setObjectName("pushButton_votar")
        
        # associar o botão com a função
        self.pushButton_votar.clicked.connect(self.votar)
        
        self.gridLayout.addWidget(self.pushButton_votar, 5, 0, 1, 1)
        self.pushButton_resultado = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_resultado.setObjectName("pushButton_resultado")
        
        self.pushButton_resultado.clicked.connect(self.resultado)
        
        self.gridLayout.addWidget(self.pushButton_resultado, 5, 1, 1, 1)
        Janela.setCentralWidget(self.centralwidget)

        self.retranslateUi(Janela)
        QtCore.QMetaObject.connectSlotsByName(Janela)

    def retranslateUi(self, Janela):
        _translate = QtCore.QCoreApplication.translate
        Janela.setWindowTitle(_translate("Janela", "Enquete"))
        self.label_pergunta.setText(_translate("Janela", "Onde você gostaria de passar o ano novo?"))
        self.radioButton_dubai.setText(_translate("Janela", "Dubai"))
        self.radioButton_paris.setText(_translate("Janela", "Paris"))
        self.radioButton_tibau.setText(_translate("Janela", "Tibau"))
        self.radioButton_casa.setText(_translate("Janela", "Em Casa"))
        self.pushButton_votar.setText(_translate("Janela", "VOTAR"))
        self.pushButton_resultado.setText(_translate("Janela", "Resultado"))

    def votar(self):
        
        msgok = QMessageBox()
        msgok.setWindowTitle("Informação")
        msgok.setText("VOTO CONFIRMADO.")
        
        if self.radioButton_dubai.isChecked():
            self.dubai += 1
            msgok.exec()
        
        elif self.radioButton_paris.isChecked():
            self.paris += 1
            msgok.exec()
        
        elif self.radioButton_tibau.isChecked():
            self.tibau += 1
            msgok.exec()
        
        elif self.radioButton_casa.isChecked():
            self.casa += 1
            msgok.exec()
        
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Erro")
            msg.setText("Escolha uma opção.")
            msg.exec()
        
        # Desativar auto-exclusivo
        self.radioButton_dubai.setAutoExclusive(False)
        self.radioButton_paris.setAutoExclusive(False)
        self.radioButton_tibau.setAutoExclusive(False)
        self.radioButton_casa.setAutoExclusive(False)
        
        # Limpar os botões
        self.radioButton_dubai.setChecked(False)
        self.radioButton_paris.setChecked(False)
        self.radioButton_tibau.setChecked(False)
        self.radioButton_casa.setChecked(False)
        
        # Ativar auto-exclusivo
        self.radioButton_dubai.setAutoExclusive(True)
        self.radioButton_paris.setAutoExclusive(True)
        self.radioButton_tibau.setAutoExclusive(True)
        self.radioButton_casa.setAutoExclusive(True)
        
        ####################################################
    
    def resultado(self):
        tx = "RESULTADO DA VOTAÇÃO \n"
        tx += f"Dubai = {self.dubai} \n"
        tx += f"Paris = {self.paris} \n"
        tx += f"Tibau = {self.tibau} \n"
        tx += f"Casa = {self.casa}"
        
        msgres = QMessageBox()
        msgres.setWindowTitle("Apuração")
        msgres.setText(tx)
        msgres.exec()
        
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Janela = QtWidgets.QMainWindow()
    ui = Ui_Janela()
    ui.setupUi(Janela)
    Janela.show()
    sys.exit(app.exec())
