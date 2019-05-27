#计算器
def ca():
    print("请输入第一项（加数、被减数、因数、被除数 等）")
    f = float(input(">"))
    print("请输入第二项（加数、减数、因数、除数 等）")
    s = float(input(">"))
    print("请输入运算类型（+、-、*、/  [对应加、减、乘、除]）")
    n = input(">")
    if n=='+':
        out = f+s
    if n=='-':
        out = f-s
    if n=='*':
        out = f*s
    if n=='/':
        out = f/s
    print('运算结果是：',out)
    input('回车键返回>')