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
    def __init__(self):
        self.kongfu = '独创煎饼方法'          #子类可以通过对父类同名属性或同名方法进行重新定义，来实现类的重写
    def make_cake(self):
        self.__init__()                          
        print(f'运用{self.kongfu}制作煎饼果子')#防止子类的属性被父类覆盖
    def Master_make_cake(self):
        Master.__init__(self)                #这里想要调用父类的同名属性和方法，所以这里需要再次调用父类的初始化。
        Master.make_cake(self)
class TuSun(Prentice):
    pass
    
test = TuSun()
test.make_cake()