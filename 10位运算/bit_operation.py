# 求一个二进制数中
# 整数通过&运算不需要转化为二进制

# 1.O(n)解法：将1循环左移，判断其&x的结果
def normal(x):
    flag = 1
    count = 0
    max = 0x80000000

    while flag <= max:
        if flag & x != 0:
            count = count + 1
        flag = flag << 1

    return count

# 2.O(1)解法
# 思路：最右边位为1，例如1101，-1后为1100，相当于最右边的1取反
# 最右边为0，直到倒数第m位为1，例如1100，倒数第三位才为1，-1后为1011，相当于第m位及以后的数字取反
# 而上述两种情况-1后的结果与原数据进行&运算，都是将本身最右边的1取反
# 1101 & 1100 = 1100     1100 & 1011 = 1000
# 综得：将x & (x-1)的效果就是将x二进制表示的最右边第一个1取反为0,x能进行几次这种操作就有几个1
def NumberOf1( x):
    # write code here
    count = 0
    while (x != 0):
        count = count + 1
        x = x & (x - 1)
    return count

print(int ('0x7fffffff',base=16))
print(hex(2147483648))

print(NumberOf1(9))