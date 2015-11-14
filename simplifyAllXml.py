# -*- coding: UTF-8 -*-
import xml.etree.ElementTree as ET
import glob
import opencc
import os


def simplify(text):
 return opencc.convert(text, config='t2s.json')

def traditionalize(text):
 return opencc.convert(text, config='zhs2zht.ini').encode('utf8')


files = glob.glob('./data/news_story_dataset/*.xml')

for file_xml in files:
	print os.path.basename(file_xml)
	tree = ET.parse(file_xml)
	root = tree.getroot()
	# print simplify(root[0].attrib['title'])
	# print os.path.basename(file_xml)
	root[0].attrib['title'] = simplify(root[0].attrib['title'].rstrip('\n'))
	# print root[0].attrib['title']
	
	if root[0][0].text != None:
		root[0][0].text = simplify(root[0][0].text.rstrip('\n'))
	# with open('./data/news_output_simplifiedChinese/' + os.path.basename(file_xml), 'w') as f:
	tree.write('./data/news_output_simplifiedChinese/' + os.path.basename(file_xml))
	# for child in root:
		# print child.attrib['title']


