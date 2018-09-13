from core.model import *
from random import shuffle

class init_service:
    def __init__(self):
        self.subject_list = []
        self.teacher_list = []
        self.activity_list = []
        self.slot_list = []
        self.population = []

    def create_population(self, daily_slots, day_num, pop_num):

        # for d in range(5):
        #     for h in range(daily_slots):
        #         self.slot_list.append(slot(day(d).name, (8+h)))

        self.slot_list=[[slot(day(d+1).name, (8+h), 0) for h in range(daily_slots)] for d in range(day_num)]

        temp_act_list = self.activity_list
        shuffle(temp_act_list)



        def create_entity():
            counter = daily_slots*day_num-1
            for d in range(day_num):
                for h in range(daily_slots):
                    self.slot_list[d][h].activity = temp_act_list[counter]
                    counter -= 1

            return self.slot_list

        for i in range(pop_num):
            self.population.append(create_entity())





