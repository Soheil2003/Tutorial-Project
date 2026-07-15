


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import pyodbc
con=pyodbc.connect("driver={sql server};server=.;database=CarShop;trusted_connection=true")
muCursor=con.cursor()
from frmmain import Ui_frmmain



class Ui_frmLogin(object):
    def login(self):
        userName=self.lineEdit.text()
        password=self.txtPassword.text()

        if userName:
            if password:
                sql="select * from tblLogin where userName=? and password=?"
                values=(userName,password)
                record=muCursor.execute(sql,values).fetchall()
                if record:
                     self.frmmain = QtWidgets.QMainWindow()
                     self.ui = Ui_frmmain()
                     self.ui.setupUi(self.frmmain)
                     self.frmmain.show()
                else:
                    self.showMessage("نام کاربری یا رمز عبور نامعتبر است")
                    self.lineEdit.setText("")
                    self.txtPassword.setText("")                
            else:
                self.showMessage("کاربر گرامی رمز عبور را وارد نمایید")
                self.txtPassword.setFocus()
        else:
            self.showMessage("کاربر گرامی نام کاربری را وارد نمایید")
            self.lineEdit.setFocus()


    def showMessage(self,text):
        message=QMessageBox()
        message.setIcon(QMessageBox.Information)
        message.setWindowTitle("پیام مدیریتی")
        message.setText(text)
        message.setStandardButtons(QMessageBox.Ok)
        message.exec()
         
        
    def setupUi(self, frmLogin):
        frmLogin.setObjectName("frmLogin")
        frmLogin.resize(469, 537)
        frmLogin.setMinimumSize(QtCore.QSize(469, 537))
        frmLogin.setMaximumSize(QtCore.QSize(469, 537))
        frmLogin.setStyleSheet("font: 16pt \"Times New Roman\";\n"
"background-color: rgb(185, 229, 232);")
        self.centralwidget = QtWidgets.QWidget(frmLogin)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 50, 151, 71))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 140, 151, 71))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(180, 61, 261, 51))
        self.lineEdit.setStyleSheet("border:2px solid #7AB2D3;")
        self.lineEdit.setObjectName("lineEdit")
        self.txtPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPassword.setGeometry(QtCore.QRect(180, 150, 261, 51))
        self.txtPassword.setStyleSheet("border:2px solid #7AB2D3;")
        self.txtPassword.setObjectName("txtPassword")
        self.btnLogin = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.login())
        self.btnLogin.setGeometry(QtCore.QRect(80, 390, 141, 61))
        self.btnLogin.setStyleSheet("QPushButton{\n"
"background-color: rgb(37,52,63);\n"
"color:white;\n"
"boredr:2px solid#FF9B51;\n"
"}\n"
"QPushButyon:hover{\n"
"background-color :rgb(255,155,81);\n"
"color:black;\n"
"border:2px solid rgb(37,52,63);\n"
"}")
        self.btnLogin.setObjectName("btnLogin")
        self.btnExit = QtWidgets.QPushButton(self.centralwidget)
        self.btnExit.setGeometry(QtCore.QRect(270, 390, 141, 61))
        self.btnExit.setStyleSheet("QPushButton{\n"
"background-color: rgb(37,52,63);\n"
"color:white;\n"
"boredr:2px solid#FF9B51;\n"
"}\n"
"QPushButyon:hover{\n"
"background-color :rgb(255,155,81);\n"
"color:black;\n"
"border:2px solid rgb(37,52,63);\n"
"}")
        self.btnExit.setObjectName("btnExit")
        frmLogin.setCentralWidget(self.centralwidget)

        self.retranslateUi(frmLogin)
        QtCore.QMetaObject.connectSlotsByName(frmLogin)

    def retranslateUi(self, frmLogin):
        _translate = QtCore.QCoreApplication.translate
        frmLogin.setWindowTitle(_translate("frmLogin", "MainWindow"))
        self.label.setText(_translate("frmLogin", "UserName:"))
        self.label_2.setText(_translate("frmLogin", "Password:"))
        self.btnLogin.setText(_translate("frmLogin", "Login"))
        self.btnExit.setText(_translate("frmLogin", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmLogin = QtWidgets.QMainWindow()
    ui = Ui_frmLogin()
    ui.setupUi(frmLogin)
    frmLogin.show()
    sys.exit(app.exec_())
