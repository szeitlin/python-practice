from mrjob.job import MRJob

class MRWordFrequencyCount(MRJob):

	def mapper(self, _, line):        #returns key-value pairs
		yield "chars", len(line)
		yield "words", len(line.split())
		yield "lines", 1
	
	def reducer(self, key, values):   #takes a key and an iterator of values, also returns key-value pairs
		yield key, sum(values)


if __name__ == '__main__':
	MRWordFrequencyCount.run()        #this part is requried for your job to run! 



##to run it, use: python word_count.py <pathtoyourfilehere.txt>

## -r inline (default)
## -r local == multiple subprocesses with some Hadoop features simulated
## -r hadoop (obvious)
## -r emr (if you have elastic mapreduce configured)


