import os, re
from time import sleep
from pytube import YouTube
from pytube import Playlist

# EXIGE que coloque o SELF
# DownloadYoutube.__init__(self, link)

# NÃO EXIGE que coloque o SELF
# super().__init__(link)


class DownloadYoutube:
    def __init__(self, link, path_Default='./download'):
        
        self.link = link
        self.path_Defalult = path_Default
        self.naoBaixados = []   
     
        
    def clearString(self, word):        
        return re.sub("[\@\<\>\/\\\|\:]", "", word)        
               
    def downloadUnico(self, paramList=''):
        
        try:
            # print(videoStatus)
            sleep(5)
            videoUrl = YouTube(self.link).streams.filter(progressive = True, file_extension='mp4')
            # pega parametros da url            
            videoStatus = YouTube(self.link)
        except:
            video = {}
            video['id']= paramList
            video['titulo']= videoStatus.title
            video['link']= self.link
            self.naoBaixados.append(video)            
            return            
        
        if paramList != '': 
            print(f"{paramList} - ", videoStatus.title)            
            videoUrl.order_by('resolution').desc().first().download(self.path_Defalult, filename_prefix= f'0{paramList}- ' if paramList < 10 else f'{paramList}- ') 
            
        else:
            videoUrl.order_by('resolution').desc().first().download(self.path_Defalult)                   
        
                
    def download_playlistMp4(self):
        playLists = Playlist(self.link)    
        path_pasta ='Mp4 - '+ playLists.title        
        caminho_completo = os.path.join(self.path_Defalult, self.clearString(path_pasta))
        
        if not os.path.exists(caminho_completo): os.mkdir(caminho_completo)  
        
        for index, play in enumerate(playLists, start=1):     
            self.link = play
            self.path_Defalult = caminho_completo            
            self.downloadUnico(index)       
            
        if self.naoBaixados != []:
            print(self.naoBaixados)   
    
    
    def linkReturn(self):
        return self.link
    

class Main(DownloadYoutube):
    def  __init__(self, link):
        super().__init__(link)   
       
        
    def status(self):        
        videoUrl = YouTube(self.link) 
                     
        statusvideo = {}
        statusvideo['titulo']=videoUrl.title
        statusvideo['thumbnail']=videoUrl.thumbnail_url
        statusvideo['duração']=videoUrl.length
        statusvideo['visualizacao']=videoUrl.views
        statusvideo['url_video']=videoUrl.embed_url
        statusvideo['id video']=videoUrl.channel_id
        statusvideo['canal']=videoUrl.author
        statusvideo['url_canal']=videoUrl.channel_url
        statusvideo['descricao']=videoUrl.description
        statusvideo['restricao']=videoUrl.age_restricted
        statusvideo['lenguage']=videoUrl.caption_tracks
        
        return statusvideo      
            

# linkDownload = 'https://www.youtube.com/watch?v=e-NJU2jpIkQ&list=PLHz_AreHm4dlgnTCx5Q3bY6Ms8_i77kfn'

# pytube = Main(linkDownload).download_playlistMp4()
# pytube = Main(linkDownload).downloadUnico()
# print(pytube['visualizacao'])



