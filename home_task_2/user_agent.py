d = {'Windows': 0, 'Ubuntu': 0, 'OS X': 0, 'Unknown': 0}
f = open('input.txt', 'r')
text = f.read()
f.close()
lines = text.split('\n')
for line in lines:
    user_agent = line.split('"')[-2]
    if 'Windows' in user_agent:
        d['Windows'] += 1
    elif 'Ubuntu' in user_agent:
        d['Ubuntu'] += 1
    elif 'Macintosh' in user_agent:
        d['OS X'] += 1
    else:
        d['Unknown'] += 1
for item in sorted([[key, d[key]] for key in d], key=lambda x: x[1]):
    print str(item[0]) + ': ' + str(item[1])
