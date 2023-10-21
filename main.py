from pytube import YouTube 
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
import os

link = "https://www.youtube.com/watch?v=3VRv8wv2dZM" # link to video

pathV = "C:\\Users\\varun\\Documents\\GitHub\\Youtube-to-mp4\\Videos\\video" # This not the final video path, this is just a temporary folder
pathA = "C:\\Users\\varun\\Documents\\GitHub\\Youtube-to-mp4\\Videos\\audio" # This not the final audio path, this is just a temporary folder
path = "C:\\Users\\varun\\Documents\\GitHub\\Youtube-to-mp4\\Videos" # This is the final path of the video

title = input("Enter a title: ") # title of final video

try:
    
    yt = YouTube(link) # video object
    
except:
    print("error")
    
audio = yt.streams.filter(only_audio=True).first() # audio clip
video = yt.streams.get_highest_resolution() # video clip





try:
    
    video.download(pathV) # downloads video
    audio.download(output_path=pathA,filename=f"{video.title}.mp3") # downloads audio
    
except:
    print("Download Error")

audio_clip = AudioFileClip("C:\\Users\\varun\\Documents\\GitHub\\Youtube-to-mp4\\Videos\\audio\\" + f"{video.title}.mp3") # path of audio
video_clip = VideoFileClip("C:\\Users\\varun\\Documents\\GitHub\\Youtube-to-mp4\\Videos\\video\\" + f"{video.title}.mp4") # path of video 

final_clip = video_clip.set_audio(audio_clip) # splices together video and audio clip for highest quality
final_clip.write_videofile("C:\\Users\\varun\\Documents\\GitHub\\Youtube-to-mp4\\Videos\\Final_Video\\" + title +".mp4") # downloads final video