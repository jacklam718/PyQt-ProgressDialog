#!/usr/bin/env python
# --*--codig: utf8 --*--

from PyQt4 import QtGui
from PyQt4 import QtCore

class BaseProgressBar(QtGui.QWidget):
    updateProgress = QtCore.pyqtSignal(str)
    def __init__(self, text='', parent=None):
        super(BaseProgressBar, self).__init__(parent)
        self.setFixedHeight(50)
        self.text  = text
        self.progressbar = QtGui.QProgressBar( )
        self.progressbar.setTextVisible(True)
        self.updateProgress.connect(self.setValue)

        self.bottomBorder = QtGui.QWidget( )
        self.bottomBorder.setStyleSheet("""
            background: palette(shadow);
        """)
        self.bottomBorder.setSizePolicy(QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed))
        self.bottomBorder.setMinimumHeight(1)

        self.label  = QtGui.QLabel(self.text)
        self.label.setStyleSheet("""
            font-weight: bold;
        """)
        self.layout = QtGui.QVBoxLayout( )
        self.layout.setContentsMargins(10,0,10,0)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.progressbar)

        self.mainLayout = QtGui.QVBoxLayout( )
        self.mainLayout.setContentsMargins(0,0,0,0)
        self.mainLayout.addLayout(self.layout)
        self.mainLayout.addWidget(self.bottomBorder)
        self.setLayout(self.mainLayout)
        self.totalValue = 0

    def setValue(self, value):
        self.totalValue += len(value)
        self.progressbar.setValue(self.totalValue)

    def setMax(self, value):
        self.progressbar.setMaximum(value)
