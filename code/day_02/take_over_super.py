class School(object):
    def __init__(self):
        self.kongfu = '黑马煎饼方法'
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')
class Master(School):
    def __init__(self):
        self.kongfu = '古法煎饼果子'
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')
        super(Master,self).__init__()        #调用Prentice的父类的初始化
        super(Master,self).make_cake()       #调用prentice的父类的make_cake方法
class Prentice(Master):               #当两个父类由同名的属性和方法时，子类优先继承第一个父类的同名属性和方法
    def __init__(self):
        self.kongfu = '独创煎饼方法'          #子类可以通过对父类同名属性或同名方法进行重新定义，来实现类的重写
    def make_cake(self):
        self.__init__()                          
        print(f'运用{self.kongfu}制作煎饼果子')#防止子类的属性被父类覆盖
    def Master_make_cake(self):
        Master.__init__(self)                #这里想要调用父类的同名属性和方法，所以这里需要再次调用父类的初始化。
        Master.make_cake(self)
    def two2make_old(self):
        # Master.__init__(self)                #一次性调用两个父类的方法，但是代码量有些大，而且需要频繁更改
        # Master.make_cake(self)      
        # School.__init__(self)                
        # School.make_cake(self)
        super(Prentice,self).__init__()        #调用Prentice的父类的初始化,super调用上一级的父类属性或方法
        super(Prentice,self).make_cake()       #调用prentice的父类的make_cake方法
test = Prentice()
test.two2make_old()