cnt_200 = 0
cnt_300_309 = 0
cnt_others = 0
cnt = 0
f = open('input.txt', 'r')
text = f.read()
lines = text.split('\n')
for line in lines:
    cnt += 1
    query = line.split('"')
    response = query[2].split(' ')[1]
    if int(response) == 200:
        cnt_200 += 1
    elif 300 <= int(response) <= 309:
        cnt_300_309 += 1
    else:
        cnt_others += 1
print cnt_200
print cnt_300_309
print cnt_others
print cnt
f.close()
