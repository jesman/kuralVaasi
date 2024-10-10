#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Filename: mp3_generator.py
Author: Jesman Anthonypillai
Email: jesman23@gmail.com
Date: 2024-09-24

Version: 1.0

Description: This script provides functionality to generate Tamil text-to-speech
             using gTTS (Google Text-to-Speech) and play the generated audio using
             the Pygame mixer module. It allows users to input Tamil text, generate 
             an MP3 file, and listen to the generated audio.

License: MIT License

"""



import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel
import gtts
import pygame
import os

class TTSApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        pygame.mixer.init()

    def initUI(self):
        self.layout = QVBoxLayout()

        # Add label above input field
        self.label = QLabel("உங்கள் உரையை உள்ளிடவும்:")
        self.layout.addWidget(self.label)

        # Create text input with placeholder text
        self.text_input = QLineEdit(self)
        self.text_input.setPlaceholderText("உங்கள் உரையை உள்ளிடவும்... ")  # Set the placeholder text inside the field
        self.layout.addWidget(self.text_input)

        # Button to generate speech file
        self.speech_button = QPushButton("ஒலிக்கோப்பு உருவாக்க ", self)
        self.speech_button.clicked.connect(self.generate_speech)
        self.layout.addWidget(self.speech_button)

        # Button to play generated speech
        self.play_button = QPushButton("ஒலிக்க விடு", self)
        self.play_button.clicked.connect(self.play_speech)
        self.layout.addWidget(self.play_button)

        self.setLayout(self.layout)
        self.setWindowTitle("உரை உரையாடல் உருவாக்கி ")
        self.setGeometry(100, 100, 300, 200)

    def generate_speech(self):
        text = self.text_input.text()
        if text:
            # Extract the first two words for the filename
            words = text.split()[:2]  # Get the first two words
            if len(words) == 0:
                file_name = "output.mp3"
            else:
                file_name = "_".join(words) + ".mp3"  # Join words with underscores

            # Sanitize the file name (keeping the period for the extension)
            file_name = file_name.replace(' ', '_').replace(',', '')  # Only replace spaces and commas

            # Generate the speech file
            tts = gtts.gTTS(text=text, lang='ta')
            tts.save(file_name)

            self.label.setText(f"உரை '{file_name}' என்ற பெயரில் உருவாக்கப்பட்டது. (Speech generated as '{file_name}'.)")
            self.audio_file = file_name  # Store the file name to play later
        else:
            self.label.setText("தயவுசெய்து உரையை உள்ளிடவும். (Please enter some text.)")

    def play_speech(self):
        # Use the generated file name instead of the fixed "output.mp3"
        if hasattr(self, 'audio_file') and os.path.exists(self.audio_file):
            pygame.mixer.music.load(self.audio_file)
            pygame.mixer.music.play()
        else:
            self.label.setText("முதலில் உரை உருவாக்கவும். (Please generate speech first.)")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = TTSApp()
    ex.show()
    sys.exit(app.exec_())


