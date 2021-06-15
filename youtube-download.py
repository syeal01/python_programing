import os
from pytube import YouTube
path="D:\\Users\\Ali\\Downloads"
url = input("Enter the link: ")

try:
    youtube_object = YouTube(url)
except: 
    print(f"Error: Unable to open {url} YouTube object")
else:
    print("Title: ", youtube_object.title)
    print(youtube_object.title[0:25])
    print("Number of views: ", youtube_object.views)
    print("Length of video: ", youtube_object.length, "seconds")
    print("Ratings: ",youtube_object.rating)
    print("Author: ", youtube_object.author)
    print("Published Date", youtube_object.publish_date)

    download = input("Download Audio or Video? ")
    if download == "A":
        print(f"Downloading audio...by {youtube_object.author}")
        audio = youtube_object.streams.get_audio_only()
        audio.download(path, filename = youtube_object.title[0:25])
    elif download == "V":
        print(f"Downloading video...by {youtube_object.author}")
        video = youtube_object.streams.get_highest_resolution()
        video.download(path, filename = youtube_object.title[0:25])
    else: print("Invalid entry")
finally:
    print("Download completed")