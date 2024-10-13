#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import sys
import pygame
import vlc
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Equalizer(QWidget):
    def __init__(self):
        super().__init__()

        self.is_playing = False
        self.audio_file = None
        self.is_slider_pressed = False  # To track if slider is being manually moved

        # Initialize VLC instance
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()

        # Initialize the scene for drawing bars
        self.scene = QGraphicsScene(self)
        self.graphics_view = QGraphicsView(self.scene, self)
        self.graphics_view.setFixedSize(300, 150)

        # Initialize UI components
        self.init_ui()

        # Initialize pygame mixer for audio playback
        pygame.mixer.init()

        # Set up a timer for updating the bars and slider
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_bar)

        # Vibrant colors for the equalizer (gradients and rainbow-style colors)
        
        
        self.color_palette = [
    QColor(255, 69, 0),    # Red-Orange
    QColor(255, 140, 0),   # Dark Orange
    QColor(255, 215, 0),   # Gold
    QColor(34, 139, 34),   # Forest Green
    QColor(0, 128, 255),   # Light Blue
    QColor(75, 0, 130),    # Indigo
    QColor(238, 130, 238), # Violet
    QColor(0, 255, 0),     # Lime
    QColor(0, 255, 255),   # Cyan
    QColor(255, 105, 180), # Hot Pink
    QColor(255, 20, 147),  # Deep Pink
    QColor(255, 165, 0),   # Orange
    QColor(70, 130, 180),  # Steel Blue
    QColor(255, 182, 193), # Light Pink
    QColor(75, 0, 130),    # Indigo
    QColor(128, 0, 128),   # Purple
    QColor(240, 128, 128), # Light Coral
    QColor(255, 255, 0),   # Yellow
    QColor(0, 128, 0),     # Green
    QColor(100, 149, 237), # Cornflower Blue
    QColor(173, 216, 230), # Light Blue
]


    def init_ui(self):
        # Set up the UI components
        self.setWindowTitle('ஒலிவடிவக்காட்ச்சி (C) 2024')
        self.setGeometry(300, 300, 400, 500)  # Adjust size to a manageable size

        # Set vibrant color mode with font size 22 and global green font color
        self.setStyleSheet("""
            background-color: #1C1C1C;  /* Dark background */
            color: gold;  /* Change font color ----- */
            font-size: 22px;
            font-family: 'Arial';  /* Change as needed */
        """)

        # Layout setup
        layout = QVBoxLayout()

        # Disable scroll bars
        self.graphics_view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.graphics_view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        layout.addWidget(self.graphics_view)

        # Set button styles with bold font and bright colors
        button_style = """
            QPushButton {
                background-color: #FF7F50;  /* Coral color */
                color: white;  
                font-size: 22px;  
                font-weight: bold;  
                border: none;  
                border-radius: 5px;  
                padding: 10px;  
            }
            QPushButton:hover {
                background-color: #FF4500;  /* OrangeRed */
            }
            QPushButton:pressed {
                background-color: #FF6347;  /* Tomato */
            }
        """

        # Open button to load the audio file
        self.open_button = QPushButton('ஒலிக்கோப்பைத் திறக்கவும்')
        self.open_button.setStyleSheet(button_style)
        self.open_button.clicked.connect(self.open_file)
        layout.addWidget(self.open_button)

        # Play button
        self.play_button = QPushButton('இசை')
        self.play_button.setStyleSheet(button_style)
        self.play_button.clicked.connect(self.play_audio)
        layout.addWidget(self.play_button)

        # Pause button
        self.pause_button = QPushButton('இடைநிறுத்து')
        self.pause_button.setStyleSheet(button_style)
        self.pause_button.clicked.connect(self.pause_audio)
        layout.addWidget(self.pause_button)

        # Stop button
        self.stop_button = QPushButton('நிறுத்து')
        self.stop_button.setStyleSheet(button_style)
        self.stop_button.clicked.connect(self.stop_audio)
        layout.addWidget(self.stop_button)

        # Horizontal layout to place the slider and the time label side by side
        slider_layout = QHBoxLayout()

        # Playback position slider
        self.position_slider = QSlider(Qt.Horizontal)
        self.position_slider.setRange(0, 100)  # Initial range
        self.position_slider.sliderMoved.connect(self.set_position)
        self.position_slider.sliderPressed.connect(self.slider_pressed)
        self.position_slider.sliderReleased.connect(self.slider_released)
        slider_layout.addWidget(self.position_slider)

        # Label to show playback time with bold font, placed at the end of the slider
        self.time_label = QLabel('00:00 / 00:00')  # Format: Current time / Total time
        self.time_label.setAlignment(Qt.AlignRight)
        self.time_label.setStyleSheet("font-weight: bold; font-size: 22px;")  # Make label text bold and size 22
        slider_layout.addWidget(self.time_label)

        layout.addLayout(slider_layout)  # Add the slider layout to the main layout

        # Volume control slider
        self.volume_slider = QSlider(Qt.Horizontal)
        self.volume_slider.setRange(0, 100)  # Volume range from 0 to 100
        self.volume_slider.setValue(100)  # Set default volume to 100
        self.volume_slider.valueChanged.connect(self.set_volume)
        
       
        
        volume_label = QLabel('ஒலி அளவு:')
        volume_label.setStyleSheet("font-weight: bold; font-size: 22px;")
        layout.addWidget(volume_label)

        # Apply style to the slider and add it to the layout
        self.volume_slider.setStyleSheet("font-weight: bold; font-size: 22px;")
        layout.addWidget(self.volume_slider)

        self.setLayout(layout)  # Apply the layout to the widget

        

        
        

    def open_file(self):
        # Open a file dialog to select an audio file
        options = QFileDialog.Options()
        self.audio_file, _ = QFileDialog.getOpenFileName(self, "Open Audio File", "", "Audio Files (*.mp3 *.wav);;All Files (*)", options=options)

        if self.audio_file:
            try:
                # Load audio file into VLC player
                media = self.instance.media_new(self.audio_file)
                self.player.set_media(media)
                
                # Update the button text to show the opened file name
                self.open_button.setText(f'நீங்கள் கேட்கும் ஒலிக்கோப்பு: {self.audio_file.split("/")[-1]}')
                print(f"Audio file loaded successfully: {self.audio_file}")
            except Exception as e:
                print(f"Error loading audio file: {e}")

    def play_audio(self):
        # Play the audio
        if self.audio_file is None:
            print("No audio file loaded.")
            return

        if not self.player.is_playing():  # Check if music is not playing
            try:
                self.player.play()  # Attempt to play
                self.is_playing = True
                self.timer.start(100)  # Start the timer to update the bar every 100 ms
                print("Audio playing.")
            except Exception as e:
                print(f"Error playing audio: {e}")

    def pause_audio(self):
        # Pause the audio
        if self.player.is_playing():
            self.player.pause()  # Pause if currently playing
            self.is_playing = False
            self.timer.stop()  # Stop the timer when paused
            print("Audio paused.")

    def stop_audio(self):
        # Stop the audio
        if self.player.is_playing():
            self.player.stop()
            self.is_playing = False
            self.timer.stop()  # Stop the timer when stopped
            print("Audio stopped.")



    #END GUI
    def set_volume(self, value):
        # Set volume of the audio player
        self.player.audio_set_volume(value)
        print(f"Volume set to: {value}")

    def set_position(self, position):
        # Set the playback position only if the slider is being moved manually
        if self.is_slider_pressed:
            total_length = self.player.get_length() // 1000  # Total length in seconds
            new_position = (position * total_length) // 100  # Calculate new position in milliseconds
            self.player.set_time(new_position * 1000)  # Set the playback position in milliseconds
            print(f"Playback position set to: {new_position} seconds")

    def slider_pressed(self):
        # Mark the slider as being pressed
        self.is_slider_pressed = True

    def slider_released(self):
        # Mark the slider as released
        self.is_slider_pressed = False





    def update_bar(self):
        # Generate random band values to simulate equalizer bars
        self.bands = [random.randint(-15, 15) for _ in range(5)]

        # Clear the previous bars from the scene
        self.scene.clear()

        # Calculate and draw bars based on band values
        bar_width = 30
        spacing = 10
        for i, band in enumerate(self.bands):
            bar_height = max(0, 100 + band * 5)

            # Get the gradient color based on bar index
            color = self.color_palette[i % len(self.color_palette)]

            bar_item = self.scene.addRect(
                i * (bar_width + spacing),
                150 - bar_height,
                bar_width,
                bar_height,
                QPen(Qt.NoPen),
                QBrush(color)
            )

        # Update playback time and position slider
        self.update_playback_time()
 
        
    def update_playback_time(self):
        # Update the playback time label and position slider if the slider isn't being manually moved
        current_time = self.player.get_time() // 1000  # Get current time in seconds
        total_time = self.player.get_length() // 1000  # Get total time in seconds

        if not self.is_slider_pressed:  # Only update the slider if it's not being dragged
            if total_time > 0:
                slider_position = (current_time * 100) // total_time
                self.position_slider.setValue(slider_position)

        # Calculate minutes and seconds for current and total times
        current_min = current_time // 60
        current_sec = current_time % 60
        total_min = total_time // 60
        total_sec = total_time % 60

        # Update the label with formatted time
        self.time_label.setText(f"{current_min:02}:{current_sec:02} / {total_min:02}:{total_sec:02}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Equalizer()
    ex.show()
    sys.exit(app.exec_())
       



