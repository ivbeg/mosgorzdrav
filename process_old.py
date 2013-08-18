# -*- coding: utf8 -*-
import sys, os, urllib, urllib2, urlparse
from BeautifulSoup import BeautifulSoup, BeautifulStoneSoup

BASE_URL = "http://www.mosgorzdrav.ru/mgz/komzdravsite.nsf/va_WebPages/sys_DigitsList_%d"
NUM_LIST_PAGES = 231


def extract_stats():
    f2 = open('extracted.txt', 'r')
    ftime = open('timeseries.csv', 'w')
    ftime.write("thedate|num_rides|num_childrides|text\n")
    i = 0
    for l in f2:
        l = l.strip()
        i += 1
        if i == 1: continue        
        thedate, text, url, filename = l.split('|')
        print url
        fsave = open('data/' + filename, 'r')
        page = BeautifulSoup(fsave.read())
        fsave.close()
        texts = page.findAll('font')
        for t in texts:
            if t.string.find(u'Всего выездов:') > -1: 
                text = t.string.split(u'Всего выездов:', 1)[1]
                words = text.split()
                total = 'N/A'
                children = 'N/A/'
                if words[0].strip(',').isdigit(): total = words[0].strip(',').strip()
                text2 = text.split(u'к детям', 1)                
                if len(text2) > 1:
                    children = text2[-1].strip(':').strip().strip(';').strip(',')
                ftime.write(('%s|%s|%s|%s\n' %(thedate, total, children, text.strip())).encode('utf8'))
                break
                
    ftime.close()
    f2.close()
    


if __name__ == "__main__":
    extract_stats()
    