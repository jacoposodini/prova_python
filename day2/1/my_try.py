import re
import argparse
from datetime import datetime
from collections import namedtuple

REG = re.compile(
    '(?:\d{1,3}\.){3}\d{1,3}'  # the ip
    '\s-\s-\s\\[(?P<date>.*?)\s.*?\\]\s'
    '"(?:GET|POST)\s(?P<resource>.*?)'
    '\s.*?"\s(?P<status_code>\d{3}).*?'
    '"(?P<referrer>.*?)"',
    re.VERBOSE)
    
def get_errors(path,err):
    
    log = []
    Log = namedtuple('Log_list',['date','referrer','resource'])    
    
    with open(path) as f:
        for line in f.readlines():
            l = REG.search(line)            
            if l is not None and l.group('status_code') == err:                
                date = datetime.strptime(l.group('date'), '%d/%b/%Y:%H:%M:%S')
                elem = Log(date, l.group('referrer'),l.group('resource'))
                log.append(elem)
    return log
            
    
def main():
    parser = argparse.ArgumentParser(description='Extract error from a log file')
    
    parser.add_argument('path', help='log to be read')
    parser.add_argument('err_code', help='error code')
    args = parser.parse_args()
    
    log = get_errors(args.path,args.err_code)
    
    for date, referrer, resource in log:
        print ("{date} {res} {ref}".format(date=date.strftime("%d/%m/%y %H:%M"), res=resource, ref=referrer))

    
if __name__ == '__main__':
    main()
