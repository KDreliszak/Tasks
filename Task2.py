"""nie jestem pewien czy w poprawnie zrozumialem polecenie ale wykonalem je w nastepujacy sposob
tniemy dana blache na pol w poprzek dluzszego boku
nastepnie tniemy jeden z otrzymanych elementow ponownie wzdluz dluzszego boku
i tak az zostanie wykonana okreslona liczba ciec"""


def cut(x, y, n):

    if y > x:
        buff = x
        x = y
        y = buff

    x = x/2
    circuit = x*2 + y*2

    if n > 1:
        n -= 1
        circuit += cut(x, y, n)
    else:
        circuit += x*2 + y*2
    return circuit

#funkcja cut wymaga podania wymiarow blachy oraz liczby ciec
print(cut(1200, 900, 10))


