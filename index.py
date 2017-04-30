from Top import Top
from Arc import Arc
from MyGraph import MyGraph
from Path import Path
from GraphPlot import GraphPlot
import random

import datetime
import time

# t0 = Top()
# t1 = Top()
# t2 = Top()
# t3 = Top()
# t4 = Top()
#
# t0.addArc(Arc(t0, t1, 1))\
#     .addArc(Arc(t0, t2, 2))\
#     .addArc(Arc(t0, t4, 4))
#
#
# t1.addArc(Arc(t1, t0, 2))\
#     .addArc(Arc(t1, t3, 8))\
#     .addArc(Arc(t1, t4, 7))
#
# t2.addArc(Arc(t2, t0, 5))\
#     .addArc(Arc(t2, t1, 4))\
#     .addArc(Arc(t2, t3, 3))
#
#
# t3.addArc(Arc(t3, t1, 2))
#
#
# t4.addArc(Arc(t4, t0, 3))\
#     .addArc(Arc(t4, t3, 1))
#
#
# myGraph = MyGraph() \
#     .addTop(t0)\
#     .addTop(t1)\
#     .addTop(t2)\
#     .addTop(t3)\
#     .addTop(t4)

numbersOfTop = random.randint(2,100)
# numbersOfTop = 10
print("Tops: %d" % (numbersOfTop))

myGraph = MyGraph()
myGraph.addRandomTopsAndArcs(numbersOfTop,12)

# time1 = datetime.datetime.now().microsecond
path = myGraph.hamiltonCycle()
# path = myGraph.hamiltonCyclePermutation()
# time2 = datetime.datetime.now().microsecond

# delta = time2 - time1
# delta = (datetime.datetime.strptime(time2,'%H:%M:%S') - datetime.datetime.strptime(time1,'%H:%M:%S'))
# print(delta)
# print(delta.microseconds)

# print(time1)
# print(time2)




print(path)
print(path.isCycle())
print(path.getValue())

graphPlot = GraphPlot()
graphPlot.drawGraphPlot(myGraph,path)
