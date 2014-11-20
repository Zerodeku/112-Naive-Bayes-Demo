# Xiaote Zhu
# NBtest.py

import sys
import json
import math
import os
import codecs

hamJFile = open('hamWords.json', 'r') 
spamJFile = open('spamWords.json', 'r')

hamWordProb = json.load(hamJFile)
spamWordProb = json.load(spamJFile)


def classify(wordSet, spamPrior):
	hamProb = math.log(1 - spamPrior)
	spamProb = math.log(spamPrior)

	for word in wordSet:
		if word in hamWordProb:
			hamProb += hamWordProb[word]
		else:
			hamProb += hamWordProb['rareWordsPlaceHolder']
		if word in spamWordProb:
			spamProb += spamWordProb[word]
		else:
			spamProb += spamWordProb['rareWordsPlaceHolder']

	if hamProb > spamProb:
		label = 0
	else:
		label = 1

	return label

def test(dataDir, spamPrior):
	hamDir = os.path.join(dataDir,'ham')
	spamDir = os.path.join(dataDir, 'spam')

	hamLabels = []
	for filename in os.listdir(hamDir):
		filepath = '%s/%s' % (hamDir, filename)
		f = codecs.open(filepath, 'r', 'ascii', errors='replace')
		filecontent = f.read()
		f.close()
		wordLists = [word for word in filecontent.strip().split()]
		fileWordSet = set(wordLists)
		hamLabels += [classify(fileWordSet, spamPrior)]

	spamLabels = []
	for filename in os.listdir(spamDir):
		filepath = '%s/%s' % (spamDir, filename)
		f = codecs.open(filepath, 'r', 'ascii', errors='replace')
		filecontent = f.read()
		f.close()
		wordLists = [word for word in filecontent.strip().split()]
		fileWordSet = set(wordLists)
		spamLabels += [classify(fileWordSet, spamPrior)]

	precision = float(sum(spamLabels))/(sum(hamLabels) + sum(spamLabels))
	recall = float(sum(spamLabels))/len(spamLabels)
	accuracy = float(sum(spamLabels) + len(hamLabels) - sum(hamLabels))/(len(spamLabels) + len(hamLabels))
	print 'precision: %f' %precision
	print 'recall: %f' %recall
	print 'accuracy: %f' %accuracy


def main():
	index = 1
	spamPrior = 0.25
	interactive = False
	dataDir = None

	# parsing command line arguments
	while index < len(sys.argv):
		if sys.argv[index] == '-p':
			index +=1
			if index >= len(sys.argv):
				print "using default prior"
			elif float(sys.argv[index]) >= 1 or float(sys.argv[index])<=0:
				print "not valid prior, using default one"
			else:
				spamPrior = float(sys.argv[index])
		elif sys.argv[index] == '-f':
			index +=1
			if index >= len(sys.argv):
				print "warning: no folder name given"
			else:
				dataDir = sys.argv[index]
		elif sys.argv[index] == '-i':
			interactive = True
		index += 1


	if interactive:
		while True:
			email = raw_input("Write me an email:")
			label = classify(set(email.split()), spamPrior)
			if label == 0:
				print "yum, yum, i love ham\n"
			elif label == 1:
				print "how dare you, you wrote me a spam\n"
	
	else:
		if dataDir == None:
			print "please give me a folder"
		else:
			test(dataDir, spamPrior)

main()
