import sys, os
ruta_carpeta1 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
sys.path.append(ruta_carpeta1)
import DatosDePrueba
ruta_carpeta1 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(ruta_carpeta1)
import mainDeck, discardDeck, newPlayerDeck

class Generator():
    #Genera el MainDeck
    def MainDeck(self,dataArray):
        mainDeck1 = mainDeck.MainDeck(len(dataArray))
        for i in dataArray:
            mainDeck1.PushBack(i)
        mainDeck1.DeckShuffle()
        return mainDeck1
    
    def DiscardDeck(self,main_deck):
        discDeck = discardDeck.DiscardDeck()
        #El PopBack retorna la última carta
        card = main_deck.PopBack()
        #Al principio del juego, evita que la primera carta sea
        #un poder
        if "power" in card:
            discDeck.Enqueue(card)
            discDeck.Enqueue(main_deck.PopBack())
        else:
            discDeck.Enqueue(card)
        return discDeck

    def PlayerDeck(self,main_deck):
        player_deck = newPlayerDeck.PlayerDeck()
        for i in range (7):
            player_deck.insert(main_deck.PopBack())
        return player_deck

    def generator(self):        
        test_arr = DatosDePrueba.data_array
        main_deck = self.MainDeck(test_arr)
        discard_deck = self.DiscardDeck(main_deck)
        deck1 = self.PlayerDeck(main_deck)
        deck2 = self.PlayerDeck(main_deck)
        deck3 = self.PlayerDeck(main_deck)
        deck4 = self.PlayerDeck(main_deck)
        print(main_deck)
        return main_deck, discard_deck, deck1, deck2, deck3, deck4
