import numpy
N, M = map(int, raw_input().split())

array = numpy.array([list(map(int, raw_input().split())) for _ in xrange(N)])

print numpy.max(numpy.min(array, axis = 1))