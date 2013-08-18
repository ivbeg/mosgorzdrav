#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys, os, urllib, urllib2, urlparse, os.path
from BeautifulSoup import BeautifulSoup, BeautifulStoneSoup

BASE_URL = "http://www.mosgorzdrav.ru/mgz/komzdravsite.nsf/va_WebPages/sys_DigitsList_%d"
NUM_LIST_PAGES = 296

def generate_list():
    f = open('pagelist.txt', 'w')
    f.write('thedate|text|url\n')
    for n in range(1, NUM_LIST_PAGES + 1, 1):
        url = BASE_URL % n
        u = urllib2.urlopen(url)
        data =  u.read()
        u.close()
        print url
        page = BeautifulSoup(data)
        all = page.findAll('a', attrs={'class': 'heading'})
        for o in all:        
            thedate = o.findPreviousSibling('span').string.encode('utf8')
            f.write('%s|%s|%s\n' %(thedate, o.string.encode('utf8'), urlparse.urljoin(url, o['href'].encode('utf8'))))
    f.close()


def extract_content():
    f = open('pagelist.txt', 'r')
    f2 = open('extracted.txt', 'w')
    f2.write('thedate|text|url|filename\n')
    i = 0
    for l in f:
        l = l.strip()
        i += 1
        if i == 1: continue 
#        print i       
        thedate, text, url = l.split('|')
        print url
        id = url.rsplit('/', 1)[1]
        id = id.split('?', 1)[0]
        if id.find('_') > -1:
            id = id.split('_', 1)[1]
        filename = id + '.html'
        if os.path.exists('data/' + filename): 
            f2.write(l + '|' + filename.encode('utf8') + '\n')
            continue
        u = urllib2.urlopen(url)
        data =  u.read()
        u.close()
        page = BeautifulSoup(data)
        body = page.find('div', attrs={'class': 'news_body'})        
        fsave = open('data/' + filename, 'w')
        fsave.write(unicode(body).encode('utf8'))
        fsave.close()
        f2.write(l + '|' + filename.encode('utf8') + '\n')
    f2.close()
    f.close()
    


if __name__ == "__main__":
#    generate_list()
    extract_content()
    