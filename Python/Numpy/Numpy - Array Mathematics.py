import numpy
N, M = map(int, raw_input().split())
A = numpy.array([list(map(int, raw_input().split())) for _ in xrange(N)])
B = numpy.array([list(map(int, raw_input().split())) for _ in xrange(N)])
print numpy.add(A, B)
print numpy.subtract(A, B)
print numpy.multiply(A, B)
print numpy.divide(A, B)
print numpy.mod(A, B)
print numpy.power(A, B)