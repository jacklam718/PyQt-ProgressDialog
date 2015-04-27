#!/usr/bin/env python
# --*--codig: utf8 --*--

from PyQt4 import QtGui
from PyQt4 import QtCore
from baseProgressBar import BaseProgressBar

class DownloadProgressBar(BaseProgressBar):
    def __init__(self, text='Downloading', parent=None):
        super(self.__class__, self).__init__(text, parent)
        style ="""
        QProgressBar {
            border: 2px solid grey;
            border-radius: 5px;
            text-align: center;
        }

        QProgressBar::chunk {
            background-color: #37DA7E;
            width: 20px;
        }"""
        self.progressbar.setStyleSheet(style)


class UploadProgressBar(BaseProgressBar):
    def __init__(self, text='Uploading', parent=None):
        super(self.__class__, self).__init__(text, parent)
        style ="""
        QProgressBar {
            border: 2px solid grey;
            border-radius: 5px;
            text-align: center;
        }

        QProgressBar::chunk {
            background-color: #88B0EB;
            width: 20px;
        }"""
        self.progressbar.setStyleSheet(style)

class ProgressDialog(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.resize(500, 250)
        self.scrollArea = QtGui.QScrollArea( )
        self.scrollArea.setWidgetResizable(True)
        self.setCentralWidget(self.scrollArea)

        self.centralWidget = QtGui.QWidget( )
        self.scrollArea.setWidget(self.centralWidget)

        self.layout = QtGui.QVBoxLayout( )
        self.layout.setAlignment(QtCore.Qt.AlignTop)
        self.layout.setContentsMargins(0,10,0,0)
        self.centralWidget.setLayout(self.layout)

    def addProgressbar(self, progressbar):
        self.layout.addWidget(progressbar)

if __name__ == "__main__":
    import random

    app = QtGui.QApplication([])
    progressNumbers = [x for x in range(1, 101)]
    progressItems = []

    while len(progressItems) <= 20:
        progressItems.append(random.choice(progressNumbers))

    progressDialog = ProgressDialog()

    for progressItem in progressItems:
        progressBar = DownloadProgressBar(text="download")
        progressBar.set_max(100)
        progressBar.set_value(' ' * progressItem)
        progressDialog.addProgressbar(progressBar)

    for progressItem in progressItems:
        progressBar = UploadProgressBar(text="Upload")
        progressBar.set_max(100)
        progressBar.set_value(' ' * progressItem)
        progressDialog.addProgressbar(progressBar)

    progressDialog.show()
    app.exec_()
