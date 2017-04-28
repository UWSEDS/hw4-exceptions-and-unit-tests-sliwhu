#303 means url valid, but file exists
#304 means url valid, file not exist
#305 means url invalid

import os
import urllib.request as ur
import sys

def get_data(url):

    filename=url.split('/')[-1]
    if os.path.exists(filename):
        print ("File exists, skipping download")
        return 303
    try:
        file=ur.urlopen(url)        
        with open(filename, 'wb') as output:
            output.write(file.read())
            print (filename, "succesfully downloaded")
            return 304
    except:
        print (sys.exc_info()[1])
        return 305

def remove_data(url):
    filename=url.split('/')[-1]
    try:
        file=ur.urlopen(url)  
        
        if os.path.exists(filename):
            os.remove(filename)
            print ("File exists, successfully removed.")
            return 303
        else:
            print ('File does not exist.')
            return 304
    except:
        print (sys.exc_info()[1])
        return 305