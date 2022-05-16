from mimetypes import init


class Car(object):
    def __init__(self,model,color,company,speedLimit):
        self.color = color
        self.company = company
        self.speedLimit = speedLimit
        self.model = model

    def start(self):
        print('Started')

    def stop(self):
        print('Stopped')

    def accelerate(self):
        print('Accelerating')
        'Accelerator Functionality Here'

    def change_gear(self,gear_type):
        print('Gear Changed')
        'Gear-Related Functionality Here'

audi = Car('A8','White','Audi', 180)
print(audi.color)
print(audi.speedLimit)
print(audi.accelerate())
print(audi.start())