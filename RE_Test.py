# -*-encoding=UTF-8-*-
#hello, python re!
import re
if __name__ == '__main__':
    #re.search只返回匹配到的第一个字符串，后面如果还有能够匹配上的字符串，则不会返回，下面输出100081
    #match = re.search(r'[1-9]\d{5}', 'BIT 100081caca100086')
    #if match:
    #    print(match.group(0))

    #re.match只从一个给定的字符串起始位置开始匹配，如果起始位置没有匹配到，则返回空，下面返回100081
    # 如果将给定字符串变为'BIT 100081'，则返回空，什么都不会打印，match对象为空！
    #match = re.match(r'[1-9]\d{5}', '100081 BIT')
    #if match:
    #    print(match.group(0))

    #re.findall函数会匹配给定字符串中所有能够匹配上的字符串，并将其放置在一个列表中，下面打印出['100081','100084']
    #ls = re.findall(r'[1-9]\d{5}', 'BIT100081 TSU100084')
    #print ls

    #split函数会将匹配到的部分去掉，把剩下的部分放在列表中，下面打印出['BIT', ' TSU', '']
    #print (re.split(r'[1-9]\d{5}', 'BIT100081 TSU100084'))

    #maxsplit=1的意思是正则表达式只匹配第一个满足条件的字符串，并去掉它，分割剩下的字符串
    #下面打印出['BIT', ' TSU100084']
    #print (re.split(r'[1-9]\d{5}', 'BIT100081 TSU100084', maxsplit=1))
    #下面打印出['BIT', ' TSU', 'cava100089hjnjn']
    #print (re.split(r'[1-9]\d{5}', 'BIT100081 TSU100084cava100089hjnjn', maxsplit=2))

    #finditer函数搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素是match对象
    #下面打印出100081，100084，100089
    #for m in re.finditer(r'[1-9]\d{5}', 'BIT100081 TSU100084cava100089hjnjn'):
    #    if m:
    #        print(m.group(0))

    #sub函数的意思是，使用一个新的给定的字符串去替换给定字符串中满足正则表达式的字符串
    #下面输出BIT:zipcode TSU:zipcodecava:zipcodehjnjn
    #print (re.sub(r'[1-9]\d{5}', ':zipcode', 'BIT100081 TSU100084cava100089hjnjn'))

    #sub其参数中还有一个count参数，用来指定替换次数
    #下面打印出BIT:zipcode TSU:zipcodecava100089hjnjn，只替换两次，后面出现的满足正则表达式的字符串不再进行替换
    #print (re.sub(r'[1-9]\d{5}', ':zipcode', 'BIT100081 TSU100084cava100089hjnjn', count=2))

    #compile函数会将一个正则表达式字符串编译为一个正则表达式规则，方便以后调用，这是面向对象的一种使用方法
    regex = re.compile(r'[1-9]\d{5}')

