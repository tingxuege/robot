# -*- coding: utf-8 -*-

import logging

import jieba
import codecs
from gensim.models.word2vec import LineSentence, Word2Vec

class training_vec:
    input_file = ''
    output_file = ''
    model_path = ''
    vec_model = ''
    model = ''
    sentence_model = ''
    def __init__(self, input, output, model, vec_model, sentence_model):
        # 语料库路径配置
        self.input_file = input
        self.output_file = output
        self.model_path = model
        self.vec_model = vec_model
        self.model = ''
        self.sentence_model = sentence_model


    def sentence2vec(self):
        # 文本分词
        i_file = open(self.input_file)
        o_file = codecs.open(self.output_file, 'w', encoding='utf-8')

        for line in i_file:
            seg_list = jieba.cut(line, cut_all=True)
            tmp = " ".join(seg_list)
            o_file.write(tmp)
        o_file.close()
        # 训练模型
        # logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
        model = Word2Vec(LineSentence(self.output_file), min_count=1, window=5)
        # 保存模型
        model.save(self.model_path)
        model.wv.save_word2vec_format(self.vec_model, binary=True)
        self.model = model


    def get_match_word(self, word):
        match_list = self.model.most_similar(word)
        for each in match_list:
            print each[0], each[1]

    def del_word_not_in_dictionary(self, list):
        while '' in list:
            list.remove('')
        del_list = []
        for word in list:
            try:
                self.model[word]
            except KeyError:
                del_list.append(word)
        for w in del_list:
            list.remove(w)
        return list

    def get_sentence_similarity(self, sentence1, sentence2):
        # 分词
        list1 = list(jieba.cut(sentence1, cut_all=True))
        list2 = list(jieba.cut(sentence2, cut_all=True))
        # list去除空元素
        while '' in list1:
            list1.remove('')
        while '' in list2:
            list2.remove('')
        list_sim = self.model.n_similarity(list1, list2)
        return list_sim

    def get_sentence_similarity_clear(self, sentence1, sentence2):
        # 分词
        tmp_list1 = list(jieba.cut(sentence1, cut_all=True))
        list2 = list(jieba.cut(sentence2, cut_all=True))
        list1 = self.del_word_not_in_dictionary(list=tmp_list1)
        if list1:
            # list去除空元素
            while '' in list1:
                list1.remove('')
            while '' in list2:
                list2.remove('')
            list_sim = self.model.n_similarity(list1, list2)
            return list_sim
        else:
            return -1


    def get_sentence_list(self):
        sentence_list = []
        i_file = open(self.sentence_model)
        for line in i_file:
            line = line.strip('\n')
            sentence_list.append(line)
        return sentence_list

    def most_similarity_sentence(self, sentence, sentence_list):
        score_dict = {}
        index = 0
        for sen in sentence_list:
            score_dict[index] = self.get_sentence_similarity_clear(sentence1=sentence, sentence2=sen)
            index += 1
        sort_dict = sorted(score_dict.iteritems(), key=lambda d: d[1], reverse=True)
        # 如果最高得分是-1，说明了list1是空的
        if sort_dict[0][1] == -1:
            return ''
        else:
            return sentence_list[sort_dict[0][0]]
