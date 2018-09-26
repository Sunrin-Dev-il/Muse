from PyQt5 import uic
from PyQt5.QtCore import QSize
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from parse import chart_parse,video_parse
from video_downloader import video
from time import sleep

import os,sys
import image_rc

form_class = uic.loadUiType("ui/Mainwindow.ui")[0]
class Main_Window(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_1.clicked.connect(self.btn_clicked_1)
        self.pushButton_2.clicked.connect(self.btn_clicked_2)
        self.pushButton_3.clicked.connect(self.btn_clicked_3)
        self.setWindowIcon(QIcon('ui/image/muse.png'))

        self.pushButton_1.setIcon(QIcon('ui/image/music-player.png'))
        self.pushButton_1.setIconSize(QSize(40, 40))
        layout = QVBoxLayout(self)
        layout.addWidget(self.pushButton_1)

        self.pushButton_2.setIcon(QIcon('ui/image/music-downloads-folder.png'))
        self.pushButton_2.setIconSize(QSize(40, 40))
        layout = QVBoxLayout(self)
        layout.addWidget(self.pushButton_2)

        self.pushButton_3.setIcon(QIcon('ui/image/icon.png'))
        self.pushButton_3.setIconSize(QSize(40, 40))
        layout = QVBoxLayout(self)
        layout.addWidget(self.pushButton_3)

    def btn_clicked_1(self):
        ct = chart()
        ct.exec()

    def btn_clicked_2(self):
        ser = search()
        ser.exec()

    def btn_clicked_3(self):
        self.close()

form_class = uic.loadUiType("ui/Chart.ui")[0]
class chart(QDialog, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.browser = QTextBrowser(self)
        self.browser.resize(530, 400)
        self.browser.move(25, 80)
        self.setWindowIcon(QIcon('ui/image/muse.png'))

        self.pushButton.setIcon(QIcon('ui/image/icon.png'))
        self.pushButton.setIconSize(QSize(40, 40))

        chart_list = chart_parse()

        ct = 1
        for key in chart_list:
            self.browser.append(str(ct) + ". "+key+" - "+chart_list[key])
            ct += 1

yt_list = {}
form_class = uic.loadUiType("ui/input_search.ui")[0]
class search(QDialog, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('ui/image/muse.png'))
        self.lineEdit.returnPressed.connect(self.lineEditInput)
        self.pushButton.setIcon(QIcon('ui/image/icon.png'))
        self.pushButton.setIconSize(QSize(40, 40))

    def lineEditInput(self):
        global yt_list

        search = self.lineEdit.text()
        yt_list = video_parse(search)

        self.close()

        yt = youtube()
        yt.exec()



form_class = uic.loadUiType("ui/Youtube.ui")[0]
class youtube(QDialog, form_class):
    global yt_list
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.browser = QTextBrowser(self)
        self.browser.resize(525, 350)
        self.browser.move(30, 100)
        self.setWindowIcon(QIcon('ui/image/muse.png'))
        self.lineEdit.returnPressed.connect(self.lineEditInput)

        self.pushButton.setIcon(QIcon('ui/image/icon.png'))
        self.pushButton.setIconSize(QSize(40, 40))


        ct = 1
        for key in yt_list:
            self.browser.append(str(ct) + ". " + key)
            ct += 1

    def lineEditInput(self):
        try:
            idx = int(self.lineEdit.text())
        except:
            QMessageBox.information(self,"Muse","숫자를 입력해주세요.")
            self.close()

        if 0< idx <len(yt_list):
            ct = 1
            for key in yt_list:
                if ct == idx:
                    yt_url = yt_list[key]
                    break
                ct += 1

            QMessageBox.information(self,"Muse","다운중...")
            if not video(yt_url):
                QMessageBox.information(self,"Muse","다운되지 않았습니다.")
                self.close()

            QMessageBox.information(self, "Muse", "성공적으로 다운되었습니다.")
            self.close()
        else:
            QMessageBox.information(self, "Muse", "잘못 입력하셨습니다.")
            self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Main_Window = Main_Window()

    Main_Window.show()
    app.exec_()
    sys.exit()