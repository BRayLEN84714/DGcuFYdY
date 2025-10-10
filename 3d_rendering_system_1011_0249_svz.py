# 代码生成时间: 2025-10-11 02:49:25
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QSurfaceFormat
from vispy import scene, visuals

"""
3D Rendering System using Python and PyQt5.
This script sets up a basic 3D rendering system using the VisPy library
to handle the 3D rendering and PyQt5 for the GUI.
"""

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('3D Rendering System')
        self.setGeometry(100, 100, 800, 600)
        self.canvas = Canvas()
        self.setCentralWidget(self.canvas.native)

    def closeEvent(self, event):
        self.canvas.close()  # Close the VisPy canvas
        super().closeEvent(event)

class Canvas(scene.SceneCanvas):
    def __init__(self):
        super().__init__()
        self.size = (800, 600)
        self.bgcolor = 'white'
        self.show()

        # Create a simple 3D cube
        self.cube = visuals.Cube(parent=self.scene, color='red', edge_color='k')
        self.view = self.central_widget.add_view()
        self.view.camera = scene.PerspectiveCamera(
            'panzoom', parent=self.view.scene,
            up="Vector3(0, 0, 1)", fov=60
        )
        self.view.camera.set_range()

    def on_close(self, event):
        # Handle closing the canvas
        self.close()

    def on_resize(self, event):
        # Handle resizing the canvas
        self.size = event.size
        self.physical_size = event.physical_size

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # Set the format for OpenGL
    QSurfaceFormat.setDefaultFormat(QSurfaceFormat())

    # Create the main window and show it
    main_window = MainWindow()
    main_window.show()

    # Start the application's event loop
    sys.exit(app.exec_())