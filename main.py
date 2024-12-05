import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget
from homePage import Ui_Dialog
from ingredientsPage import IngredientsPage
from recipesPage import RecipesPage
from recipeDetailsPage import RecipeDetailsPage


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Create a stacked widget to manage different pages
        # This acts as a container where only one page is visible at a time
        self.stackedWidget = QStackedWidget()
        self.setCentralWidget(self.stackedWidget)  # Set it as the central widget of the main window

        # Initialize all the pages
        self.ui = Ui_Dialog()  # Home page UI
        self.homeWidget = QWidget()  # Container for the home page
        self.ui.setupUi(self.homeWidget)  # Set up the home page layout

        self.ingredientsPage = IngredientsPage()  # Page for managing ingredients
        self.recipesPage = RecipesPage()  # Page for viewing recipes
        self.recipeDetailsPage = RecipeDetailsPage()  # Page to show detailed information about a recipe

        # Add all the pages to the stacked widget
        self.stackedWidget.addWidget(self.homeWidget)  # Home page
        self.stackedWidget.addWidget(self.ingredientsPage)  # Ingredients page
        self.stackedWidget.addWidget(self.recipesPage)  # Recipes page
        self.stackedWidget.addWidget(self.recipeDetailsPage)  # Recipe details page

        # Set the home page as the initial visible page
        self.stackedWidget.setCurrentWidget(self.homeWidget)

        # Lock the main window size to ensure consistency across screens whatever their size
        self.setFixedSize(600, 780)

        # Set up navigation between pages when different buttons are clicked
        # Home page buttons
        self.ui.ingredientsButton.clicked.connect(self.openIngredientsPage)  # Navigate to the ingredients page
        self.ui.recipeButton.clicked.connect(self.openRecipesPage)  # Navigate to the recipes page

        # Back button in the Ingredients page
        self.ingredientsPage.backButton.clicked.connect(self.showHomePage)  # Return to the home page

        # Back button in the Recipes page
        self.recipesPage.backButton.clicked.connect(self.showHomePage)  # Return to the home page

        # When a recipe is selected in the Recipes page, open the details page
        self.recipesPage.recipeClicked.connect(self.openRecipeDetailsPage)

        # Back button in the Recipe Details page
        self.recipeDetailsPage.backButtonClicked.connect(self.openRecipesPage)  # Return to the recipes page

    def openIngredientsPage(self):
        self.stackedWidget.setCurrentWidget(self.ingredientsPage)

    def openRecipesPage(self):
        self.stackedWidget.setCurrentWidget(self.recipesPage)

    def openRecipeDetailsPage(self, recipeData):
        self.recipeDetailsPage.updateContent(recipeData)  # Populate the details page with recipe data
        self.stackedWidget.setCurrentWidget(self.recipeDetailsPage)  # Switch to the details page

    def showHomePage(self):
        self.stackedWidget.setCurrentWidget(self.homeWidget)


if __name__ == "__main__":
    # Start the application
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()  # Show the main window
    sys.exit(app.exec_())
