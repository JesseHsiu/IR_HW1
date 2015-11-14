# -*- coding: UTF-8 -*-
import jieba
import jieba.analyse
import xml.etree.ElementTree as ET
import glob
import os
import codecs
files = glob.glob('./data/news_output_simplifiedChinese/*.xml')

for file_xml in files:
	print os.path.basename(file_xml)
	tree = ET.parse(file_xml)
	root = tree.getroot()
	
	title_cuts = jieba.cut(root[0].attrib['title'], cut_all=True)
	seg_list = jieba.cut(root[0][0].text, cut_all=True)

	with codecs.open('./data/news_cuts/' + os.path.basename(file_xml), "w", "utf-8") as f:
		# Get news title.
		for title in title_cuts:
			if title != '':
				f.write(title)
				f.write(',')
		# Content : if there is no content then skip.
		if root[0][0].text != None:
			for seg in seg_list:
				if seg !='':
					f.write(seg)
					f.write(',')
		f.closed		