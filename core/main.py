from model import *


def main():
    matek = subject("matek")
    margit = teacher("margit")
    activity1 = activity(matek, margit)
    hetfo1 = slot(day.hetfo._name_, "1", activity1)

    print(hetfo1.__str__())

if __name__=='__main__':
    main()