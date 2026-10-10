class Robot:
    def __init__(self, name, battery, speed):
        self.name = name
        self.battery = battery
        self.speed = speed

    def show_info(self):
        print(f'Robot Name: {self.name}')
        print(f'Robot Battery: {self.battery}')
        print(f'Robot Speed: {self.speed}')

    def move(self):
        print(f'{self.name} is moving .... ')

    def charge(self):
        print(f'Battery charged to {self.battery}')


ilham_robot = Robot('Sufi', 80, 5)
ilham_robot.show_info()
ilham_robot.move()
ilham_robot.charge()