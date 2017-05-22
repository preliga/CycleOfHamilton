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

from App import App
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    okno = App()
    sys.exit(app.exec_())