import argparse
from collections import defaultdict 

def word_list(f):
    
    d=defaultdict(int)
    
    lines=f.readlines()
    for line in lines:        
        for i in line.split():
            
            if len(i) < 3:
                continue
            
            d[i] += 1
    return d

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Count mostly frequent word in a given filename')
    
    #argomento obbligatorio.. come fare quello facoltativo?
    parser.add_argument('path', help='file path to be read')
    args=parser.parse_args()
    
    try:
        with open(args.path, 'r') as f:
            d = word_list(f)
        
    except IOError:
        print("Can't load file",args.path)
        exit(1)
    
    

    for i in sorted(d, key=d.get, reverse=True)[:10]:
        print(f"Occurences: {d[i]},{i}")
        
