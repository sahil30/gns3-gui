# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/noplay/code/gns3/gns3-gui/gns3/modules/vmware/ui/vmware_vm_configuration_page.ui'
#
# Created: Mon May  4 12:01:33 2015
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

import gns3.qt
from gns3.qt import QtCore, QtGui, QtWidgets


class Ui_VMwareVMConfigPageWidget(object):

    def setupUi(self, VMwareVMConfigPageWidget):
        VMwareVMConfigPageWidget.setObjectName("VMwareVMConfigPageWidget")
        VMwareVMConfigPageWidget.resize(509, 346)
        self.verticalLayout = QtWidgets.QVBoxLayout(VMwareVMConfigPageWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.uiTabWidget = QtWidgets.QTabWidget(VMwareVMConfigPageWidget)
        self.uiTabWidget.setObjectName("uiTabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.uiNameLabel = QtWidgets.QLabel(self.tab)
        self.uiNameLabel.setObjectName("uiNameLabel")
        self.gridLayout.addWidget(self.uiNameLabel, 0, 0, 1, 1)
        self.uiNameLineEdit = QtWidgets.QLineEdit(self.tab)
        self.uiNameLineEdit.setObjectName("uiNameLineEdit")
        self.gridLayout.addWidget(self.uiNameLineEdit, 0, 1, 1, 1)
        self.uiConsolePortLabel = QtWidgets.QLabel(self.tab)
        self.uiConsolePortLabel.setObjectName("uiConsolePortLabel")
        self.gridLayout.addWidget(self.uiConsolePortLabel, 1, 0, 1, 1)
        self.uiConsolePortSpinBox = QtWidgets.QSpinBox(self.tab)
        self.uiConsolePortSpinBox.setMaximum(65535)
        self.uiConsolePortSpinBox.setObjectName("uiConsolePortSpinBox")
        self.gridLayout.addWidget(self.uiConsolePortSpinBox, 1, 1, 1, 1)
        self.uiEnableConsoleCheckBox = QtWidgets.QCheckBox(self.tab)
        self.uiEnableConsoleCheckBox.setObjectName("uiEnableConsoleCheckBox")
        self.gridLayout.addWidget(self.uiEnableConsoleCheckBox, 2, 0, 1, 2)
        self.uiHeadlessModeCheckBox = QtWidgets.QCheckBox(self.tab)
        self.uiHeadlessModeCheckBox.setChecked(False)
        self.uiHeadlessModeCheckBox.setObjectName("uiHeadlessModeCheckBox")
        self.gridLayout.addWidget(self.uiHeadlessModeCheckBox, 3, 0, 1, 2)
        self.uiBaseVMCheckBox = QtWidgets.QCheckBox(self.tab)
        self.uiBaseVMCheckBox.setEnabled(True)
        self.uiBaseVMCheckBox.setObjectName("uiBaseVMCheckBox")
        self.gridLayout.addWidget(self.uiBaseVMCheckBox, 4, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 138, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 1, 1, 1)
        self.uiTabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.uiAdaptersLabel = QtWidgets.QLabel(self.tab_2)
        self.uiAdaptersLabel.setObjectName("uiAdaptersLabel")
        self.gridLayout_3.addWidget(self.uiAdaptersLabel, 0, 0, 1, 1)
        self.uiAdaptersSpinBox = QtWidgets.QSpinBox(self.tab_2)
        self.uiAdaptersSpinBox.setMinimum(1)
        self.uiAdaptersSpinBox.setMaximum(36)
        self.uiAdaptersSpinBox.setObjectName("uiAdaptersSpinBox")
        self.gridLayout_3.addWidget(self.uiAdaptersSpinBox, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(248, 178, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 2, 0, 1, 2)
        self.uiAdapterTypesComboBox = QtWidgets.QComboBox(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiAdapterTypesComboBox.sizePolicy().hasHeightForWidth())
        self.uiAdapterTypesComboBox.setSizePolicy(sizePolicy)
        self.uiAdapterTypesComboBox.setObjectName("uiAdapterTypesComboBox")
        self.gridLayout_3.addWidget(self.uiAdapterTypesComboBox, 1, 1, 1, 1)
        self.uiTabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.uiTabWidget)

        self.retranslateUi(VMwareVMConfigPageWidget)
        self.uiTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(VMwareVMConfigPageWidget)

    def retranslateUi(self, VMwareVMConfigPageWidget):
        _translate = gns3.qt.translate
        VMwareVMConfigPageWidget.setWindowTitle(_translate("VMwareVMConfigPageWidget", "VMware VM configuration"))
        self.uiNameLabel.setText(_translate("VMwareVMConfigPageWidget", "Name:"))
        self.uiConsolePortLabel.setText(_translate("VMwareVMConfigPageWidget", "Console port:"))
        self.uiEnableConsoleCheckBox.setText(_translate("VMwareVMConfigPageWidget", "Enable remote console"))
        self.uiHeadlessModeCheckBox.setText(_translate("VMwareVMConfigPageWidget", "Start VM in headless mode"))
        self.uiBaseVMCheckBox.setText(_translate("VMwareVMConfigPageWidget", "Use as a linked base VM (experimental)"))
        self.uiTabWidget.setTabText(self.uiTabWidget.indexOf(self.tab), _translate("VMwareVMConfigPageWidget", "General settings"))
        self.uiAdaptersLabel.setText(_translate("VMwareVMConfigPageWidget", "Adapters:"))
        self.label.setText(_translate("VMwareVMConfigPageWidget", "Type:"))
        self.uiTabWidget.setTabText(self.uiTabWidget.indexOf(self.tab_2), _translate("VMwareVMConfigPageWidget", "Network"))
