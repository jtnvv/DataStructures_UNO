from game import Game

g = Game()
#g.running es que está ejecutando el menú principal
while g.running:
    #curr_menu funciona para moverse entre las ventanas
    g.curr_menu.display_menu()
    g.game_loop()

#python-i18n, pygame-ce, pygame_gui