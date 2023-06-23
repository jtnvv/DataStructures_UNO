import pygame
import os

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - self.game.DISPLAY_W // 6
        self.posicion = self.game.DISPLAY_H // 8
        self.offset_creditos = self.game.DISPLAY_H // 15
        self.offset2 = - self.game.DISPLAY_W // 4
        self.offset3 = - self.game.DISPLAY_W // 6
        self.size_author = int((self.game.DISPLAY_W + self.game.DISPLAY_H)/80)
        

    def draw_cursor(self):
        self.game.draw_text('*', self.game.font_size_cursor, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()
    
    def play_music(self):
        self.ruta_musica = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'game', 'music'))
        self.musica = pygame.mixer.music.load(os.path.join(self.ruta_musica,'main_menu.mp3'))
        nombre_cancion = "Mi Canción Favorita"
        pygame.mixer.music.set_endevent(pygame.USEREVENT)
        pygame.event.post(pygame.event.Event(pygame.USEREVENT, {"name": nombre_cancion}))     
        pygame.mixer.music.set_volume(int(self.game.volumen)/100)
        pygame.mixer.music.play()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Un Jugador"
        self.singleplayer_x, self.singleplayer_y = self.mid_w, self.posicion*4
        self.optiones_x, self.optiones_y = self.mid_w, self.posicion*5
        self.creditos_x, self.creditos_y = self.mid_w, self.posicion*6
        self.cerrar_x, self.cerrar_y = self.mid_w, self.posicion*7
        self.cursor_rect.midtop = (self.singleplayer_x + self.offset, self.singleplayer_y)
         

    def display_menu(self):
        if pygame.mixer.music.get_busy() == False:
            self.play_music()
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            ruta_logo = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'game', 'Icono'))
            logo = (os.path.join(ruta_logo,'logo.png'))
            self.game.draw_image_centerx(logo,1,self.posicion)
            #self.game.draw_text('UNO', self.game.font_size_title, self.game.DISPLAY_W / 2, self.posicion)
            self.game.draw_text("Un Jugador", self.game.font_size_text, self.singleplayer_x, self.singleplayer_y)
            self.game.draw_text("Opciones", self.game.font_size_text, self.optiones_x, self.optiones_y)
            self.game.draw_text("Creditos", self.game.font_size_text, self.creditos_x, self.creditos_y)
            self.game.draw_text("Salir", self.game.font_size_text, self.cerrar_x, self.cerrar_y)
            
            self.draw_cursor()
            self.blit_screen()


    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Un Jugador':
                self.cursor_rect.midtop = (self.optiones_x + self.offset, self.optiones_y)
                self.state = 'Opciones'
            elif self.state == 'Opciones':
                self.cursor_rect.midtop = (self.creditos_x + self.offset, self.creditos_y)
                self.state = 'Creditos'
            elif self.state == 'Creditos':
                self.cursor_rect.midtop = (self.cerrar_x + self.offset, self.cerrar_y)
                self.state = 'Salir'
            elif self.state == 'Salir':
                self.cursor_rect.midtop = (self.singleplayer_x + self.offset, self.singleplayer_y)
                self.state = 'Un Jugador'

        elif self.game.UP_KEY:
            if self.state == 'Un Jugador':
                self.cursor_rect.midtop = (self.cerrar_x + self.offset, self.cerrar_y)
                self.state = 'Salir'
            elif self.state == 'Opciones':
                self.cursor_rect.midtop = (self.singleplayer_x + self.offset, self.singleplayer_y)
                self.state = 'Un Jugador'
            elif self.state == 'Creditos':
                self.cursor_rect.midtop = (self.optiones_x + self.offset, self.optiones_y)
                self.state = 'Opciones'
            elif self.state == 'Salir':
                self.cursor_rect.midtop = (self.creditos_x + self.offset, self.creditos_y)
                self.state = 'Creditos'


    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Un Jugador':
                self.game.playing = True
            elif self.state == 'Opciones':
                self.game.curr_menu = self.game.optiones
            elif self.state == 'Creditos':
                self.game.curr_menu = self.game.creditos
            elif self.state == 'Salir':
                self.game.running = False
            self.run_display = False

class OptionesMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Volumen'
        self.vol_x, self.vol_y = self.mid_w + self.offset2, self.posicion*3
        self.resolucion_x, self.resolucion_y = self.mid_w + self.offset2, self.posicion*4
        self.visualizacion_x, self.visualizacion_y = self.mid_w + self.offset2, self.posicion*5
        self.cursor_rect.midtop = (self.vol_x , self.vol_y)
  
    def draw_opciones(self, text, size, x, y):
        font = pygame.font.Font(self.game.font_name,size)
        text_surface = font.render(text, True, self.game.WHITE)
        text_rect = (x,y)
        self.game.display.blit(text_surface,text_rect)


    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Opciones', self.game.font_size_title, self.game.DISPLAY_W / 2, self.posicion)
            self.draw_opciones("Volumen", self.game.font_size_text, self.vol_x, self.vol_y)
            self.draw_opciones(str(self.game.volumen), self.game.font_size_text, self.vol_x - (self.offset3 * 2), self.vol_y )
            self.draw_opciones("Resolucion", self.game.font_size_text, self.resolucion_x, self.resolucion_y)
            self.draw_opciones(str(str(self.game.DISPLAY_W) + 'x' + str(self.game.DISPLAY_H)), self.game.font_size_text, self.resolucion_x - (self.offset3 * 2), self.resolucion_y)
            self.draw_opciones("Visualizacion", self.game.font_size_text, self.visualizacion_x, self.visualizacion_y)
            #self.draw_opciones("Pantalla completa", int(self.game.font_size_text/2), self.visualizacion_x - (self.offset3 * 2), self.visualizacion_y)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Volumen':
                self.state = 'Resolucion'
                self.cursor_rect.midtop = (self.resolucion_x, self.resolucion_y)
            elif self.state == 'Resolucion':
                self.state = 'Volumen'
                self.cursor_rect.midtop = (self.vol_x, self.vol_y)
        elif self.game.START_KEY:
            
            pass
        elif self.game.LEFT_KEY:
            if self.state == 'Volumen':
                if self.game.volumen > 0:
                    self.game.volumen -= 10
                    pygame.mixer.music.set_volume(self.game.volumen/100)
            elif self.state == 'Resolucion':
                if self.game.DISPLAY_W > 800 and self.game.DISPLAY_H > 600:
                    self.game.DISPLAY_W = 1
                    
        elif self.game.RIGHT_KEY:
            if self.state == 'Volumen':
                if self.game.volumen < 100:
                    self.game.volumen += 10
                    pygame.mixer.music.set_volume(self.game.volumen/100)

class CreditosMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Creditos', self.game.font_size_title, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - self.posicion)
            self.game.draw_text('Hecho por', self.size_author, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2)
            self.game.draw_text('Juan Acevedo', self.size_author, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + self.offset_creditos)
            self.game.draw_text('Gabriel Delgado', self.size_author, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + self.offset_creditos*2)
            self.game.draw_text('Juan Ovalle', self.size_author, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + self.offset_creditos*3)
            self.game.draw_text('David Velasquez', self.size_author, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + self.offset_creditos*4)
            self.game.draw_text('Jonathan Velosa', self.size_author, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + self.offset_creditos*5)
            self.blit_screen()
