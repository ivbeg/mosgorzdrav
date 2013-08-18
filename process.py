#!/usr/bin/env python
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
                total = '0'
                children = '0'
                if words[0].strip(',').isdigit(): total = words[0].strip(',').strip()
                text2 = text.split(u'к детям', 1)                
                if len(text2) > 1:
                    children = text2[-1].strip(':').strip().strip(';').strip(',')
                ftime.write(('%s|%s|%s|%s\n' %(thedate, total, children, text.strip())).encode('utf8'))
                break
                
    ftime.close()
    f2.close()

def extract_dead():
    f2 = open('extracted.txt', 'r')
    ftime = open('timeseries_dead.csv', 'w')
    ftime.write("thedate|dead|dead_children|text\n")
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
            if t.string.find(u'трупов:') > -1: 
                text = t.string.split(u'трупов:', 1)[1]
                words = text.split()
                total = '0'
                children = '0'
                if words[0].strip(',').isdigit(): total = words[0].strip(',').strip()
                if total == '-': total = '0'
                text2 = text.split(u'детей:', 1)                
                if len(text2) > 1:
                    children = text2[-1].strip(':').strip().strip(';').strip(',').strip('.').strip()
                    if children == '-': children = '0'
                ftime.write(('%s|%s|%s|%s\n' %(thedate, total, children, text.strip())).encode('utf8'))
                break
                
    ftime.close()
    f2.close()
    
def extract_hosp():
    f2 = open('extracted.txt', 'r')
    ftime = open('timeseries_hosp.csv', 'w')
    ftime.write("thedate|hosp|hosp_children|text\n")
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
            if t.string.find(u'госпитализировано') > -1: 
                text = t.string.split(u'госпитализировано', 1)[1].strip(':')
                words = text.split()
                total = '0'
                children = '0'
                if words[0].strip(',').isdigit(): total = words[0].strip(',').strip()
                if total == '-': total = '0'
                text2 = text.split(u'детей:', 1)                
                if len(text2) > 1:
                    children = text2[-1].strip(':').strip().strip(';').strip(',').strip('.').strip()
                    if children == '-': children = '0'
                ftime.write(('%s|%s|%s|%s\n' %(thedate, total, children, text.strip())).encode('utf8'))
                break
                
    ftime.close()
    f2.close()

def extract_hosp2():
    f2 = open('extracted.txt', 'r')
    ftime = open('timeseries_hosp2.csv', 'w')
    ftime.write("thedate|total_hosp|text\n")
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
            if not t.string: break
            if t.string.find(u'на госпитализацию') > -1: 
                text = t.string.split(u'на госпитализацию', 1)[1].strip(':')
                words = text.split()
                total = '0'
                children = '0'
                try:
        	    total = words[0].strip(',').strip()
                except:
            	    total = ''
                if not total.isdigit(): continue
                if total == '-': total = '0'
                ftime.write(('%s|%s|%s\n' %(thedate, total, text.strip())).encode('utf8'))
                break
                
    ftime.close()
    f2.close()



if __name__ == "__main__":
#    extract_stats()
#    extract_dead()
#    extract_hosp()
    extract_hosp2()
    