# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/noplay/code/gns3/gns3-gui/gns3/modules/iou/ui/iou_device_wizard.ui'
#
# Created: Mon May  4 12:01:32 2015
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

import gns3.qt
from gns3.qt import QtCore, QtGui, QtWidgets


class Ui_IOUDeviceWizard(object):

    def setupUi(self, IOUDeviceWizard):
        IOUDeviceWizard.setObjectName("IOUDeviceWizard")
        IOUDeviceWizard.resize(585, 423)
        IOUDeviceWizard.setModal(True)
        self.uiServerWizardPage = QtWidgets.QWizardPage()
        self.uiServerWizardPage.setObjectName("uiServerWizardPage")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.uiServerWizardPage)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.uiServerTypeGroupBox = QtWidgets.QGroupBox(self.uiServerWizardPage)
        self.uiServerTypeGroupBox.setObjectName("uiServerTypeGroupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.uiServerTypeGroupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.uiRemoteRadioButton = QtWidgets.QRadioButton(self.uiServerTypeGroupBox)
        self.uiRemoteRadioButton.setChecked(True)
        self.uiRemoteRadioButton.setObjectName("uiRemoteRadioButton")
        self.horizontalLayout.addWidget(self.uiRemoteRadioButton)
        self.uiCloudRadioButton = QtWidgets.QRadioButton(self.uiServerTypeGroupBox)
        self.uiCloudRadioButton.setObjectName("uiCloudRadioButton")
        self.horizontalLayout.addWidget(self.uiCloudRadioButton)
        self.uiLocalRadioButton = QtWidgets.QRadioButton(self.uiServerTypeGroupBox)
        self.uiLocalRadioButton.setObjectName("uiLocalRadioButton")
        self.horizontalLayout.addWidget(self.uiLocalRadioButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout_2.addWidget(self.uiServerTypeGroupBox, 0, 0, 1, 1)
        self.uiRemoteServersGroupBox = QtWidgets.QGroupBox(self.uiServerWizardPage)
        self.uiRemoteServersGroupBox.setObjectName("uiRemoteServersGroupBox")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.uiRemoteServersGroupBox)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.uiLoadBalanceCheckBox = QtWidgets.QCheckBox(self.uiRemoteServersGroupBox)
        self.uiLoadBalanceCheckBox.setChecked(True)
        self.uiLoadBalanceCheckBox.setObjectName("uiLoadBalanceCheckBox")
        self.gridLayout_7.addWidget(self.uiLoadBalanceCheckBox, 0, 0, 1, 2)
        self.uiRemoteServersLabel = QtWidgets.QLabel(self.uiRemoteServersGroupBox)
        self.uiRemoteServersLabel.setObjectName("uiRemoteServersLabel")
        self.gridLayout_7.addWidget(self.uiRemoteServersLabel, 1, 0, 1, 1)
        self.uiRemoteServersComboBox = QtWidgets.QComboBox(self.uiRemoteServersGroupBox)
        self.uiRemoteServersComboBox.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiRemoteServersComboBox.sizePolicy().hasHeightForWidth())
        self.uiRemoteServersComboBox.setSizePolicy(sizePolicy)
        self.uiRemoteServersComboBox.setObjectName("uiRemoteServersComboBox")
        self.gridLayout_7.addWidget(self.uiRemoteServersComboBox, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.uiRemoteServersGroupBox, 1, 0, 1, 1)
        IOUDeviceWizard.addPage(self.uiServerWizardPage)
        self.uiNameImageWizardPage = QtWidgets.QWizardPage()
        self.uiNameImageWizardPage.setObjectName("uiNameImageWizardPage")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.uiNameImageWizardPage)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout_7 = QtWidgets.QFormLayout()
        self.formLayout_7.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_7.setObjectName("formLayout_7")
        self.uiNameLabel = QtWidgets.QLabel(self.uiNameImageWizardPage)
        self.uiNameLabel.setObjectName("uiNameLabel")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.uiNameLabel)
        self.uiNameLineEdit = QtWidgets.QLineEdit(self.uiNameImageWizardPage)
        self.uiNameLineEdit.setObjectName("uiNameLineEdit")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.uiNameLineEdit)
        self.verticalLayout_2.addLayout(self.formLayout_7)
        self.groupBox = QtWidgets.QGroupBox(self.uiNameImageWizardPage)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.uiExistingImageRadioButton = QtWidgets.QRadioButton(self.groupBox)
        self.uiExistingImageRadioButton.setChecked(True)
        self.uiExistingImageRadioButton.setObjectName("uiExistingImageRadioButton")
        self.horizontalLayout_2.addWidget(self.uiExistingImageRadioButton)
        self.uiNewImageRadioButton = QtWidgets.QRadioButton(self.groupBox)
        self.uiNewImageRadioButton.setChecked(False)
        self.uiNewImageRadioButton.setObjectName("uiNewImageRadioButton")
        self.horizontalLayout_2.addWidget(self.uiNewImageRadioButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.formLayout_8 = QtWidgets.QFormLayout()
        self.formLayout_8.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_8.setObjectName("formLayout_8")
        self.uiTypeLabel = QtWidgets.QLabel(self.groupBox)
        self.uiTypeLabel.setObjectName("uiTypeLabel")
        self.formLayout_8.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.uiTypeLabel)
        self.uiTypeComboBox = QtWidgets.QComboBox(self.groupBox)
        self.uiTypeComboBox.setObjectName("uiTypeComboBox")
        self.formLayout_8.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.uiTypeComboBox)
        self.uiIOUImageLabel = QtWidgets.QLabel(self.groupBox)
        self.uiIOUImageLabel.setObjectName("uiIOUImageLabel")
        self.formLayout_8.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.uiIOUImageLabel)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.uiIOUImageListComboBox = QtWidgets.QComboBox(self.groupBox)
        self.uiIOUImageListComboBox.setObjectName("uiIOUImageListComboBox")
        self.horizontalLayout_5.addWidget(self.uiIOUImageListComboBox)
        self.uiIOUImageLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.uiIOUImageLineEdit.setObjectName("uiIOUImageLineEdit")
        self.horizontalLayout_5.addWidget(self.uiIOUImageLineEdit)
        self.uiIOUImageToolButton = QtWidgets.QToolButton(self.groupBox)
        self.uiIOUImageToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiIOUImageToolButton.setObjectName("uiIOUImageToolButton")
        self.horizontalLayout_5.addWidget(self.uiIOUImageToolButton)
        self.formLayout_8.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_5)
        self.verticalLayout_3.addLayout(self.formLayout_8)
        self.verticalLayout_2.addWidget(self.groupBox)
        IOUDeviceWizard.addPage(self.uiNameImageWizardPage)

        self.retranslateUi(IOUDeviceWizard)
        QtCore.QMetaObject.connectSlotsByName(IOUDeviceWizard)

    def retranslateUi(self, IOUDeviceWizard):
        _translate = gns3.qt.translate
        IOUDeviceWizard.setWindowTitle(_translate("IOUDeviceWizard", "New IOU device template"))
        self.uiServerWizardPage.setTitle(_translate("IOUDeviceWizard", "Server"))
        self.uiServerWizardPage.setSubTitle(_translate("IOUDeviceWizard", "Please choose a server type to run your new IOU device."))
        self.uiServerTypeGroupBox.setTitle(_translate("IOUDeviceWizard", "Server type"))
        self.uiRemoteRadioButton.setText(_translate("IOUDeviceWizard", "Remote"))
        self.uiCloudRadioButton.setText(_translate("IOUDeviceWizard", "Cloud"))
        self.uiLocalRadioButton.setText(_translate("IOUDeviceWizard", "Local"))
        self.uiRemoteServersGroupBox.setTitle(_translate("IOUDeviceWizard", "Remote servers"))
        self.uiLoadBalanceCheckBox.setText(_translate("IOUDeviceWizard", "Load balance across all available remote servers"))
        self.uiRemoteServersLabel.setText(_translate("IOUDeviceWizard", "Run on server:"))
        self.uiNameImageWizardPage.setTitle(_translate("IOUDeviceWizard", "Name and image"))
        self.uiNameImageWizardPage.setSubTitle(_translate("IOUDeviceWizard", "Please choose a descriptive name for the new IOU device and add an IOU image."))
        self.uiNameLabel.setText(_translate("IOUDeviceWizard", "Name:"))
        self.groupBox.setTitle(_translate("IOUDeviceWizard", "Image"))
        self.uiExistingImageRadioButton.setText(_translate("IOUDeviceWizard", "Existing image"))
        self.uiNewImageRadioButton.setText(_translate("IOUDeviceWizard", "New Image"))
        self.uiTypeLabel.setText(_translate("IOUDeviceWizard", "Type:"))
        self.uiIOUImageLabel.setText(_translate("IOUDeviceWizard", "IOU image:"))
        self.uiIOUImageToolButton.setText(_translate("IOUDeviceWizard", "&Browse..."))
