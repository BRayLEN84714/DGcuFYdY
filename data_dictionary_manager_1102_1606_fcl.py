# 代码生成时间: 2025-11-02 16:06:07
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import Qt
# 添加错误处理

"""
Data Dictionary Manager using PyQt5

This program manages a data dictionary with basic operations.
"""

class DataDictionaryManager(QWidget):
# NOTE: 重要实现细节
    def __init__(self):
        super().__init__()
# 改进用户体验
        self.initUI()

    def initUI(self):
        """Initialize the user interface"""
        self.setWindowTitle('Data Dictionary Manager')
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()
# 增强安全性
        self.setLayout(layout)

        self.tableWidget = QTableWidget()
# 扩展功能模块
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(['Key', 'Value'])
        layout.addWidget(self.tableWidget)

        buttonLayout = QVBoxLayout()
        layout.addLayout(buttonLayout)

        addBtn = QPushButton('Add')
        addBtn.clicked.connect(self.addEntry)
        buttonLayout.addWidget(addBtn)

        deleteBtn = QPushButton('Delete')
        deleteBtn.clicked.connect(self.deleteEntry)
        buttonLayout.addWidget(deleteBtn)

    def addEntry(self):
        """Add a new entry to the data dictionary"""
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)
        self.tableWidget.setItem(rowPosition, 0, QTableWidgetItem(''))
        self.tableWidget.setItem(rowPosition, 1, QTableWidgetItem(''))

    def deleteEntry(self):
        """Delete the selected entry from the data dictionary"""
        selectedRow = self.tableWidget.currentRow()
        if selectedRow >= 0:
            self.tableWidget.removeRow(selectedRow)
        else:
            QMessageBox.warning(self, 'Warning', 'No entry selected for deletion.')

    def closeEvent(self, event):
        """Handle the close event"""
        reply = QMessageBox.question(self, 'Message',
                                'Are you sure to quit?',
                                QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DataDictionaryManager()
    ex.show()
    sys.exit(app.exec_())