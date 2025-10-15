# 代码生成时间: 2025-10-16 02:56:24
import os
import shutil
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog, QLabel
from PyQt5.QtCore import Qt

"""
Folder Organizer is a PyQt application that allows users to select a directory and
organize the files within it based on file extensions.

Attributes:
    - source_dir (str): The path to the directory that needs to be organized.
    - dest_dir (str): The path to the directory where organized files will be moved.
"""

class FolderOrganizer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Folder Organizer')
        self.setGeometry(100, 100, 400, 200)
        self.source_dir = ''
        self.dest_dir = ''
        self.init_ui()

    def init_ui(self):
        # Layout for the application
        layout = QVBoxLayout()

        # Label for source directory selection
        self.source_label = QLabel('Select Source Directory:', self)
        layout.addWidget(self.source_label)

        # Button to select source directory
        self.source_button = QPushButton('Select Source Directory', self)
        self.source_button.clicked.connect(self.select_source_dir)
        layout.addWidget(self.source_button)

        # Label for destination directory selection
        self.dest_label = QLabel('Select Destination Directory:', self)
        layout.addWidget(self.dest_label)

        # Button to select destination directory
        self.dest_button = QPushButton('Select Destination Directory', self)
        self.dest_button.clicked.connect(self.select_dest_dir)
        layout.addWidget(self.dest_button)

        # Button to start organizing
        self.organize_button = QPushButton('Start Organizing', self)
        self.organize_button.clicked.connect(self.organize_folder)
        layout.addWidget(self.organize_button)

        # Main layout
        self.setLayout(layout)

    def select_source_dir(self):
        """
        Opens a file dialog for selecting the source directory.
        """
        self.source_dir = QFileDialog.getExistingDirectory(self, 'Select Directory')
        self.source_label.setText(f'Selected Source Directory: {self.source_dir}')

    def select_dest_dir(self):
        """
        Opens a file dialog for selecting the destination directory.
        """
        self.dest_dir = QFileDialog.getExistingDirectory(self, 'Select Directory')
        self.dest_label.setText(f'Selected Destination Directory: {self.dest_dir}')

    def organize_folder(self):
        """
        Organizes the files in the source directory based on file extensions by moving them to
        the destination directory in subdirectories named after the extensions.
        """
        if not self.source_dir or not self.dest_dir:
            print('Source and destination directories must be selected.')
            return

        try:
            for filename in os.listdir(self.source_dir):
                file_path = os.path.join(self.source_dir, filename)
                if os.path.isfile(file_path):
                    # Get file extension
                    ext = os.path.splitext(filename)[1]
                    if ext:
                        # Create a directory for the extension if it doesn't exist
                        ext_dir = os.path.join(self.dest_dir, ext[1:])
                        if not os.path.exists(ext_dir):
                            os.makedirs(ext_dir)
                        # Move the file to the new directory
                        shutil.move(file_path, os.path.join(ext_dir, filename))
            print('Files have been organized successfully.')
        except Exception as e:
            print(f'An error occurred: {e}')

if __name__ == '__main__':
    app = QApplication([])
    window = FolderOrganizer()
    window.show()
    app.exec_()