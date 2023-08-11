#类要遵循大驼峰命名
class Washer():
    def Washing(self):
        print("Washing now")
        print(self)
#self是调用函数的对象,也就是wash这个对象的内存地址
wash_1 = Washer()  #实例化wash_1对象
print("wash_1",wash_1)
wash_1.Washing() #实例方法
wash_2 = Washer()  #实例化wash_2对象
print("wash_2",wash_2)
wash_2.Washing() #实例方法      
#一个类可以创建多个对象，但是内存地址不一样