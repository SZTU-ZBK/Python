class Washer():
    def Washing(self):
        print("Washing now!!!")
    def Print_Info(self):
        print(f'洗衣机高度{self.width}')
        print(f'洗衣机高度{self.height}') #可以在类的内部通过self直接获取在类外部定义的属性值
haier_1 = Washer()
haier_1.width = 500
haier_1.height = 400
#类的属性可以在类内或类外添加
print(f'洗衣机宽度值为{haier_1.width}') 
haier_1.Print_Info()