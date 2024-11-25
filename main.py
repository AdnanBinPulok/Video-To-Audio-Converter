from moviepy.editor import VideoFileClip
import os
import tkinter as tk
from tkinter import filedialog

def convert_video_to_audio(input_video_path):
    try:
        # Load the video file
        video = VideoFileClip(input_video_path)
        
        # Extract the audio
        audio = video.audio
        
        # Generate the output audio file path
        base_name = os.path.splitext(input_video_path)[0]
        output_audio_path = f"{base_name}.mp3"
        
        # Save the audio to a file
        audio.write_audiofile(output_audio_path)
        
        print(f"Audio successfully saved to {output_audio_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    input_video_path = filedialog.askopenfilename(title="Select Video File", filetypes=[("Video Files", "*.mp4 *.avi *.mov *.mkv")])
    
    if input_video_path:
        convert_video_to_audio(input_video_path)
    else:
        print("No file selected.")