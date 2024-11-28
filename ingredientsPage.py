from PyQt5.QtWidgets import QWidget, QTableView, QLabel, QPushButton, QVBoxLayout, QDialog, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QStandardItem, QStandardItemModel, QIcon
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets

class IngredientsPage(QDialog):
    def __init__(self, parent=None):
        super(IngredientsPage, self).__init__(parent)
        self.setGeometry(100, 100, 600, 780)
        self.setWindowTitle("Ingredients")
        self.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.091, y1:0.101636, x2:0.991379, y2:0.977, stop:0 rgba(128, 194, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.setup_ui()

    def setup_ui(self):
        # Layout for the dialog
        layout = QVBoxLayout(self)

        # Title label
        self.title_label = QLabel("INGREDIENTS")
        self.title_label.setStyleSheet("""
            font: 75 48pt 'Georgia';
            color: rgba(0, 51, 102, 1); /* Dark blue text */
            background: transparent; /* Remove any background */
            margin-top: 20px; /* Adjust this value to move the title lower */
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

    def setup_table(self):
        model = QStandardItemModel()

        # Add the column titles as the first row
        column_titles = ["Ingredients", "Quantity"]
        title_row = []
        for title in column_titles:
            title_item = QStandardItem(title)
            title_item.setTextAlignment(Qt.AlignCenter)
            title_item.setFlags(Qt.ItemIsEnabled)  # Make it non-editable
            # Apply styling directly to the column title items
            font = QtGui.QFont("Georgia", 18, QtGui.QFont.Bold)  # Match title font and style
            title_item.setFont(font)
            title_row.append(title_item)
        model.appendRow(title_row)

        # Add data rows
        data = [
            ("Red Pepper", 2, "path/to/red_pepper.png"),
            ("Chicken", 1, "path/to/chicken.png"),
            ("Green Pepper", 3, "path/to/green_pepper.png"),
            ("Onion", 2, "path/to/onion.png"),
            ("Bacon", 6, "path/to/bacon.png"),
            ("Red Pepper", 2, "path/to/red_pepper.png"),
            ("Chicken", 1, "path/to/chicken.png"),
            ("Green Pepper", 3, "path/to/green_pepper.png"),
            ("Onion", 2, "path/to/onion.png"),
            ("Bacon", 6, "path/to/bacon.png"),
            
            
        ]

        for ingredient, quantity, icon_path in data:
            icon_item = QStandardItem()
            icon_item.setIcon(QIcon(icon_path))
            icon_item.setText(ingredient)
            icon_item.setTextAlignment(Qt.AlignVCenter)
            icon_item.setFlags(Qt.NoItemFlags)  # Completely disable interaction

            quantity_item = QStandardItem(str(quantity))
            quantity_item.setTextAlignment(Qt.AlignCenter)
            quantity_item.setFlags(Qt.NoItemFlags)  # Completely disable interaction

            model.appendRow([icon_item, quantity_item])

        self.table_view.setModel(model)

        # Adjust default column widths to avoid horizontal scrolling
        total_table_width = 570  # Fixed total width for the table
        column_width = total_table_width // 2  # Split width equally between columns
        self.table_view.setGeometry(14, 100, total_table_width, 400)
        self.table_view.setColumnWidth(0, column_width)
        self.table_view.setColumnWidth(1, column_width)

        # Stretch columns to fit the table width dynamically
        header = self.table_view.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

        # Remove the header views to hide them
        self.table_view.horizontalHeader().setVisible(False)
        self.table_view.verticalHeader().setVisible(False)

        # Disable horizontal scrollbars
        self.table_view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.table_view.setAlternatingRowColors(True)
        self.table_view.setSortingEnabled(False)

        # Style the table (background, gridlines, and text)
        self.table_view.setStyleSheet("""
        QTableView {
            background-color: rgba(224, 255, 255, 1);
            border: 3px solid rgba(0, 102, 204, 1);
            border-radius: 15px;  /* Smooth corners for the entire table */
            gridline-color: rgba(0, 102, 204, 0.5);
            font-family: Arial, sans-serif;
            font-size: 14px;
            color: rgba(0, 51, 102, 1);
        }

        QScrollBar:vertical {
            background: rgba(224, 255, 255, 1);
            width: 12px;
            border: none;
        }

        QScrollBar::handle:vertical {
            background: rgba(0, 102, 204, 1);
            border-radius: 6px;
        }
        """)

        # Disable all interactions on the table
        self.table_view.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)  # Disable editing
        self.table_view.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)    # Disable selection mode
        self.table_view.setFocusPolicy(Qt.NoFocus)                                   # Disable focus completely
