

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import pyodbc
con=pyodbc.connect("driver={sql server};server=.;database=CarShop;trusted_connection=true")
myCursor=con.cursor()



class Ui_frmEmployee(object):
    
     def deleteFromDb(self):
         naId=self.lineEdit_3.text()
         if naId:
              sqlSelect="select * from tblEmployee where emNaId=?"
              record=myCursor.execute(sqlSelect,naId).fetchall()
              if record:
                   message=QMessageBox()
                   message.setIcon(QMessageBox.Warning)
                   message.setWindowTitle("هشدار")
                   message.setText("آیا از حذف اطمینان دارید؟")
                   message.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
                   if message.exec()==QMessageBox.Yes:
                        sqlDelete="delete from tblEmployee where emNaId=?"
                        myCursor.execute(sqlDelete,naId)
                        myCursor.commit()
                        self.showMessage("حذف کاربر موفقیت آمیز بود")
                        self.clearScreen()
                        self.showDataInTable()
         else:
              self.showMessage("کاربر گرامی برای حذف ابتدا کد ملی  را وارد نمایید")
              self.lineEdit_3.setFocus()
    

     def search(self):
         naId=self.lineEdit_3.text()

         if naId:
                sqlSelect="select emName,emLastName,emPhone,emNaId,emBirthDate,emAddress,emZipCode  from tblEmployee where emNaId=?"
                record=myCursor.execute(sqlSelect,naId).fetchone()

                if record:
                     Name, LastName, naId , phone, birthDate, address, ZipCode=record
                     self.showMessage(f"نام:{Name}\n"
                                      f"نام خانوادگی:{LastName}\n"
                                      f"کد ملی:{naId}\n"
                                      f"موبایل:{phone}\n"
                                      f"تاریخ تولد:{birthDate}\n"
                                      f"آدرس:{address}\n"
                                      f"کد پستی{ZipCode}")  
                else:
                     self.showMessage("چنین کاربری در سیستم وجود ندارد")
                     self.lineEdit_3.setText("")
          
         else:
                self.showMessage("کاربر گرامی برای جستجو ابتدا کد ملی را وارد نمایید") 
                self.lineEdit_3.setFocus() 
        
     def showDataInTable(self):
        sql="select * from tblEmployee "
        record=myCursor.execute(sql).fetchall()
        counter=0
        for line in record:
                counter+=1
        self.tableWidget.setRowCount(counter)
        rowcounter=0
        for line in record:
                self.tableWidget.setItem(rowcounter,0,QtWidgets.QTableWidgetItem(str(line[0])))
                self.tableWidget.setItem(rowcounter,1,QtWidgets.QTableWidgetItem(line[1]))
                self.tableWidget.setItem(rowcounter,2,QtWidgets.QTableWidgetItem(line[2]))
                self.tableWidget.setItem(rowcounter,3,QtWidgets.QTableWidgetItem(line[3]))
                self.tableWidget.setItem(rowcounter,4,QtWidgets.QTableWidgetItem(line[4]))
                self.tableWidget.setItem(rowcounter,5,QtWidgets.QTableWidgetItem((line[5])))
                self.tableWidget.setItem(rowcounter,7,QtWidgets.QTableWidgetItem(str(line[7])))
                self.tableWidget.setItem(rowcounter,6,QtWidgets.QTableWidgetItem((line[6])))
                rowcounter+=1
    









     def showMessage(self,text):
        message=QMessageBox()
        message.setIcon(QMessageBox.Information)
        message.setWindowTitle("پیام مدیریتی")
        message.setText(text)
        message.setStandardButtons(QMessageBox.Ok)
        message.exec()
     def saveInDb(self):
        name=self.lineEdit.text()
        LastName=self.lineEdit_2.text()
        address=self.lineEdit_5.text()
        birthDate=self.lineEdit_6.text()
        phone=self.lineEdit_4.text()
        naId=self.lineEdit_3.text()
        ZipCode=self.lineEdit_7.text()

        if name:
            sqlSelect="select * from tblEmployee where emNaId=?"
            record=myCursor.execute(sqlSelect,naId).fetchall()
            if record:
                self.showMessage("چنین کاربری در سیستم ثبت شده است")
                self.clearScreen()            
            else:


                sql="insert into tblEmployee (emName,emLastname,emPhone,emNaId,emBirthDate,emAddress,emZipCode) values (?,?,?,?,?,?,?)"
                values=(name,LastName,phone,naId,birthDate,address,ZipCode)
                myCursor.execute(sql,values)
                myCursor.commit()

            self.showMessage("دخیره اطلاعات موفقیت آمیز بود")
            self.clearScreen()
            self.showDataInTable()

        else:
            self.showMessage("کاربر گرامی لطفا نام را وارد کنید")
            self.lineEdit.setFocus()

     def clearScreen(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_5.setText("")
        self.lineEdit_6.setText("")
        self.lineEdit_4.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_7.setText("")
    






     def setupUi(self, frmCustomer):
        frmCustomer.setObjectName("frmCustomer")
        frmCustomer.resize(1024, 617)
        frmCustomer.setMinimumSize(QtCore.QSize(1024, 617))
        frmCustomer.setMaximumSize(QtCore.QSize(1024, 617))
        frmCustomer.setStyleSheet("background-color: rgb(122, 178, 211);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 14pt \"B Yekan\";\n"
"border:2px solid white;\n"
"border-radius:10px;")
        self.centralwidget = QtWidgets.QWidget(frmCustomer)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.txtName = QtWidgets.QLabel(self.frame)
        self.txtName.setGeometry(QtCore.QRect(764, 9, 221, 61))
        self.txtName.setStyleSheet("background-color:rgb(37,52,63);\n"
"color:white;")
        self.txtName.setObjectName("txtName")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(772, 20, 121, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.txtLastName = QtWidgets.QLabel(self.frame)
        self.txtLastName.setGeometry(QtCore.QRect(490, 10, 251, 61))
        self.txtLastName.setStyleSheet("background-color:rgb(37,52,63);\n"
"color:white;")
        self.txtLastName.setObjectName("txtLastName")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(500, 20, 121, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.txtnaId = QtWidgets.QLabel(self.frame)
        self.txtnaId.setGeometry(QtCore.QRect(220, 10, 261, 61))
        self.txtnaId.setStyleSheet("background-color:rgb(37,52,63);\n"
"color:white;")
        self.txtnaId.setObjectName("txtnaId")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(230, 20, 151, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.txtphone = QtWidgets.QLabel(self.frame)
        self.txtphone.setGeometry(QtCore.QRect(690, 80, 301, 51))
        self.txtphone.setStyleSheet("background-color:rgb(37,52,63);\n"
"color:white;")
        self.txtphone.setObjectName("txtphone")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(700, 90, 171, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(10, 140, 981, 101))
        self.label_5.setStyleSheet("color:white;\n"
"background-color:rgb(37,52,63);\n"
"")
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_5.setObjectName("label_5")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setGeometry(QtCore.QRect(20, 150, 851, 81))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.txtBirthdate = QtWidgets.QLabel(self.frame)
        self.txtBirthdate.setGeometry(QtCore.QRect(380, 80, 301, 51))
        self.txtBirthdate.setStyleSheet("background-color:rgb(37,52,63);\n"
"color:white;")
        self.txtBirthdate.setObjectName("txtBirthdate")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_6.setGeometry(QtCore.QRect(390, 90, 171, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setGeometry(QtCore.QRect(19, 9, 141, 121))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_7 = QtWidgets.QLabel(self.frame_4)
        self.label_7.setGeometry(QtCore.QRect(40, 45, 55, 21))
        self.label_7.setStyleSheet("font: 6pt \"MS Shell Dlg 2\";\n"
"font: 7pt \"MS Shell Dlg 2\";\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"border:none;\n"
"")
        self.label_7.setObjectName("label_7")
        self.txtzipCode = QtWidgets.QLabel(self.frame)
        self.txtzipCode.setGeometry(QtCore.QRect(180, 80, 191, 51))
        self.txtzipCode.setStyleSheet("background-color:rgb(37,52,63);\n"
"color:white;")
        self.txtzipCode.setObjectName("txtzipCode")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_7.setGeometry(QtCore.QRect(190, 90, 91, 31))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_2)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 981, 221))
        self.tableWidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 90))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 90))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.btndelet = QtWidgets.QPushButton(self.frame_3,clicked=lambda:self.deleteFromDb())
        self.btndelet.setGeometry(QtCore.QRect(160, 10, 201, 71))
        self.btndelet.setStyleSheet("QPushButton{\n"
"background-color:rgb(37,52,63);\n"
"color:white;\n"
"border:2px solid #FF9B51;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(255,155,81);\n"
"color:black;\n"
"border:2px solid rgb(37,52,63);\n"
"}")
        self.btndelet.setObjectName("btndelet")
        self.btnNext = QtWidgets.QPushButton(self.frame_3)
        self.btnNext.setGeometry(QtCore.QRect(370, 10, 201, 71))
        self.btnNext.setStyleSheet("QPushButton{\n"
"background-color:rgb(37,52,63);\n"
"color:white;\n"
"border:2px solid #FF9B51;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(255,155,81);\n"
"color:black;\n"
"border:2px solid rgb(37,52,63);\n"
"}")
        self.btnNext.setObjectName("btnNext")
        self.btndisagne = QtWidgets.QPushButton(self.frame_3,clicked=lambda:self.search())
        self.btndisagne.setGeometry(QtCore.QRect(580, 10, 201, 71))
        self.btndisagne.setStyleSheet("QPushButton{\n"
"background-color:rgb(37,52,63);\n"
"color:white;\n"
"border:2px solid #FF9B51;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(255,155,81);\n"
"color:black;\n"
"border:2px solid rgb(37,52,63);\n"
"}")
        self.btndisagne.setObjectName("btndisagne")
        self.btnSave = QtWidgets.QPushButton(self.frame_3,clicked=lambda:self.saveInDb())
        self.btnSave.setGeometry(QtCore.QRect(790, 10, 201, 71))
        self.btnSave.setStyleSheet("QPushButton{\n"
"background-color:rgb(37,52,63);\n"
"color:white;\n"
"border:2px solid #FF9B51;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(255,155,81);\n"
"color:black;\n"
"border:2px solid rgb(37,52,63);\n"
"}")
        self.btnSave.setObjectName("btnSave")
        self.btnExit = QtWidgets.QPushButton(self.frame_3)
        self.btnExit.setGeometry(QtCore.QRect(10, 10, 141, 71))
        self.btnExit.setStyleSheet("QPushButton{\n"
"background-color:rgb(37,52,63);\n"
"color:white;\n"
"border:2px solid #FF9B51;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(255,155,81);\n"
"color:black;\n"
"border:2px solid rgb(37,52,63);\n"
"}")
        self.btnExit.setObjectName("btnExit")
        self.verticalLayout.addWidget(self.frame_3)
        frmCustomer.setCentralWidget(self.centralwidget)

        self.retranslateUi(frmCustomer)
        QtCore.QMetaObject.connectSlotsByName(frmCustomer)
        self.showDataInTable()

     def retranslateUi(self, frmCustomer):
        _translate = QtCore.QCoreApplication.translate
        frmCustomer.setWindowTitle(_translate("frmCustomer", "MainWindow"))
        self.txtName.setText(_translate("frmCustomer", "نام:"))
        self.txtLastName.setText(_translate("frmCustomer", "نام خانوادگی:"))
        self.txtnaId.setText(_translate("frmCustomer", "کدملی:"))
        self.txtphone.setText(_translate("frmCustomer", "شماره تماس:"))
        self.label_5.setText(_translate("frmCustomer", "آدرس"))
        self.txtBirthdate.setText(_translate("frmCustomer", "تاریخ تولد:"))
        self.lineEdit_6.setText(_translate("frmCustomer", "13  /  / "))
        self.label_7.setText(_translate("frmCustomer", "تصویر"))
        self.txtzipCode.setText(_translate("frmCustomer", "کد پستی"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("frmCustomer", "ردیف"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("frmCustomer", "نام مشتری"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("frmCustomer", "نام خانوادگی"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("frmCustomer", "کد ملی"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("frmCustomer", "شماره تماس"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("frmCustomer", "تاریخ تولد"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("frmCustomer", "کد پستی"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("frmCustomer", "آدرس"))
        self.btndelet.setText(_translate("frmCustomer", "حذف"))
        self.btnNext.setText(_translate("frmCustomer", "بعدی"))
        self.btndisagne.setText(_translate("frmCustomer", "ویرایش"))
        self.btnSave.setText(_translate("frmCustomer", "ذخیره"))
        self.btnExit.setText(_translate("frmCustomer", "خروج"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmCustomer = QtWidgets.QMainWindow()
    ui = Ui_frmEmployee()
    ui.setupUi(frmCustomer)
    frmCustomer.show()
    sys.exit(app.exec_())
