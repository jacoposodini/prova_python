import requests
import time
import argparse
import xml.etree.ElementTree as ET


URLS = {
    'http://www.python.org': 1000,
    'http://www.google.com': 2000,
    'http://www.yahoo.i': 2000,
    'http://www.gazzetta.com': 1000,
    'http://www.linkedin.com/': 1000,
    'www.pycon.it': 2000,
}

def test_site(URLS):
    tested=[]
    for i in URLS:
        online = False
        try:            
            start_time=time.time()
            req = requests.request('GET', i, timeout=URLS[i]/1000)
            online=True
            tested.append([i,time.time()-start_time,req.status_code,online,URLS[i]])
        except requests.Timeout:
            tested.append([i,time.time()-start_time,'Timeout',online,URLS[i]])
        except requests.RequestException as e:
            tested.append([i,time.time()-start_time,'ERR',online,URLS[i]])
            
    return tested

def main():
    
    parser=argparse.ArgumentParser(description='Test websites')
    parser.add_argument('-x', help="Print a XML report")
    args = parser.parse_args()
    
       
    tested=test_site(URLS)
    for url,rx_time,status,online,max_time in tested:
        response = "OK" if online else "KO"
        print ("{:40} {:.3f} {} \t\t{}".format(url,rx_time,status,response))
        


if __name__=='__main__':
    main()
