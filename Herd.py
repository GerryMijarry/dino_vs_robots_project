from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()

    def create_herd(self):
        dino1 = Dinosaur('T-Rex', 300)
        dino2 = Dinosaur('Stegasaurus', 200)
        dino3 = Dinosaur('Velociraptor', 100)

        self.dinosaurs.extend([dino1, dino2, dino3])
