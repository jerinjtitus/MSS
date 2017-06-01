# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_topview_mapappearance.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!


from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MapAppearanceDialog(object):
    def setupUi(self, MapAppearanceDialog):
        MapAppearanceDialog.setObjectName(_fromUtf8("MapAppearanceDialog"))
        MapAppearanceDialog.resize(465, 265)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MapAppearanceDialog.sizePolicy().hasHeightForWidth())
        MapAppearanceDialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(MapAppearanceDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.cbDrawGraticule = QtGui.QCheckBox(MapAppearanceDialog)
        self.cbDrawGraticule.setObjectName(_fromUtf8("cbDrawGraticule"))
        self.verticalLayout.addWidget(self.cbDrawGraticule)
        self.cbDrawCoastlines = QtGui.QCheckBox(MapAppearanceDialog)
        self.cbDrawCoastlines.setChecked(True)
        self.cbDrawCoastlines.setObjectName(_fromUtf8("cbDrawCoastlines"))
        self.verticalLayout.addWidget(self.cbDrawCoastlines)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.cbFillWaterBodies = QtGui.QCheckBox(MapAppearanceDialog)
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
        self.cbFillWaterBodies.setObjectName(_fromUtf8("cbFillWaterBodies"))
        self.horizontalLayout.addWidget(self.cbFillWaterBodies)
        self.btWaterColour = QtGui.QPushButton(MapAppearanceDialog)
        self.btWaterColour.setMinimumSize(QtCore.QSize(135, 0))
        self.btWaterColour.setFlat(False)
        self.btWaterColour.setObjectName(_fromUtf8("btWaterColour"))
        self.horizontalLayout.addWidget(self.btWaterColour)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.cbFillContinents = QtGui.QCheckBox(MapAppearanceDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbFillContinents.sizePolicy().hasHeightForWidth())
        self.cbFillContinents.setSizePolicy(sizePolicy)
        self.cbFillContinents.setMinimumSize(QtCore.QSize(145, 0))
        self.cbFillContinents.setObjectName(_fromUtf8("cbFillContinents"))
        self.horizontalLayout_2.addWidget(self.cbFillContinents)
        self.btLandColour = QtGui.QPushButton(MapAppearanceDialog)
        self.btLandColour.setMinimumSize(QtCore.QSize(135, 0))
        self.btLandColour.setObjectName(_fromUtf8("btLandColour"))
        self.horizontalLayout_2.addWidget(self.btLandColour)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.cbDrawFlightTrack = QtGui.QCheckBox(MapAppearanceDialog)
        self.cbDrawFlightTrack.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
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
        self.cbDrawFlightTrack.setObjectName(_fromUtf8("cbDrawFlightTrack"))
        self.horizontalLayout_3.addWidget(self.cbDrawFlightTrack)
        self.btWaypointsColour = QtGui.QPushButton(MapAppearanceDialog)
        self.btWaypointsColour.setMinimumSize(QtCore.QSize(135, 0))
        self.btWaypointsColour.setObjectName(_fromUtf8("btWaypointsColour"))
        self.horizontalLayout_3.addWidget(self.btWaypointsColour)
        self.btVerticesColour = QtGui.QPushButton(MapAppearanceDialog)
        self.btVerticesColour.setMinimumSize(QtCore.QSize(135, 0))
        self.btVerticesColour.setObjectName(_fromUtf8("btVerticesColour"))
        self.horizontalLayout_3.addWidget(self.btVerticesColour)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.cbLabelFlightTrack = QtGui.QCheckBox(MapAppearanceDialog)
        self.cbLabelFlightTrack.setObjectName(_fromUtf8("cbLabelFlightTrack"))
        self.horizontalLayout_4.addWidget(self.cbLabelFlightTrack)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.buttonBox = QtGui.QDialogButtonBox(MapAppearanceDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(MapAppearanceDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), MapAppearanceDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), MapAppearanceDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(MapAppearanceDialog)

    def retranslateUi(self, MapAppearanceDialog):
        MapAppearanceDialog.setWindowTitle(_translate("MapAppearanceDialog", "Top View Map Appearance", None))
        self.cbDrawGraticule.setText(_translate("MapAppearanceDialog", "draw graticule", None))
        self.cbDrawCoastlines.setText(_translate("MapAppearanceDialog", "draw coastlines", None))
        self.cbFillWaterBodies.setText(_translate("MapAppearanceDialog", "fill map background", None))
        self.btWaterColour.setText(_translate("MapAppearanceDialog", "colour", None))
        self.cbFillContinents.setText(_translate("MapAppearanceDialog", "fill continents", None))
        self.btLandColour.setText(_translate("MapAppearanceDialog", "colour", None))
        self.cbDrawFlightTrack.setText(_translate("MapAppearanceDialog", "draw flight track", None))
        self.btWaypointsColour.setText(_translate("MapAppearanceDialog", "colour of waypoints", None))
        self.btVerticesColour.setText(_translate("MapAppearanceDialog", "colour of vertices", None))
        self.cbLabelFlightTrack.setText(_translate("MapAppearanceDialog", "label flight track", None))

