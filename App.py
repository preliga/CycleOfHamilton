from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QLineEdit, QPushButton, QHBoxLayout, QMessageBox
from MyGraph import MyGraph
from GraphPlot import GraphPlot
import time

class App(QWidget):

    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        self.interfejs()

    def interfejs(self):

        numbersOfTopDefault = '5';
        valueOfArcDefault = '15'

        # etykiety
        numbersOfTopLabel = QLabel("Liczba wierzchołków", self)
        valueOfArcLabel = QLabel("Maksymalna wartość wierzchołków", self)

        # przypisanie widgetów do układu tabelarycznego
        ukladT = QGridLayout()
        ukladT.addWidget(numbersOfTopLabel, 0, 0)
        ukladT.addWidget(valueOfArcLabel, 1, 0)

        # 1-liniowe pola edycyjne
        self.numbersOfTopInput = QLineEdit()
        self.valueOfArcInput = QLineEdit()

        self.numbersOfTopInput.setText(numbersOfTopDefault)
        self.valueOfArcInput.setText(valueOfArcDefault)

        ukladT.addWidget(self.numbersOfTopInput, 0, 1)
        ukladT.addWidget(self.valueOfArcInput, 1, 1)

        # przyciski
        generujBtn = QPushButton("&Generuj graf", self)
        generujBtn.clicked.connect(self.graphGenerate)

        ukladH = QHBoxLayout()
        ukladH.addWidget(generujBtn)

        self.neighborhoodList = QLabel("<b>Lista sąsiedztwa:</b>", self)
        self.cycleP = QLabel("<b>Wartość cyklu (dokładny):</b>", self)
        self.cycle = QLabel("<b>Wartość cyklu:</b>", self)
        self.timeP = QLabel("<b>Czas dokładny:</b>", self)
        self.time = QLabel("<b>Czas:</b>", self)

        ukladF = QGridLayout()
        ukladF.addWidget(self.cycleP, 0, 0)
        ukladF.addWidget(self.cycle, 1, 0)
        ukladF.addWidget(self.timeP, 2, 0)
        ukladF.addWidget(self.time, 3, 0)
        ukladF.addWidget(self.neighborhoodList, 4, 0)

        ukladT.addLayout(ukladF, 3, 0, 1, 3)

        ukladT.addLayout(ukladH, 2, 0, 1, 3)
        # przypisanie utworzonego układu do okna
        self.setLayout(ukladT)

        self.setGeometry(20, 20, 300, 100)
        self.setWindowTitle("Generator Grafu")
        self.show()

    def graphGenerate(self):
        try:
            numbersOfTop = int(self.numbersOfTopInput.text())
            valueOfArc = int(self.valueOfArcInput.text())

            myGraph = MyGraph()
            myGraph.addRandomTopsAndArcs(numbersOfTop,valueOfArc)

            current_milli_time = lambda: int(round(time.time() * 1000))

            timeOd = current_milli_time()
            path = myGraph.hamiltonCycle()
            timeDo = current_milli_time()

            time1 = (timeDo - timeOd) *0.001

            timeOd = current_milli_time()
            pathP = myGraph.hamiltonCycleAllPath() #aby wyłączyć algorytm dokładny zakomentować linijkę
            timeDo = current_milli_time()

            time2 = (timeDo - timeOd) *0.001

            self.neighborhoodList.setText("<b>Lista sąsiedztwa:</b> <br>%s" % myGraph)
            self.cycleP.setText("<b>Wartość cyklu (dokładny):</b> %d<br>%s" % (pathP.getValue(),pathP)) #aby wyłączyć algorytm dokładny zakomentować linijkę
            self.cycle.setText("<b>Wartość cyklu:</b> %d<br>%s" % (path.getValue(),path))
            self.timeP.setText("<b>Czas dokładny:</b> %s [s]" % time2)
            self.time.setText("<b>Czas:</b> %s [s]" % time1)

            graphPlot = GraphPlot()
            graphPlot.drawGraphPlot(myGraph,pathP) #aby wyłączyć algorytm dokładny zakomentować linijkę
            #graphPlot.drawGraphPlot(myGraph, path) #aby wyłączyć algorytm dokładny ODKOMENTOWAć linijkę
            self.close()

        except ValueError:
            QMessageBox.warning(self, "Błąd", "Błędne dane", QMessageBox.Ok)
