class A():                   #默认继承object这一基类或者角顶级类，其他子类叫派生类
    def __init__(self):
        self.a = 'a'
    def PrintInfo(self):
        print(self.a)
class B(A):                   #子类默认继承父类的所有属性和方法
    pass
test = B()
test.PrintInfo()
        