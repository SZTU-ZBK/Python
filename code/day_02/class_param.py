#类属性与示例属性
#类属性为所有示例对象所共有，它可以通过类和对象进行访问
class Dog(object):
    tooth = 100
test = Dog()
#类属性是所有的对象只用同一个属性，只占用一份内存，能够节省空间
print(test.tooth)
print(Dog.tooth)
#！！！注意：类属性不能用实例属性修改，只能用类属性修改，用实例属性的话，会直接在内存里创建一个同名实例属性进行赋值