from algorithm import Black_List
from output import output


class interface(Black_List):  # 假设这就是一个接口，接口名可以随意定义，所有的子类不需要实现在这个类中的函数
    def __init__(self):
        Black_List.__init__(self)

    def Check(self):
        Black_List.stuCheckIn(self)
        Black_List.computeEvalue(self)

    def Output(self):
        pass


class Realaize_interface1(interface):
    def __init__(self):
        interface.__init__(self)

    # 实现接口中的Check函数
    def Check(self):
        interface.stuCheckIn(self)
        interface.computeEvalue(self)


class Realaize_interface2(interface):
    def __init__(self):
        interface.__init__(self)

    def Output(self):
        output()


# 实现五门课程点名方案的生成
obj1 = Realaize_interface1()
obj1.Check()

# 将所有学生本学期出勤信息导出为csv文件
obj2 = Realaize_interface2()
obj2.Output()
