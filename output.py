import pymysql
from Data_generator import course1, course2, course3, course4, course5
from sqlalchemy import create_engine
import pandas as pd

# 创建连接
con = pymysql.connect(host="localhost", user="root", password="1234", database="stuDb", port=3306)

# 创建游标对象
cur = con.cursor()

sql2 = """drop table if exists lesson"""

try:
    # 执行创建表的sql
    cur.execute(sql2)
except Exception as e:
    print(e)

# 编写创建表的sql
sql1 = """
	create table lesson(
	id int(5) ,
	score float(2,1) not null,
	class1 boolean not null,
	class2 boolean not null,
	class3 boolean not null,
	class4 boolean not null,
	class5 boolean not null,
	class6 boolean not null,
	class7 boolean not null,
	class8 boolean not null,
	class9 boolean not null,
	class10 boolean not null,
	class11 boolean not null,
	class12 boolean not null,
	class13 boolean not null,
	class14 boolean not null,
	class15 boolean not null,
	class16 boolean not null,
	class17 boolean not null,
	class18 boolean not null,
	class19 boolean not null,
	class20 boolean not null
	)
"""

try:
    # 执行创建表的sql
    cur.execute(sql1)
except Exception as e:
    print(e)



for item in [course1, course2, course3, course4, course5]:
    for id in range(item.id * 10000 + 1, item.id * 10000 + 91):
        stuId = id
        stuScore = item.scoreList[id - item.id * 10000 - 1]
        if id in item.AbStu_ids[0]:
            stuClass1 = False
        else:
            stuClass1 = True
        if id in item.AbStu_ids[1]:
            stuClass2 = False
        else:
            stuClass2 = True
        if id in item.AbStu_ids[2]:
            stuClass3 = False
        else:
            stuClass3 = True
        if id in item.AbStu_ids[3]:
            stuClass4 = False
        else:
            stuClass4 = True
        if id in item.AbStu_ids[4]:
            stuClass5 = False
        else:
            stuClass5 = True
        if id in item.AbStu_ids[5]:
            stuClass6 = False
        else:
            stuClass6 = True
        if id in item.AbStu_ids[6]:
            stuClass7 = False
        else:
            stuClass7 = True
        if id in item.AbStu_ids[7]:
            stuClass8 = False
        else:
            stuClass8 = True
        if id in item.AbStu_ids[8]:
            stuClass9 = False
        else:
            stuClass9 = True
        if id in item.AbStu_ids[9]:
            stuClass10 = False
        else:
            stuClass10 = True
        if id in item.AbStu_ids[10]:
            stuClass11 = False
        else:
            stuClass11 = True
        if id in item.AbStu_ids[11]:
            stuClass12 = False
        else:
            stuClass12 = True
        if id in item.AbStu_ids[12]:
            stuClass13 = False
        else:
            stuClass13 = True
        if id in item.AbStu_ids[13]:
            stuClass14 = False
        else:
            stuClass14 = True
        if id in item.AbStu_ids[14]:
            stuClass15 = False
        else:
            stuClass15 = True
        if id in item.AbStu_ids[15]:
            stuClass16 = False
        else:
            stuClass16 = True
        if id in item.AbStu_ids[16]:
            stuClass17 = False
        else:
            stuClass17 = True
        if id in item.AbStu_ids[17]:
            stuClass18 = False
        else:
            stuClass18 = True
        if id in item.AbStu_ids[18]:
            stuClass19 = False
        else:
            stuClass19 = True
        if id in item.AbStu_ids[19]:
            stuClass20 = False
        else:
            stuClass20 = True
        sql = "INSERT INTO lesson (id,score,class1,class2,class3,class4,class5,class6,class7,class8,class9,class10," \
              "class11,class12,class13,class14,class15,class16,class17,class18,class19,class20) values('%d','%f'," \
              "'%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d'," \
              "'%d');" % (stuId, stuScore, stuClass1, stuClass2, stuClass3, stuClass4, stuClass5, stuClass6, stuClass7,
                          stuClass8, stuClass9, stuClass10, stuClass11, stuClass12, stuClass13, stuClass14, stuClass15,
                          stuClass16, stuClass17, stuClass18, stuClass19, stuClass20)

        raw = cur.execute(sql)
        # 插入数据完后提交数据

        con.commit()

# 导出数据为csv文件
def output():
    engine = create_engine('mysql+pymysql://root:1234@127.0.0.1:3306/stuDb')
    df1 = pd.read_sql(sql='SELECT * FROM lesson', con=engine)
    df1.to_csv('stu_data.csv', index=False)

