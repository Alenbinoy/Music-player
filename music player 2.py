from pygame import mixer
from tkinter import Tk, Button, Label, filedialog

class MusicPlayer:
    def __init__(self):
        self.current_track = ""
        self.paused = False

        # Initialize pygame mixer
        mixer.init()

        # Create the main window
        self.root = Tk()
        self.root.title("^Music^Player^")

        # Create the buttons
        self.btn_select = Button(self.root, text="Select Track", command=self.select_track)
        self.btn_play_pause = Button(self.root, text="Play", command=self.play_pause)
        self.btn_stop = Button(self.root, text="Stop", command=self.stop)

        # Create the track label
        self.lbl_track = Label(self.root, text="No track selected")

        # Add the widgets to the window
        self.btn_select.pack()
        self.btn_play_pause.pack()
        self.btn_stop.pack()
        self.lbl_track.pack()

        self.root.mainloop()

    def select_track(self):
        # Open a file dialog to select a music file
        self.current_track = filedialog.askopenfilename(defaultextension=".mp3", filetypes=[("MP3 Files", "*.mp3")])

        if self.current_track:
            self.lbl_track.config(text="Selected Track: " + self.current_track)

    def play_pause(self):
        if self.current_track:
            if self.paused:
                # Unpause the music
                mixer.music.unpause()
                self.paused = False
                self.btn_play_pause.config(text="Pause")
            else:
                # Load and play the selected track
                mixer.music.load(self.current_track)
                mixer.music.play()
                self.btn_play_pause.config(text="Pause")
        else:
            print("No track selected")

    def stop(self):
        if self.current_track:
            # Stop the music
            mixer.music.stop()
            self.btn_play_pause.config(text="Play")
            self.paused = False
        else:
            print("No track selected")

# Create an instance of the MusicPlayer class
player = MusicPlayer()

