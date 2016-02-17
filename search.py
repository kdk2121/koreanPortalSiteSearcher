# #-*- coding: utf-8 -*-
import mechanize
import urllib2
import sys
from bs4 import BeautifulSoup


def search(x):

	for i in range (0,100):
		if x == 0 :
			name = '구글'
			url = 'https://www.google.co.kr/search?q=' + sys.argv[1] + '&espv=2&biw=1080&bih=778&ei=0fTDVsuXDMi10ASy14D4Bw&start=' + str(i) + '0&sa=N'
		elif x == 1:
			name = '네이버'
			url = 'https://search.naver.com/search.naver?display=10&doc_sources=&ie=utf8&nso=&qdt=&query=' + sys.argv[1] + '&qvt=&sm=tab_pge&sort=1&source=0&srcharea=0&start=' + str(i) + '1&where=site'
		elif x == 2:
			name = '다음'
			url = 'http://search.daum.net/search?nil_suggest=btn&w=site&DA=PGD&q=' + sys.argv[1] + '&page=' + str(i)
		#create a browser object to login
		browser = mechanize.Browser()
		#tell the browser we are human, and not a robot, so the mechanize library doesn't block us
		browser.set_handle_robots(False)
		browser.addheaders = [('User-Agent','Mozilla/5.0 (Windows U; Windows NT 6.0; en-US; rv:9.0.6')]
		#open the url in our virtual browser
		browser.open(url)
		html = browser.response().read()
		if sys.argv[2] in html:
			print (name)
			return str(i) + '페이지' + '\n' + url
		
	print (name)
	return '검색결과에 없습니다'

for x in range (0,3):
	print(search(x))

