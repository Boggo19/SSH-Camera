from PyQt5.QtWidgets import QDialog, QLabel, QTableView, QPushButton, QVBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont
from PyQt5.QtCore import Qt, pyqtSignal


class RecipesPage(QDialog):
    recipe_clicked = pyqtSignal(str)  # Signal to notify which recipe was clicked

    def __init__(self, parent=None):
        super(RecipesPage, self).__init__(parent)
        self.setGeometry(100, 100, 600, 780)
        self.setWindowTitle("Recipes")
        self.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.091, y1:0.101636, x2:0.991379, y2:0.977, stop:0 rgba(128, 194, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.setup_ui()

    def setup_ui(self):
        # Layout for the dialog
        layout = QVBoxLayout(self)

        # Title label
        self.title_label = QLabel("RECIPES")
        self.title_label.setStyleSheet("""
            font: 75 45pt 'Georgia';
            color: rgba(0, 51, 102, 1); /* Dark blue text */
            background: transparent; /* Remove any background */
            margin-top: 25px; /* Adjust this value to move the title lower */
        """)
        self.title_label.setAlignment(Qt.AlignCenter)

        # Add the title to the layout
        layout.addWidget(self.title_label)

        # Add a spacer for the gap between the title and the table
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)
        layout.addSpacerItem(spacer)

        # Table setup
        self.table_view = QTableView(self)
        self.setup_table()
        layout.addWidget(self.table_view)

        # Back button
        self.back_button = QPushButton("Back")
        self.back_button.setStyleSheet("""
            QPushButton {
                font: 75 18pt 'Verdana';
                color: white;
                background-color: rgba(0, 102, 204, 1);
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: rgba(0, 77, 153, 1);
            }
        """)
        self.back_button.clicked.connect(self.close)
        layout.addWidget(self.back_button)

        # Connect table click to handler
        self.table_view.clicked.connect(self.on_recipe_clicked)

    def setup_table(self):
        # Create the table model
        model = QStandardItemModel()

        # Add the column titles as the first row
        column_titles = ["Meal Name", "Ingredients to Buy"]
        title_row = []
        for title in column_titles:
            title_item = QStandardItem(title)
            title_item.setTextAlignment(Qt.AlignCenter)  # Center align the text
            title_item.setFlags(Qt.ItemIsEnabled)  # Make it non-editable
            # Apply styling directly to the column title items
            if title == "Ingredients to Buy":
                font = QFont("Georgia", 14, QFont.Bold)  # Smaller font for "Ingredients to Buy"
            else:
                font = QFont("Georgia", 18, QFont.Bold)  # Original font size for other titles
            title_item.setFont(font)
            title_row.append(title_item)

        # Add the column titles as the first row
        model.appendRow(title_row)

        # Add rows of data
        self.data = [
            ("Spaghetti Bolognese", 2),
            ("Chicken Curry", 4),
            ("Grilled Salmon", 1),
            ("Vegetable Stir-Fry", 3),
        ]

        for meal_name, ingredients_needed in self.data:
            # Meal Name
            meal_name_item = QStandardItem(meal_name)
            meal_name_item.setTextAlignment(Qt.AlignCenter)

            # Ingredients to Buy
            ingredients_item = QStandardItem(str(ingredients_needed))
            ingredients_item.setTextAlignment(Qt.AlignCenter)

            # Add the row to the table model
            model.appendRow([meal_name_item, ingredients_item])

        # Set the model for the table
        self.table_view.setModel(model)

        # Adjust column widths to make all columns the same size
        total_table_width = 570  # Total width for the table
        column_width = total_table_width // len(column_titles)  # Equal width for all columns
        self.table_view.setGeometry(14, 100, total_table_width, 500)  # Ensure table fits within the border
        for i in range(len(column_titles)):
            self.table_view.setColumnWidth(i, column_width)

        # Remove the header views to match the style from the IngredientsPage
        self.table_view.horizontalHeader().setVisible(False)
        self.table_view.verticalHeader().setVisible(False)

        # Disable all interactions with the table
        self.table_view.setEditTriggers(QTableView.NoEditTriggers)  # Disable editing
        self.table_view.setSelectionMode(QTableView.SingleSelection)  # Enable single-row selection
        self.table_view.setFocusPolicy(Qt.NoFocus)                  # Disable focus
        self.table_view.setEnabled(True)                            # Allow row selection

        # Style the table
        self.table_view.setStyleSheet("""
            QTableView {
                background-color: rgba(224, 255, 255, 1);
                border: 3px solid rgba(0, 102, 204, 1);
                border-radius: 15px;  /* Smooth corners for the entire table */
                font-family: Arial, sans-serif;
                font-size: 14px;
                color: rgba(0, 51, 102, 1);
            }
        """)

    def on_recipe_clicked(self, index):
        """Handle recipe row click."""
        selected_row = index.row()
        if selected_row > 0:  # Skip the title row
            meal_name = self.data[selected_row - 1][0]  # Get the meal name
            self.recipe_clicked.emit(meal_name)  # Emit the signal
