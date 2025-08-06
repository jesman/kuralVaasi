
"""
Filename: main.py
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

from equalizer import Equalizer
from mp3_generator import TTSApp
from help import show_help

class ThirukkuralApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('குறள் கேட்டு அதன்வழி வாழ்வோம்')
        self.setGeometry(100, 100, 1000, 600)

        self.setStyleSheet("""
            QMainWindow {
                background-color: #D7CCC8;  /* Light beige-brown background */
                color: #333333;  /* Soft gray text for readability */
                font-weight: bold;
            }
            QPushButton {
                background-color: #E6D7B9;  /* Soft tan for buttons */
                color: #333333;  /* Soft gray text */
                border: 1px solid #BCAAA4;  /* Slightly darker brown border */
                padding: 10px;
                font-size: 14px;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #BCAAA4;  /* Slightly darker brown on hover */
                color: #FFFFFF;  /* White text for contrast */
            }
            QListWidget {
                background-color: #D7CCC8;  /* Light beige-brown background */
                color: #333333;  /* Soft gray text */
                border: 1px solid #BCAAA4;  /* Slightly darker brown border */
                border-radius: 5px;
                font-weight: bold;
            }
            QTextEdit {
                background-color: #D7CCC8;  /* Light beige-brown background */
                color: #333333;  /* Soft gray text */
                border: 1px solid #BCAAA4;  /* Slightly darker brown border */
                border-radius: 5px;
                font-weight: bold;
            }
            QLineEdit {
                background-color: #D7CCC8;  /* Light beige-brown background */
                color: #333333;  /* Soft gray text */
                border: 1px solid #BCAAA4;  /* Slightly darker brown border */
                padding: 5px;
                border-radius: 5px;
                font-weight: bold;
            }
            QTabWidget::pane {
                border: 1px solid #BCAAA4;  /* Slightly darker brown border */
                background-color: #D7CCC8;  /* Light beige-brown background */
                border-radius: 5px;
            }
            QTabBar::tab {
                background: #E6D7B9;  /* Soft tan tab background */
                color: #333333;  /* Soft gray text */
                padding: 10px;
                border-radius: 5px;
                margin-right: 2px;
                font-weight: bold;
            }
            QTabBar::tab:selected {
                background: #FFFFE4;  /* Very pale yellow for selected tab */
                color: #333333;  /* Soft gray text */
                font-weight: bold;
            }
            QFrame {
                background-color: #D7CCC8;  /* Light beige-brown background */
                border: 1px solid #BCAAA4;  /* Slightly darker brown border */
                border-radius: 5px;
            }
        """)

        self.kural_data = self.load_kural_data('./data/kural.txt')
        self.kural_tam_data = self.load_kural_data('./data/kural_tam.txt')

        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.main_layout = QHBoxLayout(self.main_widget)

        self.create_sidebar()
        self.create_central_content()

    def load_kural_data(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return [line.strip() for line in file.readlines() if line.strip()]
        except Exception as e:
            print(f"Error loading data from {file_path}: {e}")
            return []

    def create_sidebar(self):
        self.sidebar = QFrame()
        self.sidebar.setFrameShape(QFrame.StyledPanel)
        self.sidebar.setFixedWidth(200)

        sidebar_layout = QVBoxLayout()
        sidebar_layout.setContentsMargins(10, 10, 10, 10)
        sidebar_layout.setSpacing(20)

        btn_thirukkural = QPushButton("திருக்குறள்")
        btn_thirukkural.clicked.connect(lambda: self.switch_view("Thirukkural"))

        btn_audio_maker = QPushButton("ஒலிக்கோப்பு உருவாக்கி")
        btn_audio_maker.clicked.connect(lambda: self.switch_view("AudioMaker"))

        btn_equalizer = QPushButton("ஒலிவடிவில் கேட்க")
        btn_equalizer.clicked.connect(lambda: self.switch_view("Equalizer"))

        help_button = QPushButton("உதவி")
        help_button.clicked.connect(lambda: self.switch_view("Help"))

        btn_exit = QPushButton("வெளியேறு")
        btn_exit.clicked.connect(self.close)

        sidebar_layout.addWidget(btn_thirukkural)
        sidebar_layout.addWidget(btn_audio_maker)
        sidebar_layout.addWidget(btn_equalizer)
        sidebar_layout.addWidget(help_button)
        sidebar_layout.addStretch()
        sidebar_layout.addWidget(btn_exit)

        self.sidebar.setLayout(sidebar_layout)
        self.main_layout.addWidget(self.sidebar)

    def create_central_content(self):
        self.stacked_widget = QStackedWidget()

        self.thirukkural_tabs = QTabWidget()
        self.create_arathuppaal_tab()
        self.create_porutpaal_tab()
        self.create_kamathuppaal_tab()
        self.stacked_widget.addWidget(self.thirukkural_tabs)

        self.equalizer_widget = Equalizer()
        self.stacked_widget.addWidget(self.equalizer_widget)

        self.audio_maker_widget = TTSApp()
        self.stacked_widget.addWidget(self.audio_maker_widget)

        self.help_widget = show_help()
        self.stacked_widget.addWidget(self.help_widget)

        self.main_layout.addWidget(self.stacked_widget)
        self.stacked_widget.setCurrentWidget(self.thirukkural_tabs)

    def switch_view(self, view_name):
        if view_name == "Thirukkural":
            self.stacked_widget.setCurrentWidget(self.thirukkural_tabs)
        elif view_name == "AudioMaker":
            self.stacked_widget.setCurrentWidget(self.audio_maker_widget)
        elif view_name == "Help":
            self.stacked_widget.setCurrentWidget(self.help_widget)
        elif view_name == "Equalizer":
            self.stacked_widget.setCurrentWidget(self.equalizer_widget)

    def create_arathuppaal_tab(self):
        arathuppaal_tab = QWidget()
        layout = QHBoxLayout()

        self.chapters_list = QListWidget()
        for chapter in self.kural_data[:38]:
            self.chapters_list.addItem(chapter)

        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("அதிகாரம் பெயர் அல்லது குறள் எண் தேடவும்...")

        search_button = QPushButton("தேடு")
        search_button.clicked.connect(self.search_kural)

        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(self.chapters_list)
        self.chapter_content = QTextEdit()
        splitter.addWidget(self.chapter_content)
        self.chapter_content.setReadOnly(True)
        splitter.setSizes([150, 400])

        self.chapters_list.currentRowChanged.connect(self.display_arathuppaal_chapter)

        search_layout = QHBoxLayout()
        search_layout.addWidget(self.search_bar)
        search_layout.addWidget(search_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(search_layout)
        main_layout.addWidget(splitter)

        arathuppaal_tab.setLayout(main_layout)
        self.thirukkural_tabs.addTab(arathuppaal_tab, "அறத்துப்பால்")

    def create_porutpaal_tab(self):
        porutpaal_tab = QWidget()
        layout = QHBoxLayout()

        self.chapters_list_porutpaal = QListWidget()
        for chapter in self.kural_data[38:108]:
            self.chapters_list_porutpaal.addItem(chapter)

        self.chapter_content_porutpaal = QTextEdit()
        self.chapter_content_porutpaal.setReadOnly(True)

        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(self.chapters_list_porutpaal)
        splitter.addWidget(self.chapter_content_porutpaal)
        splitter.setSizes([150, 400])

        self.chapters_list_porutpaal.currentRowChanged.connect(self.display_porutpaal_chapter)

        layout.addWidget(splitter)
        porutpaal_tab.setLayout(layout)
        self.thirukkural_tabs.addTab(porutpaal_tab, "பொருட்பால்")

    def create_kamathuppaal_tab(self):
        kamathuppaal_tab = QWidget()
        layout = QHBoxLayout()

        self.chapters_list_kamathuppaal = QListWidget()
        for chapter in self.kural_data[108:]:
            self.chapters_list_kamathuppaal.addItem(chapter)

        self.chapter_content_kamathuppaal = QTextEdit()
        self.chapter_content_kamathuppaal.setReadOnly(True)

        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(self.chapters_list_kamathuppaal)
        splitter.addWidget(self.chapter_content_kamathuppaal)
        splitter.setSizes([150, 400])

        self.chapters_list_kamathuppaal.currentRowChanged.connect(self.display_kamathuppaal_chapter)

        layout.addWidget(splitter)
        kamathuppaal_tab.setLayout(layout)
        self.thirukkural_tabs.addTab(kamathuppaal_tab, "காமத்துப்பால்")

    def display_arathuppaal_chapter(self, index):
        if index >= 0 and index < 38:
            start_index = index * 10
            end_index = start_index + 10
            chapter_verses = self.kural_tam_data[start_index:end_index]
            formatted_text = "\n\n".join([
                f"(குறள் எண் : {start_index + i + 1})\n{verse}" 
                for i, verse in enumerate(chapter_verses)
            ])
            self.chapter_content.setPlainText(formatted_text)
        else:
            self.chapter_content.setPlainText("அதிகாரத்தை தேர்ந்தெடுக்கவும்.")

    def display_porutpaal_chapter(self, index):
        if index >= 0 and index < 70:
            start_index = (index + 38) * 10
            end_index = start_index + 10
            chapter_verses = self.kural_tam_data[start_index:end_index]
            formatted_text = "\n\n".join([
                f"(குறள் எண் : {start_index + i + 1})\n{verse}" 
                for i, verse in enumerate(chapter_verses)
            ])
            self.chapter_content_porutpaal.setPlainText(formatted_text)
        else:
            self.chapter_content_porutpaal.setPlainText("அதிகாரத்தை தேர்ந்தெடுக்கவும்.")

    def display_kamathuppaal_chapter(self, index):
        if index >= 0 and index < 25:
            start_index = (index + 108) * 10
            end_index = start_index + 10
            chapter_verses = self.kural_tam_data[start_index:end_index]
            formatted_text = "\n\n".join([
                f"(குறள் எண் : {start_index + i + 1})\n{verse}" 
                for i, verse in enumerate(chapter_verses)
            ])
            self.chapter_content_kamathuppaal.setPlainText(formatted_text)
        else:
            self.chapter_content_kamathuppaal.setPlainText("அதிகாரத்தை தேர்ந்தெடுக்கவும்.")

    def search_kural(self):
        search_term = self.search_bar.text().strip()
        if not search_term:
            self.chapter_content.setPlainText("தேடுவதற்கான குறள் எண் அல்லது சொல் உள்ளிடவும்.")
            return
        if search_term.isdigit():
            kural_number = int(search_term)
            if 1 <= kural_number <= 1330:
                kural_index = kural_number - 1
                kural_verse = self.kural_tam_data[kural_index]
                result_text = f"(குறள் எண் : {kural_number})\n{kural_verse}"
                self.chapter_content.setPlainText(result_text)
            else:
                self.chapter_content.setPlainText("குறள் எண் தவறாக உள்ளது. 1 முதல் 1330 வரை உள்ள எண்ணை உள்ளிடவும்.")
        else:
            matching_kurals = []
            for i, verse in enumerate(self.kural_tam_data):
                if search_term in verse:
                    kural_number = i + 1
                    matching_kurals.append(f"(குறள் எண் : {kural_number})\n{verse}")
            if matching_kurals:
                result_text = "\n\n".join(matching_kurals)
                self.chapter_content.setPlainText(result_text)
            else:
                self.chapter_content.setPlainText(f"'{search_term}' என்ற சொல்லுக்கு ஏற்பவான குறள்கள் இல்லை.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ThirukkuralApp()
    window.show()
    sys.exit(app.exec_())

