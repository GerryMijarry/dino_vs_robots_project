from fleet import Fleet
from herd import Herd
import random

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        self.display_welcome()
        self.battle()
        self.display_winners()

    def display_welcome(self):
        print("Welcome to Dino Vs. Robots!!")
        
    def battle(self):
        while len(self.herd.dinosaurs) > 0 and len(self.fleet.robots) > 0:
            dice = random.randint(1, 10)
            if dice > 5:
                self.dino_turn()
                if len(self.fleet.robots) > 0:
                    self.robo_turn()
            else:
                self.robo_turn()
                if len(self.herd.dinosaurs) > 0:
                    self.dino_turn()
        
    def dino_turn(self):
        self.show_dino_opponent_options()
        dino_attacker = int(input('Which dino will be the attacker?'))
        self.show_robot_opponent_options()
        robot_target = int(input('Which robot will be the target?'))
        self.herd.dinosaurs[dino_attacker].attack(
            self.fleet.robots[robot_target])
        if self.fleet.robots[robot_target].health <= 0:
            print(str(self.fleet.robots[robot_target].name) + ' has beeped his last beep!')
            self.fleet.robots.remove(self.fleet.robots[robot_target])

    def robo_turn(self):
        self.show_robot_opponent_options()
        robot_attacker = int(input('Which robot will be the attacker?'))
        self.show_dino_opponent_options()
        dino_target = int(input('Which dino will be the target?'))
        self.fleet.robots[robot_attacker].attack(
            self.herd.dinosaurs[dino_target])
        if self.herd.dinosaurs[dino_target].health <= 0:
            print(str(self.herd.dinosaurs[dino_target].name) + ' has rawr\'d his last rawr!')
            self.herd.dinosaurs.remove(self.herd.dinosaurs[dino_target])

    def show_dino_opponent_options(self):
        print("Select your dino!")
        counter = 0
        for dino in self.herd.dinosaurs:
            print('Press ' + str(counter) + ' to select ' + dino.name)
            counter +=1

    def show_robot_opponent_options(self):
        print("Select your robot!")
        counter = 0
        for robot in self.fleet.robots:
            print('Press ' + str(counter) + ' to select ' + robot.name)
            counter +=1

    def display_winners(self):
        if len(self.fleet.robots) > len(self.herd.dinosaurs):
            print('Robots are here to stay! Asta la vista, Dinosaurs!')
        else:
            print('Dinosaurs win! Dinosaurs, Uh ..find a way!')
