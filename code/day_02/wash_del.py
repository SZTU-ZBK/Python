class Wash():
    def __init__(self):
        self.height = 500
        self.width = 400
    def __str__(self):
        return 'This is wash class'
    def __del__(self):       #当*.py执行完毕之后，对象会被删除，删除时将会执行__del__函数
        print('对象已删除')

haier = Wash()