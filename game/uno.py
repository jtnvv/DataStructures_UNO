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
        self.select_card = 0
        self.size_deck = 0
        self.turno = 0
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
        self.reverse = False
        self.block = False

    
    def display_game(self):
        self.run_display = True
        self.play_music()
        while self.run_display:
            self.game.check_events()
            self.chech_input()
            self.game.display.fill(self.game.RED)
            self.draw_decks()
            self.draw_discard_deck()
            self.draw_main_deck()
            self.check_winner()
            self.dt = self.clock.tick(60) / 1000
            self.blit_screen()
            
    def chech_input(self):
        if self.game.BACK_KEY:
            pygame.mixer.music.stop()
            self.run_display = False
            self.game.playing = False
        if self.game.RIGHT_KEY:
            match self.turno:
                case 0:
                    count = (self.select_card+1)
                    self.select_card = count % self.deck1.deckSize
                case 1:
                    count = (self.select_card+1)
                    self.select_card = count % self.deck2.deckSize
                case 2:
                    count = (self.select_card+1)
                    self.select_card = count % self.deck3.deckSize
                case 3:
                    count = (self.select_card+1)
                    self.select_card = count % self.deck4.deckSize
        if self.game.LEFT_KEY:
            match self.turno:
                case 0:
                    count = (self.select_card-1)
                    self.select_card = count % self.deck1.deckSize
                case 1:
                    count = (self.select_card-1)
                    self.select_card = count % self.deck2.deckSize
                case 2:
                    count = (self.select_card-1)
                    self.select_card = count % self.deck3.deckSize
                case 3:
                    count = (self.select_card-1)
                    self.select_card = count % self.deck4.deckSize
        if self.game.START_KEY:
            play = self.play_card()
            if play:
                self.select_card = 0
                if self.block:
                    self.change_turn()
                    self.change_turn()
                    self.block = False
                else:
                    self.change_turn()
        if self.game.UP_KEY:
            self.take_card()
            self.change_turn()

    def change_turn(self):
        if self.reverse: 
            count = self.turno - 1
            self.turno = count % self.players
        else:
            count = self.turno + 1
            self.turno = count % self.players
    
    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

    def play_music(self):
        self.ruta_musica = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'game', 'music'))
        self.musica = pygame.mixer.music.load(os.path.join(self.ruta_musica,'nice.mp3'))
        pygame.mixer.music.set_volume(int(self.game.volumen)/10)
        pygame.mixer.music.play()

    def draw_decks(self):
        for i in range(4):
            match i:
            #dibujar el primer mazo
                case 0:
                    sizedeck = self.deck1.deckSize
                    arr = self.deck1.inOrderTraversal()
                    mazo_width = ((self.max_weight/3) * (sizedeck-1)) + self.max_weight
                    mazo_height = self.max_height
                    mazo_pos_x = (self.game.DISPLAY_W / 2) - (mazo_width/2)
                    mazo_pos_y = (self.game.DISPLAY_H - self.offsety) - mazo_height
                    if i == self.turno:
                        for j in range(sizedeck):
                            puntero = arr[j]
                            carta = pygame.image.load(eval(puntero.card["image"]))
                            carta = pygame.transform.scale(carta, (self.max_weight, self.max_height))
                            pos_x = mazo_pos_x + j * self.max_weight/3
                            if j == self.select_card:
                                pos_y = (mazo_pos_y - (3*self.max_height/4)) 
                            else:
                                pos_y = mazo_pos_y
                            self.game.display.blit(carta, (pos_x,pos_y))
                    else:
                        for j in range(sizedeck):
                            puntero = arr[j]
                            carta = pygame.image.load(eval(puntero.card["image"]))
                            carta = pygame.transform.scale(carta, (self.max_weight, self.max_height))
                            pos_x = mazo_pos_x + j * self.max_weight/3
                            pos_y = mazo_pos_y
                            self.game.display.blit(carta, (pos_x,pos_y))

                #dibujar el segundo mazo
                case 1:
                    sizedeck = self.deck2.deckSize
                    arr = self.deck2.inOrderTraversal()
                    mazo_width = self.max_weight * sizedeck
                    mazo_height = self.max_height
                    mazo_pos_x = self.game.DISPLAY_W - (self.offsetx + mazo_height)
                    mazo_pos_y = (self.game.DISPLAY_H/2) + (mazo_width/6)
                    if i == self.turno:
                        for j in range(sizedeck):
                            puntero = arr[j]
                            carta = pygame.image.load(eval(puntero.card["image"]))
                            carta = pygame.transform.scale(carta, (self.max_weight, self.max_height))
                            rotated_carta = pygame.transform.rotate(carta, 90)
                            pos_y = mazo_pos_y - j * self.max_weight/3
                            if j == self.select_card:
                                pos_x = mazo_pos_x - (3*self.max_height/4)
                            else:
                                pos_x = mazo_pos_x
                            self.game.display.blit(rotated_carta, (pos_x,pos_y))
                    else:
                        for j in range(sizedeck):
                            puntero = arr[j]
                            carta = pygame.image.load(eval(puntero.card["image"]))
                            carta = pygame.transform.scale(carta, (self.max_weight, self.max_height))
                            rotated_carta = pygame.transform.rotate(carta, 90)
                            pos_y = mazo_pos_y - j * self.max_weight/3
                            pos_x = mazo_pos_x
                            self.game.display.blit(rotated_carta, (pos_x,pos_y))
                        
                #dibujar el tercer mazo
                case 2:
                    sizedeck = self.deck3.deckSize
                    arr = self.deck3.inOrderTraversal()
                    mazo_width = ((self.max_weight/3) * (sizedeck-1)) + self.max_weight
                    mazo_height = self.max_height
                    mazo_pos_x = (self.game.DISPLAY_W/2) - (mazo_width/2)
                    mazo_pos_y = self.offsety
                    if i == self.turno:
                        for j in range(sizedeck):
                            puntero = arr[j]
                            carta = pygame.image.load(eval(puntero.card["image"]))
                            carta = pygame.transform.scale(carta, (self.max_weight, self.max_height))
                            pos_x = mazo_pos_x + j * self.max_weight/3
                            if j == self.select_card:
                                pos_y = mazo_pos_y + (3*self.max_height/4)
                            else:
                                pos_y = mazo_pos_y
                            self.game.display.blit(carta, (pos_x,pos_y))
                    else:
                        for j in range(sizedeck):
                            puntero = arr[j]
                            carta = pygame.image.load(eval(puntero.card["image"]))
                            carta = pygame.transform.scale(carta, (self.max_weight, self.max_height))
                            pos_x = mazo_pos_x + j * self.max_weight/3
                            pos_y = mazo_pos_y
                            self.game.display.blit(carta, (pos_x,pos_y))
                        

                #dibujar el cuarto mazo
                case 3:
                    sizedeck = self.deck4.deckSize
                    arr = self.deck4.inOrderTraversal()
                    mazo_width = self.max_weight * sizedeck
                    mazo_height = self.max_height
                    mazo_pos_x = self.offsetx
                    mazo_pos_y = (self.game.DISPLAY_H/2) - (mazo_width/6)
                    if i == self.turno:
                        for j in range(sizedeck):
                            puntero = arr[j]
                            carta = pygame.image.load(eval(puntero.card["image"]))
                            carta = pygame.transform.scale(carta, (self.max_weight, self.max_height))
                            rotated_carta = pygame.transform.rotate(carta, 270)
                            pos_y = mazo_pos_y + j * self.max_weight/3
                            if j == self.select_card:
                                pos_x = mazo_pos_x + self.max_height
                            else:
                                pos_x = mazo_pos_x
                            self.game.display.blit(rotated_carta, (pos_x,pos_y))
                    else:
                        for j in range(sizedeck):
                            puntero = arr[j]
                            carta = pygame.image.load(eval(puntero.card["image"]))
                            carta = pygame.transform.scale(carta, (self.max_weight, self.max_height))
                            rotated_carta = pygame.transform.rotate(carta, 270)
                            pos_y = mazo_pos_y + j * self.max_weight/3
                            pos_x = mazo_pos_x
                            self.game.display.blit(rotated_carta, (pos_x,pos_y))

    def draw_discard_deck(self):
        card_data = self.discard_deck.LastCardPlayed()
        carta = pygame.image.load(eval(card_data["image"]))
        carta = pygame.transform.scale(carta, (self.max_weight, self.max_height))
        imagen_pos_x = (self.game.DISPLAY_W - self.max_weight) // 2
        imagen_pos_y = (self.game.DISPLAY_H - self.max_height) // 2
        self.game.display.blit(carta, (imagen_pos_x, imagen_pos_y))

    def draw_main_deck(self):
        ruta_imagen = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'Cards','main_deck.png'))
        carta = pygame.image.load(ruta_imagen)
        carta = pygame.transform.scale(carta, (self.max_weight, self.max_height))
        imagen_pos_x = (self.game.DISPLAY_W - self.max_weight) // 3
        imagen_pos_y = (self.game.DISPLAY_H - self.max_height) // 2
        self.game.display.blit(carta, (imagen_pos_x, imagen_pos_y))

    def play_card(self):
        match self.turno:
            case 0:
                arr = self.deck1.inOrderTraversal()
                puntero = arr[self.select_card]
                if self.check_play_card(puntero):
                    self.power_card(puntero)
                    self.discard_deck.Enqueue(puntero.card)
                    self.deck1.delete(puntero)
                    return True
                else:
                    return False
            case 1:
                arr = self.deck2.inOrderTraversal()
                puntero = arr[self.select_card]
                if self.check_play_card(puntero):
                    self.power_card(puntero)
                    self.discard_deck.Enqueue(puntero.card)
                    self.deck2.delete(puntero)
                    return True
                else:
                    return False
            case 2:
                arr = self.deck3.inOrderTraversal()
                puntero = arr[self.select_card]
                if self.check_play_card(puntero):
                    self.power_card(puntero)
                    self.discard_deck.Enqueue(puntero.card)
                    self.deck3.delete(puntero)
                    return True
                else:
                    return False
            case 3:
                arr = self.deck4.inOrderTraversal()
                puntero = arr[self.select_card]
                if self.check_play_card(puntero):
                    self.power_card(puntero)
                    self.discard_deck.Enqueue(puntero.card)
                    self.deck4.delete(puntero)
                    return True
                else:
                    return False
                
    def check_winner(self):
        if self.deck1.deckSize == 0:
            self.game.draw_center_text("Jugador 1 Gana", self.game.font_size_title, self.game.DISPLAY_W/2,self.game.DISPLAY_H/2)
            self.blit_screen()
            while self.game.playing:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                            self.game.playing = False
                            self.run_display = False
        elif self.deck2.deckSize == 0:
            self.game.draw_center_text("Jugador 2 Gana", self.game.font_size_title, self.game.DISPLAY_W/2,self.game.DISPLAY_H/2)
            self.blit_screen()
            while self.game.playing:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                            self.game.playing = False
                            self.run_display = False
        elif self.deck3.deckSize == 0:
            self.game.draw_center_text("Jugador 3 Gana", self.game.font_size_title, self.game.DISPLAY_W/2,self.game.DISPLAY_H/2)
            self.blit_screen()
            while self.game.playing:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                            self.game.playing = False
                            self.run_display = False
        elif self.deck4.deckSize == 0:
            self.game.draw_center_text("Jugador 4 Gana", self.game.font_size_title, self.game.DISPLAY_W/2,self.game.DISPLAY_H/2)
            self.blit_screen()
            while self.game.playing:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                            self.game.playing = False
                            self.run_display = False
        
    def check_play_card(self,card):
        discardCard = self.discard_deck.LastCardPlayed()
        itCard = card.card
        if "number" in itCard and "number" in discardCard:
            if itCard["number"] == discardCard["number"] or itCard["color"] == discardCard["color"]:
                return True
            else:
                return False
        elif itCard["color"] == "Black" or itCard["color"] == discardCard["color"]:
            return True
        elif "power" in itCard and "power" in discardCard:
            if itCard["power"] == discardCard["power"]:
                return True
            else:
                return False
        else:
            return False

    def take_card(self):
        card = self.main_deck.PopBack()
        match self.turno:
            case 0:
                self.deck1.insert(card)
            case 1:
                self.deck2.insert(card)
            case 2:
                self.deck3.insert(card)
            case 3:
                self.deck4.insert(card)

    def power_card(self,card):
        itCard = card.card
        if "power" in itCard:
            if itCard["power"] == "Block":
                self.block = not self.block
            elif itCard["power"] == "+2":
                if self.reverse:
                    match self.turno:
                        case 0:
                            for i in range(2):
                                self.deck4.insert(self.main_deck.PopBack())
                        case 1:
                            for i in range(2):
                                self.deck1.insert(self.main_deck.PopBack())
                        case 2:
                            for i in range(2):
                                self.deck2.insert(self.main_deck.PopBack())
                        case 3:
                            for i in range(2):
                                self.deck3.insert(self.main_deck.PopBack())
                else:
                    match self.turno:
                        case 0:
                            for i in range(2):
                                self.deck2.insert(self.main_deck.PopBack())
                        case 1:
                            for i in range(2):
                                self.deck3.insert(self.main_deck.PopBack())
                        case 2:
                            for i in range(2):
                                self.deck4.insert(self.main_deck.PopBack())
                        case 3:
                            for i in range(2):
                                self.deck1.insert(self.main_deck.PopBack())

            elif itCard["power"] == "Reverse":
                self.reverse = not self.reverse

            elif itCard["power"] == "+4":
                if self.reverse:
                    match self.turno:
                         case 0:
                            for i in range(4):
                                self.deck4.insert(self.main_deck.PopBack())
                         case 1:
                            for i in range(4):
                                self.deck1.insert(self.main_deck.PopBack())
                         case 2:
                            for i in range(4):
                                self.deck2.insert(self.main_deck.PopBack())
                         case 3:
                            for i in range(4):
                                self.deck3.insert(self.main_deck.PopBack())
                else:
                    match self.turno:
                        case 0:
                            for i in range(4):
                                self.deck2.insert(self.main_deck.PopBack())
                        case 1:
                            for i in range(4):
                                self.deck3.insert(self.main_deck.PopBack())
                        case 2:
                            for i in range(4):
                                self.deck4.insert(self.main_deck.PopBack())
                        case 3:
                            for i in range(4):
                                self.deck1.insert(self.main_deck.PopBack())
                