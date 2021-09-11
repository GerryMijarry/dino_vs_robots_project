from robot import Robot

class Fleet:
    def __init__(self):
        self.robots = []
        self.create_fleet()

    def create_fleet(self):
        robo1 = Robot('T1000', 500)
        robo2 = Robot('R2D2', 50)
        robo3 = Robot('Johnny 5', 200)
        robo4 = Robot('Wall-E', 12)

        self.robots.extend([robo1, robo2, robo3, robo4])
