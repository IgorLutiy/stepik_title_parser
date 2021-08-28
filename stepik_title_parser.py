from bs4 import BeautifulSoup
import requests
import time

def stepik_parser_kursi_loop():
        start = int(input('Введите начальное число: ')) #начальное число в адресе, с которого будем начинать парсинг
        number = int(input('Введите конечное число: ')) #конечное число в адресе, с которого будем начинать парсинг
        text_file = open('stepik.txt', 'a', encoding='utf-8')
        for i in range(start, number+1):
        	url = 'https://stepik.org/course/' + str(i) + '/promo'
        	hdr = {'User-Agent': 'Mozilla/5.0'}
        	r = requests.get(url, headers=hdr)
        	soup = BeautifulSoup(r.text, 'lxml')
        	title = soup.find('h1', attrs={'class': 'course-promo__header'})
        	leaners = soup.find('div', attrs={'class': 'course-promo-summary__students'})
        	if title != None and leaners != None:
        		try:
        			text_file.write(url + '\n') #пишем в файл адрес
        			text_file.write(title.get_text() + '\n') #пишем в файл название курса
        			text_file.write(leaners.get_text().strip() + '\n') #пишем в файл количество учащихся
        		except:
        			print('error')
        		time.sleep(1)
        	if i%100 == 0: 
        		print(i) #смотрим, сколько урлов уже прошло, выводится число кратное 100
        return True

stepik_parser_kursi_loop()
