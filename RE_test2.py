#-*- encoding=UTF-8 -*-
#下面代码是为了验证re的贪婪匹配，以及如何实现最小匹配的代码，最后附上了实现最小匹配的实现规则
import re
if __name__ == '__main__':
    match = re.search(r'PY.*N', 'PYANBNCNCN')
    #这个模式在原字符串中可以匹配多次，但是re中默认使用贪婪匹配，即匹配最长的字符串，如果不加任何标识的话
    #下面打印出PYANBNCNCN
    print(match.group(0))

    #那么该如何输出最短子串呢？,在re模式*后面加上一个?即可，下面打印出PYAN
    match2 = re.search(r'PY.*?N', 'PYANBNCNCN')
    print(match2.group(0))

    #        最小匹配操作符说明（总结为一句话，在后面加?即可实现）
    # *?     前一个字符0次或者无限次扩展，最小匹配
    # +?     前一个字符1次或者无限次扩展，最小匹配
    # ??     前一个字符0次或者1次扩展，最小匹配
    # {m,n}? 扩展前一个字符m至n次（含n次），最小匹配