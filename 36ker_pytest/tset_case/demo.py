# 统计在一个队列中的数字，有多少个正数，多少个负数，如
l = [1, 3, 5, 7, -1, -9, -4, -5, 8, -4, -5]

def count1():
    f = 0
    j = 0
    for i in l:
        if i > 0:
            f += 1
        else:
            j += 1
    print(f, j)


def count2():
    l1 = [i for i in l if i>0]
    print(len(l1))

    l2 = [i for i in l if i<0]
    print(len(l2))


# 字符串 "axbyczdj"，如果得到结果“abcd”
def slip():
    s = "axbyczdj"
    print(s[::2])
    # 已知一个字符串为“hello_world_yoyo”, 如何得到一个队列 ["hello","world","yoyo"]

    s2 = "hello_world_yoyo"
    print(s2.split('_'))
    # 已知一个数字为1，如何输出“0001”
    print('000%d' % 1)
    # 已知一个队列,如： [1, 3, 5, 7], 如何把第一个数字，放到第三个位置，得到：[3, 5, 1, 7]
    l3 = [1, 3, 5, 7]
    l3.insert(3, l3[0])
    print(l3[1:])
#     已知 a = 9, b = 8,如何交换a和b的值，得到a的值为8,b的值为9
    a = 9
    b = 8

    a, b = b, a
    print(a, b )



def shuxianhua():
# 打印出100-999所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，
# 因为153=1的三次方＋5的三次方＋3的三次方。
    for i in range(100, 1000):
        s = 0
        l = list(str(i))
        for j in l:
            s += int(j)**3
        if s == i:
            print(i)

# a = [1, 3, 10, 9, 21, 35, 4, 6]
def maopao():
    a = [1, 3, 10, 9, 21, 35, 4, 6]
    """
    1 3 10 9 21 35 4 6  
    1 3 9 10 21 4 6 35
    1 3 9 10 4 6 21 35
    1 3 9 4 6 10 21 35 
    1 3 4 6 9 10 21 35 
    """

    for j in range(len(a)-1):
        for i in range(len(a)-j-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
    print(a)


def sort1():
    #     已知一个队列[1, 3, 6, 9, 7, 3, 4, 6]
    # 按从小到大排序
    # 按从大大小排序
    # 去除重复数字
    l = [1, 3, 6, 9, 7, 3, 4, 6]
    l.sort(reverse=True)
    print(l)
    s2 = set(l)
    print(s2)


def jianceng(n):
    # 计算n!,例如n=3(计算321=6)， 求10!
    # s = 0
    # for i in range(1, n+1):
    #     s *= i
    # print(s)

    if n == 1:
        return 1
    else:
        return n*jianceng(n-1)


def feibo(n):
#     已知一个数列：1、1、2、3、5、8、13、。。。。
# 的规律为从3开始的每一项都等于其前两项的和，这是斐波那契数列。求满足规律的100以内的所以数据
    a = 0
    b = 1
    while b <100:
        print(b)
        a, b = a+b, a


if __name__ == '__main__':
    # count1()
    # slip()
    # shuxianhua()
    # maopao()
    # sort1()
    # print(jianceng(3))
    feibo(100)