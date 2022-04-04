
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(448, 385)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.input_field = QtWidgets.QLineEdit(self.centralwidget)
        self.input_field.setGeometry(QtCore.QRect(20, 40, 241, 31))
        self.input_field.setObjectName("input_field")
        self.enter_btn = QtWidgets.QPushButton(self.centralwidget)
        self.enter_btn.setGeometry(QtCore.QRect(30, 90, 181, 28))
        self.enter_btn.setObjectName("enter_btn")
        self.clear_btn = QtWidgets.QPushButton(self.centralwidget)
        self.clear_btn.setGeometry(QtCore.QRect(230, 90, 171, 28))
        self.clear_btn.setObjectName("clear_btn")
        self.nine_btn = QtWidgets.QPushButton(self.centralwidget)
        self.nine_btn.setGeometry(QtCore.QRect(30, 140, 71, 28))
        self.nine_btn.setObjectName("nine_btn")
        self.eight_btn = QtWidgets.QPushButton(self.centralwidget)
        self.eight_btn.setGeometry(QtCore.QRect(132, 140, 71, 28))
        self.eight_btn.setObjectName("eight_btn")
        self.seven_btn = QtWidgets.QPushButton(self.centralwidget)
        self.seven_btn.setGeometry(QtCore.QRect(230, 140, 71, 28))
        self.seven_btn.setObjectName("seven_btn")
        self.add_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_btn.setGeometry(QtCore.QRect(330, 140, 71, 28))
        self.add_btn.setObjectName("add_btn")
        self.six_btn = QtWidgets.QPushButton(self.centralwidget)
        self.six_btn.setGeometry(QtCore.QRect(30, 180, 71, 28))
        self.six_btn.setObjectName("six_btn")
        self.five_btn = QtWidgets.QPushButton(self.centralwidget)
        self.five_btn.setGeometry(QtCore.QRect(130, 180, 71, 28))
        self.five_btn.setObjectName("five_btn")
        self.four_btn = QtWidgets.QPushButton(self.centralwidget)
        self.four_btn.setGeometry(QtCore.QRect(230, 180, 71, 28))
        self.four_btn.setObjectName("four_btn")
        self.sub_btn = QtWidgets.QPushButton(self.centralwidget)
        self.sub_btn.setGeometry(QtCore.QRect(330, 180, 71, 28))
        self.sub_btn.setObjectName("sub_btn")
        self.three_btn = QtWidgets.QPushButton(self.centralwidget)
        self.three_btn.setGeometry(QtCore.QRect(30, 220, 71, 28))
        self.three_btn.setObjectName("three_btn")
        self.two_btn = QtWidgets.QPushButton(self.centralwidget)
        self.two_btn.setGeometry(QtCore.QRect(130, 220, 71, 28))
        self.two_btn.setObjectName("two_btn")
        self.one_btn = QtWidgets.QPushButton(self.centralwidget)
        self.one_btn.setGeometry(QtCore.QRect(230, 220, 71, 28))
        self.one_btn.setObjectName("one_btn")
        self.mul_btn = QtWidgets.QPushButton(self.centralwidget)
        self.mul_btn.setGeometry(QtCore.QRect(330, 220, 71, 28))
        self.mul_btn.setObjectName("mul_btn")
        self.zero_btn = QtWidgets.QPushButton(self.centralwidget)
        self.zero_btn.setGeometry(QtCore.QRect(30, 260, 271, 28))
        self.zero_btn.setObjectName("zero_btn")
        self.div_btn = QtWidgets.QPushButton(self.centralwidget)
        self.div_btn.setGeometry(QtCore.QRect(330, 260, 71, 28))
        self.div_btn.setObjectName("div_btn")
        self.result_field = QtWidgets.QLineEdit(self.centralwidget)
        self.result_field.setGeometry(QtCore.QRect(290, 40, 113, 31))
        self.result_field.setObjectName("result_field")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 448, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.enter_btn.setText(_translate("MainWindow", "Enter"))
        self.clear_btn.setText(_translate("MainWindow", "Clear"))
        self.nine_btn.setText(_translate("MainWindow", "9"))
        self.eight_btn.setText(_translate("MainWindow", "8"))
        self.seven_btn.setText(_translate("MainWindow", "7"))
        self.add_btn.setText(_translate("MainWindow", "+"))
        self.six_btn.setText(_translate("MainWindow", "6"))
        self.five_btn.setText(_translate("MainWindow", "5"))
        self.four_btn.setText(_translate("MainWindow", "4"))
        self.sub_btn.setText(_translate("MainWindow", "-"))
        self.three_btn.setText(_translate("MainWindow", "3"))
        self.two_btn.setText(_translate("MainWindow", "2"))
        self.one_btn.setText(_translate("MainWindow", "1"))
        self.mul_btn.setText(_translate("MainWindow", "x"))
        self.zero_btn.setText(_translate("MainWindow", "0"))
        self.div_btn.setText(_translate("MainWindow", "%"))
