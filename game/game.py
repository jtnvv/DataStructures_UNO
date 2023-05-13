import pygame
import os
from menu import *
from uno import *
from load_screen import *
from end_screen import *

class Game():
    def __init__(self):
        pygame.init()
        self.volumen = 100
        monitor_info = pygame.display.Info()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.RIGHT_KEY, self.LEFT_KEY = False, False
        self.DISPLAY_W, self.DISPLAY_H = monitor_info.current_w, monitor_info.current_h
        #self.DISPLAY_W, self.DISPLAY_H = 480, 270
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode((self.DISPLAY_W,self.DISPLAY_H),pygame.FULLSCREEN)
        ruta_capeta_font = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'game', 'fonts'))
        self.font_name = os.path.join(ruta_capeta_font,'8-BIT WONDER.TTF')
        self.BLACK, self.WHITE, self.RED = (0, 0, 0), (255, 255, 255), (255, 0, 0)
        self.main_menu = MainMenu(self)
        self.optiones = OptionesMenu(self)
        self.creditos = CreditosMenu(self)
        self.curr_menu = self.main_menu
        self.font_size_text = int((self.DISPLAY_W + self.DISPLAY_H)/60)
        self.font_size_title = int((self.DISPLAY_W + self.DISPLAY_H)/40)
        self.font_size_cursor = int((self.DISPLAY_W + self.DISPLAY_H)/70)
        self.ruta_musica = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'game', 'music'))
        #self.musica = pygame.mixer.music.load(os.path.join(self.ruta_musica,'main_menu.mp3'))
        #pygame.mixer.music.set_volume(self.volumen/100)
        #pygame.mixer.music.play(-1)

    def game_loop(self):
        self.prueba = Uno(self)
        while self.playing:
            self.load_window = Load(self).display_load()
            break
        while self.playing:
            self.a = self.prueba.display_game()
            if self.playing == False:
                self.end_window = End(self).display_end()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_ESCAPE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_RIGHT:
                    self.RIGHT_KEY = True
                if event.key == pygame.K_LEFT:
                    self.LEFT_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.RIGHT_KEY, self.LEFT_KEY = False, False

    def draw_text(self, text, size, x, y ):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)

    def draw_image_centerx(self, ruta, size,y):
        imagen = pygame.image.load(ruta)
        width, height = imagen.get_size()
        w_redimensionado = width*size
        h_redimensionado = height*size
        new_width = int(w_redimensionado*(self.DISPLAY_W)/17000)
        new_height = int(h_redimensionado*(self.DISPLAY_H)/10000)
        imagen_redimensionada = pygame.transform.scale(imagen, (new_width, new_height))
        img_x = (self.DISPLAY_W - new_width) // 2
        self.display.blit(imagen_redimensionada, (img_x,y))
        
    def draw_center_text(self, text, size, x, y ):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.BLACK)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)