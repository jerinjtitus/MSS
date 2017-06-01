# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_hexagon_dockwidget.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HexagonDockWidget(object):
    def setupUi(self, HexagonDockWidget):
        HexagonDockWidget.setObjectName("HexagonDockWidget")
        HexagonDockWidget.resize(638, 114)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(HexagonDockWidget.sizePolicy().hasHeightForWidth())
        HexagonDockWidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(HexagonDockWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(HexagonDockWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.dsbHexagonLatitude = QtWidgets.QDoubleSpinBox(HexagonDockWidget)
        self.dsbHexagonLatitude.setMinimumSize(QtCore.QSize(0, 0))
        self.dsbHexagonLatitude.setPrefix("")
        self.dsbHexagonLatitude.setMinimum(-90.0)
        self.dsbHexagonLatitude.setMaximum(90.0)
        self.dsbHexagonLatitude.setObjectName("dsbHexagonLatitude")
        self.horizontalLayout_5.addWidget(self.dsbHexagonLatitude)
        self.label_2 = QtWidgets.QLabel(HexagonDockWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.dsbHexagonLongitude = QtWidgets.QDoubleSpinBox(HexagonDockWidget)
        self.dsbHexagonLongitude.setMinimum(-180.0)
        self.dsbHexagonLongitude.setMaximum(360.0)
        self.dsbHexagonLongitude.setObjectName("dsbHexagonLongitude")
        self.horizontalLayout_5.addWidget(self.dsbHexagonLongitude)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(HexagonDockWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.dsbHexgaonRadius = QtWidgets.QDoubleSpinBox(HexagonDockWidget)
        self.dsbHexgaonRadius.setMinimum(10.0)
        self.dsbHexgaonRadius.setMaximum(9999.99)
        self.dsbHexgaonRadius.setSingleStep(10.0)
        self.dsbHexgaonRadius.setProperty("value", 200.0)
        self.dsbHexgaonRadius.setObjectName("dsbHexgaonRadius")
        self.horizontalLayout_2.addWidget(self.dsbHexgaonRadius)
        self.label_4 = QtWidgets.QLabel(HexagonDockWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.dsbHexagonAngle = QtWidgets.QDoubleSpinBox(HexagonDockWidget)
        self.dsbHexagonAngle.setMinimum(-360.0)
        self.dsbHexagonAngle.setMaximum(360.0)
        self.dsbHexagonAngle.setObjectName("dsbHexagonAngle")
        self.horizontalLayout_2.addWidget(self.dsbHexagonAngle)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pbAddHexagon = QtWidgets.QPushButton(HexagonDockWidget)
        self.pbAddHexagon.setObjectName("pbAddHexagon")
        self.horizontalLayout_6.addWidget(self.pbAddHexagon)
        self.pbRemoveHexagon = QtWidgets.QPushButton(HexagonDockWidget)
        self.pbRemoveHexagon.setObjectName("pbRemoveHexagon")
        self.horizontalLayout_6.addWidget(self.pbRemoveHexagon)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.retranslateUi(HexagonDockWidget)
        QtCore.QMetaObject.connectSlotsByName(HexagonDockWidget)

    def retranslateUi(self, HexagonDockWidget):
        _translate = QtCore.QCoreApplication.translate
        HexagonDockWidget.setWindowTitle(_translate("HexagonDockWidget", "Remote Sensing"))
        self.label.setText(_translate("HexagonDockWidget", "Center latitude"))
        self.dsbHexagonLatitude.setSuffix(_translate("HexagonDockWidget", " °N"))
        self.label_2.setText(_translate("HexagonDockWidget", "Center longitude"))
        self.dsbHexagonLongitude.setSuffix(_translate("HexagonDockWidget", " °E"))
        self.label_3.setText(_translate("HexagonDockWidget", "Radius"))
        self.dsbHexgaonRadius.setSuffix(_translate("HexagonDockWidget", " km"))
        self.label_4.setText(_translate("HexagonDockWidget", "Angle of first point"))
        self.dsbHexagonAngle.setSuffix(_translate("HexagonDockWidget", " °"))
        self.pbAddHexagon.setText(_translate("HexagonDockWidget", "Add Hexagon"))
        self.pbRemoveHexagon.setText(_translate("HexagonDockWidget", "Remove Hexagon"))

