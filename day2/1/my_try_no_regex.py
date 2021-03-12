import argparse
from datetime import datetime

   
def get_errors(path,err_code):
    
    log = []
    
    try:
        with open(path) as f:
            
                for line in f.readlines():
                    err = None
                    split = line.split()
                    
                    date = datetime.strptime(split[3][1:], '%d/%b/%Y:%H:%M:%S')                                        
                    resource = split[6]
                    try:
                        err = int(split[8])
                    except ValueError:
                        print("Invalid line")                        
                        
                    referrer = split[10]                    
                    
                    if err == int(err_code):                    
                        log.append((date, referrer, resource))                    

    except IOError:
        print("Can't open the log file")
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
