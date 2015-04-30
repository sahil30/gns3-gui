# -*- coding: utf-8 -*-
#
# Copyright (C) 2014 GNS3 Technologies Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Wizard for QEMU VMs.
"""

import sys

from gns3.qt import QtCore, QtGui, QtWidgets
from gns3.node import Node
from gns3.modules.module_error import ModuleError
from gns3.dialogs.vm_wizard import VMWizard

from .. import Qemu
from ..ui.qemu_vm_wizard_ui import Ui_QemuVMWizard
from ..pages.qemu_vm_configuration_page import QemuVMConfigurationPage


class QemuVMWizard(VMWizard, Ui_QemuVMWizard):

    """
    Wizard to create a Qemu VM.

    :param parent: parent widget
    """

    def __init__(self, qemu_vms, parent):

        super().__init__(parent)

        self.setPixmap(QtWidgets.QWizard.LogoPixmap, QtGui.QPixmap(":/icons/qemu.svg"))

        self.uiTypeComboBox.currentIndexChanged[str].connect(self._typeChangedSlot)

        # Available types
        self.uiTypeComboBox.addItems(["Default", "IOSv", "IOSv-L2", "ASA 8.4(2)", "IDS"])

        # Mandatory fields
        self.uiNameWizardPage.registerField("vm_name*", self.uiNameLineEdit)
        self.uiDiskWizardPage.registerField("hda_disk_image*", self.uiHdaDiskImageLineEdit)
        self.uiDiskImageHdbWizardPage.registerField("hdb_disk_image*", self.uiHdbDiskImageLineEdit)
        self.uiASAWizardPage.registerField("initrd*", self.uiInitrdImageLineEdit)
        self.uiASAWizardPage.registerField("kernel_image*", self.uiKernelImageLineEdit)

        self._qemu_vms = qemu_vms

        # Fill image combo boxes
        self.addImageSelector(self.uiHdaDiskExistingImageRadioButton, self.uiHdaDiskImageListComboBox, self.uiHdaDiskImageLineEdit, self.uiHdaDiskImageToolButton, QemuVMConfigurationPage.getDiskImage)
        self.addImageSelector(self.uiHdbDiskExistingImageRadioButton, self.uiHdbDiskImageListComboBox, self.uiHdbDiskImageLineEdit, self.uiHdbDiskImageToolButton, QemuVMConfigurationPage.getDiskImage)
        self.addImageSelector(self.uiLinuxExistingImageRadioButton, self.uiInitrdImageListComboBox, self.uiInitrdImageLineEdit, self.uiInitrdImageToolButton, QemuVMConfigurationPage.getDiskImage)
        self.addImageSelector(self.uiLinuxExistingImageRadioButton, self.uiKernelImageListComboBox, self.uiKernelImageLineEdit, self.uiKernelImageToolButton, QemuVMConfigurationPage.getDiskImage)

        if Qemu.instance().settings()["use_local_server"]:
            # skip the server page if we use the local server
            self.setStartId(1)

    def _typeChangedSlot(self, vm_type):
        """
        When the type of QEMU VM is changed.

        :param vm_type: type of VM
        """

        if vm_type == "IOSv":
            self.setPixmap(QtWidgets.QWizard.LogoPixmap, QtGui.QPixmap(":/symbols/iosv_virl.normal.svg"))
            self.uiNameLineEdit.setText("vIOS")
            self.uiHdaDiskImageLabel.setText("IOSv VDMK file:")
        elif vm_type == "IOSv-L2":
            self.setPixmap(QtWidgets.QWizard.LogoPixmap, QtGui.QPixmap(":/symbols/iosv_l2_virl.normal.svg"))
            self.uiNameLineEdit.setText("vIOS-L2")
            self.uiHdaDiskImageLabel.setText("IOSv-L2 VDMK file:")
        elif vm_type == "ASA 8.4(2)":
            self.setPixmap(QtWidgets.QWizard.LogoPixmap, QtGui.QPixmap(":/symbols/asa.normal.svg"))
            self.uiNameLineEdit.setText("ASA")
        elif vm_type == "IDS":
            self.setPixmap(QtWidgets.QWizard.LogoPixmap, QtGui.QPixmap(":/symbols/ids.normal.svg"))
            self.uiNameLineEdit.setText("IDS")
            self.uiHdaDiskImageLabel.setText("Disk image (hda):")
        else:
            self.setPixmap(QtWidgets.QWizard.LogoPixmap, QtGui.QPixmap(":/icons/qemu.svg"))
            self.uiHdaDiskImageLabel.setText("Disk image (hda):")
            self.uiNameLineEdit.setText("")

    def validateCurrentPage(self):
        """
        Validates the server.
        """

        if super().validateCurrentPage() is False:
            return False

        if self.currentPage() == self.uiNameWizardPage:
            name = self.uiNameLineEdit.text()
            for qemu_vm in self._qemu_vms.values():
                if qemu_vm["name"] == name:
                    QtWidgets.QMessageBox.critical(self, "Name", "{} is already used, please choose another name".format(name))
                    return False

        if self.currentPage() == self.uiBinaryMemoryWizardPage:
            if not self.uiQemuListComboBox.count():
                QtWidgets.QMessageBox.critical(self, "QEMU binaries", "Sorry, no QEMU binary has been found. Please make sure QEMU is installed before continuing")
                return False

        return True

    def initializePage(self, page_id):

        super().initializePage(page_id)

        if self.page(page_id) in [self.uiDiskWizardPage, self.uiASAWizardPage, self.uiDiskImageHdbWizardPage]:
            self.loadImagesList("/qemu/vms")
        if self.page(page_id) == self.uiBinaryMemoryWizardPage:
            try:
                Qemu.instance().getQemuBinariesFromServer(self._server, self._getQemuBinariesFromServerCallback)
            except ModuleError as e:
                QtWidgets.QMessageBox.critical(self, "Qemu binaries", "Error while getting the QEMU binaries: {}".format(e))

    def _getQemuBinariesFromServerCallback(self, result, error=False, **kwargs):
        """
        Callback for getQemuBinariesFromServer.

        :param result: server response
        :param error: indicates an error (boolean)
        """

        if error:
            QtWidgets.QMessageBox.critical(self, "Qemu binaries", "{}".format(result["message"]))
        else:
            self.uiQemuListComboBox.clear()
            for qemu in result:
                if qemu["version"]:
                    self.uiQemuListComboBox.addItem("{path} (v{version})".format(path=qemu["path"], version=qemu["version"]), qemu["path"])
                else:
                    self.uiQemuListComboBox.addItem("{path}".format(path=qemu["path"]), qemu["path"])

            is_64bit = sys.maxsize > 2 ** 32
            if sys.platform.startswith("win"):
                if self.uiTypeComboBox.currentText() != "Default" and (Qemu.instance().settings()["use_local_server"] or self.uiLocalRadioButton.isChecked()):
                    search_string = r"qemu-0.13.0\qemu-system-i386w.exe"
                elif is_64bit:
                    # default is qemu-system-x86_64w.exe on Windows 64-bit with a remote server
                    search_string = "x86_64w.exe"
                else:
                    # default is qemu-system-i386w.exe on Windows 32-bit with a remote server
                    search_string = "i386w.exe"
            elif sys.platform.startswith("darwin") and hasattr(sys, "frozen") and (Qemu.instance().settings()["use_local_server"] or self.uiLocalRadioButton.isChecked()):
                search_string = "GNS3.app/Contents/Resources/qemu/bin/qemu-system-x86_64"
            elif is_64bit:
                # default is qemu-system-x86_64 on other 64-bit platforms
                search_string = "x86_64"
            else:
                # default is qemu-system-i386 on other platforms
                search_string = "i386"

            index = self.uiQemuListComboBox.findData(search_string, flags=QtCore.Qt.MatchEndsWith)
            if index != -1:
                self.uiQemuListComboBox.setCurrentIndex(index)

    def getSettings(self):
        """
        Returns the settings set in this Wizard.

        :return: settings dict
        """

        if Qemu.instance().settings()["use_local_server"] or self.uiLocalRadioButton.isChecked():
            server = "local"
        elif self.uiRemoteRadioButton.isChecked():
            server = self.uiRemoteServersComboBox.currentText()
        else:  # Cloud is selected
            server = "cloud"

        qemu_path = self.uiQemuListComboBox.itemData(self.uiQemuListComboBox.currentIndex())
        settings = {
            "name": self.uiNameLineEdit.text(),
            "ram": self.uiRamSpinBox.value(),
            "qemu_path": qemu_path,
            "server": server,
        }

        if self.uiTypeComboBox.currentText() == "IOSv":
            settings["adapters"] = 8
            settings["hda_disk_image"] = self.uiHdaDiskImageLineEdit.text()
            settings["default_symbol"] = ":/symbols/iosv_virl.normal.svg"
            settings["hover_symbol"] = ":/symbols/iosv_virl.selected.svg"
            settings["category"] = Node.routers
        elif self.uiTypeComboBox.currentText() == "IOSv-L2":
            settings["adapters"] = 8
            settings["hda_disk_image"] = self.uiHdaDiskImageLineEdit.text()
            settings["default_symbol"] = ":/symbols/iosv_l2_virl.normal.svg"
            settings["hover_symbol"] = ":/symbols/iosv_l2_virl.selected.svg"
            settings["category"] = Node.switches
        elif self.uiTypeComboBox.currentText() == "ASA 8.4(2)":
            settings["adapters"] = 4
            settings["initrd"] = self.uiInitrdImageLineEdit.text()
            settings["kernel_image"] = self.uiKernelImageLineEdit.text()
            settings["kernel_command_line"] = "ide_generic.probe_mask=0x01 ide_core.chs=0.0:980,16,32 auto nousb console=ttyS0,9600 bigphysarea=65536 ide1=noprobe no-hlt"
            settings["options"] = "-icount auto -hdachs 980,16,32"
            if not sys.platform.startswith("darwin"):
                settings["cpu_throttling"] = 80  # limit to 80% CPU usage
            settings["process_priority"] = "low"
            settings["default_symbol"] = ":/symbols/asa.normal.svg"
            settings["hover_symbol"] = ":/symbols/asa.selected.svg"
            settings["category"] = Node.security_devices
        elif self.uiTypeComboBox.currentText() == "IDS":
            settings["adapters"] = 3
            settings["hda_disk_image"] = self.uiHdaDiskImageLineEdit.text()
            settings["hdb_disk_image"] = self.uiHdbDiskImageLineEdit.text()
            settings["options"] = "-smbios type=1,product=IDS-4215"
            settings["default_symbol"] = ":/symbols/ids.normal.svg"
            settings["hover_symbol"] = ":/symbols/ids.selected.svg"
            settings["category"] = Node.security_devices
        else:
            settings["hda_disk_image"] = self.uiHdaDiskImageLineEdit.text()
            settings["category"] = Node.end_devices

        if "options" not in settings:
            settings["options"] = ""
        if server == "local" and (sys.platform.startswith("win") and qemu_path.endswith(r"qemu-0.13.0\qemu-system-i386w.exe")) or \
                (sys.platform.startswith("darwin") and "GNS3.app" in qemu_path):
            settings["options"] += " -vga none -vnc none"
            settings["legacy_networking"] = True
        else:
            settings["options"] += " -nographic"
        settings["options"] = settings["options"].strip()

        return settings

    def nextId(self):
        """
        Wizard rules!
        """

        current_id = self.currentId()
        if self.page(current_id) == self.uiTypeWizardPage:

            if self.uiTypeComboBox.currentText().startswith("IOSv"):
                self.uiRamSpinBox.setValue(384)
            elif self.uiTypeComboBox.currentText() != "Default":
                self.uiRamSpinBox.setValue(1024)

        elif self.page(current_id) == self.uiBinaryMemoryWizardPage:

            if self.uiTypeComboBox.currentText() == "ASA 8.4(2)":
                return self.uiBinaryMemoryWizardPage.nextId() + 1

        elif self.page(current_id) == self.uiDiskWizardPage:

            if self.uiTypeComboBox.currentText() == "IDS":
                return self.uiDiskWizardPage.nextId() + 1
            return -1

        elif self.page(current_id) == self.uiASAWizardPage:
            return -1

        return QtWidgets.QWizard.nextId(self)
