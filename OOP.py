class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price
    
    def repair(self):
        self.condition = "repaired"

class AnakinsPod(Podracer):
    def boost(self):
        self.max_speed *= 2

class SebulbasPod(Podracer):
    def flame_jet(self, other_podracer):
        other_podracer.condition = "trashed"




# create a new Podracer
podracer1 = Podracer(max_speed=100, condition="perfect", price=1000)

# repair the Podracer
podracer1.repair()

# create a new AnakinsPod
anakin_pod = AnakinsPod(max_speed=150, condition="perfect", price=1500)

# boost the AnakinsPod
anakin_pod.boost()

# create a new SebulbasPod
sebulba_pod = SebulbasPod(max_speed=120, condition="perfect", price=1200)

# use the flame_jet method to trash another Podracer
sebulba_pod.flame_jet(podracer1)

