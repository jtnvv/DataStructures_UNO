import mainDeck
import discardDeck
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

def DiscardDeckTest(test):
    deckTest = discardDeck.DiscardDeck()
    for i in test:
        deckTest.Enqueue(i)
    print()
    deckTest.printDeck()
        




