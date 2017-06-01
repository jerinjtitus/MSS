# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_topview_mapappearance.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MapAppearanceDialog(object):
    def setupUi(self, MapAppearanceDialog):
        MapAppearanceDialog.setObjectName("MapAppearanceDialog")
        MapAppearanceDialog.resize(465, 265)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MapAppearanceDialog.sizePolicy().hasHeightForWidth())
        MapAppearanceDialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(MapAppearanceDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cbDrawGraticule = QtWidgets.QCheckBox(MapAppearanceDialog)
        self.cbDrawGraticule.setObjectName("cbDrawGraticule")
        self.verticalLayout.addWidget(self.cbDrawGraticule)
        self.cbDrawCoastlines = QtWidgets.QCheckBox(MapAppearanceDialog)
        self.cbDrawCoastlines.setChecked(True)
        self.cbDrawCoastlines.setObjectName("cbDrawCoastlines")
        self.verticalLayout.addWidget(self.cbDrawCoastlines)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cbFillWaterBodies = QtWidgets.QCheckBox(MapAppearanceDialog)
        self.cbFillWaterBodies.setEnabled(False)
        self.cbFillWaterBodies.setMinimumSize(QtCore.QSize(145, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(20, 19, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 19, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 19, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 19, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 19, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 19, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(173, 173, 173))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.cbFillWaterBodies.setPalette(palette)
        self.cbFillWaterBodies.setChecked(True)
        self.cbFillWaterBodies.setObjectName("cbFillWaterBodies")
        self.horizontalLayout.addWidget(self.cbFillWaterBodies)
        self.btWaterColour = QtWidgets.QPushButton(MapAppearanceDialog)
        self.btWaterColour.setMinimumSize(QtCore.QSize(135, 0))
        self.btWaterColour.setFlat(False)
        self.btWaterColour.setObjectName("btWaterColour")
        self.horizontalLayout.addWidget(self.btWaterColour)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cbFillContinents = QtWidgets.QCheckBox(MapAppearanceDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbFillContinents.sizePolicy().hasHeightForWidth())
        self.cbFillContinents.setSizePolicy(sizePolicy)
        self.cbFillContinents.setMinimumSize(QtCore.QSize(145, 0))
        self.cbFillContinents.setObjectName("cbFillContinents")
        self.horizontalLayout_2.addWidget(self.cbFillContinents)
        self.btLandColour = QtWidgets.QPushButton(MapAppearanceDialog)
        self.btLandColour.setMinimumSize(QtCore.QSize(135, 0))
        self.btLandColour.setObjectName("btLandColour")
        self.horizontalLayout_2.addWidget(self.btLandColour)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cbDrawFlightTrack = QtWidgets.QCheckBox(MapAppearanceDialog)
        self.cbDrawFlightTrack.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbDrawFlightTrack.sizePolicy().hasHeightForWidth())
        self.cbDrawFlightTrack.setSizePolicy(sizePolicy)
        self.cbDrawFlightTrack.setMinimumSize(QtCore.QSize(145, 0))
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
        self.horizontalLayout_3.addWidget(self.cbDrawFlightTrack)
        self.btWaypointsColour = QtWidgets.QPushButton(MapAppearanceDialog)
        self.btWaypointsColour.setMinimumSize(QtCore.QSize(135, 0))
        self.btWaypointsColour.setObjectName("btWaypointsColour")
        self.horizontalLayout_3.addWidget(self.btWaypointsColour)
        self.btVerticesColour = QtWidgets.QPushButton(MapAppearanceDialog)
        self.btVerticesColour.setMinimumSize(QtCore.QSize(135, 0))
        self.btVerticesColour.setObjectName("btVerticesColour")
        self.horizontalLayout_3.addWidget(self.btVerticesColour)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.cbLabelFlightTrack = QtWidgets.QCheckBox(MapAppearanceDialog)
        self.cbLabelFlightTrack.setObjectName("cbLabelFlightTrack")
        self.horizontalLayout_4.addWidget(self.cbLabelFlightTrack)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.buttonBox = QtWidgets.QDialogButtonBox(MapAppearanceDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(MapAppearanceDialog)
        self.buttonBox.accepted.connect(MapAppearanceDialog.accept)
        self.buttonBox.rejected.connect(MapAppearanceDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(MapAppearanceDialog)

    def retranslateUi(self, MapAppearanceDialog):
        _translate = QtCore.QCoreApplication.translate
        MapAppearanceDialog.setWindowTitle(_translate("MapAppearanceDialog", "Top View Map Appearance"))
        self.cbDrawGraticule.setText(_translate("MapAppearanceDialog", "draw graticule"))
        self.cbDrawCoastlines.setText(_translate("MapAppearanceDialog", "draw coastlines"))
        self.cbFillWaterBodies.setText(_translate("MapAppearanceDialog", "fill map background"))
        self.btWaterColour.setText(_translate("MapAppearanceDialog", "colour"))
        self.cbFillContinents.setText(_translate("MapAppearanceDialog", "fill continents"))
        self.btLandColour.setText(_translate("MapAppearanceDialog", "colour"))
        self.cbDrawFlightTrack.setText(_translate("MapAppearanceDialog", "draw flight track"))
        self.btWaypointsColour.setText(_translate("MapAppearanceDialog", "colour of waypoints"))
        self.btVerticesColour.setText(_translate("MapAppearanceDialog", "colour of vertices"))
        self.cbLabelFlightTrack.setText(_translate("MapAppearanceDialog", "label flight track"))

