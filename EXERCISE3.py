
#--------------------------------------------------------------------------------------------------------
file = open('text.txt')
data = str(file.read())                             
data = data.replace('.',' ')
data = data.replace('\n','')
data = data.replace(',',' ')
data = data.replace('#','')
data = data.replace('[','')
data = data.replace(']','')
data = data.replace('0','')
data = data.replace('1','')
data = data.replace('2','')
data = data.replace('3','')
data = data.replace('4','')
data = data.replace('5','')
data = data.replace('6','')
data = data.replace('7','')
data = data.replace('8','')
data = data.replace('9','')
data = data.replace('(','')
data = data.replace(')','')
data = data.replace('*','')
data = data.replace('-','')
data = data.replace('!',' ')
data = data.replace(';','')
data = data.replace(',','')
data = data.replace(':','')
data = data.replace('"',' ')
data = data.replace('_',' ')
data = data.replace("'",' ')                        #take out unwanted chars 
words = data.split(" ")                             #split words
words = list(filter(('').__ne__, words))            
#print(words)
#print(len(words))
#----------------------------------------------------------------------------------------------
for i in range (0,len(words)-3):
    #print(i)
    if len(words[i])+len(words[i+1])==20:
        item=words[i]
        item1=words[i+1]
        words.remove(item1)
        words.remove(item)                          #remove couples the their length>20
print(words)
lengths=[]
for element in words:
    lengths.append(len(element))
lengths=set(lengths)
#print(lengths)
#---------------------------------------------------------------------------------------------------------
stats=[]
for item in lengths:
    S=0
    for element in words:
        if len(element)==item:
            S+=1
    stats.append(S)
lengths= list(lengths)

for i in range (0,len(stats)):
    print(stats[i], " words with ", lengths[i], " letters.\n")          #print results
#---------------------------------------------------------------------------------------------------------