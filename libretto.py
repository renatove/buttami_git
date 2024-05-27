from datetime import datetime
class Libretto:
    def __init__(self):
        self._voti = []

    def append(self, voto):
        self._voti.append(voto)

    def media(self):
        if len(self._voti) == 0:
            raise ValueError("Elenco voti vuoto")
        punteggi = [v.punteggio for v in self._voti]
        return sum(punteggi)/len(punteggi)

class Voto:
    def __init__(self, esame, cfu, punteggio, lode, data):
        self.erame = esame
        self.cfu = cfu
        self.punteggio = punteggio
        self.lode = lode
        self.data = data
        if self.lode and self.punteggio!=30:
            raise ValueError("Lode non applicabile")

    def __str__(self):
        return (f"Esame {self.erame} superato con {self.punteggio}")

    def __repr__(self):
        return (
            f"{type(self).__name__}(esame='{self.erame}',cfu={self.cfu},punteggio={self.punteggio},lode={self.lode},data='{self.data}')"
        )

mio_libretto = Libretto()

try:
    voto_1 = Voto("Analisi matematica I", 10, 28, False,"2022-02-10")
    voto_2 = Voto("Basi di Dati", 8, 30, True,"2022-06-10")
except ValueError as e:
    print(e)
else:
    mio_libretto.append(voto_1)
    mio_libretto.append(voto_2)

print("Media dei voti: ", mio_libretto.media())


