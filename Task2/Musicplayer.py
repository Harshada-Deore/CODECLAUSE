from pygame import mixer
from tkinter import Tk, Label, Button, filedialog

class MusicPlayer:
    def __init__(self, window):
        self.window = window
        self.window.title("Music Player")
        self.window.geometry("300x100")
        
        self.select_song_button = Button(window, text="Select song", command=self.select_song)
        self.select_song_button.pack()

        self.play_button = Button(window, text="Play", command=self.play_song)
        self.play_button.pack()

        self.pause_button = Button(window, text="Pause", command=self.pause_song)
        self.pause_button.pack()

        self.stop_button = Button(window, text="Stop", command=self.stop_song)
        self.stop_button.pack()

        self.song_label = Label(window, text="No song loaded.")
        self.song_label.pack()

        self.song_path = None
        self.paused = False

    def select_song(self):
        self.song_path = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
        self.song_label.config(text="Song loaded: " + self.song_path)

    def play_song(self):
        if self.song_path:
            if self.paused:
                mixer.unpause()
                self.paused = False
            else:
                mixer.init()
                mixer.music.load(self.song_path)
                mixer.music.play()

    def pause_song(self):
        if self.song_path:
            if not self.paused:
                mixer.music.pause()
                self.paused = True

    def stop_song(self):
        if self.song_path:
            mixer.music.stop()
            self.song_label.config(text="No song loaded.")
            self.song_path = None

root = Tk()
music_player = MusicPlayer(root)
root.mainloop()
