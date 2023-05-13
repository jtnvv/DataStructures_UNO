import sys, os
ruta_carpeta1 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
sys.path.append(ruta_carpeta1)
import DatosDePrueba
ruta_carpeta1 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(ruta_carpeta1)
import mainDeck, discardDeck, playerDeck

class Generator():
    def MainDeck(main_deck):
        deckTest = mainDeck.MainDeck(len(main_deck))
        for i in main_deck:
            deckTest.PushBack(i)
        deckTest.DeckShuffle()
        return deckTest
    
    def DiscardDeck(main_deck):
        deckTest = discardDeck.DiscardDeck()
        deckTest.Enqueue(main_deck.PopBack())
        return deckTest

    def PlayerDeck(main_deck):
        player_deck = playerDeck.PlayerDeck()
        for i in range (7):
            player_deck.add_card(main_deck.PopBack())
        return player_deck

    def generator(self):        
        test_arr = DatosDePrueba.data_array
        main_deck = self.MainDeck(test_arr)
        discard_deck = self.DiscardDeck(main_deck)
        deck1 = self.PlayerDeck(main_deck)
        deck2 = self.PlayerDeck(main_deck)
        deck3 = self.PlayerDeck(main_deck)
        deck4 = self.PlayerDeck(main_deck)
        return main_deck, discard_deck, deck1, deck2, deck3, deck4

