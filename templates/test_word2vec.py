# -*- coding:utf-8 -*-

import gensim

model = gensim.models.Word2Vec.load("../model/wiki.zh.text.model")

match_list = model.most_similar(''.decode('utf-8'))
for each in match_list:
    print each[0], each[1]
print (model[u'中国'], model[u'北京'])
print (model.wv.similarity(u'中国', u'北京'))
print (model.wv.similarity(model[u'中国'], model[u'北京']))

