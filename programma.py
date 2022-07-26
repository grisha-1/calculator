# -*- coding: utf-8 -*-
from grafic import *
import sys
import pyttsx3

engine = pyttsx3.init()


# вспомгательно

class mathe:
    code_ = 0
    first_number = ''
    second_number = ''
    znak = '0'

    def talk(self, word):
        engine.say(word)
        engine.runAndWait()

    def talk_error(self):
        self.talk('пока не работает')

    # кнопки

    def one_(self):
        if self.code_ == 0:
            self.first_number = self.first_number + '1'
            ui.textEdit.setText(str(self.first_number))
        elif self.code_ == 1:
            self.second_number = self.second_number + '1'
            ui.textEdit.setText(str(self.second_number))
        print(self.first_number)
        print(self.second_number)

    def two_(self):
        if self.code_ == 0:
            self.first_number = self.first_number + '2'
            ui.textEdit.setText(str(self.first_number))
        elif self.code_ == 1:
            self.second_number = self.second_number + '2'
            ui.textEdit.setText(str(self.second_number))

    def three_(self):
        if self.code_ == 0:
            self.first_number = self.first_number + '3'
            ui.textEdit.setText(str(self.first_number))
        elif self.code_ == 1:
            self.second_number = self.second_number + '3'
            ui.textEdit.setText(str(self.second_number))

    def four_(self):
        if self.code_ == 0:
            self.first_number = self.first_number + '4'
            ui.textEdit.setText(str(self.first_number))
        elif self.code_ == 1:
            self.second_number = self.second_number + '4'
            ui.textEdit.setText(str(self.second_number))

    def five_(self):
        if self.code_ == 0:
            self.first_number = self.first_number + '5'
            ui.textEdit.setText(str(self.first_number))
        elif self.code_ == 1:
            self.second_number = self.second_number + '5'
            ui.textEdit.setText(str(self.second_number))

    def six_(self):
        if self.code_ == 0:
            self.first_number = self.first_number + '6'
            ui.textEdit.setText(str(self.first_number))
        elif self.code_ == 1:
            self.second_number = self.second_number + '6'
            ui.textEdit.setText(str(self.second_number))

    def seven_(self):
        if self.code_ == 0:
            self.first_number = self.first_number + '7'
            ui.textEdit.setText(str(self.first_number))
        elif self.code_ == 1:
            self.second_number = self.second_number + '7'
            ui.textEdit.setText(str(self.second_number))

    def eight_(self):
        if self.code_ == 0:
            self.first_number = self.first_number + '8'
            ui.textEdit.setText(str(self.first_number))
        elif self.code_ == 1:
            self.second_number = self.second_number + '8'
            ui.textEdit.setText(str(self.second_number))

    def nine_(self):
        if self.code_ == 0:
            self.first_number = self.first_number + '9'
            ui.textEdit.setText(str(self.first_number))
        elif self.code_ == 1:
            self.second_number = self.second_number + '9'
            ui.textEdit.setText(str(self.second_number))

    def zero_(self):
        if self.code_ == 0:
            self.first_number = self.first_number + '0'
            ui.textEdit.setText(str(self.first_number))
        elif self.code_ == 1:
            self.second_number = self.second_number + '0'
            ui.textEdit.setText(str(self.second_number))

    def plus_(self):
        self.code_ = 1
        self.znak = '1'

    def minus_(self):
        self.code_ = 1
        self.znak = '2'

    def multi_(self):
        self.code_ = 1
        self.znak = '3'

    def delenie_(self):
        self.code_ = 1
        self.znak = '4'

    def zpt_(self):
        if self.code_ == 0:
            self.first_number = self.first_number + '.'
        elif self.code_ == 1:
            self.second_number = self.second_number + '.'

    def deleat_(self):
        self.first_number, self.second_number = '', ''
        self.code_ = 0
        self.znak = '0'
        ui.textEdit.setText('hello')

    def ravno_(self):
        self.first_number = int(self.first_number)
        self.second_number = int(self.second_number)
        print(self.first_number, self.second_number, self.znak)
        try:
            if self.znak == '1':
                a = self.first_number + self.second_number
                ui.textEdit.setText(str(a))
            elif self.znak == '2':
                a = self.first_number - self.second_number
                ui.textEdit.setText(str(a))
            elif self.znak == '3':
                a = self.first_number * self.second_number
                ui.textEdit.setText(str(a))
            elif self.znak == '4':
                a = self.first_number / self.second_number
                ui.textEdit.setText(str(a))
        except:
            ui.textEdit.setText('ERROR')
        self.first_number, self.second_number = '', ''
        self.code_ = 0
        self.znak = '0'


classus = mathe()

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_Dialog()
ui.setupUi(MainWindow)
MainWindow.show()
MainWindow.resize(500, 500)
ui.one.clicked.connect(classus.one_)
ui.two.clicked.connect(classus.two_)
ui.three.clicked.connect(classus.three_)
ui.four.clicked.connect(classus.four_)
ui.five.clicked.connect(classus.five_)
ui.six.clicked.connect(classus.six_)
ui.seven.clicked.connect(classus.seven_)
ui.eight.clicked.connect(classus.eight_)
ui.nine.clicked.connect(classus.nine_)
ui.zero.clicked.connect(classus.zero_)
ui.plus.clicked.connect(classus.plus_)
ui.minus.clicked.connect(classus.minus_)
ui.delenie.clicked.connect(classus.delenie_)
ui.multi.clicked.connect(classus.multi_)
ui.zpt.clicked.connect(classus.talk_error)
ui.deleat.clicked.connect(classus.deleat_)

ui.ravno.clicked.connect(classus.ravno_)
ui.scobki.clicked.connect(classus.talk_error)
ui.koren.clicked.connect(classus.talk_error)
ui.procent.clicked.connect(classus.talk_error)
ui.pushButton.clicked.connect(classus.talk_error)

sys.exit(app.exec())

# шщздллорпвыфупрооолллшнкуц2каппкака
