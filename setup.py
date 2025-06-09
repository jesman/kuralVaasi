from setuptools import setup, find_packages
import platform
import subprocess

def install_vlc():
    system = platform.system()

    if system == "Darwin":  # macOS
        print("Installing VLC on macOS using Homebrew...")
        subprocess.call(["brew", "install", "--cask", "vlc"])
    elif system == "Windows":
        print("Please install VLC manually from https://www.videolan.org/vlc/")
    elif system == "Linux":
        print("Installing VLC on Linux using apt...")
        subprocess.call(["sudo", "apt-get", "install", "-y", "vlc"])
    else:
        print("Unsupported OS. Please install VLC manually.")

install_vlc()

setup(
    name="vlc_audio_player",
    version="1.0.0",
    description="Cross-platform audio player using PyQt5, VLC, and gTTS",
    author="Jesman Anthonypillai",
    python_requires="==3.9.16",
    packages=find_packages(),
    install_requires=[
        "PyQt5==5.15.9",
        "pygame==2.5.0",
        "python-vlc==3.0.8866",
        "gTTS==2.2.3"
    ],
    entry_points={
        'console_scripts': [
            'vlcplayer=vlc_audio_player.main:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
)
