# Xiaote Zhu
# NBtrain.py

import sys
import os
import json
import codecs
import math

def learnProb(folder):
	wordCount = dict()
	for filename in os.listdir(folder):
		filepath = '%s/%s' % (folder, filename)
		f = codecs.open(filepath, 'r', 'ascii', errors='replace')
		filecontent = f.read()
		f.close()
		wordLists = [word for word in filecontent.strip().split()]
		fileWordSet = set(wordLists)

		for word in fileWordSet:
			if word in wordCount:
				wordCount[word] += 1
			else:
				wordCount[word] = 1
				
	totalWordCount = float(sum(wordCount.values()))
	wordProb = dict(map(lambda (word, count): (word, math.log(count / totalWordCount)), wordCount.iteritems()))
	wordProb['rareWordsPlaceHolder'] = min(wordProb.values())
	return wordProb

def main():
	index = 1
	dataDir = None

	# parsing command line arguments
	while index < len(sys.argv):
		if sys.argv[index] == '-f':
			index += 1
			if index >= len(sys.argv):
				print "warning: no folder name given"
			else:
				dataDir = sys.argv[index]
		index += 1

	if dataDir == None:
		print "please give me a folder"
		return

	hamDir = '%s/ham' %dataDir
	spamDir = '%s/spam' %dataDir

	# learning prior
	hamCount = len(filter(lambda fname: fname.endswith('.txt'), os.listdir(hamDir)))
	spamCount = len(filter(lambda fname: fname.endswith('.txt'), os.listdir(spamDir)))
	totalCount = float(hamCount + spamCount)
	print 'hamPrior:%f' % (hamCount/totalCount)
	print 'spamPrior:%f' % (spamCount/totalCount)

	# learning conditional likelihood for each word
	hamWordProb = learnProb(hamDir)
	spamWordProb = learnProb(spamDir)

	print "TopHamWordProb:"
	print sorted(hamWordProb.items(), key=(lambda (k, v): v), reverse = True)[:30]
	print "TopSpamWordProb:"
	print sorted(spamWordProb.items(), key=(lambda (k, v): v), reverse = True)[:30]

	hamJPath = '%s/../hamWords.json' %dataDir
	spamJPath = '%s/../spamWords.json' %dataDir

	codecs.open(hamJPath,'w','utf-8').write(json.dumps(hamWordProb, indent = 2))
	codecs.open(spamJPath,'w','utf-8').write(json.dumps(spamWordProb, indent = 2))

main()

