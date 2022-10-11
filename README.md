一、搭建环境
    1.Python版本为3.10
    2.使用安装包
        -->pymysql
        -->sqlalchemy
        -->pandas
        -->random

二.运行代码
    1.直接运行
        -->终端中输入python interface.py（该操作会自动生成本学期五门课程点名方案和最终e值）
        -->obj1.Check()用于分析数据并输出抽点方案
        -->obj2.Output()用于导出本学期所有课程全部学生的到勤信息（格式为csv文件）
    2.各模块代码
        -->Data_generator.py用于随机生成五门课程二十次课中全部学生的到勤信息
        -->algorithm.py主要实现具体点名算法
        -->output.py将点名信息传入数据库并实现导出函数
        -->interface.py为接口，支持输出点名方案和导出全部到勤信息
    3.各部分函数功能及属性含义见代码注释
