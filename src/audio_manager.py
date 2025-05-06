import pygame
import os
import random

SFX_PATH = os.path.join('src', 'Audios', 'SFX')
MUSIC_PATH = os.path.join('src', 'Audios', 'Music')

class AudioManager:
    def __init__(self, sound_volume=1.0, music_volume=0.5):
        pygame.mixer.init()
        self.sound_volume = sound_volume
        self.music_volume = music_volume
        self.sfx = {}
        self.load_sfx()

    def load_sfx(self):
        # Завантажити всі SFX з папки
        for fname in os.listdir(SFX_PATH):
            if fname.endswith('.wav'):
                name = os.path.splitext(fname)[0]
                self.sfx[name] = pygame.mixer.Sound(os.path.join(SFX_PATH, fname))
                self.sfx[name].set_volume(self.sound_volume)

    def play_sfx(self, name):
        if name in self.sfx:
            self.sfx[name].play()

    def play_random_music(self):
        # Вибрати випадковий музичний файл і програти його в циклі
        music_files = [f for f in os.listdir(MUSIC_PATH) if f.endswith('.mp3') or f.endswith('.ogg') or f.endswith('.wav')]
        if music_files:
            track = random.choice(music_files)
            pygame.mixer.music.load(os.path.join(MUSIC_PATH, track))
            pygame.mixer.music.set_volume(self.music_volume)
            pygame.mixer.music.play(-1)

    def stop_music(self):
        pygame.mixer.music.stop()

    def set_sound_volume(self, volume):
        self.sound_volume = volume
        for s in self.sfx.values():
            s.set_volume(volume)

    def set_music_volume(self, volume):
        self.music_volume = volume
        pygame.mixer.music.set_volume(volume)
