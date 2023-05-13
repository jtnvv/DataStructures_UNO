import pygame
import sys, os
# pygame setup
class Prueba():
    def __init__(self, game):
        self.game = game
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.run_display = True
        self.player_pos = pygame.Vector2( self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2)
        
    
    def dibujar(self):
        self.run_display = True
        self.play_music()
        while self.run_display:
            #self.game.check_events()
            self.chech_input()
            self.game.display.fill(self.game.WHITE)
            pygame.draw.circle(self.game.display, "red", self.player_pos, 40)
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
        if keys[pygame.K_UP]:
            self.player_pos.y -= 300 * self.dt
        if keys[pygame.K_DOWN]:
            self.player_pos.y += 300 * self.dt
        if keys[pygame.K_LEFT]:
            self.player_pos.x -= 300 * self.dt
        if keys[pygame.K_RIGHT]:
            self.player_pos.x += 300 * self.dt
        

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()

    def play_music(self):
        self.ruta_musica = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'game', 'music'))
        self.musica = pygame.mixer.music.load(os.path.join(self.ruta_musica,'main_menu.mp3'))
        pygame.mixer.music.set_volume(int(self.game.volumen)/100)
        pygame.mixer.music.play()


