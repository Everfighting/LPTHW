# coding=utf-8

# int(x [,base])          将x转换为一个整数
print int('10',2)
print int('10',8)

# 默认进制为十进制
print int('10')

# hex(x)                   将一个整数转换为一个十六进制字符串
print hex(16)

# oct(x)                   将一个整数转换为一个八进制字符串
print oct(16)

# 类似的还有
# long(x [,base] )        将x转换为一个长整数
# float(x)                将x转换到一个浮点数
# complex(real [,imag])   创建一个复数


# chr(x)                   将一个整数转换为一个字符
# 按照ASCII编码进行转换
print chr(65)

# unichr(x)                将一个整数转换为Unicode字符
# 按照unicode编码进行转换
print unichr(200)

# ord(x)                   将一个字符转换为它的整数值
print ord('A')

# str(x)                  将对象 x 转换为字符串
# 转换结果为字符串不能够与整形相加
a = str(10)
try:
	b = a + 10
except BaseException as e:
	print 'can not add an int to a string'


# repr(x)                 将对象 x 转换为表达式字符串


# tuple(s)                     将序列 s 转换为一个元组
s = [1,2,3,3]
a = tuple(s)
print a

# list(s)                      将序列 s 转换为一个列表
b = list(a)
print b

# set(s)                       转换为可变集合
# 集合会去除掉重合的元素
c = set(b)
print c

d = set([1,2,5,7,9])
print d

# 集合没有+-运算，只有& | - ^
# 交集
print c&d

 # 并集
print c|d

# 差集
print d-c

# 对称差集
print d^c

# 添加一项
d.add(8)
print d

# 添加多项
d.update([10,12,14])
print d

# 集合的长度为元素的个数
print len(d)

# 使用remove()
d.remove(1)
print d

# dict(d)           创建一个字典。d 必须是一个序列 (key,value)元组。
e = {'1':'one','2':'two'}
print e
print e['1']

