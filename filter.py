# -*- coding: UTF-8 -*-
import xml.etree.ElementTree as ET
import sys, os

if __name__ == '__main__':
	if len(sys.argv) >= 3:
		docsDir = sys.argv[1]
		keywords = sys.argv[2:]
		# print keywords
		for filename in os.listdir(docsDir):
			tree = ET.parse(os.path.join(docsDir, filename))
			root = tree.getroot()
			contain = True

			for keyword in keywords:
				# if keyword.decode('utf8') not in root[0].attrib['title'].rstrip('\n'):
				# 	contain = False
				if root[0][0].text != None:
					if keyword.decode('utf8') not in root[0][0].text:
						contain = False

			if contain == True:
				print filename

			# print root[0].attrib['title'].rstrip('\n')
			


	else:
		print "Please use like 'python filter.py [Docs_Dir] [filterKeyword] [] [] [] []........'"
