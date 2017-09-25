# -*-encoding=UTF-8-*-
import re
if __name__ == '__main__':
    m = re.search(r'[1-9]\d{5}', 'cvvavava100081 caccac100084')
    #打印出待匹配的字符串，打印出cvvavava100081 caccac100084
    #print(m.string)
    #打印出正则表达式的匹配模式
    #print(m.re)
    #下面pos属性的意思是搜索字符串的开始位置和结束位置，打印出0
    #print(m.pos)
    #下面打印出27
    #print(m.endpos)

    #match函数只会打印出第一次匹配到的字符串，如果希望打印出每一次匹配到的字符串，那就应该使用finditer()函数
    #print(m.group(0))

    #打印出这次匹配在原字符串的起始位置,打印出8
    print(m.start())
    #打印出这次匹配在原字符串的结束位置，打印出14
    print(m.end())
    #打印出这两次匹配位置的二元关系，即（m.start()， m.end()），结果会放在一个元组中,结果是（8,14）
    print(m.span())


