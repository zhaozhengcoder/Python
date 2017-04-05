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
from docopt import docopt
#stations 是一个文件
from stations import stations
import requests

def print_all(getjson):
    for x in getjson['data']:
        print (">")
        print ('车次',x['queryLeftNewDTO']['station_train_code'])
        print ('起点站',x['queryLeftNewDTO']['from_station_name'])
        print ('目的站',x['queryLeftNewDTO']['to_station_name'])
        print ('出发时间',x['queryLeftNewDTO']['start_time'])
        print ('到达时间',x['queryLeftNewDTO']['arrive_time'])
        print ('历时',x['queryLeftNewDTO']['lishi'])
        print ('一等座　',x['queryLeftNewDTO']['zy_num'])
        print ('二等座　',x['queryLeftNewDTO']['ze_num'])
        print ('软卧　',x['queryLeftNewDTO']['rw_num'])
        print ('硬卧　',x['queryLeftNewDTO']['yw_num'])
        print ('硬座　',x['queryLeftNewDTO']['yz_num'])
        print ('无座　',x['queryLeftNewDTO']['wz_num'])
        print ('~~')

def print_options(getjson,arguments):
    for x in getjson['data']:
        opt='-'+x['queryLeftNewDTO']['station_train_code'][0].lower()
        if(opt in arguments.keys() and arguments[opt]==True):
            print (">")
            print ('车次',x['queryLeftNewDTO']['station_train_code'])
            print ('起点站',x['queryLeftNewDTO']['from_station_name'])
            print ('目的站',x['queryLeftNewDTO']['to_station_name'])
            print ('出发时间',x['queryLeftNewDTO']['start_time'])
            print ('到达时间',x['queryLeftNewDTO']['arrive_time'])
            print ('历时',x['queryLeftNewDTO']['lishi'])
            print ('一等座　',x['queryLeftNewDTO']['zy_num'])
            print ('二等座　',x['queryLeftNewDTO']['ze_num'])
            print ('软卧　',x['queryLeftNewDTO']['rw_num'])
            print ('硬卧　',x['queryLeftNewDTO']['yw_num'])
            print ('硬座　',x['queryLeftNewDTO']['yz_num'])
            print ('无座　',x['queryLeftNewDTO']['wz_num'])
            print ('~~')
        

def search():
    """command-line interface"""
    arguments = docopt(__doc__)
    #print(arguments)
    from_station=stations.get(arguments['<from>'])
    to_station=stations.get(arguments['<to>'])
    date=arguments['<date>']
   
    url1='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2017-04-25&leftTicketDTO.from_station=SHH&leftTicketDTO.to_station=BJP&purpose_codes=ADULT'
  
    url2='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(
        date,from_station,to_station
    )
    #print (url4)
    #print (url2)
    
    # 这里为什么要加上一个　；
    r = requests.get(url2, verify=False);
    #print (r.json())

    if('-d' in arguments.keys()or'-g' in arguments.keys()or'-k' in arguments.keys()or'-t' in arguments.keys()or'-z' in arguments.keys()):
        print_options(r.json(),arguments)
    else:
        print_all(r.json())


if __name__ == '__main__':
    search()