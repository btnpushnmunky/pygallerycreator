# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(408, 248)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listView = QtWidgets.QListView(self.centralWidget)
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)
        self.source_button = QtWidgets.QPushButton(self.centralWidget)
        self.source_button.setObjectName("source_button")
        self.verticalLayout.addWidget(self.source_button)
        self.destination_button = QtWidgets.QPushButton(self.centralWidget)
        self.destination_button.setObjectName("destination_button")
        self.verticalLayout.addWidget(self.destination_button)
        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyGalleryCreator"))
        self.source_button.setText(_translate("MainWindow", "Source"))
        self.destination_button.setText(_translate("MainWindow", "Destination"))

