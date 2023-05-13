import pygame
class Load():
    def __init__(self,game):
        self.game = game
        self.clock = pygame.time.Clock()
        self.run_display = True
        self.offset = self.game.DISPLAY_W/10
        self.weight = self.game.DISPLAY_W - (self.offset*2)
        self.cordy = (5 * self.game.DISPLAY_H)/6
        self.posicion_carga = 0
        self.tiempo_carga = 3.0
        self.tiempo_actual = 0.0
        self.barra_carga = pygame.Rect(self.offset, self.cordy, self.weight , self.offset/4)
        pygame.mixer.music.stop()
        self.size_text = int(self.game.DISPLAY_H/10)

    def display_load(self):
        self.run_display = True
        while self.run_display:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game.running = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text("Cargando", self.size_text, self.game.DISPLAY_W/2,self.game.DISPLAY_H/2)
            self.posicion_carga = int((self.tiempo_actual / self.tiempo_carga) * self.barra_carga.width)
            pygame.draw.rect(self.game.display, self.game.WHITE, self.barra_carga)
            pygame.draw.rect(self.game.display, self.game.RED, (self.barra_carga.left, 
                                                                self.barra_carga.top, self.posicion_carga, self.barra_carga.height))
            self.tiempo_actual += self.clock.tick(60) / 1000.0
            if self.tiempo_actual >= self.tiempo_carga:
                break
            self.blit_screen()

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()





