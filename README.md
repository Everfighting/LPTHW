# Learn Python the hard way
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

    - 编码设置： # -*- encoding:utf-8 -*-

    - 井号英文:octothorpe，pound，hash，mesh等。

- ex2.py

    \#为注释作用，后面代码不解释

- ex3.py

    相关数字符号，跟数学计算优先级类似。

    计算优先顺序为：“括号、指数、按位翻转（取符号）、乘、除、取余、加、减、位左移右移

    round( x [, n]  )四舍五入，n为精确度 *

- ex4.py
> 变量命名尽量有意义，用下划线连接单词。

- ex5.py
> 格式化字符：
%%百分号标记、%c字符及其ASCII码、%s字符串、%d有符号整数(十进制)、%f浮点数字(用小数点符号)


- ex6.py
> 单引号一般无差异。一般单引号会被用来创建简短的字符串。'a' 'snow'

- ex7.py
> 逗号会被解释成空格，显示在一行。
Python编码风格，解释最好另起一行，不需每行都解释，关键需解释。

- ex8.py
> 格式化输出。

- ex9.py
> \n 换行符 \t tab键 \转义字符

- ex10.py
> \\ 反斜杠 \'单引号 \"双引号 \uxxxx十六进制符  \ooo 八进制为000字符 \xhh值为十六进制数hh的字符
""" 三引号多行引用

- ex11.py
> 代码中的逗号（comma）输出的时候会变成空格。

- ex12.py
> raw_input()括号中可放入提示信息。
pydoc模块主要用来从Python模块中提取信息并生成文档。
pydoc 模块名 查看模块相关信息。

- ex13.py
> argv 和 raw_input有什么不同？
不同点在于用户输入的时机。如果参数是在用户执行命令时就要输入，那就是argv,如果是在脚本运行过程中需要用户输入，那就使用raw_input()

- ex14.py
> """定义多行字符串。
argv是所谓的参数变量,包含了你传递给Python的参数。
解包是把argv中的东西解包，将所有的参数依次赋予左边的变量名。

- ex15.py
> sys是一个库，是从中取出argv这个功能来。
txt.read意思是上txt执行read命令。

- ex16.py
> 文件相关操作：
    open - 打开文件。f = open('filename', mode)
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
> os.path中有 exists 判断文件是否存在
len()能够判断文本的长短

- ex18.py
> *args 必须放在（）才能正常工作。
*args 把所有的参数都传进来，放到名字叫args的列表中去。
**args 把所有的参数都传进来，放到名字叫做args的字典中去。

- ex19.py

- ex20.py
> seek(offset,where): where=0从起始位置移动，1从当前位置移动，2从结束位置移动。
当有换行时，会被换行截断。seek（）无返回值，故值为None。

- ex21.py
>

- ex22.py

- ex23.py

- ex24.py

- ex25.py

- ex26.py
> 执行import时不需要加.PY后缀。
- ex27.py
> 真值表 Not,or,and,not or,not and
- ex28.py

- ex29.py

- ex30.py
> if语句可以跟多个elif语句，但最后只能有一个else语句

- ex31.py

- ex32.py

- ex33.py

- ex34.py

- ex35.py

- ex36.py

- ex37.py

- ex38.py

- ex39.py

- ex40.py

- ex41.py

- ex42.py

- ex43.py

- ex44.py

- ex45.py

- ex46.py

- ex47.py

- ex48.py

- ex49.py

- ex50.py

- ex51.py

- ex52.py



