class Man:
    id = 3 # 类变量
    def __init__(self, name):
        self.name = name
        self.id_number()
 
    # @classmethod
    def id_number(cls):
        cls.id += 1
        return cls.id
 
a = Man('A')
print(a.id)
b = Man('B')
print(b.id)
print(Man.id)
#类变量是具有记忆性的，如果采用实例方法来改变类变量，实际上会直接创建对象实例对象的同名实例变量