import random

class Animal:
    def __init__(self, name, race_distance):
        '''
        This method initialize the attributes of the class animal
        Args:
        name (string): name of the animal
        race_distance (int): race length in km
        Note: You will also have to initialize the position of the 
        animal in the race at 0. position is also a class attribute
        '''
        # TODO: Initialize the different attributes
        ...

    def move(self):
        pass #Leave it as it is, just a placeholder

    def report_position(self):
        '''
        This method print the position of the animal in the race
        Note: print something like "the $animal_name$ is at position $animal_position"
        '''
        # TODO: Implement this method
        ...

    def has_finished(self):
        # TODO: Implement this method
        '''
        This method check if the animal finished the race
        Note: Bassically you want to see if the position of the 
        animal is further than the race_distance
        Returns:
        bool: finished race or not
        '''

class Hare(Animal):
    def __init__(self, race_distance):
        super().__init__("Hare", race_distance)

    def move(self):
        '''
        This function implement the move behavior of the hare
        Everyday the hare might just rest (50%) or run (50%)
        If he is running he can move its position from 0 to 5km
        Note: You would like to increase the position of the hare
        '''
        # TODO: Implement this method
        ...

class Tortoise(Animal):
    def __init__(self, race_distance):
        super().__init__("Tortoise", race_distance)

    def move(self):
        '''
        This function implement the move behavior of the tortoise
        Everyday the tortoise can move 0-5 km
        Note: You would like to increase the position of the tortoise
        '''
        # TODO: Implement this method
        ...

#Running the race
race_distance = 50
hare = Hare(race_distance)
tortoise = Tortoise(race_distance)

while not hare.has_finished() and not tortoise.has_finished():
    hare.move()
    tortoise.move()
    hare.report_position()
    tortoise.report_position()

if hare.has_finished() and tortoise.has_finished():
    print("It's a tie!")
elif hare.has_finished():
    print("The hare wins!")
else:
    print("The tortoise wins!")


