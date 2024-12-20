# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Josh\OneDrive - The College of Richard Collyer\coursework 13\UI Files\AddMenuItem.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddMenuItem(object):
    def setupUi(self, AddMenuItem):
        AddMenuItem.setObjectName("AddMenuItem")
        AddMenuItem.resize(1067, 541)
        AddMenuItem.setMinimumSize(QtCore.QSize(1067, 541))
        AddMenuItem.setMaximumSize(QtCore.QSize(1067, 541))
        AddMenuItem.setStyleSheet("")
        self.twMenuItems = QtWidgets.QTableWidget(AddMenuItem)
        self.twMenuItems.setGeometry(QtCore.QRect(310, 50, 751, 391))
        self.twMenuItems.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.twMenuItems.setTabKeyNavigation(False)
        self.twMenuItems.setProperty("showDropIndicator", False)
        self.twMenuItems.setDragDropOverwriteMode(False)
        self.twMenuItems.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.twMenuItems.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.twMenuItems.setObjectName("twMenuItems")
        self.twMenuItems.setColumnCount(0)
        self.twMenuItems.setRowCount(0)
        self.pbBack = QtWidgets.QPushButton(AddMenuItem)
        self.pbBack.setGeometry(QtCore.QRect(950, 10, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.pbBack.setFont(font)
        self.pbBack.setStyleSheet("")
        self.pbBack.setObjectName("pbBack")
        self.leItemname = QtWidgets.QLineEdit(AddMenuItem)
        self.leItemname.setGeometry(QtCore.QRect(10, 140, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.leItemname.setFont(font)
        self.leItemname.setStyleSheet("")
        self.leItemname.setObjectName("leItemname")
        self.cbCategory = QtWidgets.QComboBox(AddMenuItem)
        self.cbCategory.setGeometry(QtCore.QRect(10, 220, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cbCategory.setFont(font)
        self.cbCategory.setStyleSheet("")
        self.cbCategory.setObjectName("cbCategory")
        self.cbCategory.addItem("")
        self.cbCategory.addItem("")
        self.cbCategory.addItem("")
        self.cbCategory.addItem("")
        self.cbCategory.addItem("")
        self.pbConfirm = QtWidgets.QPushButton(AddMenuItem)
        self.pbConfirm.setGeometry(QtCore.QRect(910, 470, 141, 31))
        self.pbConfirm.setObjectName("pbConfirm")
        self.lblitemdetails = QtWidgets.QLabel(AddMenuItem)
        self.lblitemdetails.setGeometry(QtCore.QRect(10, 80, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lblitemdetails.setFont(font)
        self.lblitemdetails.setStyleSheet("")
        self.lblitemdetails.setObjectName("lblitemdetails")
        self.lblItemPrice = QtWidgets.QLabel(AddMenuItem)
        self.lblItemPrice.setGeometry(QtCore.QRect(10, 290, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lblItemPrice.setFont(font)
        self.lblItemPrice.setStyleSheet("")
        self.lblItemPrice.setObjectName("lblItemPrice")
        self.sbPrice = QtWidgets.QDoubleSpinBox(AddMenuItem)
        self.sbPrice.setGeometry(QtCore.QRect(100, 291, 62, 31))
        self.sbPrice.setMinimum(0.0)
        self.sbPrice.setMaximum(250.0)
        self.sbPrice.setProperty("value", 9.99)
        self.sbPrice.setObjectName("sbPrice")
        self.lblErrorItemName = QtWidgets.QLabel(AddMenuItem)
        self.lblErrorItemName.setGeometry(QtCore.QRect(10, 170, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblErrorItemName.setFont(font)
        self.lblErrorItemName.setText("")
        self.lblErrorItemName.setObjectName("lblErrorItemName")
        self.lblErrorCategory = QtWidgets.QLabel(AddMenuItem)
        self.lblErrorCategory.setGeometry(QtCore.QRect(10, 250, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblErrorCategory.setFont(font)
        self.lblErrorCategory.setText("")
        self.lblErrorCategory.setObjectName("lblErrorCategory")

        self.retranslateUi(AddMenuItem)
        QtCore.QMetaObject.connectSlotsByName(AddMenuItem)

    def retranslateUi(self, AddMenuItem):
        _translate = QtCore.QCoreApplication.translate
        AddMenuItem.setWindowTitle(_translate("AddMenuItem", "Dialog"))
        self.pbBack.setText(_translate("AddMenuItem", "Back"))
        self.leItemname.setPlaceholderText(_translate("AddMenuItem", "Item Name"))
        self.cbCategory.setCurrentText(_translate("AddMenuItem", "Category:"))
        self.cbCategory.setItemText(0, _translate("AddMenuItem", "Category:"))
        self.cbCategory.setItemText(1, _translate("AddMenuItem", "Starter"))
        self.cbCategory.setItemText(2, _translate("AddMenuItem", "Main"))
        self.cbCategory.setItemText(3, _translate("AddMenuItem", "Dessert"))
        self.cbCategory.setItemText(4, _translate("AddMenuItem", "Drink"))
        self.pbConfirm.setText(_translate("AddMenuItem", "Confirm"))
        self.lblitemdetails.setText(_translate("AddMenuItem", "Enter Item Details:"))
        self.lblItemPrice.setText(_translate("AddMenuItem", "Item Price:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddMenuItem = QtWidgets.QDialog()
    ui = Ui_AddMenuItem()
    ui.setupUi(AddMenuItem)
    AddMenuItem.show()
    sys.exit(app.exec_())
