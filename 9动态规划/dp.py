# 求一个长度n的绳子切割的最大乘积
# 思路：f(n) = max{f(i)*f(n-i)}
def dp_max(n):
    # 思路：至少切一刀
    # n<4时，不切的长度最大，任意切法均小于绳子本身长度
    # n>=4时，有2*2=4，可以切一刀达到最大值
    # 因为绳子是从最大长度开始切的，当n>=4时，切一刀后，比如1,3取得的最优结果应该分别是n=1和3的两根绳子本身的长度
    # 而不是f(1)=0和f(3)=2，因此当n>=4使用动态规划时，n=1，2，3三种情况应该取不切的值
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2

    # n>=4 时用动态规划
    l = [0 for i in range(n + 1)]
    l[1] = 1
    l[2] = 2
    l[3] = 3

    i = 4
    while i <= n:
        max = 0
        # 找到max{f(i)*f(n-i)}
        j = 1
        while j <= (i // 2):
            temp = l[j] * l[i - j]
            if max < temp:
                max = temp
            j = j + 1
        l[i] = max
        i = i + 1

    return l[n]


print(dp_max(8))
