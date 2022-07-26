# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 500)
        Dialog.setMinimumSize(QtCore.QSize(500, 500))
        Dialog.setMaximumSize(QtCore.QSize(500, 500))
        Dialog.setStyleSheet("QDialog{\n"
                             "background:#616061;\n"
                             "color:white;\n"
                             "}\n"
                             "")
        self.two = QtWidgets.QPushButton(Dialog)
        self.two.setGeometry(QtCore.QRect(100, 360, 51, 51))
        self.two.setStyleSheet("QPushButton{\n"
                               "background-color: #db9702;\n"
                               "border: 2px solid #f66867;\n"
                               "border-radius: 15%;\n"
                               "color:white;\n"
                               "}\n"
                               "QPushButton::hover{\n"
                               "background-color:#f5b11d;\n"
                               "}\n"
                               "QPushButton::pressed{\n"
                               "background-color:#966906;\n"
                               "}")
        self.two.setObjectName("two")
        self.three = QtWidgets.QPushButton(Dialog)
        self.three.setGeometry(QtCore.QRect(170, 360, 51, 51))
        self.three.setStyleSheet("QPushButton{\n"
                                 "background-color: #db9702;\n"
                                 "border: 2px solid #f66867;\n"
                                 "border-radius: 15%;\n"
                                 "color:white;\n"
                                 "}\n"
                                 "QPushButton::hover{\n"
                                 "background-color:#f5b11d;\n"
                                 "}\n"
                                 "QPushButton::pressed{\n"
                                 "background-color:#966906;\n"
                                 "}")
        self.three.setObjectName("three")
        self.zero = QtWidgets.QPushButton(Dialog)
        self.zero.setGeometry(QtCore.QRect(30, 430, 51, 51))
        self.zero.setStyleSheet("QPushButton{\n"
                                "background-color: #db9702;\n"
                                "border: 2px solid #f66867;\n"
                                "border-radius: 15%;\n"
                                "color:white;\n"
                                "}\n"
                                "QPushButton::hover{\n"
                                "background-color:#f5b11d;\n"
                                "}\n"
                                "QPushButton::pressed{\n"
                                "background-color:#966906;\n"
                                "}")
        self.zero.setObjectName("zero")
        self.koren = QtWidgets.QPushButton(Dialog)
        self.koren.setGeometry(QtCore.QRect(370, 430, 51, 51))
        self.koren.setStyleSheet("QPushButton{\n"
                                 "background-color: #26ff00;\n"
                                 "border: 2px solid #0d5201;\n"
                                 "border-radius: 25%;\n"
                                 "color:black;\n"
                                 "}\n"
                                 "QPushButton::hover{\n"
                                 "background-color:#6bff52;\n"
                                 "}\n"
                                 "QPushButton::pressed{\n"
                                 "background-color:#18a300;\n"
                                 "}")
        self.koren.setObjectName("koren")
        self.ravno = QtWidgets.QPushButton(Dialog)
        self.ravno.setGeometry(QtCore.QRect(100, 430, 121, 51))
        self.ravno.setStyleSheet("QPushButton{\n"
                                 "background-color: #0000ff;\n"
                                 "border: 2px solid #000000;\n"
                                 "border-radius: 15%;\n"
                                 "color:white;\n"
                                 "}\n"
                                 "QPushButton::hover{\n"
                                 "background-color:#5640ff;\n"
                                 "}\n"
                                 "QPushButton::pressed{\n"
                                 "background-color:#0b005e;\n"
                                 "}")
        self.ravno.setObjectName("ravno")
        self.seven = QtWidgets.QPushButton(Dialog)
        self.seven.setGeometry(QtCore.QRect(30, 220, 51, 51))
        self.seven.setStyleSheet("QPushButton{\n"
                                 "background-color: #db9702;\n"
                                 "border: 2px solid #f66867;\n"
                                 "border-radius: 15%;\n"
                                 "color:white;\n"
                                 "}\n"
                                 "QPushButton::hover{\n"
                                 "background-color:#f5b11d;\n"
                                 "}\n"
                                 "QPushButton::pressed{\n"
                                 "background-color:#966906;\n"
                                 "}")
        self.seven.setObjectName("seven")
        self.one = QtWidgets.QPushButton(Dialog)
        self.one.setGeometry(QtCore.QRect(30, 360, 51, 51))
        self.one.setStyleSheet("QPushButton{\n"
                               "background-color: #db9702;\n"
                               "border: 2px solid #f66867;\n"
                               "border-radius: 15%;\n"
                               "color:white;\n"
                               "}\n"
                               "QPushButton::hover{\n"
                               "background-color:#f5b11d;\n"
                               "}\n"
                               "QPushButton::pressed{\n"
                               "background-color:#966906;\n"
                               "}")
        self.one.setObjectName("one")
        self.six = QtWidgets.QPushButton(Dialog)
        self.six.setGeometry(QtCore.QRect(170, 290, 51, 51))
        self.six.setStyleSheet("QPushButton{\n"
                               "background-color: #db9702;\n"
                               "border: 2px solid #f66867;\n"
                               "border-radius: 15%;\n"
                               "color:white;\n"
                               "}\n"
                               "QPushButton::hover{\n"
                               "background-color:#f5b11d;\n"
                               "}\n"
                               "QPushButton::pressed{\n"
                               "background-color:#966906;\n"
                               "}")
        self.six.setObjectName("six")
        self.five = QtWidgets.QPushButton(Dialog)
        self.five.setGeometry(QtCore.QRect(100, 290, 51, 51))
        self.five.setStyleSheet("QPushButton{\n"
                                "background-color: #db9702;\n"
                                "border: 2px solid #f66867;\n"
                                "border-radius: 15%;\n"
                                "color:white;\n"
                                "}\n"
                                "QPushButton::hover{\n"
                                "background-color:#f5b11d;\n"
                                "}\n"
                                "QPushButton::pressed{\n"
                                "background-color:#966906;\n"
                                "}")
        self.five.setObjectName("five")
        self.four = QtWidgets.QPushButton(Dialog)
        self.four.setGeometry(QtCore.QRect(30, 290, 51, 51))
        self.four.setStyleSheet("QPushButton{\n"
                                "background-color: #db9702;\n"
                                "border: 2px solid #f66867;\n"
                                "border-radius: 15%;\n"
                                "color:white;\n"
                                "}\n"
                                "QPushButton::hover{\n"
                                "background-color:#f5b11d;\n"
                                "}\n"
                                "QPushButton::pressed{\n"
                                "background-color:#966906;\n"
                                "}")
        self.four.setObjectName("four")
        self.nine = QtWidgets.QPushButton(Dialog)
        self.nine.setGeometry(QtCore.QRect(170, 220, 51, 51))
        self.nine.setStyleSheet("QPushButton{\n"
                                "background-color: #db9702;\n"
                                "border: 2px solid #f66867;\n"
                                "border-radius: 15%;\n"
                                "color:white;\n"
                                "}\n"
                                "QPushButton::hover{\n"
                                "background-color:#f5b11d;\n"
                                "}\n"
                                "QPushButton::pressed{\n"
                                "background-color:#966906;\n"
                                "}")
        self.nine.setObjectName("nine")
        self.eight = QtWidgets.QPushButton(Dialog)
        self.eight.setGeometry(QtCore.QRect(100, 220, 51, 51))
        self.eight.setStyleSheet("QPushButton{\n"
                                 "background-color: #db9702;\n"
                                 "border: 2px solid #f66867;\n"
                                 "border-radius: 15%;\n"
                                 "color:white;\n"
                                 "}\n"
                                 "QPushButton::hover{\n"
                                 "background-color:#f5b11d;\n"
                                 "}\n"
                                 "QPushButton::pressed{\n"
                                 "background-color:#966906;\n"
                                 "}")
        self.eight.setObjectName("eight")
        self.plus = QtWidgets.QPushButton(Dialog)
        self.plus.setGeometry(QtCore.QRect(250, 220, 41, 121))
        self.plus.setStyleSheet("QPushButton{\n"
                                "background-color: #0000ff;\n"
                                "border: 2px solid #000000;\n"
                                "border-radius: 15%;\n"
                                "color:white;\n"
                                "}\n"
                                "QPushButton::hover{\n"
                                "background-color:#5640ff;\n"
                                "}\n"
                                "QPushButton::pressed{\n"
                                "background-color:#0b005e;\n"
                                "}")
        self.plus.setObjectName("plus")
        self.delenie = QtWidgets.QPushButton(Dialog)
        self.delenie.setGeometry(QtCore.QRect(250, 360, 41, 121))
        self.delenie.setStyleSheet("QPushButton{\n"
                                   "background-color: #0000ff;\n"
                                   "border: 2px solid #000000;\n"
                                   "border-radius: 15%;\n"
                                   "color:white;\n"
                                   "}\n"
                                   "QPushButton::hover{\n"
                                   "background-color:#5640ff;\n"
                                   "}\n"
                                   "QPushButton::pressed{\n"
                                   "background-color:#0b005e;\n"
                                   "}")
        self.delenie.setObjectName("delenie")
        self.multi = QtWidgets.QPushButton(Dialog)
        self.multi.setGeometry(QtCore.QRect(310, 360, 41, 121))
        self.multi.setStyleSheet("QPushButton{\n"
                                 "background-color: #0000ff;\n"
                                 "border: 2px solid #000000;\n"
                                 "border-radius: 15%;\n"
                                 "color:white;\n"
                                 "}\n"
                                 "QPushButton::hover{\n"
                                 "background-color:#5640ff;\n"
                                 "}\n"
                                 "QPushButton::pressed{\n"
                                 "background-color:#0b005e;\n"
                                 "}")
        self.multi.setObjectName("multi")
        self.minus = QtWidgets.QPushButton(Dialog)
        self.minus.setGeometry(QtCore.QRect(310, 220, 41, 121))
        self.minus.setStyleSheet("QPushButton{\n"
                                 "background-color: #0000ff;\n"
                                 "border: 2px solid #000000;\n"
                                 "border-radius: 15%;\n"
                                 "color:white;\n"
                                 "}\n"
                                 "QPushButton::hover{\n"
                                 "background-color:#5640ff;\n"
                                 "}\n"
                                 "QPushButton::pressed{\n"
                                 "background-color:#0b005e;\n"
                                 "}")
        self.minus.setObjectName("minus")
        self.procent = QtWidgets.QPushButton(Dialog)
        self.procent.setGeometry(QtCore.QRect(370, 360, 111, 51))
        self.procent.setStyleSheet("QPushButton{\n"
                                   "background-color: #26ff00;\n"
                                   "border: 2px solid #0d5201;\n"
                                   "border-radius: 25%;\n"
                                   "color:black;\n"
                                   "}\n"
                                   "QPushButton::hover{\n"
                                   "background-color:#6bff52;\n"
                                   "}\n"
                                   "QPushButton::pressed{\n"
                                   "background-color:#18a300;\n"
                                   "}")
        self.procent.setObjectName("procent")
        self.scobki = QtWidgets.QPushButton(Dialog)
        self.scobki.setGeometry(QtCore.QRect(370, 290, 111, 51))
        self.scobki.setStyleSheet("QPushButton{\n"
                                  "background-color: #26ff00;\n"
                                  "border: 2px solid #0d5201;\n"
                                  "border-radius: 25%;\n"
                                  "color:black;\n"
                                  "}\n"
                                  "QPushButton::hover{\n"
                                  "background-color:#6bff52;\n"
                                  "}\n"
                                  "QPushButton::pressed{\n"
                                  "background-color:#18a300;\n"
                                  "}")
        self.scobki.setObjectName("scobki")
        self.deleat = QtWidgets.QPushButton(Dialog)
        self.deleat.setGeometry(QtCore.QRect(370, 220, 111, 51))
        self.deleat.setStyleSheet("QPushButton{\n"
                                  "background-color: #ff0000;\n"
                                  "border: 2px solid #ffdbdb;\n"
                                  "border-radius: 15%;\n"
                                  "color:white;\n"
                                  "}\n"
                                  "QPushButton::hover{\n"
                                  "background-color:#ff5252;\n"
                                  "}\n"
                                  "QPushButton::pressed{\n"
                                  "background-color:#b50202;\n"
                                  "}")
        self.deleat.setObjectName("deleat")
        self.calku = QtWidgets.QLabel(Dialog)
        self.calku.setGeometry(QtCore.QRect(220, 20, 121, 16))
        self.calku.setStyleSheet("QTextEdit{\n"
                                 "color:#ffffff;\n"
                                 "}\n"
                                 "")
        self.calku.setObjectName("calku")
        self.zpt = QtWidgets.QPushButton(Dialog)
        self.zpt.setGeometry(QtCore.QRect(430, 430, 51, 51))
        self.zpt.setStyleSheet("QPushButton{\n"
                               "background-color: #26ff00;\n"
                               "border: 2px solid #0d5201;\n"
                               "border-radius: 25%;\n"
                               "color:black;\n"
                               "}\n"
                               "QPushButton::hover{\n"
                               "background-color:#6bff52;\n"
                               "}\n"
                               "QPushButton::pressed{\n"
                               "background-color:#18a300;\n"
                               "}")
        self.zpt.setObjectName("zpt")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(40, 60, 441, 61))
        self.textEdit.setStyleSheet("QTextEdit{\n"
                                    "background-color: #5b27a3;\n"
                                    "border: 2px solid #ffdbdb;\n"
                                    "border-radius: 15%;\n"
                                    "color:white;\n"
                                    "}\n"
                                    "")
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(30, 140, 441, 61))
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "background-color: #ff0000;\n"
                                      "border: 2px solid #ffdbdb;\n"
                                      "border-radius: 30%;\n"
                                      "color:white;\n"
                                      "}\n"
                                      "QPushButton::hover{\n"
                                      "background-color:#ff5252;\n"
                                      "}\n"
                                      "QPushButton::pressed{\n"
                                      "background-color:#b50202;\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.two.setText(_translate("Dialog", "2"))
        self.three.setText(_translate("Dialog", "3"))
        self.zero.setText(_translate("Dialog", "0"))
        self.koren.setText(_translate("Dialog", "√"))
        self.ravno.setText(_translate("Dialog", "="))
        self.seven.setText(_translate("Dialog", "7"))
        self.one.setText(_translate("Dialog", "1"))
        self.six.setText(_translate("Dialog", "6"))
        self.five.setText(_translate("Dialog", "5"))
        self.four.setText(_translate("Dialog", "4"))
        self.nine.setText(_translate("Dialog", "9"))
        self.eight.setText(_translate("Dialog", "8"))
        self.plus.setText(_translate("Dialog", "+"))
        self.delenie.setText(_translate("Dialog", ":"))
        self.multi.setText(_translate("Dialog", "*"))
        self.minus.setText(_translate("Dialog", "-"))
        self.procent.setText(_translate("Dialog", "%"))
        self.scobki.setText(_translate("Dialog", "()"))
        self.deleat.setText(_translate("Dialog", "deleat"))
        self.calku.setText(_translate("Dialog", "калькулятор v1.0"))
        self.zpt.setText(_translate("Dialog", ","))
        self.textEdit.setHtml(_translate("Dialog",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">hello</p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "озвучить"))
