from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt, pyqtSignal


class RecipeDetailsPage(QDialog):
    back_button_clicked = pyqtSignal()  # Signal to notify MainWindow to go back

    def __init__(self, meal_name=None, parent=None):
        super(RecipeDetailsPage, self).__init__(parent)
        self.setGeometry(100, 100, 600, 780)
        self.setWindowTitle("Details")
        self.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.091, y1:0.101636, x2:0.991379, y2:0.977, stop:0 rgba(128, 194, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.meal_name = meal_name or "Recipe Details"
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)

        # Title Label
        self.title_label = QLabel(f"Details for {self.meal_name}")
        self.title_label.setStyleSheet("""
            font: 75 45pt 'Georgia';
            color: rgba(0, 51, 102, 1);
        """)
        self.title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.title_label)

        # Content Label (Placeholder for recipe details)
        self.content_label = QLabel("")
        self.content_label.setStyleSheet("font: 18pt 'Verdana'; color: rgba(0, 51, 102, 1);")
        self.content_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.content_label)

        # Back Button
        self.back_button = QPushButton("Back")
        self.back_button.setStyleSheet("""
            QPushButton {
                font: 18pt 'Verdana';
                background-color: rgba(0, 102, 204, 1);
                color: white;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: rgba(0, 77, 153, 1);
            }
        """)
        self.back_button.clicked.connect(self.back_button_clicked.emit)  # Emit signal on click
        layout.addWidget(self.back_button)

        self.setLayout(layout)

    def update_content(self, meal_name):
        """Update the page content based on the selected recipe."""
        self.meal_name = meal_name
        self.title_label.setText(f"Details for {self.meal_name}")
        self.content_label.setText(f"This is where details for {self.meal_name} will be displayed.")
