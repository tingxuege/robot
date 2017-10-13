# -*- coding:utf-8 -*-
import aiml
import os
import jieba

from train_corpus import training_vec


def find_most_similarity_sentence(message, train_model):
    sentence = train_model.most_similarity_sentence\
        (sentence=message, sentence_list=train_model.get_sentence_list())
    return sentence

def seq_and_AIML_response(message):
    seg_list = jieba.cut(message, cut_all=True)
    seq_message = " ".join(seg_list)
    response = kernel.respond(seq_message)
    return response


kernel = aiml.Kernel()
seg_list = jieba.cut("加载中", cut_all=True)
train_model = ''
if os.path.isfile("bot_brain.brn"):
    # kernel.bootstrap(brainFile = "bot_brain.brn")
    kernel.bootstrap(learnFiles=os.path.abspath("aiml/std-startup.xml"), commands="load aiml b")
    kernel.saveBrain("bot_brain.brn")
    # 加载word2vec，训练词向量
    train_model = training_vec(input='./data/wrod2vec_train_data.txt', output='./data/seg_train_data.txt',
                               model='./model/software.model', vec_model='./model/software_bin.model',
                               sentence_model='./data/train_data.txt')
    train_model.sentence2vec()
else:
    kernel.bootstrap(learnFiles = os.path.abspath("aiml/std-startup.xml"), commands = "load aiml b")
    kernel.saveBrain("bot_brain.brn")

# kernel now ready for use
while True:
    message = raw_input("Enter your message to the bot: ")
    if message == "quit":
        exit()
    elif message == "save":
        kernel.saveBrain("bot_brain.brn")
    else:
        # 先匹配寒暄语句，不进行断句
        origin_message = message
        command_respose = kernel.respond(message)
        if command_respose == 'not match':
            seg_list = jieba.cut(message, cut_all=True)
            message = " ".join(seg_list)
            bot_response = kernel.respond(message)
            if bot_response == 'not match':
                most_similarity_sentence = find_most_similarity_sentence\
                    (message=origin_message, train_model=train_model)
                if most_similarity_sentence == '':
                    bot_response = '我不太明白你说的是什么？或者换种方式再问一下吧。'
                else:
                    second_message = raw_input('请问您问的是不是:'+most_similarity_sentence+'?')
                    second_reponse = kernel.respond(second_message)
                    if second_reponse == 'YES':
                        # 长句先分词再放进AIML中匹配模板
                        bot_response = seq_and_AIML_response(most_similarity_sentence)
                    else:
                        bot_response = kernel.respond('error match')

        else:
            bot_response = kernel.respond(message)
        print (bot_response)
