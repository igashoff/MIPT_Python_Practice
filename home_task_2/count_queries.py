counter = 0
f = open('input.txt', 'r')
text = f.read()
lines = text.split('\n')
for line in lines:
    query = line.split(' ')
    if query[len(query) - 1] == '"Go-http-client/1.1"':
        counter += 1
print counter
f.close()
