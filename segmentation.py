# -*- coding:utf-8 -*-
import codecs

import jieba

# jieba.load_userdict("./dictionary/dict_all.txt")

# 文本分词
i_file = open('./data/train_data.txt')
o_file = codecs.open('./data/seg_train_data.txt', 'w', encoding='utf-8')

for line in i_file:
    seg_list = jieba.cut(line, cut_all=False)
    tmp = " ".join(seg_list)
    o_file.write(tmp)
o_file.close()