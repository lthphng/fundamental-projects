from abc import ABC, abstractmethod
from enum import Enum
import random

"""
Each creature possesses one weapon.
The weapons have a value with the higher number more powerful than 
lower numbers.
When a creature A encounters creature B, their
weapons are compared. For each difference in weapons, the 
creature with the lesser weapon looses 10 life points.
For example, if creature A has magic as a weapon, and creature B
has arrow as a weapon, creature B will loose 10 life points.
If two creatures have the same weapon, no life points are lost,
but each creature will loose some of their special power.
The way each creature processes an encounter is determined by their 
update_life_level method.
"""

class Weapon (Enum):
    magic = 30
    arrow = 20
    club = 10

class Creature(ABC):
    """
    The abstract superclass that all creatures inherit from.
    """
    def __init__(self, id, name, weapon, life_points=50):
        self.id = id
        self.name = name
        self.weapon=weapon
        self.life_points = life_points

    @abstractmethod 
    def update_life_level(self, point_diff):
        self.life_points += point_diff

    @abstractmethod 
    def is_alive(self)-> bool:
        return self.life_points > 0

    @abstractmethod 
    def __str__(self):
        info_str = f'{"id:"} {self.id} {"name:"} {self.name} {"life level:"} {self.life_points} {"weapon:"} {self.weapon} {"is alive"} {self.is_alive()} '
        return(info_str)

class Conjurer(Creature):
    def __init__(self, id, name, weapon=Weapon.magic, life_points=50, num_spells=5):
        super().__init__(id, name, weapon, life_points)
        self.num_spells=num_spells

    def update_life_level(self, point_diff):
        """
        If the point_diff is positive, the Congerer increases its life points by the
        point_diff, and increases its spell count by 1.
        If the point_diff is zero, one spell is lost, no change to life points.
        If the point diff is negative, it means the other weapon was more powerful.
        A Congerer can cast a spell (one spell is subtracted) and not loose any life points; however,
        if it has no more spells left, the full points are deducted from its life points.
        """
        if point_diff>0:
            self.life_points+=point_diff
            self.num_spells+=1
        elif point_diff==0:
            self.num_spells-=1
        else:
            if self.num_spells>0:
                self.num_spells-=1
            else:
                self.life_points+=point_diff

    def is_alive(self)-> bool:
        return self.life_points>0

    def __str__(self):
        info_str=f' {"Conjurer: id:"} {self.id} {"name:"} {self.name} ' \
            f' {"life level:"} {self.life_points} '\
            f' {"weapon:"} {self.weapon} {"is alive"} {self.is_alive()}'\
            f' {"spells:"} {self.num_spells}'
        return info_str

class Elf(Creature):
    def __init__(self, id, name, weapon=Weapon.arrow, life_points=50, mind_control=1.5):
        super().__init__(id, name, weapon, life_points)
        self.mind_control=mind_control
 
    def update_life_level(self, point_diff):
        """
        If the point_diff is positive, the Elf increases its life points by the
        point_diff, and increases its mind control by 25%.
        If the point diff is zero, the Elf looses 25% if its mind control.
        If the point diff is negative, it means the other weapon was more powerful.
        An Elf can apply some mind control to lower the life points lost by 5 points
        for 25% if its mind control. If it has no more mind control left, the full points are
        deducted from its life points.
        """
        if point_diff>0:
            self.life_points+=point_diff
            self.mind_control*=1.25
        elif point_diff==0:
            self.mind_control*=0.75
        else:
            if self.mind_control>0:
                self.mind_control*=0.75
                self.life_points+=(point_diff+5)
            else:
                self.life_points+=point_diff

    def is_alive(self)-> bool:
        return self.life_points>0

    def __str__(self):
        info_str=f' {"Elf: id:"} {self.id} {"name:"} {self.name} ' \
            f' {"life level:"} {self.life_points} '\
            f' {"weapon:"} {self.weapon} {"is alive"} {self.is_alive()}'\
            f' {"mind control:"} {self.mind_control}'
        return info_str

class Golem(Creature):
    def __init__(self, id, name, weapon=Weapon.club, life_points=50, endurance=20):
        super().__init__(id, name, weapon, life_points)
        self.endurance = endurance

    def update_life_level(self, point_diff):
        """
        If the point_diff is positive, the Golem increases its life points by the 
        point_diff, and increases its endurance by 25%.
        If the point diff is zero, it looses 50% of its endurance.
        If the point diff is negative, it means the other weapon was more powerful.
        A Golem can aply some endurance (if its endurance > 0) to lower the life points lost by 5 points
        for 50% of its current endurance. It it has no more endurance, the full point_diff is 
        deducted from its life points.
        """
        if point_diff>0:
            self.life_points+=point_diff
            self.endurance*=1.25
        elif point_diff==0:
            self.endurance*=0.5
        else:
            if self.endurance>0:
                self.endurance*=0.5
                self.life_points+=(point_diff+5)
            else:
                self.life_points+=point_diff

    def is_alive(self)-> bool:
        return self.life_points > 0

    def __str__(self):
        info_str = f' {"Golem: id:"} {self.id} {"name:"} {self.name} ' \
           f' {"life level:"} {self.life_points} ' \
           f' {"weapon:"} {self.weapon} {"is alive"} {self.is_alive()}' \
           f' {"endurance:"} {self.endurance}'
        return info_str

# TODO: implement this function:
def do_engagement(creatureA, creatureB):
    """
    Rules of engagement:
    If either creature is dead, nothing happens.
    If both are alive, call the is_5percent_or_less function. 
    If true, creatureA dies and no further action occurs.
    Otherwise: calculate the weapon difference, and
    pass that to creatureA's update_life_level method.
    Pass in the negative (multiply by -1) difference to
    creatureB's update_life_level method.
    """
    if creatureA.is_alive() and creatureB.is_alive():
        if is_5percent_or_less():
            creatureA.life_points = 0
        else:
            diff = (creatureA.weapon.value - creatureB.weapon.value)
            creatureA.update_life_level(diff)
            creatureB.update_life_level(-1*diff)

# allow for a seed value to be set in the random number generator.
def set_seed(seed_val):
    random.seed(seed_val)

def is_5percent_or_less()-> bool:
    """
    Returns True if a random number is generated with a 5%
    probability, False otherwise.
    """
    num = random.random()
    return (num <= 0.05)

# uses the random number generator to create ID numbers.
def generate_id()-> str:
    lower = 111
    upper = 999
    return str(random.randint(lower, upper))

# print all creatures on the list.
def print_all(list):
    for i in range(0, len(list)):
        print(list[i])

if __name__=="__main__":
    # some code to help test and debug your code:
    set_seed(123456)
    creatures = []
    # make some creatures for testing:
    elf1 = Elf(generate_id(), "Eowyn", Weapon.arrow)
    conj1 = Conjurer(generate_id(), "Gandalf", Weapon.magic)
    conj2 = Conjurer(generate_id(), "Morgana", Weapon.magic)
    gol1 = Golem(generate_id(), "Turf", Weapon.club)
    creatures.append(elf1)
    creatures.append(conj1)
    creatures.append(conj2)
    creatures.append(gol1)
    print_all(creatures)
    print(" ")
    #test Conjurer update_life_level method with point diff negative.
    conj1.update_life_level(-20)
    res = (conj1.life_points == 50)
    print("life points be 50"+res)
    res=(conj1.num_spells == 4)
    print("num spells be 4"+res)
    # write statements that test the update_life_level method for
    # when the diff is positive, zero, and negative for all three classes.
    print(" ")
    a=do_engagement(conj1, elf1)
      # if is_5percent_or_less returns True, Gandalf points will be 0- and he dies.
      # Otherwise, the weapon diff is 10, so Gandalf gains 10 life points and adds one spell,
      # Eowyn looses 5 life points and mind control is now 1.125.
    print_all(creatures)
    count=0
    for i in range(1, 100):
        if is_5percent_or_less():
            count+=1
    r=(count>=2 and count<=8)
    print(a)
