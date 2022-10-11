import random


class Course:
    def __init__(self, id):
        self.id = id
        self.scoreList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0, 0, 0]
        self.AbStu_ids = []
        self.lowStu = []

    def list_append(self, x):
        self.AbStu_ids.append(x)

    def list_add(self, idx, add_ids):
        temp = self.AbStu_ids[idx] + add_ids
        self.AbStu_ids[idx] = temp

    def __str__(self):
        return str(self.AbStu_ids)


# 生成单次课程因故缺席名单
def create_AbsentStu_check(AbsentStu_ids, total_students, BadStu_ids):
    AbsentStu_nums = [0, 1, 2, 3]
    AbsentStu_num = random.choice(AbsentStu_nums)  # 生成每次因故缺席人数

    temp = total_students

    for i in temp[::-1]:
        for j in BadStu_ids:
            if i == j:
                temp.remove(i)

    temp = random.sample(temp, AbsentStu_num)

    AbsentStu_ids = temp

    return


# 某次课某个经常缺勤者的到勤情况
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


def create_BadStu_check(BadStu_ids, item):
    for j in range(0, 20):
        temp = list()
        for i in BadStu_ids:
            if rate_random() == 0:
                temp.append(i)
        item.list_append(temp)


def create_term():
    count_course = 0

    for item in [course1, course2, course3, course4, course5]:
        BadStu_nums = [5, 6, 7, 8]
        BadStu_num = random.choice(BadStu_nums)  # 生成学期经常缺课人数

        totalStudents = list(range(10001 + count_course * 10000, 10091 + count_course * 10000))  # 生成单课程学生ID列表

        item.lowStu = random.sample(totalStudents, 18)  # 生成绩点低的学生名单
        lowRange = [1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5]
        norRange = [2.6, 2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9]

        for id in item.lowStu:
            item.scoreList[id - count_course * 10000 - 10001] = random.choice(lowRange)

        for id in totalStudents:
            if id in item.lowStu:
                pass
            else:
                item.scoreList[id - count_course * 10000 - 10001] = random.choice(norRange)

        BadStu_ids = random.sample(item.lowStu, BadStu_num)  # 生成本学期经常缺勤名单

        #print(BadStu_ids)

        create_BadStu_check(BadStu_ids, item)

        AbsentStu_ids = list()

        for idx in range(0, 20):
            create_AbsentStu_check(AbsentStu_ids, totalStudents, BadStu_ids)
            item.list_add(idx, AbsentStu_ids)

        count_course += 1

    return


course1 = Course(1)
course2 = Course(2)
course3 = Course(3)
course4 = Course(4)
course5 = Course(5)

create_term()

