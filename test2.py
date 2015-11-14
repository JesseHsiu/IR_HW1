# -*- coding: UTF-8 -*-
import logging
from gensim import corpora, models, similarities
from collections import defaultdict

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


documents = ["政府原本希望公布高薪的一百家企業藉以帶動企業加薪風氣，但全國自主勞工聯盟執行長朱維立認為，這只是政府為了吹捧少數企業，想要帶動企業加薪風氣仍相當困難，高薪與加薪未必有連動效應。朱維立更指出，政府不要報喜不報憂，很多企業看似員工有高薪，但其實存在許多勞資爭議的狀況，也有勞動條件不佳的情形，不乏血汗換高薪；公布高薪一百企業，並無法解決勞資爭議的問題，政府應該更全面性去了解及公布企業各種勞動條件、爭端與待遇問題。",
             "二二八連假第一天，鐵公路運輸都爆出狀況，國道「塞爆」，鐵道則是「等爆」，數十萬民眾怨聲連連；朝野立委痛責交通部長葉匡時規劃不當、應變不及，要負全責。昨天陽光普照，國道全線湧現一百九十六萬輛次，早上六點半國道五號就出現車潮，台北到宜蘭平常五十分鐘可達，結果卻塞了三小時才到；各遊樂園附近更是從早上八點就大塞車，新竹以北國道塞得最嚴重，關西交流道宛如大型停車場，民眾大呼掃興。國道塞，搭火車的民眾更碰上連假史上最大斷線事件。上午八時許一列由田中開往花蓮的太魯閣號，行經中壢、埔心間時，車頂集電弓勾到電車線的三角架，一下扯掉了卅座電車線的三角架，不但列車失去電力，也導致行車秩序大亂，全天共一百一十八列車受影響，平均誤點逾一小時，至少耽誤五萬七千位旅客。交通部昨天沒人願意出面談責任歸屬，部長葉匡時只以簡訊回覆「在忙」，並指「鐵路問題問鐵路局，國道問題問次長」。民進黨立委蔡其昌痛罵，昨天全台交通主動脈「高速公路」塞到微血管「地方道路」，鐵路、空運也接連出包，葉匡時躲起來納涼，塞車之苦卻要民眾吞下。逢甲大學運管系副教授李克聰說，交通部太小看二二八公路車流，誤判「春節剛過不至於有大批車潮」，預測車輛數也失準，事實上昨天車潮並非事先預期的「都會型」、「地區型」車流，而是有不少中長程車流也上路，輸運出包，決策者要負最大責任。李克聰說，高公局根本不懂得eTag已能掌握用路人的「起迄點」，將部分有景點或人口聚集的交流道視為熱點，以差別費率方式分散到其他交流道，就可降低多車路段壓力，交通部卻都沒有做。親民黨立委陳怡潔表示，交通部的危機處理已經讓人民失去信任，葉匡時身為政務官理應知所進退！交通部常務次長陳建宇表示，國道車潮確實超過預估，台鐵已盡全力搶修，事故責任仍待釐清，交通部會深切檢討，給民眾一個交代。",
             "The EPS user interface management system",
             "System and human system engineering testing of EPS",
             "Relation of user perceived response time to error measurement",
             "The generation of random binary unordered trees",
             "The intersection graph of paths in trees",
             "Graph minors IV Widths of trees and well quasi ordering",
             "Graph minors A survey"]

stoplist = set('for a of the and to in'.split())
texts = [[word for word in document.lower().split() if word not in stoplist] for document in documents]

frequency = defaultdict(int)

dictionary = corpora.Dictionary.load('/usr/local/lib/python2.7/site-packages/jieba/dict.txt')

for text in texts:
    for token in text:
        frequency[token] += 1

texts = [[token for token in text if frequency[token] > 1]
         for text in texts]

from pprint import pprint   # pretty-printer
pprint(texts)