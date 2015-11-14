# -*- coding: UTF-8 -*-
import jieba
import jieba.analyse

seg_list = jieba.cut_for_search("政府原本希望公布高薪的一百家企业藉以带动企业加薪风气，但全国自主劳工联盟执行长朱维立认为，这只是政府为了吹捧少数企业，想要带动企业加薪风气仍相当困难，高薪与加薪未必有连动效应。朱维立更指出，政府不要报喜不报忧，很多企业看似员工有高薪，但其实存在许多劳资争议的状况，也有劳动条件不佳的情形，不乏血汗换高薪；公布高薪一百企业，并无法解决劳资争议的问题，政府应该更全面性去了解及公布企业各种劳动条件、争端与待遇问题。")  # 搜索引擎模式
print(", ".join(seg_list))

# jieba.set_dictionary('data/dict.txt.big.txt')

# sentance = "小儿呱呱坠地，新手父母兴奋地迎接新生命的到来，却又担心孩子的发育是否正常。新生儿时期，幼儿除了喝奶，多半在睡，不易评估，此时可以感受孩子吸吮是否有力，会不会常呛奶，四肢活动是否对称。渐渐地，孩子清醒的时间变多，与家人的互动变频繁，3个月大以前，孩子会看人、微笑及转头找声源；4到5个月大，脖子可以挺直，七坐八爬十站、1岁走路，若到1岁3个月还不会放手走路，应转介专科医师评估是否有运动迟缓。部分正常的孩子未经爬行就会走路。1岁以前若有偏好一侧的情形，少动的那边可能有问题。细动作方面，正常婴儿的手是自然张开的，4个月后如过度握拳不张，须进一步评估。6个月大会拨开盖脸的手帕，7、8个月大会抓东西往嘴送，此时也是开始长牙的阶段。9个月以前会换手拿东西、拍拍手，11个月大的时候会用拇指和食指捏起小东西，1岁左右会用笔涂鸦和撕纸。语言是认知行为发展重要的指标。2、3个月大的婴儿开始有社交性的微笑，会咕咕作声，追寻行动中的物体。7个月大后会发出无实际意义的巴巴或搭搭的声音，1岁左右开始有意义的叫爸妈。若1岁半时仍无有意义的单字，应请专科医师评估。脱离婴儿时期，孩子的步态渐稳，开始会快走；2岁以前会扶栏杆自己上下楼梯、双脚跳；3岁单脚站；4岁单脚跳；5岁两脚交换跳。细动作方面，2岁会翻书；3岁画直线；4岁画圆圈；5岁画X；6岁画三角形。语言方面，2岁以前至少应会说双字词；3岁会说句子；4岁会说自己的名字，正确使用代名词「你的」「我的」及说出性别；5岁能认颜色；6岁能排数字卡。社会行为方面，2岁以前会自己脱衣服；3岁会穿脱没有鞋带的鞋子，用汤匙喝汤；4岁会自己穿衣服；5岁能自己穿裤子；6岁能拉上或解开拉鍊，并学会遵守简单的游戏规则。然而孩子总有发展快慢的差异性。一般而言，可观察2至6个月，如孩子的能力虽微幅落后，但慢慢赶上，就可较为放心，否则须寻求专家诊断治疗。台大医院小儿部小儿神经科主治医师范碧娟"

# seg_list = jieba.cut(sentance, cut_all=True)
# print("Full Mode: " + "/ ".join(seg_list))  # 全模式


# tags = jieba.analyse.extract_tags(sentance, topK=20)

# print(",".join(tags))

# words = pseg.cut("我来到了黄金海岸")
# for word, flag in words:
# 	print('%s %s' % (word, flag))

# seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
# print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

# seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
# print(", ".join(seg_list))

# seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
# print(", ".join(seg_list))
# -*- coding: UTF-8 -*-
# from __future__ import unicode_literals
# import sys,os
# sys.path.append("../")
# from whoosh.index import create_in,open_dir
# from whoosh.fields import *
# from whoosh.qparser import QueryParser

# from jieba.analyse import ChineseAnalyzer

# analyzer = ChineseAnalyzer()

# schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT(stored=True, analyzer=analyzer))
# if not os.path.exists("tmp"):
#     os.mkdir("tmp")

# ix = create_in("tmp", schema) # for create new index
# #ix = open_dir("tmp") # for read only
# writer = ix.writer()

# writer.add_document(
#     title="document1",
#     path="/a",
#     content="This is the first document we’ve added!"
# )

# writer.add_document(
#     title="document2",
#     path="/b",
#     content="The second one 你 中文测试中文 is even more interesting! 吃水果"
# )

# writer.add_document(
#     title="document3",
#     path="/c",
#     content="买水果然后来世博园。"
# )

# writer.add_document(
#     title="document4",
#     path="/c",
#     content="工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作"
# )

# writer.add_document(
#     title="document4",
#     path="/c",
#     content="咱俩交换一下吧。"
# )

# writer.commit()
# searcher = ix.searcher()
# parser = QueryParser("content", schema=ix.schema)

# for keyword in ("水果世博园","你","first","中文","交换机","交换"):
#     print("result of ",keyword)
#     q = parser.parse(keyword)
#     results = searcher.search(q)
#     for hit in results:
#         print(hit.highlights("content"))
#     print("="*10)

# for t in analyzer("我的好朋友是李明;我爱北京天安门;IBM和Microsoft; I have a dream. this is intetesting and interested me a lot"):
#     print(t.text)