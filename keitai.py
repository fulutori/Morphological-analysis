# coding: utf-8
import MeCab
import sys

def wether(text):
	#textを形態素解析して、名詞のみのリストを返す
	tagger = MeCab.Tagger ('-d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd') #使用する辞書
	tagger.parse('')
	results = tagger.parse(text).replace('	',',').replace('EOS','').split() #形態素解析してリストに格納

	#微妙に整形
	for idx, result in enumerate(results):
		results[idx] = result.split(',')

	keywords = []   #targetで抽出したものを格納するリスト
	target = "名詞"     #「品詞細分類」が「固有名詞」の名詞を抽出

	for result in results:
		if result[1] == target:
			keywords.append(result[0])
	return keywords

text = '艦隊これくしょんは最高だな。'
keywords = wether(text)

for i in keywords:
	print(i)
