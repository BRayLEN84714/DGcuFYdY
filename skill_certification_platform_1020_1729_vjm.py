# 代码生成时间: 2025-10-20 17:29:38
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget

class SkillCertificationPlatform(QWidget):
    """
    A PyQt5 application for a skill certification platform.
    """
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """
        Initializes the user interface.
        """
        # Set the title of the window
        self.setWindowTitle('Skill Certification Platform')

        # Create a vertical layout
        self.layout = QVBoxLayout()

        # Create a label for user input
        self.label = QLabel('Enter your name and skills separated by commas:')
        self.layout.addWidget(self.label)

        # Create a line edit for user input
        self.line_edit = QLineEdit()
        self.layout.addWidget(self.line_edit)

        # Create a button to submit skills
        self.submit_button = QPushButton('Submit Skills')
        self.submit_button.clicked.connect(self.submit_skills)
        self.layout.addWidget(self.submit_button)

        # Create a list widget to display skills
        self.list_widget = QListWidget()
        self.layout.addWidget(self.list_widget)

        # Set the layout for the window
        self.setLayout(self.layout)

    def submit_skills(self):
        """
        Handles the submission of skills by the user.
        """
        # Get the input from the line edit
        user_input = self.line_edit.text()

        # Check if the input is empty
        if not user_input.strip():
            self.display_error('No input provided.')
            return

        # Split the input into skills
        skills = [skill.strip() for skill in user_input.split(',')]

        # Clear the list widget
        self.list_widget.clear()

        # Add skills to the list widget
        for skill in skills:
            self.list_widget.addItem(skill)

    def display_error(self, message):
        """
        Displays an error message to the user.
        """
        QMessageBox = QMessageBox = QApplication.create('QMessageBox')
        QMessageBox.warning(self, 'Error', message)


if __name__ == '__main__':
    # Create an application
    app = QApplication(sys.argv)

    # Create an instance of the SkillCertificationPlatform class
    platform = SkillCertificationPlatform()
    platform.show()

    # Run the application
    sys.exit(app.exec_())