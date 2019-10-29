import random
from src.unipedal import Unipedal
from src.bipedal import Bipedal
from src.quadrupedal import Quadrupedal
from src.arachnid import Arachnid
from src.radial import Radial
from src.aeronautical import Aeronautical

valid_types = ['U', 'B', 'Q', 'AR', 'RD', 'AN']
chores = ['do the dishes', 'sweep the house', 'do the laundry', 'take out the recycling', 'make a sammich',
          'mow the lawn', 'rake the leaves', 'give the dog a bath', 'bake some cookies', 'wash the car']

chore_times = {'do the dishes': 1000, 'sweep the house': 3000,
               'do the laundry': 10000, 'take out the recycling': 4000,
               'make a sammich': 7000, 'mow the lawn': 20000,
               'rake the leaves': 18000, 'give the dog a bath': 14500,
               'bake some cookies': 8000, 'wash the car': 20000}
millisecond_divisor = 1000
num_chores = 5


def validate_robot_type(entered_type):
    """ Validates if the entered type is a valid robot type. """
    is_valid = False
    print('Trying to make robot of type: %s' % entered_type)
    if entered_type in valid_types:
        is_valid = True
    return is_valid


def create_robot_of_type(robot_type, name):
    """ Creates a robot of a given type and assigns the robot a name provided by the user.
        Also sets the chore list for the robot which is created. """
    new_robot = None
    if robot_type == 'U':
        new_robot = Unipedal(name)
    if robot_type == 'B':
        new_robot = Bipedal(name)
    if robot_type == 'Q':
        new_robot = Quadrupedal(name)
    if robot_type == 'AR':
        new_robot = Arachnid(name)
    if robot_type == 'RD':
        new_robot = Radial(name)
    if robot_type == 'AN':
        new_robot = Aeronautical(name)
    new_robot.set_chore_list(generate_random_chore_list())
    return new_robot


def generate_random_chore_list():
    """ Generates a random set of 5 chores for the robot to complete """
    ch_list = random.sample(chores, k=num_chores)
    return ch_list


def get_time_for_chore(chore_name):
    """ Returns the time in seconds for the robot to complete the selected chore. """
    return chore_times[chore_name] / millisecond_divisor
