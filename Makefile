#phase 1
test:
	python sim.py \
	data/news_story_dataset/ \
	data/simplicity \
	data/query_story.xml \
	phase1_result.csv	

all:
	sudo apt-get install python-pip
	sudo pip install numpy
	sudo apt-get install liblapack-dev
	sudo apt-get install gfortran
	sudo pip install --upgrade gensim
	sudo pip install jieba
	sudo pip install python-dateutil
	sudo apt-get install opencc

clean:
	rm -f *.pyc
	rm -f *.csv