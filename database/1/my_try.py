import argparse
import sqlite3

#problema!! Non funziona con le lettere accentate

def main():
    
    parser = argparse.ArgumentParser(description='some try with SQL database')
    parser.add_argument('path', help='fil path to be read')
    args=parser.parse_args()
    
    
    
    print("Init SQL")
    try:
        con = sqlite3.connect(":memory:")
    except:
        print ("Error accessing Database")
        exit(1)
    
    cur = con.cursor()
    cur.execute("CREATE TABLE words (word TEXT)")
    
    try:
        with open(args.path, mode='r', encoding='utf-8') as f:
            populate_db(f,cur)
    except IOError:
        print ("can't open {}".format(args.path))
        exit(1)
        
    print (show_db(cur,10))

def populate_db(f,cur):
    lines=f.readlines()
    for line in lines:
        for i in line.split():
            if len(i)<3:
                continue
            
            cur.execute("INSERT INTO words VALUES('{}')".format(i))


def show_db(cur, limit):
    cur.execute("SELECT word, COUNT(word) as cnt FROM words GROUP BY word ORDER BY cnt DESC LIMIT {}".format(limit))
    results=cur.fetchall()
    return results
            


   
if __name__=='__main__':
    main()
