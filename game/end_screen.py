import pygame, uno

class End():
    def __init__(self,game):
        self.game = game
        self.run_display = True
        pygame.mixer.music.stop()
        self.size_text = int(self.game.DISPLAY_H/15)

    def display_end(self):
        self.run_display = True
        while self.run_display:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                        self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text("Gracias por jugar", self.size_text, self.game.DISPLAY_W/2,self.game.DISPLAY_H/6)
            #self.game.draw_text("Gracias por jugar", self.size_text, self.game.DISPLAY_W/2,self.game.DISPLAY_H/6)
            nombres = self.game.marcadores.names
            victorias = self.game.marcadores.victory
            offset = self.game.DISPLAY_H/10
            contador = 1
            for i in nombres:
                name = i
                count = victorias[self.game.marcadores.polyHash(i)]
                self.game.draw_text(str(name), self.size_text, self.game.DISPLAY_W/2.5,self.game.DISPLAY_H/6 + (contador * offset))
                self.game.draw_text(str(count), self.size_text, self.game.DISPLAY_W/2.5 + self.game.DISPLAY_W/4,self.game.DISPLAY_H/6 + (contador * offset))
                contador += 1
            self.blit_screen()

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()





