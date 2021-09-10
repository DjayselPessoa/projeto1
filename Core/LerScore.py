import csv
from pathlib import Path

'''
    Essa classe virou um método dentro do arquivo AbrirCSV.py
    This class has become a method within the AbrirCSV.py
'''

class LerScore:

    def lerscore(self, position, pegarDirRaiz):
        self.pegarDirRaiz = pegarDirRaiz
        self.position = position
        position = self.position

        scoreUser = []
        codPath = "#"+str(position - 1)
        nomeArquivoSCORE = "score_"+codPath+".csv"
        pathTratado = str(self.pegarDirRaiz)
        home = Path(pathTratado)
        sourcePath = Path(home, "Data", nomeArquivoSCORE)

        for f in csv.DictReader(open(sourcePath), delimiter=','):
            scoreUser.append(f["SCORE"])

        print(scoreUser)
        return scoreUser


ObjLerScore = LerScore()
