l = range(1, 101)
for i in xrange(0, 100):
    print l[i],
print
for i in range(0, 100):
    if l[i] % 3 == 0 and l[i] % 5 == 0 and l[i] >= 5:
        l[i] = 'BazQux'
    elif l[i] % 3 == 0 and l[i] >= 3:
        l[i] = 'Baz'
    elif l[i] % 5 == 0 and l[i] >= 5:
        l[i] = 'Qux'
for i in xrange(0, 100):
    print l[i],
