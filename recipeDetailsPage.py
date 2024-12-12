from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QFrame
from PyQt5.QtGui import QPixmap, QFont, QImage
from PyQt5.QtCore import Qt, pyqtSignal
import base64


class RecipeDetailsPage(QDialog):
    backButtonClicked = pyqtSignal()  # Signal to notify MainWindow to go back

    def __init__(self, parent=None):
        super(RecipeDetailsPage, self).__init__(parent)
        self.setGeometry(100, 100, 600, 780)
        self.setWindowTitle("Recipe Details")
        self.setStyleSheet("""
            background-color: qlineargradient(
                spread:pad, x1:0.091, y1:0.101636, x2:0.991379, y2:0.977, 
                stop:0 rgba(128, 194, 255, 255), stop:1 rgba(255, 255, 255, 255)
            );
        """)
        self.setupUi()

    def setupUi(self):
        layout = QVBoxLayout(self)

        # Title (Recipe Name)
        self.titleLabel = QLabel("Recipe Name", self)
        self.titleLabel.setStyleSheet("""
            font: 75 36pt 'Georgia';
            color: rgba(0, 51, 102, 1);
            background-color: transparent;
        """)
        self.titleLabel.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.titleLabel)

        # Recipe Image Placeholder
        self.imageLabel = QLabel(self)
        self.imageLabel.setAlignment(Qt.AlignCenter)
        self.imageLabel.setFixedHeight(200)
        self.imageLabel.setStyleSheet("""
            background-color: rgba(240, 240, 240, 1);
            border: 2px solid rgba(0, 102, 204, 1);
            border-radius: 10px;
        """)
        layout.addWidget(self.imageLabel)

        # Description
        self.descriptionLabel = QLabel("Short recipe description goes here.", self)
        self.descriptionLabel.setWordWrap(True)
        self.descriptionLabel.setStyleSheet("""
            font: 16pt 'Verdana';
            color: rgba(0, 51, 102, 1);
            margin: 10px 20px;
            background-color: transparent;
        """)
        layout.addWidget(self.descriptionLabel)

        # Nutritional Information
        nutritionLayout = QHBoxLayout()
        self.nutritionValues = []
        nutritionLabels = ["kcal", "Protein", "Carbs", "Fat", "Fibre", "Salt"]
        for nutrient in nutritionLabels:
            frame = QFrame(self)
            frame.setFixedSize(75, 70)
            frame.setStyleSheet("""
                border-radius: 10px;
                background-color: rgba(224, 255, 255, 1);
            """)
            layoutInFrame = QVBoxLayout(frame)
            layoutInFrame.setContentsMargins(0, 0, 0, 0)

            valueLabel = QLabel("0", self)
            valueLabel.setFont(QFont("Verdana", 15, QFont.Bold))
            valueLabel.setAlignment(Qt.AlignCenter)
            valueLabel.setStyleSheet("color: rgba(0, 51, 102, 1); background-color: transparent;")
            layoutInFrame.addWidget(valueLabel)
            self.nutritionValues.append(valueLabel)

            nutrientLabel = QLabel(nutrient, self)
            nutrientLabel.setFont(QFont("Verdana", 10))
            nutrientLabel.setAlignment(Qt.AlignCenter)
            nutrientLabel.setStyleSheet("color: rgba(0, 51, 102, 1); background-color: transparent;")
            layoutInFrame.addWidget(nutrientLabel)

            nutritionLayout.addWidget(frame)
        layout.addLayout(nutritionLayout)

        # Prep Time and Cook Time
        self.prepLabel = QLabel("Prep Time: 0 minutes", self)
        self.prepLabel.setStyleSheet("font: 14pt 'Verdana'; color: rgba(0, 51, 102, 1); background-color: transparent; margin-left: 20px; padding-top: 20px;")

        self.cookLabel = QLabel("Cook Time: 0 minutes", self)
        self.cookLabel.setStyleSheet("font: 14pt 'Verdana'; color: rgba(0, 51, 102, 1); background-color: transparent; padding-top: 20px;")

        timeLayout = QHBoxLayout()
        timeLayout.addWidget(self.prepLabel)
        timeLayout.addStretch()
        timeLayout.addWidget(self.cookLabel)
        layout.addLayout(timeLayout)

        # Instructions
        self.instructionsLabel = QLabel("Instructions go here.", self)
        self.instructionsLabel.setWordWrap(True)
        self.instructionsLabel.setStyleSheet("""
            font: 14pt 'Verdana';
            color: rgba(0, 51, 102, 1);
            margin: 10px 20px;
            background-color: transparent;
            margin-left: 20px;
        """)
        layout.addWidget(self.instructionsLabel)

        # Spacer to push the Back button to the bottom
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Back Button
        self.backButton = QPushButton("Back", self)
        self.backButton.setStyleSheet("""
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
        self.backButton.clicked.connect(self.backButtonClicked.emit)
        layout.addWidget(self.backButton)

        self.setLayout(layout)

    def updateContent(self, recipeData):
        self.titleLabel.setText(recipeData.get("name", "Unknown Recipe"))

        # Convert binary data to image
        base64Data = base64.b64encode(recipeData.get('image')).decode('utf-8')
        imageData = base64.b64decode(base64Data)
        qImage = QImage.fromData(imageData)

        # Handle image
        if qImage:
            pixmap = QPixmap.fromImage(qImage)
            self.imageLabel.setPixmap(pixmap.scaled(400, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        else:
            self.imageLabel.setText("No Image Available")
            self.imageLabel.setAlignment(Qt.AlignCenter)
            self.imageLabel.setStyleSheet("color: rgba(0, 51, 102, 1); font: 14pt 'Verdana'; background-color: transparent;")

        # Description
        self.descriptionLabel.setText(recipeData.get("description", "No description available."))

        # Nutrition
        for i, value in enumerate(recipeData.get("nutrition", [0, 0, 0, 0, 0, 0])):
            self.nutritionValues[i].setText(str(value))

        # Prep and Cook Times
        self.prepLabel.setText(f"Prep Time: {recipeData.get('prepTime', 'N/A')}")
        self.cookLabel.setText(f"Cook Time: {recipeData.get('cookTime', 'N/A')}")

        # Instructions
        self.instructionsLabel.setText(recipeData.get("instructions", "No instructions provided."))

