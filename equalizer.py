#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Filename: equalizer.py
Author: Jesman Anthonypillai
Email: jesman23@gmail.com
Date: 2024-07-14
Version: 1.0
Description: This script provides functionality to generate Tamil text-to-speech
             using gTTS (Google Text-to-Speech) and play the generated audio using
             the Pygame mixer module. It allows users to input Tamil text, generate 
             an MP3 file, and listen to the generated audio.

License: MIT License

"""


import random
import sys
import pygame

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Equalizer(QMainWindow):  # Change from QWidget to QMainWindow
    def __init__(self):
        super().__init__()
        self.bands = [random.randint(-15, 15) for _ in range(5)]  # Simulate random band values
        self.is_playing = False  # Track playback state
        self.audio_file = None  # Initialize audio file path

        # Initialize the scene for drawing bars
        self.scene = QGraphicsScene(self)
        self.graphics_view = QGraphicsView(self.scene, self)
        self.graphics_view.setFixedSize(300, 150)

        self.init_ui()

        # Initialize pygame mixer for audio playback
        pygame.mixer.init()

        # Set up a timer for updating the bars
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_bar)  # Connect timer to update_bar method

        # Color definitions for the equalizer
        self.orange1 = QColor(255, 165, 0)
        self.orange2 = QColor(255, 155, 0)

    def init_ui(self):
        # Set up the UI components
        self.setWindowTitle('ஒலிவடிவக்காட்ச்சி(C) 2024')
        self.setGeometry(100, 100, 300, 200)

        # Set dark mode style
        self.setStyleSheet("background-color: #2E2E2E; color: white;")
        
        # Layout setup
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        layout.addWidget(self.graphics_view)  # Add the graphics view to the layout

        self.open_button = QPushButton('ஒலிக்கோப்பைத் திறக்கவும்')
        self.open_button.clicked.connect(self.open_file)
        layout.addWidget(self.open_button)

        self.play_button = QPushButton('இசைக்க | நிறுத்த | மீண்டும் இசைக்க')
        self.play_button.clicked.connect(self.play_pause)
        layout.addWidget(self.play_button)

        central_widget.setLayout(layout)

    def update_bar(self):
        # Generate random band values to simulate equalizer bars
        self.bands = [random.randint(-15, 15) for _ in range(5)]

        # Clear the previous bars from the scene
        self.scene.clear()

        # Calculate and draw bars based on band values
        bar_width = 40
        spacing = 10
        for i, band in enumerate(self.bands):
            bar_height = max(0, 100 + band * 5)  # Calculate height based on band value

            # Get the color based on bar height
            color = self.get_color(bar_height)  # Use self.get_color() if it's a method of the class

            bar_item = self.scene.addRect(
                i * (bar_width + spacing),
                150 - bar_height,  # Adjust position to draw upwards
                bar_width,
                bar_height,
                QPen(Qt.NoPen),  # No border
                QBrush(color)    # Set color as brush
            )

    def get_color(self, bar_height):
        # Define minimum and maximum values for the color range
        min_value = 100
        max_value = 150

        # Calculate a ratio between 0 and 1 based on bar height
        ratio = (bar_height - min_value) / (max_value - min_value)
        ratio = max(0, min(ratio, 1))  # Clamp ratio between 0 and 1

        # Define starting and ending colors using RGB values
        start_color = QColor(255, 165, 0)  # RGB for orange
        end_color = QColor(255, 0, 0)      # RGB for red

        # Use linear interpolation to get a color between start and end
        color = QColor(
            start_color.red() * (1 - ratio) + end_color.red() * ratio,
            start_color.green() * (1 - ratio) + end_color.green() * ratio,
            start_color.blue() * (1 - ratio) + end_color.blue() * ratio
        )
        return color

    def open_file(self):
        # Open a file dialog to select an audio file
        options = QFileDialog.Options()
        self.audio_file, _ = QFileDialog.getOpenFileName(self, "Open Audio File", "", "Audio Files (*.mp3 *.wav);;All Files (*)", options=options)

        if self.audio_file:
            try:
                pygame.mixer.music.load(self.audio_file)
                print(f"Audio file loaded successfully: {self.audio_file}")
            except pygame.error as e:
                print(f"Error loading audio file: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

    def play_pause(self):
        # Play or pause the audio
        if self.audio_file is None:
            print("No audio file loaded.")
            return

        if not pygame.mixer.music.get_busy():  # Check if music is not playing
            try:
                pygame.mixer.music.play()  # Attempt to play
                self.is_playing = True
                self.timer.start(100)  # Start the timer to update the bar every 100 ms
                print("Audio playing.")
            except pygame.error as e:
                print(f"Error playing audio: {e}")
        else:
            pygame.mixer.music.pause()  # Pause if currently playing
            self.is_playing = False
            self.timer.stop()  # Stop the timer when paused
            print("Audio paused.")
