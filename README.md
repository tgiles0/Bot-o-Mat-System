# BOT-O-MAT
Use any language to complete this challenge. The implementation is up to you: it can be a command-line application or have a graphical interface.

Your application should collect a name and robot type from the types we list below. For each, it should create a Robot of the type the user chooses, e.g. Larry, Bipedal. 

Given the list of tasks below, your application should then assign the Robot a set of five tasks, all of which complete after a duration that we show in milliseconds. 



- Collect a name and robot type from user.
- Instantiate a Robot of the type provided by the user with the name provided by the user
  - for example: Bipedal, Larry
- Set up methods on Robot to complete tasks from the provided list

## Robot
Robot completes tasks and removes them from the list when they are done (i.e. enough time has passed since starting the task).

## Tasks
Tasks have a description and an estimated time to complete.

```
[
  {
    description: 'do the dishes',
    eta: 1000,
  },{
    description: 'sweep the house',
    eta: 3000,
  },{
    description: 'do the laundry',
    eta: 10000,
  },{
    description: 'take out the recycling',
    eta: 4000,
  },{
    description: 'make a sammich',
    eta: 7000,
  },{
    description: 'mow the lawn',
    eta: 20000,
  },{
    description: 'rake the leaves',
    eta: 18000,
  },{
    description: 'give the dog a bath',
    eta: 14500,
  },{
    description: 'bake some cookies',
    eta: 8000,
  },{
    description: 'wash the car',
    eta: 20000,
  },
]
```

## Types
```
{ 
  UNIPEDAL: 'Unipedal',
  BIPEDAL: 'Bipedal',
  QUADRUPEDAL: 'Quadrupedal',
  ARACHNID: 'Arachnid',
  RADIAL: 'Radial',
  AERONAUTICAL: 'Aeronautical'
}
```

## Features to add once the core functionality is complete
Be creative and have fun! Use this list or create your own features.
- Allow users to create multiple robots at one time
- Create a leaderboard for tasks completed by each Robot
- Create tasks specific for each robot type, this could work in conjunction with the leaderboard. For e.g. robots that are assigned tasks that their type can’t perform won’t get “credit” for finishing the task.
- Add persistance for tasks, bots and leaderboard stats


## Authors
- Scott Hoffman <https://github.com/scottshane>
- Olivia Osby <https://github.com/oosby>


## Implementation and Usage Information
The Bot-o-Mat system has been developed using Python 3.8 and has been verified to run on MacOS. The Bot-o-Mat system should also be able to run on Linux. The only dependency required is that Python 3.8 is installed on the machine which is running the Bot-o-Mat system.

### How can I run the Bot-o-Mat system?
In order to run the Bot-o-Mat system you must first download or clone this GitHub repository. Once you have the project on your machine, from a terminal/console window navigate into the bot-o-mat-tgiles0 directory.

`cd bot-o-mat-tgiles0-master`

Within that directory there is a python file which can be executed using Python 3.

`python3 bot-o-mat.py`

Once you execute this above command the terminal/console will start running the Bot-o-Mat system and further instructions for running this system will be printed to the terminal/console window.

### What can the Bot-o-Mat system do?

There are three commands that are supported by the Bot-o-Mat system.

1. Create one or more robots and put them to work. Command: `r`. After entering `r` when prompted by the Bot-o-Mat system you can create up to 10 robots at once. These robots are then all assigned 5 random chores and will immediately start working on their assigned chores. Note that each robot type has two different chores which they are unable to complete. If a robot is unable to complete a certain chore that chore will remain on the robot's chore list and a message will be printed showing that the robot was unable to complete that assigned task.
2. View the Bot-o-Mat robot leaderboard. Command: `l`. After entering `l` the Bot-o-Mat system will either display a message that no robots have been created and so the leaderboard cannot be displayed or if robots have been created a separate window will open showing the leaderboard for all of the robots that have been created. After the leaderboard window is opened in order to continue interacting with the Bot-o-Mat system, the leaderboard window must be closed.
3. Exit the Bot-o-Mat system. Command: `x`. After entering `x` the Bot-o-Mat system will close. Note data of robots created in a previous run of the Bot-o-Mat system are not currently stored and saved anywhere so closing the Bot-o-Mat system and restarting the Bot-o-Mat system will reset the robots and the chores that they have completed. 
