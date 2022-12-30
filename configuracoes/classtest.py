import os, re
from time import sleep
from pytube import YouTube
from pytube import Playlist
from threading import Thread

# EXIGE que coloque o SELF
# DownloadYoutube.__init__(self, link)

# NÃO EXIGE que coloque o SELF

# ffmpeg  fazer download para converter arquivo mp4 para mp3 sem conflito
# de alguns players
# Download :   https://ffmpeg.org/download.html

class DownloadYoutube:
    def __init__(self, link, path_Default='./download'):
        
        self.link = link
        self.path_Defalult = path_Default
        self.lenghtList = 0   
        self.fileSizeFull = 0
    
    def checkIsList(self):
        
        try:            
            if len(Playlist(self.link)) > 2:
                print('E uma lista: ', len(Playlist(self.link))," Links")
                self.lenghtList = len(Playlist(self.link))
                return True
        except:
            # print("NÃO E UMA LISTA")
            return False         
        
            
    def progressBar(self,stream=None, chunk=None, bytes_remaining=None):
        
        if bytes_remaining != 0:
            porcentagem = 100 * (self.fileSizeFull / bytes_remaining) 
            bar = "|" * int(porcentagem) + "-" * (100 - int(porcentagem))
            print(f"\r| {bar} | {porcentagem:.2f}%", end="\r")
        else:
            porcentagem = 100  
            bar = "|" * int(porcentagem) + "-" * (100 - int(porcentagem))
            print(f"\r| {bar} | {porcentagem:.2f}%", end="\r")

    def fileSize(self):
        videoUrl = YouTube(self.link)
        chunck = videoUrl.streams.filter(only_audio = True).first()
        file = chunck.filesize
        self.fileSizeFull= file
    
    def clearString(self, word):        
        return re.sub("[\@\<\>\/\\\|\:]", "", word)  
              
               
    def downloadUnico(self, paramList=''):                  
        self.fileSize()
        # videoUrl = YouTube(self.link).streams.filter(progressive = True, file_extension='mp4')
        videoUrl = YouTube(self.link, on_progress_callback=self.progressBar).streams.filter(progressive = True, file_extension='mp4')
        
        if paramList != '': 
            print(f'Download: Restam - {self.lenghtList - paramList}')
            videoUrl.order_by('resolution').desc().first().download(self.path_Defalult, filename_prefix= f'0{paramList}- ' if paramList < 10 else f'{paramList}- ') 
            
        else:
            print(f'Download: {self.link}')
            videoUrl.order_by('resolution').desc().first().download(self.path_Defalult)                   
        
                
    def download_playlistMp4(self):
        if self.checkIsList() == True:
            
            playLists = Playlist(self.link)    
            path_pasta ='Mp4 - '+ playLists.title        
            caminho_completo = os.path.join(self.path_Defalult, self.clearString(path_pasta))
            
            if not os.path.exists(caminho_completo): os.mkdir(caminho_completo)  
            
            for index, play in enumerate(playLists, start=1):     
                self.link = play
                self.path_Defalult = caminho_completo            
                
                inicio = Thread(target=self.downloadUnico, args=(index,))   
                inicio.start()  # inicia o task
                inicio.join()
            
                
        elif self.checkIsList() == False:
            iniciar = Thread(target=self.downloadUnico)
            iniciar.start()
            iniciar.join()
    
    
    def linkReturn(self):
        return self.link



class Mp3(DownloadYoutube):
    def __init__(self, link):
        super().__init__(link)       
     
    
    def mp3Download(self):
        # url input from user
        yt = YouTube(self.link )
        
        # extract only audio
        video = yt.streams.filter(only_audio=True).first()           
        
        # download the file
        out_file = video.download(output_path=self.path_Defalult)
        
        # save the file
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        
        # result of success
        print(yt.title + " has been successfully downloaded.")
                
        # ffmpeg  fazer download para converter arquivo mp4 para mp3 sem conflito
        # de alguns players
        # foi testado no VLC roodou normalmente
        
        
        pass

class Main(DownloadYoutube):
    def  __init__(self, link):
        super().__init__(link)   
       
        
    def status(self):        
        videoUrl = YouTube(self.link) 
                     
        statusvideo = {}
        statusvideo['titulo']=       videoUrl.title
        statusvideo['thumbnail']=    videoUrl.thumbnail_url
        statusvideo['duração']=      videoUrl.length
        statusvideo['visualizacao']= videoUrl.views
        statusvideo['url_video']=    videoUrl.embed_url
        statusvideo['id video']=     videoUrl.channel_id
        statusvideo['canal']=        videoUrl.author
        statusvideo['url_canal']=    videoUrl.channel_url
        statusvideo['descricao']=    videoUrl.description
        statusvideo['restricao']=    videoUrl.age_restricted
        statusvideo['lenguage']=     videoUrl.caption_tracks
        
        return statusvideo      
    def openPathFile(self):
        path = os.path.join(os.path.dirname(self.path_Defalult), self.path_Defalult)
        os.startfile(path) 


