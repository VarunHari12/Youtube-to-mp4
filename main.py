from pytube import YouTube 
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
import os

link = "https://www.youtube.com/watch?v=3VRv8wv2dZM" # link to video

pathV = "C:\\Users\\varun\\Documents\\GitHub\\Youtube-to-mp4\\Videos\\video" # whatever path you would like to choose
pathA = "C:\\Users\\varun\\Documents\\GitHub\\Youtube-to-mp4\\Videos\\audio"
path = "C:\\Users\\varun\\Documents\\GitHub\\Youtube-to-mp4\\Videos"

title = input("Enter a title: ")

try:
    
    yt = YouTube(link)
    
except:
    print("error")
    
audio = yt.streams.filter(only_audio=True).first()   
video = yt.streams.get_highest_resolution()





try:
    
    video.download(pathV)
    audio.download(output_path=pathA,filename=f"{video.title}.mp3")
    
except:
    print("Download Error")

audio_clip = AudioFileClip("C:\\Users\\varun\\Documents\\GitHub\\Youtube-to-mp4\\Videos\\audio\\" + f"{video.title}.mp3")
video_clip = VideoFileClip("C:\\Users\\varun\\Documents\\GitHub\\Youtube-to-mp4\\Videos\\video\\" + f"{video.title}.mp4")

final_clip = video_clip.set_audio(audio_clip)
final_clip.write_videofile("C:\\Users\\varun\\Documents\\GitHub\\Youtube-to-mp4\\Videos\\Final_Video\\" + title +".mp4")