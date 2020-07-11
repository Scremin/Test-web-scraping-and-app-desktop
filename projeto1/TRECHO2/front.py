# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'front_testeUi_1.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(441, 657)

        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        
        MainWindow.setStyleSheet("*{\n"
        "font-size:12px;\n"
        "font-familiy:Yu Gothic UI Semibold;\n"
        "font-weight:75;\n"
        #"font-weight:bold;\n"
        "color:rgb(230, 45, 0);\n"
        " }\n"
        "QWidget{\n"
        "        }\n"
        "        QFrame{\n"
        "            background:rgb(255, 255, 255);\n"
        "        }\n"
        "        QPushButton{\n"
        "            border-style:outset;\n"
        "            border-radius: 10px;\n"
        "            background:rgb(200, 200, 200);\n"
        "            color:rgb(191, 60, 0);\n"
        "        }\n"
        "        QPushButton:pressed{\n"
        "            background:reb(224,0,0);\n"
        "            border-style:inset;;\n"
        "        }")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 441, 671))
        self.label.setText("")
        self.label.setObjectName("label")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 421, 81))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 100, 421, 81))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 190, 421, 81))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 280, 421, 81))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(370, 530, 31, 101))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../../../AppData/Local/Programs/Python/Python37/ISlogo.png"))
        self.label_2.setObjectName("label_2")
        
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 370, 421, 81))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 460, 421, 81))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        
        # Outras características da página.
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 441, 21))
        self.menubar.setObjectName("menubar")
        # opção de menu interativo no menuBar. PARTE 1.
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar) # SET MENUBAR
        # STATUSBAR
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar) # SET STATUSBAR
        # opção de menu interativo no menuBar. PARTE 2.
        self.actionSUBMENU = QtWidgets.QAction(MainWindow)
        self.actionSUBMENU.setObjectName("actionSUBMENU")
        self.menuFile.addAction(self.actionSUBMENU)
        self.menubar.addAction(self.menuFile.menuAction()) # ADD AO MENUBAR
        # opção de menu interativo no menuBar. PARTE 3.
        self.actionSUBMENU2 = QtWidgets.QAction(MainWindow)
        self.actionSUBMENU2.setObjectName("actionSUBMENU2")
        self.menuFile.addAction(self.actionSUBMENU2)
        self.menubar.addAction(self.menuFile.menuAction()) # ADD AO MENUBAR

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #self.actionSUBMENU.triggered.connect(lambda: self.busca('parâmetro a ser passado'))
        #self.actionSUBMENU.triggered.connect(lambda: self.busca())
        self.actionSUBMENU.triggered.connect(self.busca)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def busca(self):
        '''
            Inicia o processo de scraping.
            O resultado é temporariamente armazenado num arquivo pk1.
        '''
        try:
            mainCall()
        except:
            print('main.py em falha...')
        #

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "INFO_AUX"))
        
        self.pushButton.setText(_translate("MainWindow", ""))
        self.pushButton_2.setText(_translate("MainWindow", ""))
        self.pushButton_3.setText(_translate("MainWindow", ""))
        self.pushButton_4.setText(_translate("MainWindow", ""))
        self.pushButton_5.setText(_translate("MainWindow", ""))
        self.pushButton_6.setText(_translate("MainWindow", "SISTEMA INICIADO"))

        self.menuFile.setTitle(_translate("MainWindow", "OP"))
        self.actionSUBMENU.setText(_translate("MainWindow", "BUSCA"))
        self.actionSUBMENU2.setText(_translate("MainWindow", "ATUALIZAÇÃO"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
