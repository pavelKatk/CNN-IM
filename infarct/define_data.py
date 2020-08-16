from IPython.display import display 
from wfdb import processing 
import numpy as np 
import shutil 
import wfdb 
import tools as st
import os

def definition_data():
	diagnosis = []
	records = []
	input = open('records.txt', 'r')
	for line in input:
		line = line.replace("\n","")
		arr = line.split('/')
		_, fields = wfdb.rdsamp(arr[1], pb_dir='ptbdb/' + arr[0] + '/') 
		if 'Healthy control' in fields['comments'][4]:
			diagnosis.append(1)
			records.append(line)
		if 'Myocardial infarction' in fields['comments'][4]:
			if 'inferior' in fields['comments'][5]:
				diagnosis.append(0)
				records.append(line)
	f = open('upd_records.txt','w')
	ff = open('diagnosis.txt','w')
	f.write("\n".join([str(x) for x in records]))
	ff.write("\n".join([str(x) for x in diagnosis]))
	f.close()
	ff.close()
