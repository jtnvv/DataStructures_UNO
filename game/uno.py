import pygame
import sys, os
from generator import Generator

class Uno():
    def __init__(self, game):
        self.game = game
        self.offsetx = self.game.DISPLAY_W/30
        self.offsety = self.game.DISPLAY_H/25
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.run_display = True
        self.select_card = 1
        self.size_deck = 0
        self.turno = 1
        self.players = 4
        generador = Generator()
        self.deck_data = generador.generator()
        self.main_deck = self.deck_data[0]
        self.discard_deck = self.deck_data[1]
        self.deck1 = self.deck_data[2]
        self.deck2 = self.deck_data[3]
        self.deck3 = self.deck_data[4]
        self.deck4 = self.deck_data[5]
        self.max_weight = self.game.DISPLAY_W/10
        self.max_height = self.game.DISPLAY_H/5

    
    def display_game(self):
        self.run_display = True
        self.play_music()
        while self.run_display:
            self.game.check_events()
            self.chech_input()
            self.game.display.fill(self.game.RED)
            self.draw_decks()
            #self.draw_discard_deck()
            #self.draw_main_deck()
            #self.dt = self.clock.tick(60) / 1000
            self.blit_screen()
            
    def chech_input(self):
        if self.game.BACK_KEY:
            pygame.mixer.music.stop()
            self.run_display = False
            self.game.playing = False
        if self.game.RIGHT_KEY:
            if self.select_card < self.deck1.size:
                self.select_card +=1
            else:
                self.select_card = 1
        if self.game.LEFT_KEY:
            if self.select_card > 1:
                self.select_card -=1
            else:
                self.select_card = self.deck1.size
        #if keys[pygame.K_UP]:
            #self.player_pos.x -= 300 * self.dt
    
    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

    def play_music(self):
        self.ruta_musica = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'game', 'music'))
        self.musica = pygame.mixer.music.load(os.path.join(self.ruta_musica,'main_menu.mp3'))
        pygame.mixer.music.set_volume(int(self.game.volumen)/100)
        pygame.mixer.music.play()

    def draw_decks(self):
        for i in range(1, 5):
            #dibujar el primer mazo
            if i == 1:
                sizedeck = self.deck1.deck_size()
                puntero = self.deck1.head
                mazo_width = self.max_weight * sizedeck
                mazo_height = self.max_height
                mazo_pos_x = (self.game.DISPLAY_W / 2) - (mazo_width / 3)
                mazo_pos_y = (self.game.DISPLAY_H - self.offsety) - mazo_height 
                if i == self.turno:
                    for i in range(1,sizedeck+1):
                        carta = pygame.image.load(eval(puntero.card["image"]))
                        carta = pygame.transform.scale(carta, (self.max_weight, self.max_height))
                        pos_x = mazo_pos_x + i * self.max_weight/3
                        if i == self.select_card:
                            pos_y = mazo_pos_y - (3*self.max_height/4)
                        else:
                            pos_y = mazo_pos_y
                        self.game.display.blit(carta, (pos_x,pos_y))
                        puntero = puntero.next
                else:
                    for i in range(1,sizedeck+1):
                        carta = pygame.image.load(eval(puntero.card["image"]))
                        carta = pygame.transform.scale(carta, (self.max_weight, self.max_height))
                        pos_x = mazo_pos_x + i * self.max_weight/3
                        pos_y = mazo_pos_y
                        self.game.display.blit(carta, (pos_x,pos_y))
                        puntero = puntero.next

            #dibujar el segundo mazo
            if i == 2:
                sizedeck = self.deck2.deck_size()
                puntero = self.deck2.head
                mazo_width = self.max_weight * sizedeck
                mazo_height = self.max_height
                mazo_pos_x = self.game.DISPLAY_W - (self.offsetx + mazo_height)
                mazo_pos_y = (self.game.DISPLAY_H/2) + (mazo_width/6)
                if i == self.turno:
                    for i in range(1,sizedeck+1):
                        carta = pygame.image.load(eval(puntero.card["image"]))
                        carta = pygame.transform.scale(carta, (self.max_weight, self.max_height))
                        rotated_carta = pygame.transform.rotate(carta, 90)
                        pos_y = mazo_pos_y - i * self.max_weight/3
                        if i == self.select_card:
                            pos_x = mazo_pos_x + self.max_height
                        else:
                            pos_x = mazo_pos_x
                        self.game.display.blit(rotated_carta, (pos_x,pos_y))
                        puntero = puntero.next
                else:
                    for i in range(1,sizedeck+1):
                        carta = pygame.image.load(eval(puntero.card["image"]))
                        carta = pygame.transform.scale(carta, (self.max_weight, self.max_height))
                        rotated_carta = pygame.transform.rotate(carta, 90)
                        pos_y = mazo_pos_y - i * self.max_weight/3
                        pos_x = mazo_pos_x
                        self.game.display.blit(rotated_carta, (pos_x,pos_y))
                        puntero = puntero.next
                    
            #dibujar el tercer mazo
            if i == 3:
                sizedeck = self.deck3.deck_size()
                puntero = self.deck3.head
                mazo_width = self.max_weight * sizedeck
                mazo_height = self.max_height
                mazo_pos_x = (self.game.DISPLAY_W/2) - (mazo_width/3)
                mazo_pos_y = self.offsety
                if i == self.turno:
                    for i in range(1,sizedeck+1):
                        carta = pygame.image.load(eval(puntero.card["image"]))
                        carta = pygame.transform.scale(carta, (self.max_weight, self.max_height))
                        pos_x = mazo_pos_x + i * self.max_weight/3
                        if i == self.select_card:
                            pos_y = mazo_pos_y + self.max_height
                        else:
                            pos_y = mazo_pos_y
                        self.game.display.blit(carta, (pos_x,pos_y))
                        puntero = puntero.next
                else:
                    for i in range(1,sizedeck+1):
                        carta = pygame.image.load(eval(puntero.card["image"]))
                        carta = pygame.transform.scale(carta, (self.max_weight, self.max_height))
                        pos_x = mazo_pos_x + i * self.max_weight/3
                        pos_y = mazo_pos_y
                        self.game.display.blit(carta, (pos_x,pos_y))
                        puntero = puntero.next
                    

            #dibujar el cuarto mazo
            if i == 4:
                sizedeck = self.deck4.deck_size()
                puntero = self.deck4.head
                mazo_width = self.max_weight * sizedeck
                mazo_height = self.max_height
                mazo_pos_x = self.offsetx
                mazo_pos_y = (self.game.DISPLAY_H/2) + (mazo_width/6)
                if i == self.turno:
                    for i in range(1,sizedeck+1):
                        carta = pygame.image.load(eval(puntero.card["image"]))
                        carta = pygame.transform.scale(carta, (self.max_weight, self.max_height))
                        rotated_carta = pygame.transform.rotate(carta, 270)
                        pos_y = mazo_pos_y - i * self.max_weight/3
                        if i == self.select_card:
                            pos_x = mazo_pos_x + self.max_height
                        else:
                            pos_x = mazo_pos_x
                        self.game.display.blit(rotated_carta, (pos_x,pos_y))
                        puntero = puntero.next
                else:
                    for i in range(1,sizedeck+1):
                        carta = pygame.image.load(eval(puntero.card["image"]))
                        carta = pygame.transform.scale(carta, (self.max_weight, self.max_height))
                        rotated_carta = pygame.transform.rotate(carta, 90)
                        pos_y = mazo_pos_y - i * self.max_weight/3
                        pos_x = mazo_pos_x
                        self.game.display.blit(rotated_carta, (pos_x,pos_y))
                        puntero = puntero.next

    #def draw_discard_deck(self):

    #def draw_main_deck(self):

