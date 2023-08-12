class BrayPotato():
    def __init__(self):
        self. cookTime = 0
        self.state = '生的'
        self.condiments = []
    def addCondiment(self,condiment):
        self.condiments.append(condiment)
    def cook(self,time):
        self.cookTime += time
        if 0<=self.cookTime<3:
            self.state = '生的'
        elif 3<=self.cookTime<5:
            self.state = '半生不熟'
        elif 5<=self.cookTime <8:
            self.state = '熟了'
        elif self.cookTime>=8:
            self.state = '糊了'
    def __str__(self):
        return (f'cookTime:{self.cookTime},state:{self.state},condiments:{self.condiments}')
brayPotato = BrayPotato()
brayPotato.addCondiment('胡椒粉')
brayPotato.cook(4)
print(brayPotato)
brayPotato.addCondiment('辣椒酱')
brayPotato.cook(3)
print(brayPotato)        
