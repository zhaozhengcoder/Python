# -*- coding: utf-8 -*-
import os, sys
import jieba, codecs, math
import jieba.posseg as pseg


names = {}			# 姓名字典
relationships = {}	# 关系字典

#limenames 记录的是每一行出现的名字， 也就是说，只有出现在用一行的名字才认为是有关系的
lineNames = []		# 每段内人物关系

# count names
jieba.load_userdict("dict.txt")		# 加载字典
with codecs.open("busan.txt", "r", "utf8") as f:
	for line in f.readlines():
		#按行输出文件
		#print line
		#poss 包含两个key，一个是word，一个是flag
		"""
		words=pseg.cut("我爱北京天安门")
		for word ,flag in words:
  		  	print ('%s %s' %(word,flag))

  		 输出的格式是：
  		 我   r
  		 爱   v
  		 北京  ns
  		 天安门  ns
		"""
		poss = pseg.cut(line)		# 分词并返回该词词性
		#给list添加一个为空的list
		lineNames.append([])		# 为新读入的一段添加人物名称列表
		for w in poss:
			if w.flag != "nr" or len(w.word) < 2:
				continue			# 当分词长度小于2或该词词性不为nr时认为该词不为人名
			#[-1]表示最后一个元素
			#limenames 记录的是每一行出现的名字， 也就是说，只有出现在用一行的名字才认为是有关系的
			lineNames[-1].append(w.word)		# 为当前段的环境增加一个人物
			if names.get(w.word) is None:
				names[w.word] = 0
				relationships[w.word] = {}
			names[w.word] += 1					# 该人物出现次数加 1

# explore relationships
for line in lineNames:					# 对于每一段
	for name1 in line:					
		for name2 in line:				# 每段中的任意两个人
			if name1 == name2:
				continue
			#如果名字1 和名字2 不相同的话
			#也就是说，关系的抽取是基于 这一行有没有出现这两个名字
			if relationships[name1].get(name2) is None:		# 若两人尚未同时出现则新建项
				relationships[name1][name2]= 1
			else:
				relationships[name1][name2] = relationships[name1][name2]+ 1		# 两人共同出现次数加 1

# output
with codecs.open("busan_node.txt", "w", "utf-8") as f:
	f.write("Id Label Weight\r\n")
	for name, times in names.items():
		f.write(name + " " + name + " " + str(times) + "\r\n")

with codecs.open("busan_edge.txt", "w", "gbk") as f:
	f.write("Source Target Weight\r\n")
	for name, edges in relationships.items():
		for v, w in edges.items():
			if w > 3:
				f.write(name + " " + v + " " + str(w) + "\r\n")