# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Viewer.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1012, 883)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.Base = QtWidgets.QGroupBox(self.centralwidget)
        self.Base.setTitle("")
        self.Base.setObjectName("Base")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Base)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.Base)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.VertexButton = QtWidgets.QPushButton(self.groupBox)
        self.VertexButton.setCheckable(True)
        self.VertexButton.setAutoRepeat(False)
        self.VertexButton.setAutoExclusive(False)
        self.VertexButton.setObjectName("VertexButton")
        self.horizontalLayout_2.addWidget(self.VertexButton)
        self.WireButton = QtWidgets.QPushButton(self.groupBox)
        self.WireButton.setCheckable(True)
        self.WireButton.setAutoRepeat(False)
        self.WireButton.setAutoExclusive(False)
        self.WireButton.setObjectName("WireButton")
        self.horizontalLayout_2.addWidget(self.WireButton)
        self.FaceButton = QtWidgets.QPushButton(self.groupBox)
        self.FaceButton.setCheckable(True)
        self.FaceButton.setChecked(True)
        self.FaceButton.setAutoRepeat(False)
        self.FaceButton.setAutoExclusive(False)
        self.FaceButton.setObjectName("FaceButton")
        self.horizontalLayout_2.addWidget(self.FaceButton)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalSlider = QtWidgets.QSlider(self.groupBox_3)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout_2.addWidget(self.horizontalSlider)
        self.horizontalSlider_2 = QtWidgets.QSlider(self.groupBox_3)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.verticalLayout_2.addWidget(self.horizontalSlider_2)
        self.horizontalSlider_3 = QtWidgets.QSlider(self.groupBox_3)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.verticalLayout_2.addWidget(self.horizontalSlider_3)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.groupBox_3)
        self.horizontalLayout_3.setStretch(0, 4)
        self.horizontalLayout_3.setStretch(1, 5)
        self.gridLayout_4.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.Base)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout.addWidget(self.groupBox_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 6)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(0, 6)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.Base, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1012, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuPrimitive = QtWidgets.QMenu(self.menubar)
        self.menuPrimitive.setObjectName("menuPrimitive")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionVertex = QtWidgets.QAction(MainWindow)
        self.actionVertex.setCheckable(True)
        self.actionVertex.setObjectName("actionVertex")
        self.actionWire = QtWidgets.QAction(MainWindow)
        self.actionWire.setCheckable(True)
        self.actionWire.setObjectName("actionWire")
        self.actionFace = QtWidgets.QAction(MainWindow)
        self.actionFace.setCheckable(True)
        self.actionFace.setChecked(True)
        self.actionFace.setObjectName("actionFace")
        self.actionFileOpen = QtWidgets.QAction(MainWindow)
        self.actionFileOpen.setObjectName("actionFileOpen")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionColor = QtWidgets.QAction(MainWindow)
        self.actionColor.setObjectName("actionColor")
        self.actionBox = QtWidgets.QAction(MainWindow)
        self.actionBox.setObjectName("actionBox")
        self.actionCone = QtWidgets.QAction(MainWindow)
        self.actionCone.setObjectName("actionCone")
        self.actionCylinder = QtWidgets.QAction(MainWindow)
        self.actionCylinder.setObjectName("actionCylinder")
        self.actionSphere = QtWidgets.QAction(MainWindow)
        self.actionSphere.setObjectName("actionSphere")
        self.actionClear = QtWidgets.QAction(MainWindow)
        self.actionClear.setObjectName("actionClear")
        self.actionCullFace = QtWidgets.QAction(MainWindow)
        self.actionCullFace.setObjectName("actionCullFace")
        self.actionCullFace.setCheckable(True)

        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuView.addAction(self.actionVertex)
        self.menuView.addAction(self.actionWire)
        self.menuView.addAction(self.actionFace)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionCullFace)

        self.menuPrimitive.addAction(self.actionBox)
        self.menuPrimitive.addAction(self.actionCone)
        self.menuPrimitive.addAction(self.actionCylinder)
        self.menuPrimitive.addAction(self.actionSphere)
        self.menuPrimitive.addSeparator()
        self.menuPrimitive.addAction(self.actionClear)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuPrimitive.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.horizontalSlider.setMaximum(255)
        self.horizontalSlider_2.setMaximum(255)
        self.horizontalSlider_3.setMaximum(255)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "VR LAB"))
        self.VertexButton.setText(_translate("MainWindow", "Vertex"))
        self.WireButton.setText(_translate("MainWindow", "Wire"))
        self.FaceButton.setText(_translate("MainWindow", "Face"))
        self.groupBox_3.setTitle(_translate("MainWindow", "GroupBox"))
        self.groupBox_2.setTitle(_translate("MainWindow", "View"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuPrimitive.setTitle(_translate("MainWindow", "Primitive"))
        self.actionVertex.setText(_translate("MainWindow", "Vertex"))
        self.actionWire.setText(_translate("MainWindow", "Wire"))
        self.actionFace.setText(_translate("MainWindow", "Face"))
        self.actionFileOpen.setText(_translate("MainWindow", "FileOpen"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionColor.setText(_translate("MainWindow", "Color"))
        self.actionBox.setText(_translate("MainWindow", "Box"))
        self.actionCone.setText(_translate("MainWindow", "Cone"))
        self.actionCylinder.setText(_translate("MainWindow", "Cylinder"))
        self.actionSphere.setText(_translate("MainWindow", "Sphere"))
        self.actionCullFace.setText(_translate("MainWindow", "CullFace"))
        self.actionClear.setText(_translate("MainWindow", "Clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
