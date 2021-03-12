import argparse
from collections import Counter 

def word_list(f):
    
    #cnt = Counter()
    words = []
    
    lines = f.readlines()
    for line in lines:        
        for i in line.split():
            
            if len(i) < 3:
                continue
            
            words.append(i)
            #cnt[i] += 1
            
    cnt = Counter(words)
    return cnt

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Count mostly frequent word in a given filename')
    
    #argomento obbligatorio.. come fare quello facoltativo?
    parser.add_argument('path', help='file path to be read')
    args = parser.parse_args()
    
    try:
        with open(args.path, 'r') as f:
            cnt = word_list(f)
        
    except IOError:
        print("Can't load file",args.path)
        exit(1)
    
       
    for i,j in cnt.most_common(10):
        print ("WORD: ",i, "\tOCCURENCIES: ",j)
