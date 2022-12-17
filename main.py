from configuracoes.classtest import *
import re
from threading import Thread
from time import sleep

def main():
    
    width = 50
    warningSleep = 4
    multlinks = []
    
    while True:
        print("*"*width)
        print("  Menu Principal  ".center(width,"*"))
        print("*"*width)
        print("  Escolha uma opção  ".ljust(width," "))
        
        menu ="""
        [1] - Fazer Download Unico
        [2] - Fazer Download de uma Lista de Videos
        [3] - Download Multilinks
        [4] - Link Status
        [5] - Abrir Local Download
        [6] - Fazer Download Mp3
        
        
        [0] - Sair (Exit)
        
        """
        print(menu)
        entrada = input('Digite uma das opções: ')
        
        # @ DOWNLOAD UNICO VIDEO
        if entrada == "1": 
            url = input('Insira o link do Youtube: ')
            
            if re.findall(r"^https://www.you",url):
                try:            
                    Main(url).downloadUnico()
                    print("  Download Concuido  ".center(width,"#"))
                    print("\n")  
                    sleep(warningSleep)
                except:
                    print("  Download Error  ".center(width,"#"))
                   
            else:
                print("  Link Invalido  ".center(width,"#"))
                sleep(warningSleep)
            
        # @ DOWNLOAD LISTA DE VIDEOS 
        elif entrada == "2":             
            url = input('Insira o link do Youtube: ')
            
            if re.findall(r"^https://www.you",url):
                try:            
                    Main(url).download_playlistMp4()
                except:
                    opcoes = """
                    Não ah Lista de Videos, Deseja fazer um
                    único download  ?
                    
                    [1] - SIM
                    [2] - NÃO                    
                    """
                    print(opcoes)
                    select = input("Digite uma das Opções: ")
                    if select == "1": 
                        Main(url).downloadUnico()
                        print("  Download Concuido  ".center(width,"#"))
                        print("\n")  
                        sleep(warningSleep)
            else:
                print("  Link Invalido  ".center(width,"#"))
                sleep(warningSleep)
                
        
        # DOWNLOAD MULTI LINKS
        elif entrada == "3": 
            maisLinks = True
            
            while maisLinks:
                opcoes ="""
                    Pode demorar, Deseja Continuar o Multlinks ?
                    [1] - SIM
                    [2] - NÃO
                """
                print(opcoes)
                
                selecionar = input('Digite uma Opção: ')
                maisLinks = False
                if selecionar == "1":
                    while True:
                        link = input("Digite o link do Youtube: [0] iniciar download :  ")
                        
                        if re.findall(r"^https://www.you",link) or "0":
                            if link != "0":
                                if not link in multlinks:
                                    multlinks.append(link)
                                    print(f"Links Nº : {len(multlinks)}") 
                                    
                                    if len(multlinks) >= 10: break  # Limita a 7 Links para download
                                
                            if link == "0": break       
                    
                        else:
                            print("\n  Link Invalido  ".center(width,"#"))
                            print("\n")  
                            sleep(warningSleep) 
                        
                    if len(multlinks) > 0:
                        while (len(multlinks)!= 0):
                            for video in multlinks:
                                try:
                                    try:
                                        Main(video).download_playlistMp4()
                                        print(f" [{len(multlinks)}] Download Concuido  ".center(width,"#"))  
                                        print("\n")  
                                        multlinks.pop(0)
                                        sleep(warningSleep)                   
                                    except:                                        
                                        Main(video).downloadUnico()
                                        print(f" [{len(multlinks)}] Download Concuido  ".center(width,"#"))
                                        print("\n")  
                                        multlinks.pop(0)
                                        sleep(warningSleep)
                                except:
                                        print('Error Download')
                                        print("\n")  
                                        sleep(warningSleep)                                  
                            
                                                
                elif selecionar == "2":                     
                    continue            
            
        # @ STATUS
        elif entrada == "4": 
            url = input('Insira o link do Youtube: ')
            
            if re.findall(r"^https://www.you",url):
                try:            
                    stats = Main(url).status()
                    
                    banner = f"""
                        Titulo: {stats['titulo']}
                        Canal: {stats['canal']}
                        Visualizações: {stats['visualizacao']}
                        Linguagem: {stats['lenguage']}
                        Thumbnail: {stats['thumbnail']}
                        Url do Video: {stats['url_video']}
                    
                    """
                    print(banner)
                    input('Enter para Sair: ')
                except:
                    print("  Download Error  ".center(width,"#"))
                    print("\n")  
                    sleep(warningSleep)
                   
            else:
                print("  Link Invalido  ".center(width,"#"))
                print("\n")  
                sleep(warningSleep)
        
         # @ ABRIR PASTA DE DOWNLOADS 
        elif entrada == "5":  
            url = "https://www.youtube.com/watch?v=NvvBPPQ7DEo"
            Main(url).openPathFile()   
            
        # @ DOWNLOAD UNICO VIDEO
        elif entrada == "6": 
            url = input('Insira o link do Youtube: ')
            
            if re.findall(r"^https://www.you",url):
                try:            
                    Mp3(url).mp3Download()
                    print("  Download Concuido  ".center(width,"#"))
                    print("\n")  
                    sleep(warningSleep)
                except:
                    print("  Download Error  ".center(width,"#"))
                   
            else:
                print("  Link Invalido  ".center(width,"#"))
                sleep(warningSleep)
        
        elif entrada == "0": 
            exit()

if __name__ == '__main__':
    main()
    
    
