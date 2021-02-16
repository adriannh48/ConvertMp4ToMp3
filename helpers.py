from pytube import YouTube
import os 
from moviepy.editor import *

class Helpers :

    def GetVideoByUrl(url):
        try:

            directory = os.path.dirname(os.path.realpath(__file__))
            directory = directory + '/tmp'

            yt = YouTube(url)
            nameFile = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(directory)
            
            return nameFile

        except NameError: 
            return False

    def ConvertMp4ToMp3 (path , nameFile):
        try:
            directory = os.path.dirname(os.path.realpath(__file__))
            directory = directory + '/tmp'

            nameMusic = os.path.splitext(nameFile)[0]+''
            musicFileDirectory = os.path.join(directory , directory, nameMusic + ".mp3")

            video = VideoFileClip(os.path.join(directory + path ,directory, nameFile))
            video.audio.write_audiofile(musicFileDirectory)
            video.close()
            
            return musicFileDirectory

        except NameError:
            return False

    def GetNameFileByVideo(nameFile) :
        
        return os.path.split(nameFile)
        
    
    def RemoveArquive(path):
        try:
            os.remove(path)
            return True
        except NameError:
            return NameError