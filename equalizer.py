
"""
Filename: equalizer.py
Author: Jesman Anthonypillai
Email: jesman23@gmail.com
Date: 2025-08-05
Version: 1.12
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

class Equalizer(QWidget):
    def __init__(self):
        super().__init__()

        self.is_playing = False
        self.audio_file = None
        self.is_slider_pressed = False  # To track if slider is being manually moved
        self.total_length = 0  # To store total audio length in seconds

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

        # Vibrant colors for the equalizer
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
        self.setGeometry(300, 300, 400, 500)

        self.setStyleSheet("""
            background-color: #1C1C1C;
            color: gold;
            font-size: 22px;
            font-family: 'Arial';
        """)

        layout = QVBoxLayout()
        self.graphics_view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.graphics_view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        layout.addWidget(self.graphics_view)

        button_style = """
            QPushButton {
                background-color: #FF7F50;
                color: white;
                font-size: 22px;
                font-weight: bold;
                border: none;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #FF4500;
            }
            QPushButton:pressed {
                background-color: #FF6347;
            }
        """

        self.open_button = QPushButton('ஒலிக்கோப்பைத் திறக்கவும்')
        self.open_button.setStyleSheet(button_style)
        self.open_button.clicked.connect(self.open_file)
        layout.addWidget(self.open_button)

        self.play_button = QPushButton('இசை')
        self.play_button.setStyleSheet(button_style)
        self.play_button.clicked.connect(self.play_audio)
        layout.addWidget(self.play_button)

        self.pause_button = QPushButton('இடைநிறுத்து')
        self.pause_button.setStyleSheet(button_style)
        self.pause_button.clicked.connect(self.pause_audio)
        layout.addWidget(self.pause_button)

        self.stop_button = QPushButton('நிறுத்து')
        self.stop_button.setStyleSheet(button_style)
        self.stop_button.clicked.connect(self.stop_audio)
        layout.addWidget(self.stop_button)

        slider_layout = QHBoxLayout()
        self.position_slider = QSlider(Qt.Horizontal)
        self.position_slider.setRange(0, 100)
        self.position_slider.sliderMoved.connect(self.set_position)
        self.position_slider.sliderPressed.connect(self.slider_pressed)
        self.position_slider.sliderReleased.connect(self.slider_released)
        slider_layout.addWidget(self.position_slider)

        self.time_label = QLabel('00:00 / 00:00')
        self.time_label.setAlignment(Qt.AlignRight)
        self.time_label.setStyleSheet("font-weight: bold; font-size: 22px;")
        slider_layout.addWidget(self.time_label)
        layout.addLayout(slider_layout)

        self.volume_slider = QSlider(Qt.Horizontal)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(100)
        self.volume_slider.valueChanged.connect(self.set_volume)
        volume_label = QLabel('ஒலி அளவு:')
        volume_label.setStyleSheet("font-weight: bold; font-size: 22px;")
        layout.addWidget(volume_label)
        self.volume_slider.setStyleSheet("font-weight: bold; font-size: 22px;")
        layout.addWidget(self.volume_slider)

        self.setLayout(layout)

    def open_file(self):
        options = QFileDialog.Options()
        self.audio_file, _ = QFileDialog.getOpenFileName(self, "Open Audio File", "", "Audio Files (*.mp3 *.wav);;All Files (*)", options=options)
        if self.audio_file:
            try:
                pygame.mixer.music.load(self.audio_file)
                self.open_button.setText(f'நீங்கள் கேட்கும் ஒலிக்கோப்பு: {self.audio_file.split("/")[-1]}')
                # Estimate total length using pygame.mixer.Sound
                sound = pygame.mixer.Sound(self.audio_file)
                self.total_length = sound.get_length()
                print(f"Audio file loaded successfully: {self.audio_file}")
            except Exception as e:
                print(f"Error loading audio file: {e}")

    def play_audio(self):
        if self.audio_file is None:
            print("No audio file loaded.")
            return
        if not self.is_playing:
            try:
                pygame.mixer.music.play()
                self.is_playing = True
                self.timer.start(100)
                print("Audio playing.")
            except Exception as e:
                print(f"Error playing audio: {e}")

    def pause_audio(self):
        if self.is_playing:
            pygame.mixer.music.pause()
            self.is_playing = False
            self.timer.stop()
            print("Audio paused.")

    def stop_audio(self):
        if self.is_playing:
            pygame.mixer.music.stop()
            self.is_playing = False
            self.timer.stop()
            print("Audio stopped.")

    def set_volume(self, value):
        pygame.mixer.music.set_volume(value / 100.0)
        print(f"Volume set to: {value}")

    def set_position(self, position):
        if self.is_slider_pressed:
            new_position = (position * self.total_length) / 100
            pygame.mixer.music.play(start=new_position)
            self.is_playing = True
            self.timer.start(100)
            print(f"Playback position set to: {new_position} seconds")

    def slider_pressed(self):
        self.is_slider_pressed = True

    def slider_released(self):
        self.is_slider_pressed = False

    def update_bar(self):
        self.bands = [random.randint(-15, 15) for _ in range(5)]
        self.scene.clear()
        bar_width = 30
        spacing = 10
        for i, band in enumerate(self.bands):
            bar_height = max(0, 100 + band * 5)
            color = self.color_palette[i % len(self.color_palette)]
            bar_item = self.scene.addRect(
                i * (bar_width + spacing),
                150 - bar_height,
                bar_width,
                bar_height,
                QPen(Qt.NoPen),
                QBrush(color)
            )
        self.update_playback_time()

    def update_playback_time(self):
        current_time = pygame.mixer.music.get_pos() / 1000  # Get current time in seconds
        if not self.is_slider_pressed and self.total_length > 0:
            slider_position = (current_time * 100) / self.total_length
            self.position_slider.setValue(int(slider_position))
        current_min = int(current_time // 60)
        current_sec = int(current_time % 60)
        total_min = int(self.total_length // 60)
        total_sec = int(self.total_length % 60)
        self.time_label.setText(f"{current_min:02}:{current_sec:02} / {total_min:02}:{total_sec:02}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Equalizer()
    ex.show()
    sys.exit(app.exec_())
