class Vehicle:
    def __init__(self,maxspeed,mileage):
        self.maxspeed = maxspeed
        self.mileage = mileage
modelx = Vehicle(240,18)
print('the maximum speed:', modelx.maxspeed)
print('the mileage:', modelx.mileage)