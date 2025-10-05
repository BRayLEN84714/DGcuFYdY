# 代码生成时间: 2025-10-05 18:51:53
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QTextEdit, QMessageBox
from PyQt5.QtCore import Qt
import sqlite3

"""
Database Migration Tool using PyQt5
This tool helps to migrate data from one SQLite database to another.
"""

class DatabaseMigrationTool(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Setting up the main window
        self.setWindowTitle('Database Migration Tool')
        self.setGeometry(100, 100, 600, 400)

        # Layout
        layout = QVBoxLayout()

        # Source Database Path
        self.source_db_label = QLabel('Source Database Path:')
        self.source_db_edit = QTextEdit()
        layout.addWidget(self.source_db_label)
        layout.addWidget(self.source_db_edit)

        # Destination Database Path
        self.dest_db_label = QLabel('Destination Database Path:')
        self.dest_db_edit = QTextEdit()
        layout.addWidget(self.dest_db_label)
        layout.addWidget(self.dest_db_edit)

        # Migration Button
        self.migration_btn = QPushButton('Migrate')
        self.migration_btn.clicked.connect(self.migrateDatabase)
        layout.addWidget(self.migration_btn)

        # Status Label
        self.status_label = QLabel('')
        layout.addWidget(self.status_label)

        self.setLayout(layout)

    def migrateDatabase(self):
        # Get the paths from the text fields
        source_db_path = self.source_db_edit.toPlainText()
        dest_db_path = self.dest_db_edit.toPlainText()

        # Error handling
        if not source_db_path or not dest_db_path:
            QMessageBox.warning(self, 'Error', 'Please enter both source and destination database paths.')
            return

        try:
            # Connect to the source database
            with sqlite3.connect(source_db_path) as source_conn:
                with sqlite3.connect(dest_db_path) as dest_conn:
                    source_cursor = source_conn.cursor()
                    dest_cursor = dest_conn.cursor()

                    # Copy the tables and data from the source to the destination
                    for table_name in self.getTableNames(source_cursor):
                        self.copyTable(source_cursor, dest_cursor, table_name)

            # Show success message
            QMessageBox.information(self, 'Success', 'Database migration completed successfully.')
            self.status_label.setText('Migration successful.')
        except sqlite3.Error as e:
            # Show error message
            QMessageBox.critical(self, 'Error', f'An error occurred: {e}')
            self.status_label.setText(f'Migration failed: {e}')

    def getTableNames(self, cursor):
        # Get the list of table names from the database
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        return [row[0] for row in cursor.fetchall()]

    def copyTable(self, source_cursor, dest_cursor, table_name):
        # Copy the structure and data of a table
        source_cursor.execute(f'PRAGMA table_info({table_name})')
        columns = [row[1] for row in source_cursor.fetchall()]
        column_str = ', '.join(columns)

        # Create the table in the destination database
        dest_cursor.execute(f'CREATE TABLE {table_name} ({column_str})')

        # Copy the data from the source to the destination table
        source_cursor.execute(f'SELECT * FROM {table_name}')
        rows = source_cursor.fetchall()
        for row in rows:
            column_values = ', '.join([f"'{val}'" if isinstance(val, str) else str(val) for val in row])
            dest_cursor.execute(f'INSERT INTO {table_name} VALUES ({column_values})')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DatabaseMigrationTool()
    ex.show()
    sys.exit(app.exec_())