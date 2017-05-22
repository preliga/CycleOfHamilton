class Top:

    counter = 0

    __key = 0

    __arcs = []

    def __init__(self):
        self.__key = Top.counter
        self.__arcs = []
        Top.counter += 1

    def getKey(self):
        return self.__key

    def getArcs(self):
        return self.__arcs

    def addArc(self, _arc):
        self.__arcs.append(_arc)
        return self

    def getArcsList(self):
        arcList = ""

        for arc in self.__arcs:
            arcList += str(arc.getTo()) + "(" + str(arc.getValue()) + ") "

        return arcList


    def isArcTo(self, _to):
        for arc in self.__arcs:
            if arc.getTo() == _to:
                return True

    def getArcTo(self, _to):
        for arc in self.__arcs:
            if arc.getTo() == _to:
                return arc

    def getName(self):
        return self.__class__.__name__

    def __str__(self):
        return str(self.__key)