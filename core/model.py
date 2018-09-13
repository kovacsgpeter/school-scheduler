from enum import Enum

class day(Enum):
    hetfo=1
    kedd=2
    szerda=3
    csutortok=4
    pentek=5

class slot:

    def __init__(self, day=None, hour=None, activity=None):
        self.__day = day
        self.__hour = hour
        self.activity = activity

    def __repr__(self):
        pass

    def __str__(self):
        return "{} {} {}".format(self.__day, self.__hour, self.activity.__str__())



class activity:

    def __init__(self, subject, teacher):
        self.subject = subject
        self.teacher = teacher

    def __repr__(self):
        pass

    def __str__(self):
        return "{} {}".format(self.subject.__str__(), self.teacher.__str__())


class subject:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        pass

    def __str__(self):
        return "{}".format(self.name)


class teacher:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        pass

    def __str__(self):
        return "{}".format(self.name)
