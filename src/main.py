import mainDeck
import datos
test = datos.DatosDePrueba.data_array
deckTest = mainDeck.MainDeck(len(test))
for i in test:
    deckTest.PushBack(i)
deckTest.DeckPrint()
print()
print("Ahora mezclado")
deckTest.DeckShuffle()
print()
deckTest.DeckPrint()

