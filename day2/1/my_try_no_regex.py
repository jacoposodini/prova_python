import argparse
from datetime import datetime

   
def get_errors(path,err_code):
    
    log=[]
    
       
    try:
        with open(path) as f:
            
            
            for line in f.readlines():
                err=0
                cnt=0
                cnt2=0
                for element in line.split():
                    cnt += 1;
                    
                    if cnt == 4:
                        date = datetime.strptime(element[1:], '%d/%b/%Y:%H:%M:%S')
                        #print (date)
                    if cnt == 7:
                        resource = element
                        #print (resource)
                    if err == 0:
                        try:
                            err = int(element)                            
                            #print(err)
                        except ValueError:
                            pass;
                    if err != 0:
                        cnt2 +=1
                    
                    if cnt2 == 3:
                        referrer = element
                        #print (referrer)
                if err == int(err_code):                    
                    log.append((date, referrer, resource))                    

    except IOError:
        print("Can't open the log file")
    return log
            
    
def main():
    parser = argparse.ArgumentParser(description='Extract error from a log file')
    
    parser.add_argument('path', help='log to be read')
    parser.add_argument('err_code', help='error code')
    args=parser.parse_args()
    
    log=get_errors(args.path,args.err_code)
    
    for date, referrer, resource in log:
        print ("{date} {res} {ref}".format(date=date.strftime("%d/%m/%y %H:%M"), res=resource, ref=referrer))
        
    
if __name__ == '__main__':
    main()
