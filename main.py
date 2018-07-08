import datetime
import os
from collections import defaultdict

class messageChunk:
	def __init__(self, name, time):
		self.name = name
		self.time = time



def findWordOccurences():
	wordOccurences = defaultdict(int)
	with open('message.json') as f:
		for line in f:
			if "content" in line:
				temp = line[18:-3]
				sentence = temp.split()
				for word in sentence:
					word = word.lower()
					wordOccurences[word]+=1
				total = sorted(wordOccurences.items(), key=lambda x:x[1])
				# for x in range(10):
	total = total[::-1]
	for x in range(50):
		print( '#', x+1 ,total[x])


def findCommentsPerMonth():
	date = defaultdict(int)
	with open('message.json') as f:
		for line in f:
			if "sender_name" in line:
				temp = f.readline()
				temp = temp[19:29]
				temp = str(datetime.datetime.fromtimestamp(int(temp)))
				temp = temp[:7]
				date[temp]+=1

	for d in date:
		print(d, ",",date[d])

def findTotalComments(file):
	totalComments = 0
	isValidChat = False
	with open(file) as f:
		for line in f:
			if "sender_name" in line:
				totalComments+=1;
			if "\"participants\": [" in line:
				isValidChat = True
				participants = []
				while (True):
					temp = f.readline()
					participant = ""
					if '],' in temp:
						break
					temp = temp[5:]
					for char in temp:
						if (char=='\"'):
							break
						participant+=char
					participants.append(participant)
	if(isValidChat):
		if participants.length(==1):
			print(totalComments,",", end = "")
			print(participants)

def forEveryFile():
	for (dirpath, dirnames, filenames) in os.walk('./'):
		for filename in filenames:
			if (filename == "message.json"):
				fileToOpen = dirpath + '/' +filename
				findTotalComments(fileToOpen)




forEveryFile()


















