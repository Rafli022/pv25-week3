import sys
import random
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtCore import Qt, QEvent

class MouseTracker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tugas Week 3 - (F1D022022 - Rafli)")
        self.setGeometry(100, 100, 600, 400)
        
        self.label = QLabel("x: 0, y: 0", self)
        self.label.setGeometry(50, 50, 120, 30)
        self.label.setAlignment(Qt.AlignCenter)
        
        self.setMouseTracking(True)
        self.label.installEventFilter(self)
    
    def mouseMoveEvent(self, event):
        self.label.setText(f"x: {event.x()}, y: {event.y()}")
    
    def eventFilter(self, obj, event):
        if obj == self.label and event.type() == QEvent.Enter:
            self.move_label_randomly()
        return super().eventFilter(obj, event)
    
    def move_label_randomly(self):
        new_x = random.randint(0, self.width() - self.label.width())
        new_y = random.randint(0, self.height() - self.label.height())
        self.label.move(new_x, new_y)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MouseTracker()
    window.show()
    sys.exit(app.exec_())