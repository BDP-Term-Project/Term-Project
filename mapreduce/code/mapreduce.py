from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.protocol import RawProtocol

class MRWordCount(MRJob):
	OUTPUT_PROTOCOL = RawProtocol
	
	def steps(self):
		return[
				MRStep(mapper = self.mapper,
					combiner = self.combiner,
					reducer = self.reducer),
				MRStep(reducer = self.sort_reduce)
				]
	
	def mapper(self, _, line):
		words = line.split(' ')
		
		for word in words:
			if word != '""':
				yield (word, 1)
	
	def combiner(self, word, counts):
		yield (word, sum(counts))
	
	def reducer(self, word, counts):
		yield (100000-(sum(counts)), word)
	
	def sort_reduce(self, count, words):
		for word in words:
			yield (word, str(100000-count))

if __name__ == '__main__':
	MRWordCount.run()

