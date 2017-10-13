# -*- coding: utf-8 -*-

# 文本分词
import codecs
import jieba
from gensim.models.word2vec import LineSentence, Word2Vec

def del_word_not_in_dictionary(list, model):
    while '' in list:
        list.remove('')
    del_list = []
    for word in list:
        try:
            model[word]
        except KeyError:
            del_list.append(word)
    for w in del_list:
        list.remove(w)
    return list

def get_sentence_similarity(list1, sentence2, model):
    # 分词
    list2 = list(jieba.cut(sentence2, cut_all=True))
    # list去除空元素
    while '' in list1:
        list1.remove('')
    while '' in list2:
        list2.remove('')
    list_sim = model.n_similarity(list1, list2)
    return list_sim



i_file = open('./data/wrod2vec_train_data.txt')
o_file = codecs.open('./data/tmp_data.txt', 'w', encoding='utf-8')
sentence_list = []
for line in i_file:
    seg_list = jieba.cut(line, cut_all=True)
    tmp = " ".join(seg_list)
    o_file.write(tmp)
o_file.close()
# 训练模型
# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
model = Word2Vec(LineSentence('./data/tmp_data.txt'), min_count=1, window=5)
sentence_obama = '鸭蛋瓦塔丝袜放射科的eRad登记工作站中，我点那个申请单按钮的时候，出错了，屏幕显示，需要启动视频设备'
sentence_president = '放射科的eRad登记工作站中点申请单按钮显示：请启动视频设备'
sentence3 = '对于一些医生误删掉病程记录的'
list1 = list(jieba.cut(sentence_obama, cut_all=True))
list2 = list(jieba.cut(sentence_president, cut_all=True))
list3 = list(jieba.cut(sentence3,cut_all=True))
distance1 = model.wmdistance(list1, list2)
distance2 = model.wmdistance(list2, list3)
print (distance1)
print (distance2)
del_word_not_in_dictionary(list2, model)
clean_list = del_word_not_in_dictionary(list=list1, model=model)
sim = get_sentence_similarity(list1=clean_list, sentence2='虚拟机死机，操作不了的', model=model)
print (sim)
# tmp_file = open('./data/train_data.txt')
# for line in tmp_file:
#     line = line.strip('\n')
#     lst = list(jieba.cut(line, cut_all=True))
#     while '' in lst:
#         lst.remove('')
#     print ('list1:{0}'.format(lst).decode('utf-8'))
#     print ('list2:{0}'.format(list1).decode('utf-8'))
#     print ('distance:{0}'.format(model.wmdistance(lst, list2)))


