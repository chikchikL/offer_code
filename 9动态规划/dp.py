# 求一个长度n的绳子切割的最大乘积
def dp_max(n):
    l = [0 for i in range(n + 1)]
    l[2] = 1
    l[3] = 2

    i = 4
    while i <= n:

        i = i + 1
