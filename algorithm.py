from output import course1, course2, course3, course4, course5


# 此函数用于实现二十次的具体点名过程并输出点名方案
def stuCheckOut(blacklist):
    for i in [course1, course2, course3, course4, course5]:
        print('第', i.id, '门课程的学期点名方案如下:')
        blacklist.stuDict.clear()
        for idx in range(0, 1):
            allCheck(i, blacklist, idx)
        for jdx in range(1, 20):
            normalCheck(i, blacklist, jdx)


class Black_List:
    def __init__(self):
        # 用字典实现黑名单
        self.stuDict = {}
        # 有效点名次数
        self.effectiveNum = 0
        # 总点名次数
        self.totalNum = 0

    # 通过学生id将学生加入黑名单
    def addDict(self, key):
        # 学生加入黑名单的初始value为2
        self.stuDict[key] = 2

    # 更新黑名单，将value=0的学生从黑名单剔除
    def updateDict(self):
        for key in list(self.stuDict.keys()):
            if self.stuDict[key] == 0:
                self.stuDict.pop(key)
        # print(self.stuDict)

    # 此函数用于实现二十次的具体点名过程并输出点名方案
    def stuCheckIn(self):
        stuCheckOut(self)

    # 该函数用于计算并输出e值
    def computeEvalue(self):
        e = round(self.effectiveNum / self.totalNum, 6)
        print("本学期五次课程的总e值为:", e)


# 本函数用于实现在一次课程的一次点名中抽点全部绩点<=2.5的学生
def allCheck(courseN, blacklist, idx):
    print('第', idx + 1, '次:', courseN.lowStu)
    blacklist.totalNum += 18
    for id1 in courseN.abStuIds[idx]:
        if courseN.scoreList[id1 - courseN.id * 10000 - 1] <= 2.5:
            blacklist.effectiveNum += 1
            blacklist.addDict(id1)
    blacklist.updateDict()


# 本函数用于实现在一次课程的一次点名中只点id存在于黑名单上的学生
def normalCheck(courseN, blacklist, jdx):
    print('第', jdx + 1, '次:', list(blacklist.stuDict.keys()))
    blacklist.totalNum += len(blacklist.stuDict)
    for id1 in blacklist.stuDict.keys():
        if id1 in courseN.abStuIds[jdx]:
            blacklist.stuDict[id1] += 1
            blacklist.effectiveNum += 1
        else:
            blacklist.stuDict[id1] -= 1
    blacklist.updateDict()
