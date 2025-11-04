# 代码生成时间: 2025-11-04 14:56:59
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QMessageBox
from datetime import datetime

"""
考勤打卡系统
"""

class AttendanceSystem(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 设置窗口标题和大小
        self.setWindowTitle('考勤打卡系统')
        self.resize(400, 200)

        # 创建布局
        layout = QVBoxLayout()

        # 用户名输入框
        self.username_label = QLabel('用户名:')
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText('请输入用户名')

        # 打卡按钮
        self.check_in_button = QPushButton('打卡')
        self.check_in_button.clicked.connect(self.check_in)

        # 布局添加控件
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.check_in_button)

        # 设置布局
        self.setLayout(layout)

    def check_in(self):
        # 获取用户名
        username = self.username_input.text()

        # 检查用户名是否为空
        if not username:
            QMessageBox.warning(self, '警告', '用户名不能为空！')
            return

        # 打卡成功提示
        QMessageBox.information(self, '提示', f'{username} 打卡成功！')

        # 记录打卡时间
        self.record_attendance(username)

    def record_attendance(self, username):
        # 记录打卡时间
        attendance_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'{username} 打卡时间：{attendance_time}')
        # 可以在这里添加代码将打卡时间保存到文件或数据库中

"""
主函数
"""
if __name__ == '__main__':
    app = QApplication(sys.argv)
    attendance_system = AttendanceSystem()
    attendance_system.show()
    sys.exit(app.exec_())