import pygame
import sys, os
from generator import Generator

class Uno():
    def __init__(self, game):
        self.game = game
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.run_display = True
        self.select_card = 1
        self.size_deck = 0
        self.turno = 1
        self.players = 4
        generador = Generator(self)
        self.deck_data = generador.generator()
        self.main_deck = self.deck_data[0]
        self.discard_deck = self.deck_data[1]
        self.deck1 = self.deck_data[2]
        self.deck2 = self.deck_data[3]
        self.deck3 = self.deck_data[4]
        self.deck4 = self.deck_data[5]

    
    def display_game(self):
        self.run_display = True
        self.play_music()
        while self.run_display:
            self.chech_input()
            self.game.display.fill(self.game.RED)
            self.draw_decks()
            self.draw_discard_deck()
            self.draw_main_deck()
            self.dt = self.clock.tick(60) / 1000
            self.blit_screen()
            
    def chech_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.playing = False
                self.game.running = False
                self.run_display = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.mixer.music.stop()
            self.run_display = False
            self.game.playing = False
        if keys[pygame.K_RIGHT]:
            self.player_pos.y -= 300 * self.dt
        if keys[pygame.K_LEFT]:
            self.player_pos.y += 300 * self.dt
        if keys[pygame.K_UP]:
            self.player_pos.x -= 300 * self.dt
    
    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()

    def play_music(self):
        self.ruta_musica = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'game', 'music'))
        self.musica = pygame.mixer.music.load(os.path.join(self.ruta_musica,'main_menu.mp3'))
        pygame.mixer.music.set_volume(int(self.game.volumen)/100)
        pygame.mixer.music.play()

    def draw_decks(self):
        
    def draw_discard_deck(self):

    def draw_main_deck(self):

