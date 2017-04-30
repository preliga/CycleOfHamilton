class Arc:
    __from = ""
    __to = ""
    __value = ""

    def __init__(self, _from, _to, _value):
        self.__from = _from
        self.__to = _to
        self.__value = _value

    def getTo(self):
        return self.__to

    def getFrom(self):
        return self.__from

    def getValue(self):
        return self.__value