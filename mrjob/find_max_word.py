from mrjob.job import MRJob
import re

WORD_RE = re.compile(r"[\w/']+")

class MRMostUsedWord(MRJob):
	
	def mapper_get_words(self, _, line):
	#yield each word in the line
		for word in WORD_RE.findall(line):
			yield (word.lower(), 1)

	def combiner_count_words(self, word, counts):
	#accumulator
		yield (word, sum(counts))

	def reducer_count_words(self, word, counts):
	#send all (num_occurrences, word) to the same reducer
		yield None, (sum(counts), word)

	def reducer_find_max_word(self, _, word_count_pairs):
	#each item is (count, word)
		yield max(word_count_pairs)

	def steps(self):
		return [
			self.mr(mapper = self.mapper_get_words,
				combiner = self.combiner_count_words,
				reducer = self.reducer_count_words),
			self.mr(reducer = self.reducer_find_max_word)
		]


if __name__ == '__main__':
	MRMostUsedWord.run()


