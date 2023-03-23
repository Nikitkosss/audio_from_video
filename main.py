import os
os.environ["IMAGEIO_FFMPEG_EXE"] = "C:\\ffmpeg\\bin\\ffmpeg.exe"
import tkinter as tk
from tkinter import filedialog
import moviepy.editor

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

video_file = moviepy.editor.VideoFileClip(file_path)
audio_file = video_file.audio
audio_name = input("Назвоите аудио файл: ")
audio_file.write_audiofile(f"{audio_name}.mp3")
