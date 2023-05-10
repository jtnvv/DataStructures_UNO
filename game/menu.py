import pygame

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - self.game.DISPLAY_W // 6
        self.posicion = self.game.DISPLAY_H // 8

    def draw_cursor(self):
        self.game.draw_text('*', self.game.font_size_cursor, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Un Jugador"
        self.singleplayer_x, self.singleplayer_y = self.mid_w, self.posicion*3
        self.optiones_x, self.optiones_y = self.mid_w, self.posicion*4
        self.creditos_x, self.creditos_y = self.mid_w, self.posicion*5
        self.cerrar_x, self.cerrar_y = self.mid_w, self.posicion*6
        self.cursor_rect.midtop = (self.singleplayer_x + self.offset, self.singleplayer_y)


    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('UNO', self.game.font_size_title, self.game.DISPLAY_W / 2, self.posicion)
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
        self.vol_x, self.vol_y = self.mid_w, self.posicion*3
        self.resolucion_x, self.resolucion_y = self.mid_w, self.posicion*4
        self.cursor_rect.midtop = (self.vol_x + self.offset, self.vol_y)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Opciones', self.game.font_size_title, self.game.DISPLAY_W / 2, self.posicion)
            self.game.draw_text("Volumen", self.game.font_size_text, self.vol_x, self.vol_y)
            self.game.draw_text("Resolucion", self.game.font_size_text, self.resolucion_x, self.resolucion_y)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Volumen':
                self.state = 'Resolucion'
                self.cursor_rect.midtop = (self.resolucion_x + self.offset, self.resolucion_y)
            elif self.state == 'Resolucion':
                self.state = 'Volumen'
                self.cursor_rect.midtop = (self.vol_x + self.offset, self.vol_y)
        elif self.game.START_KEY:
            
            pass

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
            self.game.draw_text('Creditos', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text('Hecho por Juan', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 10)
            self.blit_screen()
