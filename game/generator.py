import sys, os
ruta_carpeta1 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
sys.path.append(ruta_carpeta1)
import DatosDePrueba
ruta_carpeta1 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(ruta_carpeta1)
import mainDeck, discardDeck, newPlayerDeck

class Generator():
    def MainDeck(self,main_deck):
        deckTest = mainDeck.MainDeck(len(main_deck))
        for i in main_deck:
            deckTest.PushBack(i)
        deckTest.DeckShuffle()
        return deckTest
    
    def DiscardDeck(self,main_deck):
        deckTest = discardDeck.DiscardDeck()
        card = main_deck.PopBack()
        if card["color"] == "Black":
            deckTest.Enqueue(card)
            deckTest.Enqueue(main_deck.PopBack())
        else:
            deckTest.Enqueue(card)
        return deckTest

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
        return main_deck, discard_deck, deck1, deck2, deck3, deck4

