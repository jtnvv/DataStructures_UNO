import mainDeck
import discardDeck
import playerDeck
import sys
import os
ruta_carpeta1 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
sys.path.append(ruta_carpeta1)
import DatosDePrueba
def MainDeckTest(test):
    deckTest = mainDeck.MainDeck(len(test))
    for i in test:
        deckTest.PushBack(i)
    deckTest.DeckPrint()
    print()
    print("<----  Shuffle  --->")
    deckTest.DeckShuffle()
    print()
    deckTest.DeckPrint()
    print()
    print()
    return deckTest

def DiscardDeckTest(test):
    deckTest = discardDeck.DiscardDeck()
    for i in test:
        deckTest.Enqueue(i)
    print()
    deckTest.printDeck()
        
def PlayerDeckTestDeal(test):
    main_Deck = MainDeckTest(test)
    deckTest = playerDeck.PlayerDeck()
    for i in range(7):
        card = main_Deck.PopBack()
        deckTest.add_card(card)
    deckTest.deckPrint()

test_arr = DatosDePrueba.data_array

#MainDeckTest(test_arr)
#DiscardDeckTest(test_arr)
#PlayerDeckTestDeal(test_arr)



