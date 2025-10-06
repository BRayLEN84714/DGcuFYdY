# 代码生成时间: 2025-10-07 03:53:26
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTableWidget, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import pyqtSlot

"""
元数据管理系统使用PyQt5框架实现。
该系统允许用户添加、查看、修改和删除元数据记录。
"""

class MetadataManagementSystem(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """初始化用户界面"""
        self.setWindowTitle('元数据管理系统')
        self.setGeometry(100, 100, 800, 600)

        # 创建中心窗口小部件
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)
        layout = QVBoxLayout(centralWidget)

        # 创建表头
        self.metadataTable = QTableWidget()
        self.metadataTable.setColumnCount(3)
        self.metadataTable.setHorizontalHeaderLabels(['ID', '名称', '值'])
        layout.addWidget(self.metadataTable)

        # 创建操作按钮
        buttonsWidget = QWidget()
        buttonsLayout = QVBoxLayout(buttonsWidget)

        # 添加按钮
        addButton = QPushButton('添加')
        addButton.clicked.connect(self.addMetadata)
        buttonsLayout.addWidget(addButton)

        # 删除按钮
        deleteButton = QPushButton('删除')
        deleteButton.clicked.connect(self.deleteMetadata)
        buttonsLayout.addWidget(deleteButton)

        # 修改按钮
        editButton = QPushButton('修改')
        editButton.clicked.connect(self.editMetadata)
        buttonsLayout.addWidget(editButton)

        layout.addWidget(buttonsWidget)

        # 创建底部布局
        bottomWidget = QWidget()
        bottomLayout = QVBoxLayout(bottomWidget)

        # ID输入框
        self.idLineEdit = QLineEdit()
        bottomLayout.addWidget(self.idLineEdit)

        # 名称输入框
        self.nameLineEdit = QLineEdit()
        bottomLayout.addWidget(self.nameLineEdit)

        # 值输入框
        self.valueLineEdit = QLineEdit()
        bottomLayout.addWidget(self.valueLineEdit)

        layout.addWidget(bottomWidget)

    @pyqtSlot()
    def addMetadata(self):
        """添加元数据记录"""
        try:
            id = self.idLineEdit.text()
            name = self.nameLineEdit.text()
            value = self.valueLineEdit.text()
            if not all([id, name, value]):
                raise ValueError('所有字段均为必填项')
            newRowIndex = self.metadataTable.rowCount()
            self.metadataTable.insertRow(newRowIndex)
            self.metadataTable.setItem(newRowIndex, 0, QTableWidgetItem(id))
            self.metadataTable.setItem(newRowIndex, 1, QTableWidgetItem(name))
            self.metadataTable.setItem(newRowIndex, 2, QTableWidgetItem(value))
        except ValueError as e:
            QMessageBox.warning(self, '错误', str(e))

    @pyqtSlot()
    def deleteMetadata(self):
        """删除元数据记录"""
        try:
            selectedRow = self.metadataTable.currentRow()
            if selectedRow >= 0:
                self.metadataTable.removeRow(selectedRow)
            else:
                raise ValueError('请先选择一个记录')
        except ValueError as e:
            QMessageBox.warning(self, '错误', str(e))

    @pyqtSlot()
    def editMetadata(self):
        """编辑元数据记录"""
        try:
            selectedRow = self.metadataTable.currentRow()
            if selectedRow >= 0:
                id = self.idLineEdit.text()
                name = self.nameLineEdit.text()
                value = self.valueLineEdit.text()
                if not all([id, name, value]):
                    raise ValueError('所有字段均为必填项')
                self.metadataTable.setItem(selectedRow, 0, QTableWidgetItem(id))
                self.metadataTable.setItem(selectedRow, 1, QTableWidgetItem(name))
                self.metadataTable.setItem(selectedRow, 2, QTableWidgetItem(value))
            else:
                raise ValueError('请先选择一个记录')
        except ValueError as e:
            QMessageBox.warning(self, '错误', str(e))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MetadataManagementSystem()
    window.show()
    sys.exit(app.exec_())