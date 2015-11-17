# -*- coding: UTF-8 -*-
import xml.etree.ElementTree as ET
import sys, os

if __name__ == '__main__':
	count = 1
	if len(sys.argv) >= 3:
		docsDir = sys.argv[1]
		files = sys.argv[2:]
		# print keywords
		for filename in files:
			tree = ET.parse(os.path.join(docsDir, filename+".xml"))
			root = tree.getroot()
			# contain = True
			print count,root[0].attrib['title']
			count+=1
			# if root[0][0].text != None:
					# print root[0][0].text
			# for keyword in keywords:
				# if keyword.decode('utf8') not in root[0].attrib['title'].rstrip('\n'):
				# 	contain = False
			# 	if root[0][0].text != None:
			# 		if keyword.decode('utf8') not in root[0][0].text:
			# 			contain = False
			# if contain == True:
			# 	print filename
	else:
		print "Please use like 'python filter.py [Docs_Dir] [filterKeyword] [] [] [] []........'"
