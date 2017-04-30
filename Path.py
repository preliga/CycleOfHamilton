class Path:

    __arcs = []
    __tops = []

    def __init__(self):
        self.__tops = []
        self.__arcs = []


    def isCycle(self):
        if len(self.__arcs) < 1:
            return False

        for i in range(len(self.__arcs)):
            if \
                    self.__tops[i] != self.__arcs[i].getFrom() \
                or \
                    self.__tops[i+1] != self.__arcs[i].getTo():
                return False

        return self.__arcs[len(self.__arcs) - 1].getTo().isArcTo(self.__tops[0])

    def getCyclePars(self):
        if not self.isCycle():
            return []
        else:
            cycle = self.getPathPars()
            cycle.append( (str(self.__tops[len(self.__tops) - 1].getKey()), str(self.__tops[0].getKey())) )

            return cycle


    def getPathPars(self):
        path = []
        for arc in self.__arcs:
            path.append((str(arc.getFrom().getKey()),str(arc.getTo().getKey()) ))

        return path

    def addArc(self, _arc):
        self.__arcs.append(_arc)
        return self

    def removeArc(self, _arc):
        self.__arcs.remove(_arc)
        return self

    def addTop(self, _top):
        self.__tops.append(_top)
        return self

    def removeTop(self, _top):
        self.__tops.remove(_top)
        return self

    def getValue(self):
        if len(self.__tops) < 1:
            return -1

        suma = 0

        for arc in self.__arcs:
            suma += arc.getValue()

        return suma

    def getSize(self):
        return len(self.__tops)

    def getStart(self):
        if len(self.__tops) < 1: return None

        return self.__tops[0]

    def __str__(self):
        path = "Path: "

        for top in self.__tops:
            path += str(top.getKey()) + " "

        return path
