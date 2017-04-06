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
from prettytable import PrettyTable

def print_all(getjson,pt):
    for x in getjson['data']:
        r1=x['queryLeftNewDTO']['station_train_code']
        r2=x['queryLeftNewDTO']['from_station_name']
        r3=x['queryLeftNewDTO']['to_station_name']
        r4=x['queryLeftNewDTO']['start_time']
        r5=x['queryLeftNewDTO']['arrive_time']
        r6=x['queryLeftNewDTO']['lishi']
        r7=x['queryLeftNewDTO']['zy_num']
        r8=x['queryLeftNewDTO']['ze_num']
        r9=x['queryLeftNewDTO']['rw_num']
        r10=x['queryLeftNewDTO']['yw_num']
        r11=x['queryLeftNewDTO']['yz_num']
        r12=x['queryLeftNewDTO']['wz_num']
        pt.add_row([r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12])
    print(pt)

def print_options(getjson,pt,arguments):
    for x in getjson['data']:
        opt='-'+x['queryLeftNewDTO']['station_train_code'][0].lower()
        if(opt in arguments.keys() and arguments[opt]==True):
            r1=x['queryLeftNewDTO']['station_train_code']
            r2=x['queryLeftNewDTO']['from_station_name']
            r3=x['queryLeftNewDTO']['to_station_name']
            r4=x['queryLeftNewDTO']['start_time']
            r5=x['queryLeftNewDTO']['arrive_time']
            r6=x['queryLeftNewDTO']['lishi']
            r7=x['queryLeftNewDTO']['zy_num']
            r8=x['queryLeftNewDTO']['ze_num']
            r9=x['queryLeftNewDTO']['rw_num']
            r10=x['queryLeftNewDTO']['yw_num']
            r11=x['queryLeftNewDTO']['yz_num']
            r12=x['queryLeftNewDTO']['wz_num']
            pt.add_row([r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12])
    print(pt)
        

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
    #python3 train_tickets2.py -g 上海 北京 2017-04-25  注意４要写成０４，不要写成2017-4-25
    #print (url1)
    #print (url2)
    

    # 这里为什么要加上一个;
    r = requests.get(url1, verify=False);
    #print (r.json())


    header='车次 起点站 目的站 出发时间 到达时间 历时 一等座 二等座 软卧 硬卧 硬座 无座'.split()
    pt=PrettyTable()
    pt._set_field_names(header)


    if('-d' in arguments.keys()or'-g' in arguments.keys()or'-k' in arguments.keys()or'-t' in arguments.keys()or'-z' in arguments.keys()):
        print_options(r.json(),pt,arguments)
    else:
        print_all(r.json(),pt)

    
if __name__ == '__main__':
    search()