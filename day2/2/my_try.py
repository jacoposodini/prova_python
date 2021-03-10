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

       
def make_XML(sites,destination):
    '''
<urltests>
  <test>
    <url>http://www.python.org</url>
    <result>fail</result>
    <details>
      <connectiontest>success</connectiontest>
      <timetest elapsed="2410" maxtime="2000">fail</timetest>
    </details>
  </test>
  ...
</urltests>
'''
    troot = ET.Element('urltests')
    try:
        with open(destination, "wb") as f:
        
            for url,rx_time,status,online,max_time in sites:
                ttest = ET.SubElement(troot, 'test')
                turl = ET.SubElement(ttest, 'url')
                turl.text = url            
                tdetails = ET.SubElement(ttest,'details')
                tconn = ET.SubElement(tdetails, 'connectiontest')
                tconn.text = 'success' if online else 'fail'            
            
                if online:
                    #ttimetest = ET.SubElement(tdetails, 'timetest', {'elapsed': '{:.2f}'.format(t), 'maxtime': '{:.2f}'.format(max_time)})
                    ttimetest = ET.SubElement(tdetails, 'timetest', {'elapsed': '{:.2f}'.format(rx_time*1000), 'maxtime': '{:.2f}'.format(max_time)})
                    #ttimetest = ET.SubElement(tdetails, 'timetest')
                    ttimetest.text = 'success' if (rx_time*1000) < max_time else 'failed'
                    
            f.write(ET.tostring(troot))
    except IOError:
        print("Can't open XML file {}".format(destination))
        
    return troot
        
def main():
    
    parser=argparse.ArgumentParser(description='Test websites')
    parser.add_argument('-x', help="Print a XML report")
    args = parser.parse_args()
    
       
    tested=test_site(URLS)
    for url,rx_time,status,online,max_time in tested:
        response = "OK" if online else "KO"
        print ("{:40} {:.3f} {} \t\t{}".format(url,rx_time,status,response))
        
    if args.x:
        #print (args.x)
        XML=make_XML(tested, args.x)  


if __name__=='__main__':
    main()
