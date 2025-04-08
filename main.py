import tkinter 
from pytube import YouTube
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: "system" (default), "dark", "light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("YouTube Video Downloader")
        self.geometry("600x400")

        # Create URL entry
        self.url_label = customtkinter.CTkLabel(self, text="YouTube Video URL:")
        self.url_label.pack(pady=10)
        self.url_entry = customtkinter.CTkEntry(self, width=400)
        self.url_entry.pack(pady=10)

        # Create download button
        self.download_button = customtkinter.CTkButton(self, text="Download", command=self.download_video)
        self.download_button.pack(pady=20)

        # Create status label
        self.status_label = customtkinter.CTkLabel(self, text="")
        self.status_label.pack(pady=10)

    def download_video(self):
        url = self.url_entry.get()
        if url:
            try:
                yt = YouTube(url)
                stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
                stream.download()
                self.status_label.configure(text="Download completed!", text_color="green")
            except Exception as e:
                self.status_label.configure(text=f"Error: {str(e)}", text_color="red")
        else:
            self.status_label.configure(text="Please enter a valid URL.", text_color="red")