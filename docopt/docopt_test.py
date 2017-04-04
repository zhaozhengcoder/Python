# coding: utf-8
"""命令行火车票查看器
Usage:
    tickets [-gdtkz] <from> <to> <date>

Options:
    -h,--help   显示帮助菜单
    -g          高铁
    -d          动车
    -t          特快
    -k          快速
    -z          直达

Example:
    tickets 北京 上海 2016-10-10
    tickets -dg 成都 南京 2016-10-10
"""
#上面这个很重要　

from docopt import docopt

arguments = docopt(__doc__)
#print all
print(arguments)

#输出参数
print (arguments['<from>'])
print (arguments['<to>'])
print (arguments['<date>'])

#处理选项
options=[]
for key in arguments:
    if arguments[key]==True:
        print (key)
        options.append(key)

#输出选项
print (">")
for x in options:
    print (x)

