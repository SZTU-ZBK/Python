#类的私有属性和方法，在属性名和方法名前加两个下滑线__,即为私有属性或者方法
class Master(object):
    def __init__(self):
        self.kongfu = '古法煎饼果子'
        self.__money = 10000          #子类无法继承，但在python中一般会定义get_***（）来获取类的私有属性，set_***()来修改类的私有属性
    def __make_cake(self):            #子类无法继承
        print(f'运用{self.kongfu}制作煎饼果子')
    def get_money(self):
        return self.__money
class Prentice(Master):              
    
    pass
test = Prentice()
print(test.get_money())
test.make_cake()
