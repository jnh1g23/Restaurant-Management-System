# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\21heffernajn42\Downloads\Coursework (1)\UI Files\StartersPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StartersPage(object):
    def setupUi(self, StartersPage):
        StartersPage.setObjectName("StartersPage")
        StartersPage.resize(647, 421)

        self.retranslateUi(StartersPage)
        QtCore.QMetaObject.connectSlotsByName(StartersPage)

    def retranslateUi(self, StartersPage):
        _translate = QtCore.QCoreApplication.translate
        StartersPage.setWindowTitle(_translate("StartersPage", "Dialog"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StartersPage = QtWidgets.QDialog()
    ui = Ui_StartersPage()
    ui.setupUi(StartersPage)
    StartersPage.show()
    sys.exit(app.exec_())