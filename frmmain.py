from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from frmCustomer import Ui_frmCustomer 
from frmEmployee import Ui_frmEmployee
import webbrowser



class Ui_frmmain(object):
     def web(self):
        webbrowser.open("https://ocw.sharif.ir/")
     



     def showEmployeForm(self):
      self.frmEmployee = QtWidgets.QMainWindow()
      self.ui = Ui_frmEmployee()
      self.ui.setupUi(self.frmEmployee)
      self.frmEmployee.show()
    

     def exitForm(self):
        message=QMessageBox()
        message.setIcon(QMessageBox().Warning)
        message.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        message.setText("آیا مایلید خارج شوبد؟")
        message.setWindowTitle("هشدار")
        if message.exec()==QMessageBox.Yes:
            QtCore.QCoreApplication.exit()

     def showMinimize(self):
        frmmain.showMinimized()


     def showCustomerForm(self):
      self.frmCustomer = QtWidgets.QMainWindow()
      self.ui = Ui_frmCustomer()
      self.ui.setupUi(self.frmCustomer)
      self.frmCustomer.show()



     def setupUi(self, frmmain):
        frmmain.setObjectName("frmmain")
        #frmmain.resize(1143, 607)
        frmmain.showFullScreen()
        frmmain.setStyleSheet("background-color: rgb(157, 157, 157);\n"
"font: 14pt \"B Yekan\";")
        self.centralwidget = QtWidgets.QWidget(frmmain)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(121, 180, 183);\n"
"border:2px solid #FEFBF3;\n"
"border-radius:15px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 90))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 90))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_7 = QtWidgets.QFrame(self.frame_3)
        self.frame_7.setStyleSheet("border:none;")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.btnClose = QtWidgets.QPushButton(self.frame_7,clicked=lambda:self.exitForm())
        self.btnClose.setGeometry(QtCore.QRect(10, 20, 41, 28))
        self.btnClose.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/downlod1/close.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnClose.setIcon(icon)
        self.btnClose.setIconSize(QtCore.QSize(40, 40))
        self.btnClose.setObjectName("btnClose")
        self.btnMin = QtWidgets.QPushButton(self.frame_7,clicked=lambda:self.showMinimize())
        self.btnMin.setGeometry(QtCore.QRect(70, 20, 41, 28))
        self.btnMin.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/downlod1/minimize.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnMin.setIcon(icon1)
        self.btnMin.setIconSize(QtCore.QSize(40, 40))
        self.btnMin.setObjectName("btnMin")
        self.horizontalLayout_2.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.frame_3)
        self.frame_8.setStyleSheet("border:none;")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.frame_8)
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.horizontalLayout_2.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(self.frame_3)
        self.frame_9.setStyleSheet("border:none;")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_2.addWidget(self.frame_9)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setStyleSheet("border-image: url(:/downlod1/unnamed.jpg);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout.addWidget(self.frame_4)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(260, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(260, 16777215))
        self.frame_2.setStyleSheet("background-color: rgb(121, 180, 183);\n"
"border:2px solid #FEFBF3;\n"
"border-radius:15px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 200))
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame_5.setStyleSheet("border:none;\n"
"border-image: url(:/downlod1/images (1).png);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_2.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.btncustomer = QtWidgets.QPushButton(self.frame_6,clicked=lambda:self.showCustomerForm())
        self.btncustomer.setGeometry(QtCore.QRect(10, 10, 211, 71))
        self.btncustomer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btncustomer.setStyleSheet("QPushButton{\n"
"background-color:rgb(37,52,63);\n"
"color:white;\n"
"border:2px solid #FF9B51;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(255,155,81);\n"
"color:white;\n"
"border:2px solid rgb(37,52,63);\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/downlod1/Customer (رسانیکا).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btncustomer.setIcon(icon2)
        self.btncustomer.setIconSize(QtCore.QSize(40, 40))
        self.btncustomer.setObjectName("btncustomer")
        self.btnSell = QtWidgets.QPushButton(self.frame_6,clicked=lambda:self.showEmployeForm())
        self.btnSell.setGeometry(QtCore.QRect(10, 90, 211, 71))
        self.btnSell.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSell.setStyleSheet("QPushButton{\n"
"background-color:rgb(37,52,63);\n"
"color:white;\n"
"border:2px solid #FF9B51;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(255,155,81);\n"
"color:white;\n"
"border:2px solid rgb(37,52,63);\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/downlod1/shoppingcartcheckout (1).svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSell.setIcon(icon3)
        self.btnSell.setIconSize(QtCore.QSize(40, 40))
        self.btnSell.setObjectName("btnSell")
        self.btnAdd = QtWidgets.QPushButton(self.frame_6,clicked=lambda:self.web())
        self.btnAdd.setGeometry(QtCore.QRect(10, 180, 211, 71))
        self.btnAdd.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAdd.setStyleSheet("QPushButton{\n"
"background-color:rgb(37,52,63);\n"
"color:white;\n"
"border:2px solid #FF9B51;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(255,155,81);\n"
"color:white;\n"
"border:2px solid rgb(37,52,63);\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/downlod1/input (1).svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAdd.setIcon(icon4)
        self.btnAdd.setIconSize(QtCore.QSize(40, 40))
        self.btnAdd.setObjectName("btnAdd")
        self.btnSerch = QtWidgets.QPushButton(self.frame_6)
        self.btnSerch.setGeometry(QtCore.QRect(10, 270, 211, 71))
        self.btnSerch.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSerch.setStyleSheet("QPushButton{\n"
"background-color:rgb(37,52,63);\n"
"color:white;\n"
"border:2px solid #FF9B51;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(255,155,81);\n"
"color:white;\n"
"border:2px solid rgb(37,52,63);\n"
"}")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/downlod1/pageview.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSerch.setIcon(icon5)
        self.btnSerch.setIconSize(QtCore.QSize(40, 40))
        self.btnSerch.setObjectName("btnSerch")
        self.verticalLayout_2.addWidget(self.frame_6)
        self.horizontalLayout.addWidget(self.frame_2)
        frmmain.setCentralWidget(self.centralwidget)

        self.retranslateUi(frmmain)
        QtCore.QMetaObject.connectSlotsByName(frmmain)

     def retranslateUi(self, frmmain):
        _translate = QtCore.QCoreApplication.translate
        frmmain.setWindowTitle(_translate("frmmain", "MainWindow"))
        self.label.setText(_translate("frmmain", "فروش خودروAMG"))
        self.btncustomer.setText(_translate("frmmain", "بخش مشتریان"))
        self.btnSell.setText(_translate("frmmain", "بخش فروش"))
        self.btnAdd.setText(_translate("frmmain", "بخش ثبت نام"))
        self.btnSerch.setText(_translate("frmmain", "بخش استعلام"))
import imagec_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmmain = QtWidgets.QMainWindow()
    ui = Ui_frmmain()
    ui.setupUi(frmmain)
    frmmain.show()
    sys.exit(app.exec_())
