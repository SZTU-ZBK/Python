class Dog(object):
    @staticmethod        #静态方法装饰器
    def PrintInfo():
        print("这是一个狗类！！！")
Dog.PrintInfo()
#当不需要使用类或对象内的变量时，为了减小内存占用，可以直解使用静态方法