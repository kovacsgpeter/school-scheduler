from model import *
from service import *

def main():
    matek = subject("matek")
    angol = subject("angol")
    nemet = subject("nemet")
    irodalom = subject("irodalom")

    margit = teacher("margit")

    activity1 = activity(matek, margit)
    activity2 = activity(angol, margit)
    activity3 = activity(nemet, margit)
    activity4 = activity(irodalom, margit)

    service = init_service()

    service.activity_list.append(activity1)
    service.activity_list.append(activity2)
    service.activity_list.append(activity3)
    service.activity_list.append(activity4)

    service.activity_list.append(activity1)
    service.activity_list.append(activity2)
    service.activity_list.append(activity3)
    service.activity_list.append(activity4)

    service.activity_list.append(activity1)
    service.activity_list.append(activity2)
    service.activity_list.append(activity3)
    service.activity_list.append(activity4)

    service.activity_list.append(activity1)
    service.activity_list.append(activity2)
    service.activity_list.append(activity3)
    service.activity_list.append(activity4)

    service.activity_list.append(activity1)
    service.activity_list.append(activity2)
    service.activity_list.append(activity3)
    service.activity_list.append(activity4)


    service.create_population(4, 5, 10)

    # for d in service.slot_list:
    #     for h in d:
    #         print(h.__str__())
            # print(service.slot_list[i].__str__())

    for p in service.population:
        for d in service.slot_list:
            for h in d:
                print(h.__str__())
            # print(service.slot_list[i].__str__())


if __name__=='__main__':
    main()