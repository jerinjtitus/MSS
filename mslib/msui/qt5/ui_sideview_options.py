# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_sideview_options.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SideViewOptionsDialog(object):
    def setupUi(self, SideViewOptionsDialog):
        SideViewOptionsDialog.setObjectName("SideViewOptionsDialog")
        SideViewOptionsDialog.resize(460, 519)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(SideViewOptionsDialog)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(SideViewOptionsDialog)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.sbPbot = QtWidgets.QSpinBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sbPbot.sizePolicy().hasHeightForWidth())
        self.sbPbot.setSizePolicy(sizePolicy)
        self.sbPbot.setPrefix("")
        self.sbPbot.setMinimum(30)
        self.sbPbot.setMaximum(1100)
        self.sbPbot.setProperty("value", 1050)
        self.sbPbot.setObjectName("sbPbot")
        self.horizontalLayout.addWidget(self.sbPbot)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.sbPtop = QtWidgets.QSpinBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sbPtop.sizePolicy().hasHeightForWidth())
        self.sbPtop.setSizePolicy(sizePolicy)
        self.sbPtop.setMinimum(20)
        self.sbPtop.setMaximum(1050)
        self.sbPtop.setProperty("value", 200)
        self.sbPtop.setObjectName("sbPtop")
        self.horizontalLayout.addWidget(self.sbPtop)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(SideViewOptionsDialog)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cbDrawFlightLevels = QtWidgets.QCheckBox(self.groupBox_2)
        self.cbDrawFlightLevels.setObjectName("cbDrawFlightLevels")
        self.verticalLayout_2.addWidget(self.cbDrawFlightLevels)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_2)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.horizontalLayout_3.addWidget(self.tableWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btAdd = QtWidgets.QPushButton(self.groupBox_2)
        self.btAdd.setObjectName("btAdd")
        self.verticalLayout.addWidget(self.btAdd)
        self.btDelete = QtWidgets.QPushButton(self.groupBox_2)
        self.btDelete.setObjectName("btDelete")
        self.verticalLayout.addWidget(self.btDelete)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(SideViewOptionsDialog)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.cbDrawFlightTrack = QtWidgets.QCheckBox(self.groupBox_3)
        self.cbDrawFlightTrack.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbDrawFlightTrack.sizePolicy().hasHeightForWidth())
        self.cbDrawFlightTrack.setSizePolicy(sizePolicy)
        self.cbDrawFlightTrack.setMinimumSize(QtCore.QSize(140, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(20, 19, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 19, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 19, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 19, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(173, 173, 173))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.cbDrawFlightTrack.setPalette(palette)
        self.cbDrawFlightTrack.setChecked(True)
        self.cbDrawFlightTrack.setObjectName("cbDrawFlightTrack")
        self.horizontalLayout_4.addWidget(self.cbDrawFlightTrack)
        self.btWaypointsColour = QtWidgets.QPushButton(self.groupBox_3)
        self.btWaypointsColour.setMinimumSize(QtCore.QSize(140, 0))
        self.btWaypointsColour.setObjectName("btWaypointsColour")
        self.horizontalLayout_4.addWidget(self.btWaypointsColour)
        self.btVerticesColour = QtWidgets.QPushButton(self.groupBox_3)
        self.btVerticesColour.setMinimumSize(QtCore.QSize(140, 0))
        self.btVerticesColour.setObjectName("btVerticesColour")
        self.horizontalLayout_4.addWidget(self.btVerticesColour)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.cbFillFlightTrack = QtWidgets.QCheckBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbFillFlightTrack.sizePolicy().hasHeightForWidth())
        self.cbFillFlightTrack.setSizePolicy(sizePolicy)
        self.cbFillFlightTrack.setMinimumSize(QtCore.QSize(140, 0))
        self.cbFillFlightTrack.setObjectName("cbFillFlightTrack")
        self.horizontalLayout_5.addWidget(self.cbFillFlightTrack)
        self.btFillColour = QtWidgets.QPushButton(self.groupBox_3)
        self.btFillColour.setMinimumSize(QtCore.QSize(140, 0))
        self.btFillColour.setObjectName("btFillColour")
        self.horizontalLayout_5.addWidget(self.btFillColour)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.cbLabelFlightTrack = QtWidgets.QCheckBox(self.groupBox_3)
        self.cbLabelFlightTrack.setObjectName("cbLabelFlightTrack")
        self.horizontalLayout_6.addWidget(self.cbLabelFlightTrack)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.verticalLayout_4.addWidget(self.groupBox_3)
        self.buttonBox = QtWidgets.QDialogButtonBox(SideViewOptionsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_4.addWidget(self.buttonBox)

        self.retranslateUi(SideViewOptionsDialog)
        self.buttonBox.accepted.connect(SideViewOptionsDialog.accept)
        self.buttonBox.rejected.connect(SideViewOptionsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SideViewOptionsDialog)

    def retranslateUi(self, SideViewOptionsDialog):
        _translate = QtCore.QCoreApplication.translate
        SideViewOptionsDialog.setWindowTitle(_translate("SideViewOptionsDialog", "Side View Options"))
        self.groupBox.setTitle(_translate("SideViewOptionsDialog", "Vertical Extent"))
        self.label_2.setText(_translate("SideViewOptionsDialog", "Vertical extent:"))
        self.sbPbot.setSuffix(_translate("SideViewOptionsDialog", " hPa"))
        self.label_3.setText(_translate("SideViewOptionsDialog", "to"))
        self.sbPtop.setSuffix(_translate("SideViewOptionsDialog", " hPa"))
        self.groupBox_2.setTitle(_translate("SideViewOptionsDialog", "Flight Levels"))
        self.cbDrawFlightLevels.setText(_translate("SideViewOptionsDialog", "draw the following flight levels:"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("SideViewOptionsDialog", "flight levels"))
        self.btAdd.setText(_translate("SideViewOptionsDialog", "add"))
        self.btDelete.setText(_translate("SideViewOptionsDialog", "delete selected"))
        self.groupBox_3.setTitle(_translate("SideViewOptionsDialog", "Flight Track Colours"))
        self.cbDrawFlightTrack.setText(_translate("SideViewOptionsDialog", "draw flight track"))
        self.btWaypointsColour.setText(_translate("SideViewOptionsDialog", "colour of waypoints"))
        self.btVerticesColour.setText(_translate("SideViewOptionsDialog", "colour of vertices"))
        self.cbFillFlightTrack.setText(_translate("SideViewOptionsDialog", "fill flight track"))
        self.btFillColour.setText(_translate("SideViewOptionsDialog", "colour"))
        self.cbLabelFlightTrack.setText(_translate("SideViewOptionsDialog", "label flight track"))

