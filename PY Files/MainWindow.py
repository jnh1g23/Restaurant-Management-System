# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Josh\Downloads\OneDrive_2022-11-22\coursework 8\UI Files\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1067, 600)
        MainWindow.setMinimumSize(QtCore.QSize(1067, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1067, 600))
        self.TaskbarFrame = QtWidgets.QFrame(MainWindow)
        self.TaskbarFrame.setGeometry(QtCore.QRect(0, 0, 1067, 61))
        self.TaskbarFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TaskbarFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TaskbarFrame.setObjectName("TaskbarFrame")
        self.pbBookings = QtWidgets.QPushButton(self.TaskbarFrame)
        self.pbBookings.setGeometry(QtCore.QRect(10, 10, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(12)
        self.pbBookings.setFont(font)
        self.pbBookings.setObjectName("pbBookings")
        self.pbCalendar = QtWidgets.QPushButton(self.TaskbarFrame)
        self.pbCalendar.setGeometry(QtCore.QRect(230, 10, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(12)
        self.pbCalendar.setFont(font)
        self.pbCalendar.setObjectName("pbCalendar")
        self.pbSeating = QtWidgets.QPushButton(self.TaskbarFrame)
        self.pbSeating.setGeometry(QtCore.QRect(460, 10, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(12)
        self.pbSeating.setFont(font)
        self.pbSeating.setObjectName("pbSeating")
        self.pbLogout = QtWidgets.QPushButton(self.TaskbarFrame)
        self.pbLogout.setGeometry(QtCore.QRect(920, 10, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(12)
        self.pbLogout.setFont(font)
        self.pbLogout.setObjectName("pbLogout")
        self.pbManagement = QtWidgets.QPushButton(self.TaskbarFrame)
        self.pbManagement.setGeometry(QtCore.QRect(690, 10, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(12)
        self.pbManagement.setFont(font)
        self.pbManagement.setObjectName("pbManagement")
        self.DisplayWidget = QtWidgets.QStackedWidget(MainWindow)
        self.DisplayWidget.setGeometry(QtCore.QRect(0, 60, 1067, 541))
        self.DisplayWidget.setObjectName("DisplayWidget")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dialog"))
        self.pbBookings.setText(_translate("MainWindow", "Bookings"))
        self.pbCalendar.setText(_translate("MainWindow", "Calendar"))
        self.pbSeating.setText(_translate("MainWindow", "Seating"))
        self.pbLogout.setText(_translate("MainWindow", "Log out"))
        self.pbManagement.setText(_translate("MainWindow", "Management"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
