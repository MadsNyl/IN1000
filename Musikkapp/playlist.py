import os, vlc

class Playlist:
    def __init__(self, name):
        self.name = name
        self.playlist = []
    
    def store_music(self):
        self.playlist = []
        songs = os.listdir('Musikkapp/musikk')
        for song in songs:
            self.playlist.append(song)
    
    def show_music(self):
        for song in self.playlist:
            print(song)
            print('.' * 10)
    
    def play_music(self, title):
        match = False
        for song in self.playlist:
            if song == title:
                match = True
        if match:
            player = vlc.MediaPlayer(f'Musikkapp/musikk/{title}')
            player.play() 
            run = True
            while run:
                user_input = input('Pause: "pause".\nReplay: "play":\nNew song: "new": ')
                if user_input == 'pause':
                    player.pause()
                elif user_input == 'play':
                    player.play()
                elif user_input == 'new':
                    player.stop()
                    run = False
            