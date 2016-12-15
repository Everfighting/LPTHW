# Learn Python the hard way(第三版)）
#####笔记内容来自练习中的总结并略有扩展。
#####扩展以类似ex3_1.py形式命名，表示对ex3内容的扩展
#####书中python版本为2,部分内容3已经不适用

- 前言
    - 学习诀窍：读和写、注重细节、发现不同
    - 注意点：不要复制粘贴。坚持完成。

- ex0.py

    - 终端运行时CTRL-D退出
    - linux常用命令：

            mkdir  创建文件夹
            rmdir  删除文件夹
            cd     切换目录
            pwd    所在文件位置
            ls/dir 所在目录所有文件信息
            touch  创建新文件

- ex1.py

    - 编码设置： # -*- encoding:utf-8 -*- 、#coding:utf-8
    - 井号英文:octothorpe，pound，hash，mesh等。
    - ^标记出错误的位置。
    - 注意阅读错误信息，判断类型及可能原因。

- ex2.py

    - \#为注释作用，后面代码不解释
    - \#若在字符串中则不做注释。
    - 多行注释方法：每一行放\#

- ex3.py

    - 关数字符号，跟数学计算优先级类似。
    - 计算优先顺序为：“括号、指数、按位翻转（取符号）、乘、除、取余、加、减、位左移右移
    - round( x [, n]  )四舍五入，n为精确度.（有时会存在进制转换误差。）
    - %取余 5%3 = 2 divmod(5,3) = (1,2)
    - 7/4 = 1 地板除，去尾法 7.0/4.0 = 1.75
    - 5**2 = 25  乘方
    - 计算扩展看ex3_1

- ex4.py
    - python中没有变量类型声明这一步。
    - 变量命名尽量有意义，用下划线连接单词。
    - '='两边加上空格会更易阅读，实际无影响。

- ex5.py
    - 格式化字符：

            %%百分号标记
            %c字符及其ASCII码
            %s字符串 (采用str()的显示)
            %d有符号整数(十进制)
            %f浮点数字(用小数点符号)
            %r字符串 (采用repr()的显示)
    - round()函数，误差产生原因：一些十进制小数不能够精确地用二进制来表示。


- ex6.py
    - 单引号一般无差异。一般单引号会被用来创建简短的字符串。'a' 'snow'
    - python三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符。
    - 布尔值，False中的F不能小写
    - 字符串类型与布尔类型不能相加
    - 字符串相关操作看ex6_1

- ex7.py
    - 逗号会被解释成空格，显示在一行。
    - 字符序列可以乘以整型数字，实现复制输出。'*'*10
    - Python编码风格，解释最好另起一行，不需每行都解释，关键需解释。
    - PEP8风格要点见PEP8.md

- ex8.py
    - 格式化输出。

- ex9.py

        \n 换行符
        \t tab键
        \转义字符
        \v 纵向制表符

- ex10.py
    - """ 三引号多行字符串
    - 转义字符\

            \\ 反斜杠
            \'单引号
            \"双引号
            \uxxxx十六进制符
            \ooo 八进制为000字符
            \xhh值为十六进制数hh的字符

- ex11.py

- ex12.py
    - raw_input()括号中可放入提示信息。
    - pydoc模块主要用来从Python模块中提取信息并生成文档。

            windows：
            python -m pydoc <modulename>
            linux:
            pydoc <modulename>

- ex13.py
    - argv 和 raw_input有什么不同？

            如果参数是在用户执行命令时就要输入，那就是argv
            如果是在脚本运行过程中需要用户输入，那就使用raw_input()
    - 一个实现某类特定功能的变量、函数、类的集合。类似模块、库。
    - python ex13.py second third 脚本后面跟的是参数。
    - from .....import.....是导入外部模块的固定格式，也可import.....。

            sys.argv 通过import sys 导入，且导入了sys模块下所有对象
            argv     通过from sys import argv 导入，且只导入了argv变量

- ex14.py

        argv是所谓的参数变量,包含了你传递给Python的参数。
        解包是把argv中的东西解包，将所有的参数依次赋予左边的变量名。

- ex15.py
    - sys是一个库，是从中取出argv这个功能来。
    - txt.read意思是上txt执行read命令。

- ex16.py

    - 文件相关操作：open - 打开文件。f = open('filename', mode)
    - 使用'W'，文件若存在，首先要清空，然后（重新）创建
    - 使用'a'模式 ，把所有要写入文件的数据都追加到文件的末尾，如果文件不存在，将自动被创建。

            相关参数
            w     以写方式打开，
            a     以追加模式打开 (从 EOF 开始, 必要时创建新文件)
            r+     以读写模式打开
            w+     以读写模式打开 (参见 w )
            a+     以读写模式打开 (参见 a )
            rb     以二进制读模式打开
            wb     以二进制写模式打开 (参见 w )
            ab     以二进制追加模式打开 (参见 a )
            rb+    以二进制读写模式打开 (参见 r+ )
            wb+    以二进制读写模式打开 (参见 w+ )
            ab+    以二进制读写模式打开 (参见 a+ )

            close - 关闭文件。
            read - 读取文件。
            readline - 读取文本文件中的一行。
            truncate - 清空文件。
            write(stuff) -将stuff写入文件。

- ex17.py
    - os.path中有 exists 判断文件是否存在
    - len()能够判断文本的长短

- ex18.py
    - *args 必须放在（）才能正常工作。
    - *args 把所有的参数都传进来，放到名字叫args的列表中去。
    - **args 把所有的参数都传进来，放到名字叫做args的字典中去。
    - 函数定义的注意事项：

            1.以def关键字开始函数定义
            2.函数名字可以是任意名字，但最好是能够反映函数功能的名字，并不与python关键字重复
            3.紧跟函数名的是一对括号
            4.括号中可以包含参数，也可以空着，若有多个参数，参数之间以逗号分隔，可以让参数等于某个值即设定了该参数的默认值，在调用时，若没有给出该参数，则使用默认值。
            5.括号后面是一个冒号
            6.函数体需要整体缩进相同的距离，python将冒号以下缩进相同的内容视为函数体。
            7.函数可以使用return返回某个值

- ex19.py

        可以在函数里用变量名 cheese_and_crackers(cheese_count, boxes_of_crackers)
        可以在函数里做运算 cheese_and_crackers(10+20, 5+6)
        甚至可以把运算跟变量相结合  cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers+1000)
    - raw_input() 默认输出的为字符串 需转换int(raw_input())
    - python函数的参数分类

            1.必备参数
            2.缺省参数:即默认值。默认值在函数定义时用等号设置
            3.命名参数:命名参数和函数调用关系紧密，调用方用参数的命名确定传入的参数值。
            4.不定长参数：需要一个函数能处理比当初声明时更多的参数.加了'*'或'**'的变量名。
    - 全局变量和局部变量

            定义在函数内部的变量，作用域为函数体内，属于局部变量，只能在函数内部进行访问；
            定义在函数外部的变量，作用域为整个脚本，属于全局变量，能在脚本的任意地方访问；

- ex20.py
    - seek(offset,where)

            where=0从起始位置移动，1从当前位置移动，2从结束位置移动。
            当有换行时，会被换行截断。seek（）无返回值，故值为None。
    - 文件读取：

            f.read(size)
            f.readline()
            f.readlines()
    - x += y 与 x = x + y 一样

- ex21.py
    - return返回结果，return None不返回内容。

- ex22.py

- ex23.py
    - 更多渠道阅读别人的代码,如github。

- ex24.py
    - 字符串乘法'-'*
    - 跨行字符续在一行显示 \
    - tab \t 、换行 \n

- ex25.py
    - split str.split([sep[, maxsplit]])
    - sorted(iterable[, cmp[, key[, reverse]]])
    - L.pop([index]) -> item -- remove and return item at index (default last).

- ex26.py
    - 执行import时不需要加.PY后缀。

- ex27.py
    - 真值表 Not,or,and,not or,not and 学会判断。
    - 数字0，None类型，空字符串，空列表，空字典，空元组也被认为是False。

- ex28.md

- ex29.py
    - 注意缩进，防止if悬挂。

- ex30.py
    - if语句可以跟多个elif语句，但最后只能有一个else语句

- ex31.py
    - if...elif/else结构，只需要检查到第一个为True就停止继续执行。

- ex32.py
    - 列表的计数是从0开始，如果是从右计数是-1开始的。
    - range、list用法见ex32_1，冒泡算法的实现！***

- ex33.py
    - list.append()用法

- ex34.py
    - list[index] index从0到len(list)-1

- ex35.py
    - if...elif...else判断
    - raw_input()获取输入信息
    - 线程模块方法
    - run(): 用以表示线程活动的方法。
    - start():启动线程活动。

- ex36.py

- ex37.py
    - 认识关键字

- ex38.py
    -列表操作

            创建列表：list1 = ['physics', 'chemistry', 1997, 2000];
            访问列表中的值：print "list1[0]: ", list1[0]
            更新列表：list1[2] = 2001;
            在列表末尾添加新的对象：list.append(obj)
            删除列表元素：del list1[1];
            移除列表中某个值的第一个匹配项：list.remove(obj)
            反向列表中元素：list.reverse()
            比较两个列表的元素:cmp(list1, list2)

            python脚本操作：
                len([1, 2, 3]) 列表长度
                [1, 2, 3] + [4, 5, 6] 同类型列表组合
                ['Hi!'] * 4 列表重复
                3 in [1, 2, 3] 判断元素是否在列表中
                for x in [1, 2, 3]: print x, 迭代出元素

- ex39.py
    - 字典操作

            创建字典：
                d = {key1 : value1, key2 : value2 }
                值可以取任何数据类型，但键必须是不可变的(可哈希)，如字符串，数字或元组。

            修改字典
                dict['Age'] = 8; # update existing entry
                dict['School'] = "DPS School"; # Add new entry

            删除字典元素
                dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
                del dict['Name']; # 删除键是'Name'的条目
                dict.clear();     # 清空词典所有条目
                del dict ;        # 删除词典

            字典键的特性
                不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住。
                键必须不可变(可哈希)，所以可以用数字，字符串或元组充当，所以用列表就不行。

            字典内置函数&方法
                cmp(dict1, dict2) #比较两个字典元素。
                len(dict)		  #计算字典元素个数，即键的总数。
                str(dict)         #输出字典可打印的字符串表示。
                type(variable)    #返回输入的变量类型，如果变量是字典就返回字典类型。

            Python字典包含了以下内置方法：
                dict.clear()    #删除字典内所有元素
                dict.copy()     #返回一个字典的浅复制
                dict.fromkeys() #创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
                dict.get(key, default=None) #返回指定键的值，如果值不在字典中返回default值
                dict.has_key(key) #如果键在字典dict里返回true，否则返回false
                dict.items() #以列表返回可遍历的(键, 值) 元组数组
                dict.keys() #以列表返回一个字典所有的键
                dict.setdefault(key, default=None) #和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
                dict.update(dict2) #把字典dict2的键/值对更新到dict里
                dict.values() #以列表返回字典中的所有值

- ex40.py
    - self变量

            在创建__init__或者别的函数时需要多加一个self变量。
            如果不加self会造成代码歧义。有了self，self.cheese = 'Franck'
            就清楚说明是实例的属性：self.cheese
    - 模块的理解

            模块可以当做一种特殊的字典，通过他们可以存储一些python代码，然后通过‘.’操作符访问这些代码。
            Python还有一种代码结构实现类似的目的，就是类，通过类可以把一组函数和数据放到一个容器中，从而用‘.’操作符访问。

- ex41.py
    - self 是 Python 创建的额外的一个参数，确保函数能够正常工作。
    - __init__ 函数，为class设置内部变量的方式，用self.设置到self上面。
    - [:]复制整个列表。

- ex42.py
    - 类、对象、实例
    - super函数

- ex43.py

- ex44.py
    - 继承、合成、覆写

- ex45.py

- ex46.py
    - pip：用于安装其他软件的软件

            pip install SomePackage #安装包
            pip install --upgrade SomePackage #升级包
            pip uninstall SomePackage #卸载包

- ex47.py
    - nose：自动化测试框架

            使用nose运行简单，只要遵循简单规则来组织你的库和代码；
            设置测试环境简单；nose有非常多内建的插件来帮助你捕捉输出，错误信息等。

- ex48.py
    - try...except...

            异常处理，运行代码段放到try中，出错之后需要运行except中的代码段。

    - 字符串split用法

            stuff = raw_input('> ') # 提示输入字符串内容
            words = stuff.split() # 对字符串按照空格进行拆分
            print words # 打印出拆分后的列表

- ex49.py
    - peek、match、skip

- ex50.py

- ex51.py

- ex52.py



