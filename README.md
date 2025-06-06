
# 🎵 Python Music Player App

A sleek and simple desktop music player built with Python and Tkinter that plays local MP3 files from a `Musics/` folder. It extracts metadata and album cover from the audio file and displays it with playback controls.

---

## 🚀 Features

- ✅ Load all MP3 files from the `Musics/` directory
- 🖼️ Automatically displays album art (if embedded in ID3 tag)
- ▶️ Play / ⏸ Pause / ⏭ Next / ⏮ Previous controls
- ⏱️ Shows track duration and current position
- 📟 Displays file name and status
- 🔥 Lightweight and responsive GUI

---

## 📂 Folder Structure

```
project-folder/
│
├── main.py
└── Musics/
    ├── song1.mp3
    ├── song2.mp3
    └── ...
```

---

## 📦 Installation

Install required Python libraries using pip:

```bash
pip install pygame mutagen pillow
```

---

## ▶️ Run the App

After placing your MP3 files into the `Musics/` folder, run the player:

```bash
python main.py
```

---

## 📸 Screenshot

![Music Player Screenshot](https://raw.githubusercontent.com/mostafabaghi/python-music-player-app/main/screenshot.png)

---

## 🧠 Tip

Make sure your MP3 files include ID3 album art tags if you want cover images to display.

---

## 🔗 Author

Created with ❤️ by [Mostafa Baghi](https://github.com/mostafabaghi)