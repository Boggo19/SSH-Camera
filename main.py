import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QStackedWidget
from homePage import Ui_Dialog
from ingredientsPage import IngredientsPage
from recipesPage import RecipesPage  # Import RecipesPage


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Initialize the main stacked widget
        self.stacked_widget = QStackedWidget(self)
        self.setCentralWidget(self.stacked_widget)

        # Create and set up the home page
        self.ui = Ui_Dialog()
        self.home_widget = QWidget(self)  # Parent the home widget to MainWindow
        self.ui.setupUi(self.home_widget)

        # Create and set up the ingredients page
        self.ingredients_page = IngredientsPage(self)  # Parent the ingredients page to MainWindow

        # Create and set up the recipes page
        self.recipes_page = RecipesPage(self)  # Parent the recipes page to MainWindow

        # Add all pages to the stacked widget
        self.stacked_widget.addWidget(self.home_widget)
        self.stacked_widget.addWidget(self.ingredients_page)
        self.stacked_widget.addWidget(self.recipes_page)

        # Set the initial page to the home page
        self.stacked_widget.setCurrentWidget(self.home_widget)

        # Set fixed size to match the home page
        self.setFixedSize(self.home_widget.size())

        # Connect buttons for navigation
        self.ui.ingredientsButton.clicked.connect(self.open_ingredients_page)
        self.ui.recipeButton.clicked.connect(self.open_recipes_page)  # Connect recipe button to open the recipes page
        self.ingredients_page.back_button.clicked.connect(self.show_home_page)
        self.recipes_page.back_button.clicked.connect(self.show_home_page)

    def open_ingredients_page(self):
        """Switch to the Ingredients Page."""
        self.stacked_widget.setCurrentWidget(self.ingredients_page)  # Switch to the ingredients page
        self.setFixedSize(self.ingredients_page.size())  # Adjust the window size to match the ingredients page

    def open_recipes_page(self):
        """Switch to the Recipes Page."""
        self.stacked_widget.setCurrentWidget(self.recipes_page)  # Switch to the recipes page
        self.setFixedSize(self.recipes_page.size())  # Adjust the window size to match the recipes page

    def show_home_page(self):
        """Switch back to the Home Page."""
        self.stacked_widget.setCurrentWidget(self.home_widget)  # Switch to the home page
        self.setFixedSize(self.home_widget.size())  # Adjust the window size to match the home page


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
