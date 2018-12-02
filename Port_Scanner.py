'''
# Python Port Scanner Automation #
# 개발일 / 버전 : `18.12.02 / V 1.0  #
# 아이디어, 개발 : zeromini #
'''

import os
import nmap
import sys
import csv
from threading import *
import pandas as pd

global result


def main():
	print('port Scanning')


def file_read_scan():
	#print('test')
	try:
		r = open ('c:/iplist.txt', mode='rt')
		f = open ('c:/result.csv','w')
		read_result = [line.split('\n') for line in r.readlines()]
		r.close()
		f.close()
		nm = nmap.PortScanner()

		for i in read_result:
			print('Scanning Ip Address : '+i[0])
			ip_put = str(line.replace('\n',''))
			result = nm.scan(hosts=i[0], ports='20-443', arguments='-sV')
			with open('c:/result.csv','a') as f:		
				f.writelines(nm.csv())

	except:
		pass


'''
nm = nmap.PortScanner()
result = nm.scan(hosts='127.0.0.1', ports='20-443',arguments='-sV')

print(nm.csv())

with open('result.csv','w') as f:
	f.writelines(nm.csv().replace(';',','))
'''

if __name__ == '__main__':
    	file_read_scan()
    	excel_result = pd.read_excel('c:/result.csv') 
    	excel_split_result = excel_result.str.split(';', expand=True)
    