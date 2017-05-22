from Path import Path
from Top import Top
import random
from Arc import Arc
import copy

class MyGraph:

    __tops = []

    def __init__(self):
        self.__tops = []

    def addTop(self, _top):
        self.__tops.append(_top)
        return self

    def getTops(self):
        return self.__tops

    def getTopsList(self):
        topsList = []

        for top in self.__tops:
            topsList.append(str(top.getKey()))

        return topsList

    def getTopsLabel(self):
        topsLabel = {}
        for i in range(len(self.__tops)):
            topsLabel[str(i)] = str(self.__tops[i].getKey())

        return topsLabel

    def addRandomTopsAndArcs(self, _numbersOfTop, _valueOfArc):
        tops = []
        for i in range(_numbersOfTop):
            tops.append(Top())

        for topFrom in tops:
            for topTo in tops:
                if topFrom != topTo:
                    if random.randint(0, 2) != 1:
                        topFrom.addArc(Arc(topFrom, topTo, random.randint(1, _valueOfArc)))

        for top in tops:
            self.addTop(top)



    def hamiltonCycle(self, _top = None):
        visited = []
        path = Path()

        if _top == None:
            _top = self.__tops[random.randint(0,len(self.__tops)-1)]

        self.DFSHamilton(_top,visited,path)

        return path

    def DFSHamilton(self, _top, _visited, _path):
        _path.addTop(_top)

        if _path.getSize() < len(self.__tops):

            _visited.append(_top)

            for arc in _top.getArcs():
                if arc.getTo() not in _visited:
                    _path.addArc(arc)

                    if self.DFSHamilton(arc.getTo(),_visited,_path):
                        return True

                    _path.removeArc(arc)

            _visited.remove(_top)
        else:
            if _path.isCycle():
                return True

        _path.removeTop(_top)

        return False


    def hamiltonCycleAllPath(self):

        minPath = Path()
        for top in self.__tops:
            path = Path()
            path.addTop(top)
            self.__allPath(top,path,minPath)

        return minPath

    def __allPath(self,_top, _path, _minPath):
        for arc in _top.getArcs():
            if arc.getTo() not in _path:
                _path.addTop(arc.getTo())
                _path.addArc(arc)

                if _path.getSize() == len(self.__tops):
                    if _minPath.getValue() == -1 or _minPath.getValue() > _path.getValue():
                        if _path.isCycle():
                            _minPath.myCopy(_path)

                self.__allPath(arc.getTo(), _path, _minPath)

                _path.removeTop(arc.getTo())
                _path.removeArc(arc)


    def hamiltonCyclePermutation(self):
        tops = self.__tops.copy()

        path = [Path()]

        self.__permutation(len(tops), tops, path)

        return path[0]

    def __permutation(self, _k, _tops, _path):
        if _k == 0:
            p = [self.__checkPermutation(_tops)]
            if p[0] != None and ( _path[0].getValue() == -1 or p[0].getValue() < _path[0].getValue()):
                _path[0] = p[0]

        else:
            for i in range(_k):
                _tops[i], _tops[_k - 1] = _tops[_k - 1], _tops[i]
                self.__permutation(_k - 1,_tops,_path)
                _tops[i], _tops[_k - 1] = _tops[_k - 1], _tops[i]

    def __checkPermutation(self, _tops):

        path = Path()
        for i in range(len(_tops)):
            path.addTop(_tops[i])

            if i != 0:
                if _tops[i-1].isArcTo(_tops[i]):
                    path.addArc(_tops[i-1].getArcTo(_tops[i]))
                else:
                    return None

        if path.isCycle():
            return path
        else:
            return None


    def __str__(self):
        graphStr = ''
        for top in self.__tops:
            graphStr += str(top) + ": " + top.getArcsList() + "<br>"
        return graphStr