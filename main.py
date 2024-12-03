import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget
from homePage import Ui_Dialog
from ingredientsPage import IngredientsPage
from recipesPage import RecipesPage
from recipeDetailsPage import RecipeDetailsPage


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Initialize the main stacked widget
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # Initialize pages
        self.ui = Ui_Dialog()
        self.home_widget = QWidget()
        self.ui.setupUi(self.home_widget)

        self.ingredients_page = IngredientsPage()
        self.recipes_page = RecipesPage()
        self.recipe_details_page = RecipeDetailsPage()

        # Add pages to stacked widget
        self.stacked_widget.addWidget(self.home_widget)
        self.stacked_widget.addWidget(self.ingredients_page)
        self.stacked_widget.addWidget(self.recipes_page)
        self.stacked_widget.addWidget(self.recipe_details_page)

        # Set the initial page
        self.stacked_widget.setCurrentWidget(self.home_widget)
        self.setFixedSize(600, 780)

        # Connect navigation buttons
        self.ui.ingredientsButton.clicked.connect(self.open_ingredients_page)
        self.ui.recipeButton.clicked.connect(self.open_recipes_page)
        self.ingredients_page.back_button.clicked.connect(self.show_home_page)
        self.recipes_page.back_button.clicked.connect(self.show_home_page)
        self.recipes_page.recipe_clicked.connect(self.open_recipe_details_page)

        # Connect back signal from RecipeDetailsPage
        self.recipe_details_page.back_button_clicked.connect(self.open_recipes_page)

    def open_ingredients_page(self):
        """Switch to the Ingredients Page."""
        self.stacked_widget.setCurrentWidget(self.ingredients_page)

    def open_recipes_page(self):
        """Switch to the Recipes Page."""
        self.stacked_widget.setCurrentWidget(self.recipes_page)

    def open_recipe_details_page(self, meal_name):
        """Switch to the Recipe Details Page."""
        self.recipe_details_page.update_content(meal_name)
        self.stacked_widget.setCurrentWidget(self.recipe_details_page)

    def show_home_page(self):
        """Switch back to the Home Page."""
        self.stacked_widget.setCurrentWidget(self.home_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
