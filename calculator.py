# 计算器
expression = input("请输入表达式：")
try:
    result = eval(expression)
    print(f"结果是{result}")
except:
    print("输入有误！")