from fleet import Fleet
from herd import Herd

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
        pass
        
    def dino_turn(self):
        pass

    def robo_turn(self):
        pass

    def show_dino_opponent_options(self):
        pass

    def show_robot_opponent_options(self):
        pass

    def display_winners(self):
        if len(self.fleet.robots) > len(self.herd.dinosaurs):
            print('Robots are here to stay! Asta la vista, Dinosaurs')
        else:
            print('Dinosaurs win! Dinosaurs, Uh ..find a way!')
