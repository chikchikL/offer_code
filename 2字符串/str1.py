# 将字符串中每个空格替换成'%20'
# 思路：遍历整个字符串计算空格个数，确定替换后的字符串总长度，然后将原来字符串的内容从后往前覆盖

def replace_space(str):
    c1 = len(str)
    c2 = c1
    for x in str:
        if x == ' ':
            c2 = c2 + 2
    # 这里需要将str长度改造下，否则会报 list assignment index out of range 通过插入空格完成
    for x in range(c2 - c1):
        str.append(' ')
    i = c1 - 1
    j = c2 - 1
    # i向前移动，如果碰到空格，j将空格替换为%20，否则j直接复制i的内容
    # 循环直到i走到index =0处
    while i >= 0:
        if str[i] == ' ':
            str[j] = '0'
            str[j - 1] = '2'
            str[j - 2] = '%'
            j = j - 3
        else:
            str[j] = str[i]
            j = j-1
        print(str)
        i = i - 1


str = list(' f fgg')
replace_space(str)
print('最终结果', ''.join(str))
l = []
global l 