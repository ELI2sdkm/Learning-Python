# 编写一个 computegrade 函数，用来计算成绩等级：该函数将分数作为参数，并返回一个字符串形式的分数（即成绩等级）。
score = eval(input())


def computer_grade():
    if 1 >= score >= 0:
        if score >= 0.9:
            grade = 'A'
        elif score >= 0.8:
            grade = 'B'
        elif score >= 0.7:
            grade = 'C'
        elif score >= 0.6:
            grade = 'D'
        else:
            grade = 'E'
        return grade
    else:
        print("输入有误，成绩应在0~1间")


print(computer_grade())
