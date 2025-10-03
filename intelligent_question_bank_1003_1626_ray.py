# 代码生成时间: 2025-10-03 16:26:36
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QTextEdit, QLabel
from PyQt5.QtCore import Qt

"""
智能题库系统
@author: Your Name
@version: 1.0
"""

class QuestionBank(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 设置窗口标题和初始大小
        self.setWindowTitle('智能题库系统')
        self.setGeometry(100, 100, 800, 600)

        # 创建中心窗口
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # 添加题目显示文本框
        self.question_label = QLabel('请输入题目：', self)
        self.question_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.question_label)

        # 添加题目编辑框
        self.question_text = QTextEdit(self)
        layout.addWidget(self.question_text)

        # 添加导入题目按钮
        self.import_button = QPushButton('导入题目', self)
        self.import_button.clicked.connect(self.import_questions)
        layout.addWidget(self.import_button)

        # 添加保存题目按钮
        self.save_button = QPushButton('保存题目', self)
        self.save_button.clicked.connect(self.save_questions)
        layout.addWidget(self.save_button)

    def import_questions(self):
        # 打开文件对话框，选择题目文件
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, '导入题目', '',
                                                  'Text Files (*.txt);;All Files (*)', options=options)
        if file_name:
            try:
                # 读取题目文件内容
                with open(file_name, 'r', encoding='utf-8') as file:
                    questions = file.readlines()
                # 将题目内容显示在编辑框中
                self.question_text.setText(''.join(questions))
            except Exception as e:
                print(f'导入题目失败：{e}')

    def save_questions(self):
        # 打开文件对话框，保存题目文件
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, '保存题目', '',
                                                  'Text Files (*.txt);;All Files (*)', options=options)
        if file_name:
            try:
                # 将编辑框中的题目内容保存到文件
                with open(file_name, 'w', encoding='utf-8') as file:
                    file.write(self.question_text.toPlainText())
            except Exception as e:
                print(f'保存题目失败：{e}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    question_bank = QuestionBank()
    question_bank.show()
    sys.exit(app.exec_())