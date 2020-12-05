# выгрузить данные по адресу https://introcs.cs.princeton.edu/python/21function/princeton-files.txt


import sys,random
import requests
import os
url = 'https://introcs.cs.princeton.edu/python/21function/princeton-files.txt'
r = requests.get(url, allow_redirects=True)
fileName = 'web_numbers.txt'
open(fileName, 'wb').write(r.content)

websiteNumbers = open(fileName)
numbers = websiteNumbers.readlines()
websiteNumbers.close()
data=[]
for number in numbers:
    data.append(int(number))
os.remove(fileName)


def benford(data):
    i=len(data)
    digits=[]
    while i>0:
        num=str(data[i-1])
        first_digit=num[0]
        digits.append(first_digit)
        i-=1
    j=len(digits)
    digit=[]
    while j>0:
        fir_dig=int(digits[j-1])
        digit.append(fir_dig)
        j-=1
    n1=0
    n2=0
    n3=0
    n4=0
    n5=0
    n6=0
    n7=0
    n8=0
    n9=0
    k=0
    dat=len(digit)
    while k<=dat-1:
        if digit[k]==1:
            n1+=1
        elif digit[k]==2:
            n2+=1
        elif digit[k]==3:
            n3+=1
        elif digit[k]==4:
            n4+=1
        elif digit[k]==5:
            n5+=1
        elif digit[k]==6:
            n6+=1
        elif digit[k]==7:
            n7+=1
        elif digit[k]==8:
            n8+=1
        elif digit[k]==9:
            n9+=1
        k+=1
    n=[n1,n2,n3,n4,n5,n6,n7,n8,n9]
    freq=[]
    h=0
    h1=len(n)
    while h<=h1-1:
        chs=n[h]*100/len(data)
        freq.append(chs)
        h+=1

    chast=[
        ['Frequency of 1: '+str(freq[0])+'%',],
        ['Frequency of 2: '+str(freq[1])+'%',],
        ['Frequency of 3: '+str(freq[2])+'%',],
        ['Frequency of 4: '+str(freq[3])+'%',],
        ['Frequency of 5: '+str(freq[4])+'%',],
        ['Frequency of 6: '+str(freq[5])+'%',],
        ['Frequency of 7: '+str(freq[6])+'%',],
        ['Frequency of 8: '+str(freq[7])+'%',],
        ['Frequency of 9: '+str(freq[8])+'%',]
    ]
    return chast

for item in benford(data) : print(item)
