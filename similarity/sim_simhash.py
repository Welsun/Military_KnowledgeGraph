#!/usr/bin/env python3
# coding: utf-8
# File: sim_simhash.py
# Author: lhy<lhy_in_blcu@126.com,https://huangyong.github.io>
# Date: 18-4-27

from simhash import Simhash
import jieba.posseg as pseg
from mongodb_models import Mongo

class SimHaming:
    '''利用64位数，计算海明距离'''
    def haming_distance(self, code_s1, code_s2):
        x = (code_s1 ^ code_s2) & ((1 << 64) - 1)
        ans = 0
        while x:
            ans += 1
            x &= x - 1
        return ans
    '''利用相似度计算方式,计算全文编码相似度'''
    def get_similarity(self, a, b):
        if a > b :
            return b / a
        else:
            return a / b

    '''对全文进行分词,提取全文特征,使用词性将虚词等无关字符去重'''
    def get_features(self, string):
        word_list=[word.word for word in pseg.cut(string) if word.flag[0] not in ['u','x','w','o','p','c','m','q']]
        return word_list

    '''计算两个全文编码的距离'''
    def get_distance(self, code_s1, code_s2):
        return self.haming_distance(code_s1, code_s2)

    '''对全文进行编码'''
    def get_code(self, string):
        return Simhash(self.get_features(string)).value

    '''计算s1与s2之间的距离'''
    def distance(self, s1, s2):
        code_s1 = self.get_code(s1)
        code_s2 = self.get_code(s2)
        similarity = (100 - self.haming_distance(code_s1,code_s2)*100/64)/100
        return similarity

def test():
    simer = SimHaming()
    text1="中国的人口是多少"
    client = Mongo().connectDB()
    col = client["questions_data"]
    max_similarity=0
    max_id=""
    for question in col.find():
        similarity = simer.distance(text1,question["question"])
        if similarity > max_similarity:
            max_similarity=similarity
            max_id=question["_id"]
        print(similarity)
    question = col.find_one({"_id":max_id})
    print(question)



test()