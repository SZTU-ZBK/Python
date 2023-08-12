#魔法方法__str__:print该类时将会返回__str__返回的字符，一般return的时对该类的解释说明
class Wash():
    def __init__(self,height,width):
        self.height = height
        self.width = width
    def __str__(self):
        return '这是一个洗衣机类！！！'
    def Print_Info(self):
        print(f'洗衣机高度为：{self.height},洗衣机宽度为：{self.width}')
        
haier = Wash(500,400)
haier.Print_Info()
print(haier)  