# IR_HW1

## Dependency
Install these module before run it.
* numpy(`pip install numpy`, [github](https://github.com/numpy/numpy))
* gensim(`pip install -U gensim`, [github](https://github.com/piskvorky/gensim/))
* jieba(`pip install jieba`, [github](https://github.com/fxsjy/jieba))
* opencc(`brew install opencc` or download it on github and then run `make`, `sudo make install`, [github](https://github.com/BYVoid/OpenCC))
* python-dateutil(`pip install python-dateutil`, [github](https://github.com/dateutil/dateutil))

## Run it
`python sim.py [originDocs_Dir] [outputDocs_Dir] [queryFile] [resultFileName]`

* originDocs_Dir : 解壓縮training data的Folder
* outputDocs_Dir : 存入簡體字的Folder，請先建立好。
* queryFile : Query的file位置
* resultFileName : 最終輸出File的名稱(e.g: result.csv)
