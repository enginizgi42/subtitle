from youtube_transcript_api import YouTubeTranscriptApi
import os


#srt=YouTubeTranscriptApi.get_transcript("")
srt = YouTubeTranscriptApi.get_transcript("cND9bWTLjLA",languages=['tr'])

text = ""
with open("file.txt", "w") as file:
    for i in srt:
        text += i["text"]+"\n"
    file.write(text) 
os.startfile("file.txt")
