import datetime
import json
import os
from collections import defaultdict

# class message_class:
# 	def __init__(self):
# 		self.participants = None
# 		self.wordOccurrence = defaultdict(lambda: defaultdict(int))
# 		self.messageOccurrence = defaultdict(lambda: defaultdict(int))

class message_class:
	def __init__(self):
		self.participants = None
		self.wordOccurrence = defaultdict(int)
		self.messageOccurrence = defaultdict(int)
		
def analyzeFile(message_file,message_data):
	with open(message_file) as data_file:
		data = data_file.read()
		data = json.loads(data)
		for message in data['messages']:
			time = datetime.datetime.fromtimestamp(message['timestamp_ms']/1000.0)
			message_data.messageOccurrence[message['sender_name']][str(time.year)+'-'+str(time.month)] += 1
			if 'content' in message:
				message_data.wordOccurrence[message['sender_name']][str(time.year)+'-'+str(time.month)] += len(message['content'].split())


def forPerson(dir):
	dir_folder = "dir"
	message_data = message_class()
	for (dirpath, dirnames, filenames) in os.walk(dir_folder):
		for filename in filenames:
			if filename.endswith(".json"):
				analyzeFile(dirpath + '/' + filename,message_data)
	output_file = open(dir_folder + '/' +'output.csv','w')
	for key in message_data.messageOccurrence:
		output_file.write(key + '\n')
		for time in message_data.messageOccurrence[key]:
			output_file.write(str(time)+','+str(message_data.messageOccurrence[key][time])+','+str(message_data.wordOccurrence[key][time])+'\n')

participants = defaultdict(message_class)

def group(dir):
	with open(dir) as data_file:
		data = data_file.read()
		data = json.loads(data)
		key = []
		if len(data['participants']) > 2:
			return
		for participant in data['participants']:
			key.append(participant["name"])
		key = ",".join(key)
		for message in data['messages']:
			participants[key].messageOccurrence[message['sender_name']] += 1
			if 'content' in message:
				participants[key].wordOccurrence[message['sender_name']] += len(message['content'].split())

def traverseFolder():
	for path, sub_path, file_names in  os.walk("/mnt/c/Users/black/Downloads/messages/"):
		for file in file_names:
			if file.endswith(".json"):
				group(os.path.join(path,file))
	#output_file = open(dir_folder + '/' +'output.csv','w')
	output_list = []
	for key in participants:
		total = 0
		output_string = ""
		for person in participants[key].wordOccurrence:
			total += participants[key].wordOccurrence[person]
			output_string += person + ',' + str(participants[key].wordOccurrence[person]) + ","
		output_list.append([total,output_string])
	output_list.sort(reverse = True)
	for output in output_list:
		print(output[0], ",", output[1])

traverseFolder()


















