# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_imageloop_widget.ui'
#
# Created: Wed Sep  8 10:53:33 2010
#      by: PyQt4 UI code generator 4.6.1
#
# WARNING! All changes made in this file will be lost!


from PyQt4 import QtCore, QtGui


class Ui_ImageLoopWidget(object):
    def setupUi(self, ImageLoopWidget):
        ImageLoopWidget.setObjectName("ImageLoopWidget")
        ImageLoopWidget.resize(553, 393)
        ImageLoopWidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.verticalLayout = QtGui.QVBoxLayout(ImageLoopWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtGui.QFrame(ImageLoopWidget)
        self.frame.setMinimumSize(QtCore.QSize(120, 22))
        self.frame.setMaximumSize(QtCore.QSize(120, 14))
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Plain)
        self.frame.setLineWidth(1)
        self.frame.setObjectName("frame")
        self.btZoomIn = QtGui.QToolButton(self.frame)
        self.btZoomIn.setGeometry(QtCore.QRect(0, 1, 20, 20))
        self.btZoomIn.setMinimumSize(QtCore.QSize(20, 20))
        self.btZoomIn.setMaximumSize(QtCore.QSize(20, 20))
        self.btZoomIn.setAutoRaise(True)
        self.btZoomIn.setObjectName("btZoomIn")
        self.btZoomOut = QtGui.QToolButton(self.frame)
        self.btZoomOut.setGeometry(QtCore.QRect(17, 1, 20, 20))
        self.btZoomOut.setMinimumSize(QtCore.QSize(20, 20))
        self.btZoomOut.setMaximumSize(QtCore.QSize(20, 20))
        self.btZoomOut.setAutoRaise(True)
        self.btZoomOut.setObjectName("btZoomOut")
        self.btZoomNormalSize = QtGui.QToolButton(self.frame)
        self.btZoomNormalSize.setGeometry(QtCore.QRect(38, 1, 30, 20))
        self.btZoomNormalSize.setMinimumSize(QtCore.QSize(30, 20))
        self.btZoomNormalSize.setMaximumSize(QtCore.QSize(30, 20))
        self.btZoomNormalSize.setCheckable(False)
        self.btZoomNormalSize.setAutoRaise(True)
        self.btZoomNormalSize.setObjectName("btZoomNormalSize")
        self.btFitToWindow = QtGui.QToolButton(self.frame)
        self.btFitToWindow.setGeometry(QtCore.QRect(67, 1, 25, 20))
        self.btFitToWindow.setMinimumSize(QtCore.QSize(25, 20))
        self.btFitToWindow.setMaximumSize(QtCore.QSize(25, 14))
        self.btFitToWindow.setCheckable(True)
        self.btFitToWindow.setAutoRaise(True)
        self.btFitToWindow.setObjectName("btFitToWindow")
        self.tbLevel_down = QtGui.QToolButton(self.frame)
        self.tbLevel_down.setGeometry(QtCore.QRect(92, 8, 25, 14))
        self.tbLevel_down.setMinimumSize(QtCore.QSize(25, 14))
        self.tbLevel_down.setMaximumSize(QtCore.QSize(30, 14))
        self.tbLevel_down.setAutoRaise(True)
        self.tbLevel_down.setArrowType(QtCore.Qt.DownArrow)
        self.tbLevel_down.setObjectName("tbLevel_down")
        self.tbLevel_up = QtGui.QToolButton(self.frame)
        self.tbLevel_up.setGeometry(QtCore.QRect(92, -1, 25, 14))
        self.tbLevel_up.setMinimumSize(QtCore.QSize(25, 14))
        self.tbLevel_up.setMaximumSize(QtCore.QSize(30, 14))
        self.tbLevel_up.setAutoRaise(True)
        self.tbLevel_up.setArrowType(QtCore.Qt.UpArrow)
        self.tbLevel_up.setObjectName("tbLevel_up")
        self.horizontalLayout_2.addWidget(self.frame)
        self.lblInfo = QtGui.QLabel(ImageLoopWidget)
        self.lblInfo.setMinimumSize(QtCore.QSize(0, 20))
        self.lblInfo.setMaximumSize(QtCore.QSize(16777215, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setItalic(False)
        font.setUnderline(False)
        font.setBold(True)
        self.lblInfo.setFont(font)
        self.lblInfo.setObjectName("lblInfo")
        self.horizontalLayout_2.addWidget(self.lblInfo)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.scrollArea = QtGui.QScrollArea(ImageLoopWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget(self.scrollArea)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 539, 351))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(ImageLoopWidget)
        QtCore.QMetaObject.connectSlotsByName(ImageLoopWidget)

    def retranslateUi(self, ImageLoopWidget):
        ImageLoopWidget.setWindowTitle(
            QtGui.QApplication.translate("ImageLoopWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.btZoomIn.setToolTip(
            QtGui.QApplication.translate("ImageLoopWidget", "zoom in", None, QtGui.QApplication.UnicodeUTF8))
        self.btZoomIn.setText(
            QtGui.QApplication.translate("ImageLoopWidget", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.btZoomOut.setToolTip(
            QtGui.QApplication.translate("ImageLoopWidget", "zoom out", None, QtGui.QApplication.UnicodeUTF8))
        self.btZoomOut.setText(
            QtGui.QApplication.translate("ImageLoopWidget", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.btZoomNormalSize.setToolTip(
            QtGui.QApplication.translate("ImageLoopWidget", "reset image size to original size", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.btZoomNormalSize.setText(
            QtGui.QApplication.translate("ImageLoopWidget", "orig", None, QtGui.QApplication.UnicodeUTF8))
        self.btFitToWindow.setToolTip(QtGui.QApplication.translate("ImageLoopWidget", "fit image size to window", None,
                                                                   QtGui.QApplication.UnicodeUTF8))
        self.btFitToWindow.setText(
            QtGui.QApplication.translate("ImageLoopWidget", "fit", None, QtGui.QApplication.UnicodeUTF8))
        self.tbLevel_down.setToolTip(
            QtGui.QApplication.translate("ImageLoopWidget", "decrease level", None, QtGui.QApplication.UnicodeUTF8))
        self.tbLevel_down.setText(
            QtGui.QApplication.translate("ImageLoopWidget", "\\/", None, QtGui.QApplication.UnicodeUTF8))
        self.tbLevel_up.setToolTip(
            QtGui.QApplication.translate("ImageLoopWidget", "increase level", None, QtGui.QApplication.UnicodeUTF8))
        self.tbLevel_up.setText(
            QtGui.QApplication.translate("ImageLoopWidget", "/\\", None, QtGui.QApplication.UnicodeUTF8))
        self.lblInfo.setText(QtGui.QApplication.translate("ImageLoopWidget", "<Product Information>", None,
                                                          QtGui.QApplication.UnicodeUTF8))
