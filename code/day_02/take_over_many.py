class Master(object):
    def __init__(self):
        self.kongfu = '古法煎饼果子'
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')
class School(object):
    def __init__(self):
        self.kongfu = '黑马煎饼方法'
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')
class Prentice(Master,School):               #当两个父类由同名的属性和方法时，子类优先继承第一个父类的同名属性和方法
    pass
test = Prentice()
test.make_cake()