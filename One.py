# Kate Williams
# 6/7/2018

wordList = ["PHP", "Exercises", "Backend"]

shortList = []
longList = []
tup = ()

x = 0
while x < 3:
    shortList.append(len(wordList[x]))
    shortList.append(wordList[x])
    longList.append(tuple(shortList))
    x += 1
    shortList = []

#print(max(longList))
print(longList)