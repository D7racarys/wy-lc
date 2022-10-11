import random


class Course:
    def __init__(self, id):
        # 课程id
        self.id = id
        # 该课程所有学生绩点
        self.scoreList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0, 0, 0]
        # 该课程在本学期所有实际缺勤学生名单
        self.abStuIds = []
        # 该课程绩点<=2.5的学生名单
        self.lowStu = []

    # 将某次课程实际学生缺勤名单加入AbStu_ids
    def list_append(self, x):
        self.abStuIds.append(x)

    # 将某次课单个缺勤学生id添加到本次课程缺勤名单
    def list_add(self, idx, add_ids):
        temp = self.abStuIds[idx] + add_ids
        self.abStuIds[idx] = temp

    def __str__(self):
        return str(self.abStuIds)


# 生成单次课程因故缺席名单
def create_AbsentStu_check(absentStuIds, totalStudents, badStuIds):
    absentStuNums = [0, 1, 2, 3]
    absentStuNum = random.choice(absentStuNums)  # 生成每次因故缺席人数

    temp = totalStudents

    for i in temp[::-1]:
        for j in badStuIds:
            if i == j:
                temp.remove(i)

    temp = random.sample(temp, absentStuNum)

    absentStuIds = temp

    return


# 生成某次课某个经常缺勤者的到勤情况
def rate_random():
    x = [1, 0]
    p = [0.2, 0.8]
    start = 0
    random_num = random.random()
    for id1, score in enumerate(p):
        start += score
        if random_num <= start:
            break
    return x[id1]


#
def create_BadStu_check(badStuIds, item):
    for j in range(0, 20):
        temp = list()
        for i in badStuIds:
            if rate_random() == 0:
                temp.append(i)
        item.list_append(temp)


# 用于生成本学期所有课程学生到勤情况
def create_term():
    count_course = 0

    for item in [course1, course2, course3, course4, course5]:
        badStuNums = [5, 6, 7, 8]
        badStuNum = random.choice(badStuNums)  # 生成学期经常缺课人数

        # 用于生成总学生名单
        totalStudents = list(range(10001 + count_course * 10000, 10091 + count_course * 10000))  # 生成单课程学生ID列表

        item.lowStu = random.sample(totalStudents, 18)  # 生成绩点低的学生名单
        lowRange = [1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5]
        norRange = [2.6, 2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9]

        # 随机生成低绩点学生的绩点
        for id in item.lowStu:
            item.scoreList[id - count_course * 10000 - 10001] = random.choice(lowRange)

        # 随机生成其他学生的绩点
        for id in totalStudents:
            if id in item.lowStu:
                pass
            else:
                item.scoreList[id - count_course * 10000 - 10001] = random.choice(norRange)

        badStuIds = random.sample(item.lowStu, badStuNum)  # 生成本学期经常缺勤名单

        # print(BadStu_ids)

        create_BadStu_check(badStuIds, item)

        # 初始生成本次课程缺勤名单
        absentStuIds = list()

        for idx in range(0, 20):
            create_AbsentStu_check(absentStuIds, totalStudents, badStuIds)
            item.list_add(idx, absentStuIds)

        count_course += 1

    return


# 实例化课程类
course1 = Course(1)
course2 = Course(2)
course3 = Course(3)
course4 = Course(4)
course5 = Course(5)

# 执行生成全部到勤信息
create_term()
