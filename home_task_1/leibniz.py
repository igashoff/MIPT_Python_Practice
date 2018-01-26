x = 0.0
deg = 0
for i in xrange(1, 20, 2):
    x += ((-1) ** deg) * (4.0 / i)
    deg += 1
print x
