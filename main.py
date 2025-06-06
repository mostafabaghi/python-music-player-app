import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import pygame
from mutagen.mp3 import MP3
from mutagen.id3 import ID3
from io import BytesIO

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Music Player")
        self.root.geometry("400x500")
        self.root.configure(bg="#1e1e1e")

        pygame.mixer.init()
        self.music_dir = "Musics"
        self.track_list = self.load_local_tracks()
        self.track_index = 0
        self.is_playing = False
        self.current_track_length = 0

        self.setup_ui()
        if self.track_list:
            self.load_track()

    def load_local_tracks(self):
        if not os.path.exists(self.music_dir):
            os.makedirs(self.music_dir)
        return [os.path.join(self.music_dir, f) for f in os.listdir(self.music_dir) if f.endswith(".mp3")]

    def load_track(self):
        filepath = self.track_list[self.track_index]
        pygame.mixer.music.load(filepath)
        audio = MP3(filepath)

        self.current_track_length = int(audio.info.length)
        self.progress_slider.config(to=self.current_track_length)
        self.duration_label.config(text=self.format_time(self.current_track_length))

        # Load cover if exists
        self.load_cover(filepath)

        self.track_info.config(text=os.path.basename(filepath))
        self.play()

    def load_cover(self, filepath):
        try:
            audio = MP3(filepath, ID3=ID3)
            for tag in audio.tags.values():
                if tag.FrameID == "APIC":
                    image = Image.open(BytesIO(tag.data)).resize((200, 200))
                    photo = ImageTk.PhotoImage(image)
                    self.cover_label.config(image=photo)
                    self.cover_label.image = photo
                    return
            raise Exception("No cover found")
        except:
            self.cover_label.config(image="", text="🎵", font=("Arial", 80), fg="gray")

    def setup_ui(self):
        self.cover_label = tk.Label(self.root, bg="#1e1e1e")
        self.cover_label.pack(pady=20)

        self.track_info = tk.Label(self.root, text="", fg="white", bg="#1e1e1e", font=("Arial", 12))
        self.track_info.pack()

        self.progress_slider = ttk.Scale(self.root, from_=0, to=100, orient="horizontal")
        self.progress_slider.pack(fill="x", padx=20, pady=10)

        self.duration_label = tk.Label(self.root, text="0:00", fg="gray", bg="#1e1e1e")
        self.duration_label.pack()

        controls = tk.Frame(self.root, bg="#1e1e1e")
        controls.pack(pady=10)

        prev_btn = ttk.Button(controls, text="⏮", command=self.prev_track)
        prev_btn.pack(side="left", padx=5)

        self.play_btn = ttk.Button(controls, text="▶", command=self.toggle_play)
        self.play_btn.pack(side="left", padx=5)

        next_btn = ttk.Button(controls, text="⏭", command=self.next_track)
        next_btn.pack(side="left", padx=5)

        self.status = tk.Label(self.root, text="", fg="gray", bg="#1e1e1e")
        self.status.pack(pady=5)

        self.update_progress()

    def set_status(self, msg):
        self.status.config(text=msg)

    def play(self):
        pygame.mixer.music.play()
        self.is_playing = True
        self.play_btn.config(text="⏸")
        self.set_status("Playing...")

    def toggle_play(self):
        if self.is_playing:
            pygame.mixer.music.pause()
            self.is_playing = False
            self.play_btn.config(text="▶")
            self.set_status("Paused")
        else:
            pygame.mixer.music.unpause()
            self.is_playing = True
            self.play_btn.config(text="⏸")
            self.set_status("Playing...")

    def prev_track(self):
        self.track_index = (self.track_index - 1) % len(self.track_list)
        self.load_track()

    def next_track(self):
        self.track_index = (self.track_index + 1) % len(self.track_list)
        self.load_track()

    def update_progress(self):
        if self.is_playing:
            pos = pygame.mixer.music.get_pos() // 1000
            self.progress_slider.set(pos)
        self.root.after(1000, self.update_progress)

    def format_time(self, seconds):
        m, s = divmod(seconds, 60)
        return f"{int(m)}:{int(s):02d}"

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()