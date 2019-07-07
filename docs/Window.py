
from .MyApp import Ui_MainWindow
from .View import OpenGLView
from .Primitive import Box, Cone, Cylinder, Sphere
from .Dialog.BoxDialog import Ui_Dialog as BoxDialog
from .Dialog.ConeDialog import Ui_Dialog as ConeDialog
from .Dialog.SphereDialog import Ui_Dialog as SphereDialog

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MyWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.OpenGL = OpenGLView(self.groupBox_2)
        self.OpenGL.setObjectName('OpenGL')
        self.gridLayout_5.addWidget(self.OpenGL, 0, 0, 1, 1)

        self.connectMenu()
        self.connectButton()
        self.connectSlider()
        self.horizontalSlider.setValue(200)
        self.horizontalSlider_2.setValue(200)
        self.horizontalSlider_3.setValue(200)
        self.show()

    def OnCloseDocument(self):
        QApplication.quit()

    def connectSlider(self):
        self.horizontalSlider.sliderMoved.connect(self.OnRSlider)
        self.horizontalSlider_2.sliderMoved.connect(self.OnGSlider)
        self.horizontalSlider_3.sliderMoved.connect(self.OnBSlider)

    def connectMenu(self):
        self.actionClose.triggered.connect(self.OnCloseDocument)
        self.actionVertex.triggered.connect(self.OnVertex)
        self.actionWire.triggered.connect(self.OnWire)
        self.actionFace.triggered.connect(self.OnFace)
        self.actionCullFace.triggered.connect(self.OnCullFace)

        self.actionBox.triggered.connect(self.DrawBox)
        self.actionCone.triggered.connect(self.DrawCone)
        self.actionCylinder.triggered.connect(self.DrawCylinder)
        self.actionSphere.triggered.connect(self.DrawSphere)
        self.actionClear.triggered.connect(self.Clear)

    def connectButton(self):
        self.VertexButton.clicked.connect(self.OnVertex)
        self.WireButton.clicked.connect(self.OnWire)
        self.FaceButton.clicked.connect(self.OnFace)

    def OnVertex(self):
        self.actionVertex.setChecked(True)
        self.actionWire.setChecked(False)
        self.actionFace.setChecked(False)
        self.VertexButton.setChecked(True)
        self.WireButton.setChecked(False)
        self.FaceButton.setChecked(False)

        OpenGLView.m_Mode = GL_POINTS

    def OnWire(self):
        self.actionVertex.setChecked(False)
        self.actionWire.setChecked(True)
        self.actionFace.setChecked(False)
        self.VertexButton.setChecked(False)
        self.WireButton.setChecked(True)
        self.FaceButton.setChecked(False)

        OpenGLView.m_Mode = GL_LINE

    def OnFace(self):
        self.actionVertex.setChecked(False)
        self.actionWire.setChecked(False)
        self.actionFace.setChecked(True)
        self.VertexButton.setChecked(False)
        self.WireButton.setChecked(False)
        self.FaceButton.setChecked(True)

        OpenGLView.m_Mode = GL_POLYGON

    def OnCullFace(self):
        if not OpenGLView.gl_CULL_FACE:
            print(1)
            self.actionCullFace.setChecked(True)
            OpenGLView.gl_CULL_FACE = 1
        else:
            print(2)
            self.actionCullFace.setChecked(False)
            OpenGLView.gl_CULL_FACE = 0

    def DrawBox(self):
        dlg = BoxDialog()
        dlg.setupUi(dlg)
        dlg.exec_()
        if dlg.flag:
            OpenGLView.m_Object = None
            OpenGLView.m_Object = Box()
            OpenGLView.m_Object.setValue(dlg.width, dlg.depth, dlg.height)

    def DrawCone(self):
        dlg = ConeDialog()
        dlg.setupUi(dlg)
        dlg.exec_()
        if dlg.flag:
            OpenGLView.m_Object = None
            OpenGLView.m_Object = Cone()
            OpenGLView.m_Object.setValue(dlg.radius, dlg.height)

    def DrawCylinder(self):
        dlg = ConeDialog()
        dlg.setupUi(dlg)
        dlg.exec_()
        if dlg.flag:
            OpenGLView.m_Object = None
            OpenGLView.m_Object = Cylinder()
            OpenGLView.m_Object.setValue(dlg.radius, dlg.height)

    def DrawSphere(self):
        dlg = SphereDialog()
        dlg.setupUi(dlg)
        dlg.exec_()
        if dlg.flag:
            OpenGLView.m_Object = None
            OpenGLView.m_Object = Sphere()
            OpenGLView.m_Object.setValue(dlg.radius)

    def Clear(self):
        OpenGLView.m_Object = None

    def OnRSlider(self):
        OpenGLView.m_rValue = self.horizontalSlider.value()

    def OnGSlider(self):
        OpenGLView.m_gValue = self.horizontalSlider_2.value()

    def OnBSlider(self):
        OpenGLView.m_bValue = self.horizontalSlider_3.value()


