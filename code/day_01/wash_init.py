#__init__魔法方法初始化
class Washer():
    def __init__(self,height,width):
        self.height = height
        self.width = width
    def Print_Info(self):
        print(f'洗衣机的高度{self.height}')
        print(f'洗衣机的宽度{self.width}')

haier = Washer(500,400)
haier.Print_Info()
media = Washer(600,500)
media.Print_Info()