import argparse
import os.path
import zipfile


def zip_all(dest,src):
    print(f"ZIP TO {dest}, {src}")
    zf = zipfile.ZipFile(dest, mode='w')
    for f in src:
        print(f"Adding {f}...")
        zf.write(f)
    
    print("closing..")
    zf.close()
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Zip all the file given in the first argument passed')
    
    parser.add_argument('zipfile', help='destination zip file')
    parser.add_argument('srcfile', help='files to be zipped', nargs='+')
    
    args=parser.parse_args()
    
    print(args)
    print(args.srcfile)

    for i in args.srcfile:
        if os.path.isfile(i) == False:
            print (f"file {i} does not exist")
            exit(1)
    
    overwrite=''
    if os.path.isfile(args.zipfile):
        while (overwrite != 'Y' and overwrite != 'N'):
            print(f"File {args.zipfile} already exists, overwrite? [Y,N]")
            overwrite = input()
            overwrite = overwrite.upper()
    
    if overwrite=='N':
        exit(0)
    else:
        zip_all(args.zipfile,args.srcfile)
        
        
        
