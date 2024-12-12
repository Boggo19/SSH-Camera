from PyQt5.QtWidgets import QDialog, QLabel, QTableView, QPushButton, QVBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QStandardItem, QStandardItemModel, QIcon, QFont
from PyQt5.QtCore import Qt, pyqtSignal
import QueryFunction


class RecipesPage(QDialog):
    recipeClicked = pyqtSignal(dict)  # Signal to notify selected recipe details

    def __init__(self, parent=None):
        super(RecipesPage, self).__init__(parent)
        self.setGeometry(100, 100, 600, 780)
        self.setWindowTitle("Recipes")
        self.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.091, y1:0.101636, x2:0.991379, y2:0.977, stop:0 rgba(128, 194, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.setupUi()

    def setupUi(self):
        # Layout for the dialog
        layout = QVBoxLayout(self)

        # Title label
        self.titleLabel = QLabel("RECIPES")
        self.titleLabel.setStyleSheet("""
            font: 75 45pt 'Georgia';
            color: rgba(0, 51, 102, 1); 
            background: transparent; 
            margin-top: 25px; 
        """)
        self.titleLabel.setAlignment(Qt.AlignCenter)

        # Add the title to the layout
        layout.addWidget(self.titleLabel)

        # Subtitle label
        self.subtitleLabel = QLabel("Click on the meals for more information!")
        self.subtitleLabel.setStyleSheet("""
            font: 18pt 'Georgia';
            color: rgba(0, 77, 153, 1);
            background: transparent;
            margin-top: 15px;
        """)
        self.subtitleLabel.setAlignment(Qt.AlignCenter)

        # Add the subtitle to the layout
        layout.addWidget(self.subtitleLabel)

        # Add a spacer for the gap between the title and the table
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

        # Connect table click to handler
        self.tableView.clicked.connect(self.onRecipeClicked)

    def setupTable(self):
        # Create the table model
        model = QStandardItemModel()

        # Add the column titles as the first row
        columnTitles = ["Meal Name", "Ingredients to Buy"]
        titleRow = []
        for title in columnTitles:
            titleItem = QStandardItem(title)
            titleItem.setTextAlignment(Qt.AlignCenter)  # Center align the text
            titleItem.setFlags(Qt.ItemIsEnabled)  # Make it non-editable
            # Apply styling to the column title items
            if title == "Ingredients to Buy":
                font = QFont("Georgia", 14, QFont.Bold)  # Set font size
            else:
                font = QFont("Georgia", 18, QFont.Bold)  # Set font size
            titleItem.setFont(font)
            titleRow.append(titleItem)

        # Add the column titles as the first row
        model.appendRow(titleRow)


        ingredients = QueryFunction.getIngredients()
        recipes = QueryFunction.getRecipes(ingredients)
        recipes = sorted(recipes, key=lambda r:r[1])
        self.data = recipes
        
        # Add rows of data
        # self.data = [
        #     {
        #         "name": "Spaghetti Bolognese",
        #         "ingredientsToBuy": 2,
        #         "imagePath": "path/to/spaghetti.jpg",
        #         "description": "A classic Italian pasta dish with rich tomato sauce.",
        #         "nutrition": [600, 25, 40, 20, 4, 2.0],
        #         "prepTime": "15 minutes",
        #         "cookTime": "30 minutes",
        #         "instructions": "1. Boil pasta.\n2. Prepare sauce.\n3. Combine and serve."
        #     },
        #     {
        #         "name": "Chicken Curry",
        #         "ingredientsToBuy": 4,
        #         "imagePath": "path/to/curry.jpg",
        #         "description": "A flavorful curry with tender chicken and spices.",
        #         "nutrition": [600, 25, 40, 20, 4, 2.0],
        #         "prepTime": "20 minutes",
        #         "cookTime": "40 minutes",
        #         "instructions": "1. Marinate chicken.\n2. Cook curry base.\n3. Add chicken and simmer."
        #     },
        # ]

        for meal, qtyToBuy in self.data:
            # Meal Name
            mealNameItem = QStandardItem(meal)
            mealNameItem.setTextAlignment(Qt.AlignCenter)

            # Ingredients to Buy
            ingredientsItem = QStandardItem(str(qtyToBuy))
            ingredientsItem.setTextAlignment(Qt.AlignCenter)

            # Add the row to the table model
            model.appendRow([mealNameItem, ingredientsItem])

        # Set the model for the table
        self.tableView.setModel(model)

        # Adjust column widths to make all columns the same size
        totalTableWidth = 570  # Total width for the table
        columnWidth = totalTableWidth // len(columnTitles)  # Equal width for all columns
        self.tableView.setGeometry(14, 100, totalTableWidth, 500)  # Ensure table fits within the border
        for i in range(len(columnTitles)):
            self.tableView.setColumnWidth(i, columnWidth)

        # Remove the header views to match the style from the IngredientsPage
        self.tableView.horizontalHeader().setVisible(False)
        self.tableView.verticalHeader().setVisible(False)

        # Disable all interactions with the table
        self.tableView.setEditTriggers(QTableView.NoEditTriggers)  # Disable any editing
        self.tableView.setSelectionMode(QTableView.SingleSelection)
        self.tableView.setFocusPolicy(Qt.NoFocus)  # Disable focus
        self.tableView.setEnabled(True)  # Allow row selection of recipe

        # Style the table
        self.tableView.setStyleSheet("""
            QTableView {
                background-color: rgba(224, 255, 255, 1);
                border: 3px solid rgba(0, 102, 204, 1);
                border-radius: 15px;  
                font-family: Arial, sans-serif;
                font-size: 14px;
                color: rgba(0, 51, 102, 1);
            }
        """)

    def sortRecipesByIngredients(self):
        # Sort the recipes by the number of ingredients to buy
        self.data.sort(key=lambda recipe: recipe["ingredientsToBuy"])

    def onRecipeClicked(self, index):
        selectedRow = index.row()
        if selectedRow > 0:  # Skip the title row
            recipeName = self.data[selectedRow - 1][0]  # Fetch the recipe name
            recipeData = QueryFunction.getRecipeInfo(recipeName)[0]

            #Convert to json format
            jsonRecipe = {
                "name": recipeData[0],
                "ingredientsToBuy": QueryFunction.getRecipeIngredients(recipeData[0]),
                "image": recipeData[1],
                "description": recipeData[2],
                "nutrition": [recipeData[3], recipeData[4], recipeData[5], recipeData[6], recipeData[7], recipeData[8]],
                "prepTime": recipeData[9],
                "cookTime": recipeData[10],
                "instructions": recipeData[11]
            }
            self.recipeClicked.emit(jsonRecipe)  # Send the signal with the full recipe data
