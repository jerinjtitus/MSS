# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'msui/ui_performance_settings.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PerformanceSettingsDialog(object):
    def setupUi(self, PerformanceSettingsDialog):
        PerformanceSettingsDialog.setObjectName("PerformanceSettingsDialog")
        PerformanceSettingsDialog.resize(319, 241)
        self.buttonBox = QtWidgets.QDialogButtonBox(PerformanceSettingsDialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 200, 271, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.dteTakeoffTime = QtWidgets.QDateTimeEdit(PerformanceSettingsDialog)
        self.dteTakeoffTime.setGeometry(QtCore.QRect(160, 100, 141, 22))
        self.dteTakeoffTime.setObjectName("dteTakeoffTime")
        self.label = QtWidgets.QLabel(PerformanceSettingsDialog)
        self.label.setGeometry(QtCore.QRect(20, 100, 91, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.dsbTakeoffWeight = QtWidgets.QDoubleSpinBox(PerformanceSettingsDialog)
        self.dsbTakeoffWeight.setGeometry(QtCore.QRect(160, 130, 141, 22))
        self.dsbTakeoffWeight.setDecimals(0)
        self.dsbTakeoffWeight.setMaximum(9999999.0)
        self.dsbTakeoffWeight.setSingleStep(1000.0)
        self.dsbTakeoffWeight.setObjectName("dsbTakeoffWeight")
        self.dsbFuel = QtWidgets.QDoubleSpinBox(PerformanceSettingsDialog)
        self.dsbFuel.setGeometry(QtCore.QRect(160, 160, 141, 22))
        self.dsbFuel.setDecimals(0)
        self.dsbFuel.setMaximum(9999999.0)
        self.dsbFuel.setSingleStep(1000.0)
        self.dsbFuel.setObjectName("dsbFuel")
        self.label_2 = QtWidgets.QLabel(PerformanceSettingsDialog)
        self.label_2.setGeometry(QtCore.QRect(20, 130, 121, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(PerformanceSettingsDialog)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 101, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.cbShowPerformance = QtWidgets.QCheckBox(PerformanceSettingsDialog)
        self.cbShowPerformance.setGeometry(QtCore.QRect(20, 20, 141, 20))
        self.cbShowPerformance.setObjectName("cbShowPerformance")
        self.pbLoadPerformance = QtWidgets.QPushButton(PerformanceSettingsDialog)
        self.pbLoadPerformance.setGeometry(QtCore.QRect(210, 50, 93, 28))
        self.pbLoadPerformance.setObjectName("pbLoadPerformance")
        self.lbAircraftName = QtWidgets.QLabel(PerformanceSettingsDialog)
        self.lbAircraftName.setGeometry(QtCore.QRect(80, 60, 121, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lbAircraftName.setFont(font)
        self.lbAircraftName.setObjectName("lbAircraftName")
        self.label_5 = QtWidgets.QLabel(PerformanceSettingsDialog)
        self.label_5.setGeometry(QtCore.QRect(20, 60, 51, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(PerformanceSettingsDialog)
        self.buttonBox.accepted.connect(PerformanceSettingsDialog.accept)
        self.buttonBox.rejected.connect(PerformanceSettingsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(PerformanceSettingsDialog)

    def retranslateUi(self, PerformanceSettingsDialog):
        _translate = QtCore.QCoreApplication.translate
        PerformanceSettingsDialog.setWindowTitle(_translate("PerformanceSettingsDialog", "PerformanceSettingsDialog"))
        self.label.setText(_translate("PerformanceSettingsDialog", "Take off time"))
        self.label_2.setText(_translate("PerformanceSettingsDialog", "Takeoff weight (lb)"))
        self.label_3.setText(_translate("PerformanceSettingsDialog", "Fuel (lb)"))
        self.cbShowPerformance.setText(_translate("PerformanceSettingsDialog", "Show Performance"))
        self.pbLoadPerformance.setText(_translate("PerformanceSettingsDialog", "Load"))
        self.lbAircraftName.setText(_translate("PerformanceSettingsDialog", "Dummy"))
        self.label_5.setText(_translate("PerformanceSettingsDialog", "Aircraft:"))

