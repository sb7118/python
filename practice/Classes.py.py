class car:
    def __init__(self , name , topSpeed):
        self.name = name
        self.topSpeed = topSpeed


    def cars(self):
        print(f'the name of car is {self.name} and its top speed is {self.topSpeed}')
'''first make an object , then class name = values to the constructor'''
car1 = car("lamborgini" , 200)
car2 = car("bugatti" , 250)
'''the first one to call will execute first'''
car1.cars()
car2.cars()