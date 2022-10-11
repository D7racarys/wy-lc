from output import course1, course2, course3, course4, course5


def stuCheckOut(blacklist):
    for i in [course1, course2, course3, course4, course5]:
        print('第',i.id,'门课程的学期点名方案如下:')
        blacklist.stuDict.clear()
        for idx in range(0, 1):
            allCheck(i, blacklist, idx)
        for jdx in range(1, 20):
            normalCheck(i, blacklist, jdx)


class Black_List:
    def __init__(self):
        self.stuDict = {}
        # 有效点名次数
        self.effectiveNum = 0
        # 总点名次数
        self.totalNum = 0

    def addDict(self, key):
        self.stuDict[key] = 2

    def updateDict(self):
        for key in list(self.stuDict.keys()):
            if self.stuDict[key] == 0:
                self.stuDict.pop(key)
        # print(self.stuDict)

    def stuCheckIn(self):
        stuCheckOut(self)

    def computeEvalue(self):
        e = round(self.effectiveNum / self.totalNum, 6)
        print("本学期五次课程的总e值为:", e)


# 列表搜寻函数
def allCheck(courseN, blacklist, idx):
    print('第', idx+1, '次:', courseN.lowStu)
    blacklist.totalNum += 18
    for id1 in courseN.AbStu_ids[idx]:
        if courseN.scoreList[id1 - courseN.id * 10000 - 1] <= 2.5:
            blacklist.effectiveNum += 1
            blacklist.addDict(id1)
    blacklist.updateDict()


def normalCheck(courseN, blacklist, jdx):
    print('第', jdx+1, '次:', list(blacklist.stuDict.keys()))
    blacklist.totalNum += len(blacklist.stuDict)
    for id1 in blacklist.stuDict.keys():
        if id1 in courseN.AbStu_ids[jdx]:
            blacklist.stuDict[id1] += 1
            blacklist.effectiveNum += 1
        else:
            blacklist.stuDict[id1] -= 1
    blacklist.updateDict()
