from PyQt5.QtWidgets import (
    QDialog, QTableView, QLabel, QPushButton, QVBoxLayout, QSpacerItem, QSizePolicy
)
from PyQt5.QtGui import QStandardItem, QStandardItemModel, QFont
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets


class IngredientsPage(QDialog):
    def __init__(self, parent=None):
        super(IngredientsPage, self).__init__(parent)
        self.setGeometry(100, 100, 600, 780)
        self.setWindowTitle("Ingredients")
        self.setStyleSheet("""
            background-color:qlineargradient(
                spread:pad, x1:0.091, y1:0.101636, x2:0.991379, y2:0.977,
                stop:0 rgba(128, 194, 255, 255), stop:1 rgba(255, 255, 255, 255)
            );
        """)
        self.setupUi()

    def setupUi(self):
        layout = QVBoxLayout(self)

        # Title label
        self.titleLabel = QLabel("INGREDIENTS")
        self.titleLabel.setStyleSheet("""
            font: 75 45pt 'Georgia';
            color: rgba(0, 51, 102, 1);
            background: transparent;
            margin-top: 25px;
        """)
        self.titleLabel.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.titleLabel)

        # Spacer between the title and the table
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)
        layout.addSpacerItem(spacer)

        # Table setup
        self.tableView = QTableView(self)
        self.setupTable()
        layout.addWidget(self.tableView)

        # Back button
        self.backButton = QPushButton("Back")
        self.backButton.setStyleSheet("""
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
        self.backButton.clicked.connect(self.close)
        layout.addWidget(self.backButton)

        self.setLayout(layout)

    def setupTable(self):
        model = QStandardItemModel()

        # Add the column titles as the first row
        columnTitles = ["Ingredients", "Quantity"]
        titleRow = []
        for title in columnTitles:
            titleItem = QStandardItem(title)
            titleItem.setTextAlignment(Qt.AlignCenter)
            titleItem.setFlags(Qt.ItemIsEnabled)  # Make it non-editable
            font = QFont("Georgia", 18, QFont.Bold)  # Use QFont directly
            titleItem.setFont(font)
            titleRow.append(titleItem)
        model.appendRow(titleRow)

        # Add data rows
        data = [
            ("Red Pepper", 2),
            ("Chicken", 1),
            ("Green Pepper", 3),
            ("Onion", 2),
            ("Bacon", 6),
        ]

        for ingredient, quantity in data:
            ingredientItem = QStandardItem(ingredient)
            ingredientItem.setTextAlignment(Qt.AlignVCenter)
            ingredientItem.setFlags(Qt.NoItemFlags)  # Completely disable interaction

            quantityItem = QStandardItem(str(quantity))
            quantityItem.setTextAlignment(Qt.AlignCenter)
            quantityItem.setFlags(Qt.NoItemFlags)  # Completely disable interaction

            model.appendRow([ingredientItem, quantityItem])

        self.tableView.setModel(model)

        # Adjust default column widths
        totalTableWidth = 570
        columnWidth = totalTableWidth // len(columnTitles)
        self.tableView.setGeometry(14, 100, totalTableWidth, 400)
        self.tableView.setColumnWidth(0, columnWidth)
        self.tableView.setColumnWidth(1, columnWidth)

        # Stretch columns to fit the table width dynamically
        header = self.tableView.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

        # Remove the header views to hide them
        self.tableView.horizontalHeader().setVisible(False)
        self.tableView.verticalHeader().setVisible(False)

        # Disable horizontal scrollbars
        self.tableView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSortingEnabled(False)

        # Style the table
        self.tableView.setStyleSheet("""
        QTableView {
            background-color: rgba(224, 255, 255, 1);
            border: 3px solid rgba(0, 102, 204, 1);
            border-radius: 15px;
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
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableView.setFocusPolicy(Qt.NoFocus)
    