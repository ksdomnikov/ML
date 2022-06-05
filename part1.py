with open('sentences.txt','r') as file:
    data = file.readlines()
for tx in data:
    tx.split()
for i in range(len(data)):
    data[i] = data[i].lower()
for i in range(len(data)):
    data[i] = data[i].split()
data = dict.data
with open('sentences.txt','r') as file:
    data = file.readlines()
for i in range (len(data)):
    data[i].remove('')
for i in range (len(data)):
    for j in range(len(data[i])):
        if data[i][j] == '':
            del data[i][j]