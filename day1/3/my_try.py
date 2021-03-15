import argparse
import os
import mimetypes

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Walk recursively a path to find media')
    parser.add_argument('path', help='path to traverse')
    
    args = parser.parse_args()
    
    audio = []
    video = []
    image = []
    
   
    for root, dirs, files in os.walk(args.path, topdown=True):
        for name in files:

            try:
                if mimetypes.guess_type(name)[0].find("audio") >= 0:
                    audio.append(name)
                elif mimetypes.guess_type(name)[0].find("video") >= 0:
                    video.append(name)
                elif mimetypes.guess_type(name)[0].find("image") >= 0:
                    image.append(name)
            except AttributeError:
                continue
            
    print("AUDIO FILES:")
    for i in audio:
        print (i)
    print("VIDEO FILES:")
    for i in video:
        print (i)
    print("IMAGE FILES:")
    for i in image:
        print (i)
