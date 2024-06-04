import tkinter as tk
from tkinter import filedialog
import os
from moviepy.editor import VideoFileClip

def video_to_audio():
    file_path = file_entry.get()
    if os.path.exists(file_path):
        try:
            clip = VideoFileClip(file_path)
            audio_file = os.path.splitext(file_path)[0] + ".wav"
            clip.audio.write_audiofile(audio_file, codec='pcm_s16le')
            print("Successfully converted {} into audio!".format(file_path))
            status_label.config(text="Successfully converted!")
        except Exception as e:
            print("Error:", e)
            status_label.config(text="Error during conversion!")
    else:
        status_label.config(text="File not found!")

def browse_file():
    file_path = filedialog.askopenfilename()
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)

# Create the main window
root = tk.Tk()
root.title("Video to Audio Converter")

# Add a label and entry field for file selection
file_label = tk.Label(root, text="Select Video File:")
file_label.pack()
file_entry = tk.Entry(root, width=50)
file_entry.pack()
browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.pack()

# Add a button to start conversion
convert_button = tk.Button(root, text="Convert to Audio", command=video_to_audio)
convert_button.pack()

# Add a label for status updates
status_label = tk.Label(root, text="")
status_label.pack()

# Run the main event loop
root.mainloop()


#  For  #MP3

# import tkinter as tk
# from tkinter import filedialog
# import os
# from moviepy.editor import VideoFileClip

# def video_to_audio():
#     file_path = file_entry.get()
#     if os.path.exists(file_path):
#         try:
#             clip = VideoFileClip(file_path)
#             audio_file = os.path.splitext(file_path)[0] + ".mp3"
#             clip.audio.write_audiofile(audio_file)
#             print("Successfully converted {} into audio!".format(file_path))
#             status_label.config(text="Successfully converted!")
#         except Exception as e:
#             print("Error:", e)
#             status_label.config(text="Error during conversion!")
#     else:
#         status_label.config(text="File not found!")

# def browse_file():
#     file_path = filedialog.askopenfilename()
#     file_entry.delete(0, tk.END)
#     file_entry.insert(0, file_path)

# # Create the main window
# root = tk.Tk()
# root.title("Video to Audio Converter")

# # Add a label and entry field for file selection
# file_label = tk.Label(root, text="Select Video File:")
# file_label.pack()
# file_entry = tk.Entry(root, width=50)
# file_entry.pack()
# browse_button = tk.Button(root, text="Browse", command=browse_file)
# browse_button.pack()

# # Add a button to start conversion
# convert_button = tk.Button(root, text="Convert to Audio", command=video_to_audio)
# convert_button.pack()

# # Add a label for status updates
# status_label = tk.Label(root, text="")
# status_label.pack()

# # Run the main event loop
# root.mainloop()


