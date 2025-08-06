
"""
Filename: help.py
Author: Jesman Anthonypillai
Email: jesman23@gmail.com
Date: 2025-08-05
Version: 1.12

Description: This script provides functionality to generate help 
             Module for main app

License: MIT License
"""

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton


class show_help(QWidget):
    def __init__(self):
        super().__init__()

        # Set the window title
        self.setWindowTitle("உதவி")

        # Create a vertical layout
        layout = QVBoxLayout()

        # Add help content
        help_text = (
            "குறள் கேட்டு அதன்வழி வாழ்வோம்!\n\n"
            "இந்த மென்பொருள், திருக்குறளை கேட்டு அதன் அறிவுரைகளை நம் வாழ்க்கையில்\n"
            "கடைபிடிக்க உதவுகிறது.\n"
            "1330 குறளின் அறிவுரைகளையும் கேட்டு அதன் தத்துவங்களை உள்வாங்கிப் படிப்பதுடன்,\n"
            "அதை ஒலிவடிவில் சேமித்து, நீங்கள் பயன்பெறுவதுடன் பிறருடன் பகிர்ந்து தமிழுக்கும் சேவை செய்யுங்கள்.\n\n"
            "முக்கிய அம்சங்கள்:\n"
            "1. திருக்குறள் தேடல்: நீங்கள் விரும்பிய குறள்களை எளிதில் தேடி கண்டுபிடிக்க முடியும்.\n"
            "2. ஒலிக் கோப்பு உருவாக்கம்: தேடல் செய்த குறள்களைப் பயன்படுத்தி அவற்றை ஒலிக்கோப்பாக தயாரிக்கலாம்.\n"
            "3. ஒலிவடிவில் கேட்கலாம்: பக்கப் பட்டியில் உள்ள 'ஒலிவடிவில் கேட்க' பொத்தானை அழுத்தி, உங்கள் "
            "தெரிவை உள்ளிட்டு கேட்கலாம்.\n\n"
            "இந்த மென்பொருள் PyQt5 மற்றும் பிற திறந்த வெளி தொழில்நுட்பங்களின் மூலம் உருவாக்கப்பட்டது.\n"
            "பயனுள்ள தனித்தன்மைகளுடன் எளிய வழியில் கிரகிக்க சிறப்பாக வடிவமைக்கப்பட்டுள்ளது.\n\n"
            "இந்த மென்பொருளைப் பற்றி:\n"
            "பதிப்பு 1.0\n"
            "உருவாக்கம் மற்றும் நிர்வாகம்:\n"
            "ஜெஸ்மன் அந்தோணிப்பிள்ளை\n"
            "Jesman Anthonypillai\n"
            "jesman23@gmail.com\n"
        )

        # Create a QLabel to display the help text
        help_label = QLabel(help_text)  # Create QLabel with the help text
        help_label.setStyleSheet("font-size: 18px; color: blue; font-weight: bold;")  # Set style for QLabel
        
        help_label.setWordWrap(True)  # Ensure text wraps within the window
        layout.addWidget(help_label)

        # Create a close button
        close_button = QPushButton("மூடு")  # Button text in Tamil
        close_button.setStyleSheet("background-color: lightgray; border: 1px solid gray;")  # Set style for QPushButton
        
        close_button.clicked.connect(self.close)  # Connect the button to the close method
        layout.addWidget(close_button)

        # Set the layout for the widget
        self.setLayout(layout)


# Usage example in your main application
if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    help_window = show_help()
    help_window.show()
    sys.exit(app.exec_())
