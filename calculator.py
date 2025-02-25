# 计算器
def add(a, b):
    """返回两数之和"""
    return a + b
def substract(a, b):
    """返回两数之差"""
    return a - b
def multiply(a, b):
    """返回两数之积"""
    return a * b
def divide(a, b):
    """返回两数之商,处理除零错误"""
    try:
        return a / b
    except ZeroDivisionError:
        return "除数不能为零!"

def main():
    """主函数入口"""
    # 读取用户输入
    num1 = float(input("请输入第一个数字:"))
    operator = input("请输入运算符(+,-,*,/):")
    num2 = float(input("请输入第二个数字:"))

    # 根据运算符选择函数
    if operator == "+":
        result = add(num1, num2)
    elif operator == "-":
        result = substract(num1, num2)
    elif operator == "*":
        result = multiply(num1, num2)
    elif operator == "/":
        result = divide(num1, num2)
    else:
        result = "无效的运算符!"
    
    # 输出结果
    print("结果:", result)

if __name__ == "__main__":
    main()

