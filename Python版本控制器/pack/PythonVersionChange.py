# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Python版本控制器.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

import sys, os, win32api, win32con, _winreg

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

class Ui_python_version_change(object):
    def setupUi(self, python_version_change):
        python_version_change.setObjectName(_fromUtf8("python_version_change"))
        python_version_change.setEnabled(True)
        python_version_change.resize(230, 117)
        python_version_change.setMinimumSize(QtCore.QSize(230, 117))
        python_version_change.setMaximumSize(QtCore.QSize(230, 117))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("python.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        python_version_change.setWindowIcon(icon)
        self.groupBox = QtGui.QGroupBox(python_version_change)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 211, 101))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(5, 60, 99, 33))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(107, 60, 99, 33))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(80, 30, 121, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.retranslateUi(python_version_change)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.change_environment_Python27)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL("clicked()"), self.change_environment_Python35)
        QtCore.QMetaObject.connectSlotsByName(python_version_change)
        python_version_change.setTabOrder(self.lineEdit, self.pushButton)
        python_version_change.setTabOrder(self.pushButton, self.pushButton_2)

    def retranslateUi(self, python_version_change):
        python_version_change.setWindowTitle(_translate("python_version_change", "Python版本切换器", None))
        self.groupBox.setTitle(_translate("python_version_change", "Python版本", None))
        self.pushButton.setText(_translate("python_version_change", "使用 Python2.7", None))
        self.pushButton_2.setText(_translate("python_version_change", "使用 Python3.5", None))
        self.label.setText(_translate("python_version_change", "当前版本：", None))
        self.lineEdit.setText(_translate("python_version_change", self.get_python_version(), None))

    def get_python_version(self):
        path_content = os.getenv('Path')
        prefix = 'Python'
        version_num1 = (path_content[path_content.index(prefix)+len(prefix):])[:1]
        version_num2 = (path_content[path_content.index(prefix)+len(prefix):])[1:2]
        version = prefix + ' ' + version_num1 + '.' + version_num2
        return version

    def change_environment_Python27(self):
        path = os.getenv('Path')
        new_path = path.replace('Python35', 'Python27')
        key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,'System\\CurrentControlSet\\Control\\Session Manager\\Environment', 0, _winreg.KEY_WRITE)
        _winreg.SetValueEx(key, 'Path', 0, _winreg.REG_SZ, new_path)
        _winreg.CloseKey(key)
        win32api.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SETTINGCHANGE, 0, 'Environment')
        self.lineEdit.setText("Python 2.7")

    def change_environment_Python35(self):
        path = os.getenv('Path')
        new_path = path.replace('Python27', 'Python35')
        key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,'System\\CurrentControlSet\\Control\\Session Manager\\Environment', 0, _winreg.KEY_WRITE)
        _winreg.SetValueEx(key, 'Path', 0, _winreg.REG_SZ, new_path)
        _winreg.CloseKey(key)
        win32api.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SETTINGCHANGE, 0, 'Environment')
        change = self.get_python_version()
        self.lineEdit.setText("Python 3.5")


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_python_version_change()
    ui.setupUi(Form)
    Form.show()
    app.exec_()