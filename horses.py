#!/usr/bin/python
import re
import urllib
from BeautifulSoup import BeautifulSoup as soup

def main():
    gethorsenames()

def gethorsenames():
    ''' this function reads a list of horsenames from file '''
    horsenames="./horsenames.txt"
    horsename=open(horsenames,"r").readlines()
    count=0
    for n in horsename:
        count+=1
        print n
        readhorse(n)

def readhorse(horsename):
    '''  this function reads the primary web page for eachhorse '''
    horsename1 = horsename.replace(" ","+")
    webstring = "http://www.pedigreequery.com/"+horsename1
    horsename=horsename.strip()
    print repr(horsename)
    hsoup = soup(urllib.urlopen(webstring)).findAll(text=re.compile("{2-d} DP =",re.IGNORECASE))
    hsoup2 = soup(urllib.urlopen(webstring)).findAll(text=re.compile("Earnings",re.IGNORECASE))
    #hsoup = soup(urllib.urlopen(webstring))
    hsoup = str(hsoup)
    hsoup2 = str(hsoup2)
    dhorsename = horsename.rstrip()+".txt"
    with open(dhorsename,'w') as webout:
        webout.write(hsoup)
        webout.write(hsoup2)



if __name__ == '__main__':
	main()
