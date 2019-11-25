import src.bom_helper as bh
import src.leaderboard as ldr
import threading

welcome_msg = 'Hello and welcome to the Bot-o-Mat interactive system!'

info_msg = """This system was built with you in mind! No one likes to do chores and so for that reason
we created Bot-o-Mat. Simply tell us the name and type of robot you would like to make and
the Bot-o-Mat system will create your robot and assign it to some of the chores that normally
you would have to complete."""

instructions = """Here is how you can interact with the Bot-o-Mat system.\n
To create a robot enter "r". You will then be asked a few questions including the following:\n
How many robots would you like to create?\nWhat type of robot do you want to create?
What name do you want to give to your robot?\n\nThe system will then display the chores each
of your robots are completing and how long it takes for the robots to complete each of those chores.\n
After at least one robot has been created you can view a leaderboard of the robots that have spent the most time
working by entering "l". However the leaderboard cannot be viewed until at least one robot has been created.
To exit the Bot-o-Mat system enter "x".\n"""

robot_types = """Enter "U" for Unipedal\nEnter "B" for Bipedal\nEnter "Q" for Quadrupedal
Enter "AR" for Arachnid\nEnter "RD" for Radial\nEnter "AN" for Aeronautical\n"""

robot_list = []


def main():
    """ Main function which allows users to interact with the bot-o-mat system """
    welcome_user()
    print('Bot-o-Mat system is now ready.')
    print('To create a robot enter "r". To quit enter "x". To view the leaderboard press "l".')
    response = ''
    while (response != 'r') and (response != 'x') and (response != 'l'):
        """ Reset robots_created to false at the beginning of this loop each time. """
        robots_created = False
        response = input('Please enter either "r" or "x" or "l": ')
        if response == 'r':
            create_robot()
            robots_created = True
        if response == 'x':
            print('Thank you for using the Bot-o-Mat system! Goodbye.')
            exit(0)
        if (response != 'r') and (response != 'x') and (response != 'l'):
            print('\nUnrecognized response, please enter either "r" or "x".')
        if response == 'l':
            if len(robot_list) > 0:
                ldr.show_leaderboard(robot_list)
            else:
                print('Cannot display leaderboard until after robots have been created.')
                print('First create some robots to then view the leaderboard.\n')
            """ Reset response to empty string for loop to continue """
            response = ''
        if robots_created:
            """ Reset response to empty string for loop to continue """
            response = ''
            print('Robots finished completing their assigned chores.')
            print('What would you like to do now?')
            print('To create a robot enter "r". To quit enter "x". To view the leaderboard press "l".')


def welcome_user():
    """ Prints welcome messages as well as instructions for the user. """
    print(welcome_msg)
    print()
    print(info_msg)
    print()
    print(instructions)


def create_robot():
    """ This function allows a user to create multiple robots at a time.
        After creating robots they are all put to work """
    print('How many robots would you like to create?')
    good_input = False
    num_robots = 0
    while not good_input:
        robots = input('Enter a number between 1 and 10: ')
        try:
            num_robots = int(robots)
            if (num_robots > 0) and (num_robots < 11):
                good_input = True
            else:
                print('Sorry unable to make %s robots\n' % str(num_robots))
        except ValueError:
            print('Invalid input: %s\n' % robots)

    print('Ok we will create %s robots' % str(num_robots))
    count = 0
    """ Make as many robots as the user requested. """
    while count < num_robots:
        print('Making robot %s' % str(count + 1))
        print('What type of robot would you like to create?')
        print(robot_types)
        valid_robot_type = False
        selected_type = ''
        while not valid_robot_type:
            selected_type = input('Select robot type: ')
            valid_robot_type = bh.validate_robot_type(selected_type)
            if not valid_robot_type:
                print('Robot type: %s is not valid. Please enter a valid type.' % selected_type)
        """ A valid robot type has been entered. The selected_type will be something valid by this point. """
        robot_name = input('Enter a name for the robot: ')
        print()
        created_robot = bh.create_robot_of_type(selected_type, robot_name)
        robot_list.append(created_robot)
        count += 1
    put_robots_to_work(robot_list, num_robots)


def put_robots_to_work(robots, num_robots):
    """ This function starts a new thread for each robot and calls the complete_chores function
        of each robot. """
    print('%s New Robots were created' % num_robots)
    print('Putting the robots to work. This may take some time depending on how many robots have been created.\n')
    robot_threads = []
    for robot in robots:
        try:
            r_thread = threading.Thread(target=robot.complete_chores)
            robot_threads.append(r_thread)
            r_thread.start()
        except:
            print('Error starting thread.')

    for thread in robot_threads:
        thread.join()


if __name__ == "__main__":
    main()
