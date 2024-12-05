from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowTitle("SSH Meals")
        Dialog.setFixedSize(600, 780)  # Fixed size for all screens
        Dialog.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.091, y1:0.101636, x2:0.991379, y2:0.977, stop:0 rgba(128, 194, 255, 255), stop:1 rgba(255, 255, 255, 255));")

        # Main widget for the dialog
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 600, 780))
        self.widget.setObjectName("widget")

        # Title Label
        self.lblSSHmeals = QtWidgets.QLabel(self.widget)
        self.lblSSHmeals.setGeometry(QtCore.QRect(60, 50, 481, 101))  # Title remains the same
        self.lblSSHmeals.setStyleSheet("""
            font: 75 48pt 'Georgia';
            color: rgba(0, 51, 102, 1);
            background-color: transparent;
        """)
        self.lblSSHmeals.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblSSHmeals.setObjectName("lblSSHmeals")

        # Ingredients Button
        self.ingredientsButton = QtWidgets.QPushButton(self.widget)
        self.ingredientsButton.setGeometry(QtCore.QRect(140, 320, 300, 120))  # Slightly moved up
        self.ingredientsButton.setStyleSheet(self._button_stylesheet())
        self._set_dynamic_font(self.ingredientsButton, "Ingredients")
        self.ingredientsButton.setObjectName("ingredientsButton")

        # Recipe Button
        self.recipeButton = QtWidgets.QPushButton(self.widget)
        self.recipeButton.setGeometry(QtCore.QRect(140, 500, 300, 120))  # Larger gap between buttons
        self.recipeButton.setStyleSheet(self._button_stylesheet())
        self._set_dynamic_font(self.recipeButton, "Recipe Suggestions", multiline=True)  # Allow multi-line text
        self.recipeButton.setObjectName("recipeButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def _button_stylesheet(self):
        """Returns consistent button styling."""
        return """
            QPushButton {
                border-radius: 25px;
                border-color: rgba(255, 215, 0, 1);
                background-color: rgba(0, 102, 204, 1);
                font: 75 24pt 'Verdana';
                color: white;
                padding: 0px 5px; /* Ensure vertical space for multi-line text */
            }
            QPushButton:hover {
                background-color: rgba(0, 77, 153, 1);
            }
        """

    def _set_dynamic_font(self, button, text, multiline=False):
        """Dynamically set the font size for button text to fit inside the button."""
        # If multiline is enabled, adjust text to include line breaks
        if multiline:
            text = "Recipe\nSuggestions"  # Force correct multi-line format

        button.setText(text)
        font = QtGui.QFont("Verdana")
        font.setPointSize(24)  # Default font size
        button.setFont(font)

        # Adjust font size to ensure text fits inside the button
        metrics = QtGui.QFontMetrics(font)
        while (metrics.boundingRect(button.text()).width() > button.width() - 10 or
               metrics.boundingRect(button.text()).height() > button.height() - 10):
            font.setPointSize(font.pointSize() - 1)  # Reduce font size
            button.setFont(font)
            metrics = QtGui.QFontMetrics(font)

        # Center the text properly within the button
        button.setStyleSheet(button.styleSheet() + "padding: 0px 5px;")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "SSH Meals"))
        self.lblSSHmeals.setText(_translate("Dialog", "SSH MEALS"))
