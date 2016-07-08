# coding=utf-8
# python中字符串的操作非常丰富，python本身提过了一些内置函数供调用。
import string

S = 'hello world! you can do it! WHO　ARE YOU? I am 100 years old    我是中文'

# 把字符串的第一个字符大写
print S.capitalize()


# 返回一个原字符串居中,并使用空格填充至长度 width 的新字符串
print S.center(5)


# 返回 str 在 S 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
print S.count('w', 0, len(S))

#以 encoding 指定的编码格式解码 S，如果出错默认报一个 ValueError的异常
print S.decode('utf-8', 'strict')

# 检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.
print S.endswith('obj', 0, len(S))

# 检测 str 是否包含在 S 中，如果 beg 和 end 指定范围，则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回-1
print S.find('s', 0, len(S))
print S.find('z', 0, len(S))

# 跟find()方法一样，只不过如果str不在 S中会报一个异常.
print S.index('s',0, len(S))

# # 如果 S 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
print S.isalnum()

# 如果 S 至少有一个字符并且所有字符都是字母则返回 True,否则返回 False
print S.isalpha()

# # 如果 S 只包含十进制数字则返回 True 否则返回 False.
# print S.isdecimal()

# 如果 S 只包含数字则返回 True 否则返回 False.
print S.isdigit()

# 如果S中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
print S.islower()

# 如果 S 中只包含数字字符，则返回 True，否则返回 False
# print S.isnumeric()

# 如果 S 中只包含空格，则返回 True，否则返回 False.
print S.isspace()

# 如果 S 是标题化的(见 title())则返回 True，否则返回 False
print S.istitle()

# 如果 S 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
print S.isupper()

# Merges (concatenates)以 S 作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
print '-'.join(['1','2','3','4'])

# 转换 S 中所有大写字符为小写.
print S.lower()

# 翻转 S 中的大小写
print S.swapcase()

# 把 S 中的 str1 替换成 str2,如果 num 指定，则替换不超过 num 次.
print S.replace('w','o',1)

# 以 str 为分隔符切片 S，如果 num有指定值，则仅分隔 num 个子字符串
print S.split(" ", 3)




