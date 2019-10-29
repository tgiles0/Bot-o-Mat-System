from src.robot import Robot
import src.bom_helper as bh
import time
import copy


class Aeronautical(Robot):
    def __init__(self, name):
        super(Aeronautical, self).__init__(name)
        self.type = 'Aeronautical'
        self.chore_list = []
        self.time_worked_on_chores = 0

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def set_chore_list(self, ch_list):
        self.chore_list = ch_list

    def update_time_working_on_chores(self, time_on_chore):
        self.time_worked_on_chores += time_on_chore

    def get_robot_score(self):
        return self.time_worked_on_chores

    def can_perform_chore(self, chore):
        ret_value = True
        if chore == 'take out the recycling' or chore == 'make a sammich':
            ret_value = False
        return ret_value

    def complete_chores(self):
        chores_to_complete = copy.deepcopy(self.chore_list)
        for chore in chores_to_complete:
            print(self.name + ' started: ' + chore)
            if self.can_perform_chore(chore):
                time_in_seconds = bh.get_time_for_chore(chore)
                time.sleep(time_in_seconds)
                print(self.name + ' completed: ' + chore + '\n')
                """ Now that Robot completed the chore it can be removed from its list. """
                # print('Copied list')
                # print(chores_to_complete)
                self.chore_list.remove(chore)
                """ Update the time the robot has spent working on chores """
                self.update_time_working_on_chores(time_in_seconds)
                # print('Original list')
                # print(self.chore_list)
            else:
                print(self.name + ' is unable to complete the task: ' + chore + '\n')
