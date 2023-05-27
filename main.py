import os, sys, pygame
ruta_carpeta1 = os.path.abspath(os.path.join(os.path.dirname(__file__), 'game'))
sys.path.append(ruta_carpeta1)
import init_game
g =init_game.Game()
#g.running es que está ejecutando el menú principal
while g.running:
    #curr_menu funciona para moverse entre las ventanas
    g.curr_menu.display_menu()
    g.game_loop()

