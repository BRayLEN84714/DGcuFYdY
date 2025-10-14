# 代码生成时间: 2025-10-14 17:33:58
import sys
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QTextEdit, QLabel

"""
Sensor data collection application using PyQt framework.
This application creates a GUI that allows users to collect data from sensors.
"""

class SensorDataCollectionThread(QThread):
    """
    Thread for collecting sensor data.
    It emits signals to update the UI with the collected data.
    """
    data_collected = pyqtSignal(str)
    
    def __init__(self, sensor):
        super().__init__()
        self.sensor = sensor
        self.running = False
        
    def run(self):
        """
        Start the data collection process.
        """
        self.running = True
        while self.running:
            try:
                # Simulate sensor data collection
                data = self.sensor.read_data()
                self.data_collected.emit(data)
            except Exception as e:
                # Handle any exceptions that occur during data collection
                self.data_collected.emit(str(e))
            finally:
                # Add a delay to simulate data collection interval
                QThread.sleep(1)
        
    def stop(self):
        """
        Stop the data collection process.
        """
        self.running = False

class SensorDataCollectionApp(QMainWindow):
    """
    Main application window for sensor data collection.
    """
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        """
        Initialize the UI components.
        """
        self.setWindowTitle('Sensor Data Collection')
        self.setGeometry(100, 100, 800, 600)
        self.createLayout()
        self.show()
        
    def createLayout(self):
        """
        Create the layout for the UI components.
        """
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.statusLabel = QLabel('Status: Idle')
        layout.addWidget(self.statusLabel)
        
        self.startButton = QPushButton('Start Collection')
        self.startButton.clicked.connect(self.startCollection)
        layout.addWidget(self.startButton)
        
        self.stopButton = QPushButton('Stop Collection')
        self.stopButton.clicked.connect(self.stopCollection)
        layout.addWidget(self.stopButton)
        
        self.dataTextEdit = QTextEdit()
        layout.addWidget(self.dataTextEdit)
        
    def startCollection(self):
        "