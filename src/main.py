import mainDeck
import sys
import os
ruta_carpeta1 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
sys.path.append(ruta_carpeta1)
import DatosDePrueba
deckTest = mainDeck.MainDeck(len(DatosDePrueba.data_array))
for i in DatosDePrueba.data_array:
    deckTest.PushBack(i)
deckTest.DeckPrint()
print()
print("<----  Shuffle  --->")
deckTest.DeckShuffle()
print()
deckTest.DeckPrint()

