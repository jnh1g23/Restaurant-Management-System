# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Josh\OneDrive - The College of Richard Collyer\coursework 13\UI Files\TableSelection.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Table(object):
    def setupUi(self, Table):
        Table.setObjectName("Table")
        Table.resize(1067, 481)
        self.lblGuestsLeft = QtWidgets.QLabel(Table)
        self.lblGuestsLeft.setGeometry(QtCore.QRect(20, 20, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lblGuestsLeft.setFont(font)
        self.lblGuestsLeft.setText("")
        self.lblGuestsLeft.setAlignment(QtCore.Qt.AlignCenter)
        self.lblGuestsLeft.setObjectName("lblGuestsLeft")

        self.retranslateUi(Table)
        QtCore.QMetaObject.connectSlotsByName(Table)

    def retranslateUi(self, Table):
        _translate = QtCore.QCoreApplication.translate
        Table.setWindowTitle(_translate("Table", "Dialog"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Table = QtWidgets.QDialog()
    ui = Ui_Table()
    ui.setupUi(Table)
    Table.show()
    sys.exit(app.exec_())
