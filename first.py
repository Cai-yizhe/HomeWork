import math

print('二进制 1111011 转十进制', int("1111011", 2))
print('二进制 1111011 转十进制', eval("0b1111011"))

# 十进制转二进制
print('十进制18 转二进制', bin(18))
print('十进制 18 转二进制', "{0:b}".format(18))

# 八进制转十进制
print('八进制 011转十进制', int("011", 8))
print('八进制 011转十进制 ', eval("0o011"))

# 十进制转八进制

print('十进制 30转八进制', oct(30))
print('十进制 30转八进制', "{0:o}".format(30))

# 十六进制转十进制
print('十六进制 12 转十进制 ', int("12", 16))
print('十六进制 12 转十进制', eval("0x12"))
# 十进制转十六进制
print('十进制 87 转十六进制', hex(87))
print('十进制 87转十六进制', "{0:x}".format(87))

name = input("name:")
Chinese = float(input("Chinese scores:"))
Math = float(input("Math scores:"))
English = float(input("English scores:"))
sum = Chinese + Math + English
average = sum / 3
print("总分=%.2f" % sum)
print("平均=%.2f" % average)

# 已知三角形的边长求三角形的面积和周长import math
a = float(input('a= '))
b = float(input('b= '))
c = float(input('c= '))
if a + b > c and a + c > b and b + c > a:
    d = a + b + c
    e = (a + b + c) / 2
    f = math.sqrt(e * (e - a) * (e - b) * (e - c))
    # 计算三角形面积
    # sprt()方法返回数字x的平方根,sqrt()是不能直接访问的，需要导入 math;模块，通过静态对象调用该方法。
    # 计算半周长
    print('三角形的周长为:' + str(d))
    print('三角形的面积为:%.2f' % f)
else:
    print('三条变得长度不能构成三角形')
