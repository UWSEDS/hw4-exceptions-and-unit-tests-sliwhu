import os
import urllib.request as ur

def get_data(url):
    try:
        filename=url.split('/')[-1]
        if os.path.exists(filename):
            print ("File exists, skipping download")
            return False
        file=ur.urlopen(url)        
        with open(filename, 'wb') as output:
            output.write(file.read())
            print (filename, "succesfully downloaded")
            return True
    except:
        print ('Invalid url')
        return False

def remove_data(url):
    try:
        filename=url.split('/')[-1]
        if os.path.exists(filename):
            os.remove(filename)
            print ("File exists, successfully removed.")
            return True
        else:
            print ('File does not exist.')
            return False
    except:
        print ('Invalid url')