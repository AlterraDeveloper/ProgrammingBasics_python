import sys
import stdio

numList = list(sys.argv[1])

maxcount = 0
value = None
location = None

i = 1
while i < len(numList) - 1:
    resList = []
    count = 0
    if numList[i] > numList[i - 1]:
        resList += [numList[i]]
        j = i + 1
        while j < len(numList):
            if numList[i] == numList[j]:
                resList += [numList[j]]
                j += 1
            elif numList[i] < numList[j]:
                i = j
                break
            else:
                count = len(resList)
                if count > maxcount:
                    maxcount = count
                    value = resList[1]
                    location = i
                i = j
    else:
        i += 1

print("Самая длинная последовательност расположена по индексу: " + str(location))
print("Длина: " + str(maxcount))
print("Значение : " + str(value))