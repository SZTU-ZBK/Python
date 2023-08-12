class Dog(object):
    __tooth = 10

    @classmethod                #当需要访问类的私有属性时，采用类方法进行访问
    def get_tooth(cls):         #类方法一般与类对象配合使用，可以节省内存
        return cls.__tooth
dog_1 = Dog()
print(dog_1.get_tooth())