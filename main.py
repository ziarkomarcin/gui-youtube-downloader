import tkinter 
from pytube import YouTube
import customtkinter
import subprocess
import os

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

        # Create file name entry
        self.filename_label = customtkinter.CTkLabel(self, text="File Name (optional):")
        self.filename_label.pack(pady=10)
        self.filename_entry = customtkinter.CTkEntry(self, width=400)
        self.filename_entry.pack(pady=10)

        # Create download button
        self.download_button = customtkinter.CTkButton(self, text="Download", command=self.download_video)
        self.download_button.pack(pady=20)

        # Create status label
        self.status_label = customtkinter.CTkLabel(self, text="")
        self.status_label.pack(pady=10)

    def download_video(self):
        url = self.url_entry.get()
        filename = self.filename_entry.get().strip()  # Pobierz nazwę pliku od użytkownika
        if url:
            try:
                # Utwórz folder "videos" w tym samym katalogu co main.py, jeśli nie istnieje
                download_path = os.path.join(os.getcwd(), "videos")
                os.makedirs(download_path, exist_ok=True)

                # Jeśli użytkownik podał nazwę pliku, użyj jej, w przeciwnym razie użyj domyślnej nazwy
                output_template = os.path.join(download_path, f"{filename}.%(ext)s") if filename else os.path.join(download_path, "%(title)s.%(ext)s")

                # Uruchom yt-dlp z określoną ścieżką pobierania
                subprocess.run(["python", "-m", "yt_dlp", "-o", output_template, url], check=True)
                self.status_label.configure(text="Download completed!", text_color="green")
            except Exception as e:
                self.status_label.configure(text=f"Error: {str(e)}", text_color="red")
        else:
            self.status_label.configure(text="Please enter a valid URL.", text_color="red")

if __name__ == "__main__":
    app = App()
    app.mainloop()