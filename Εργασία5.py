f = open('text.txt')
data = str(f.read())
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
data = data.replace('?','')
data = data.replace(',','')
data = data.replace(':','')
data = data.replace('"',' ')
data = data.replace('_',' ')
data = data.replace("'",' ')                        
data = data.lower()
#print(data)
words = data.split(" ")                             
words = list(filter(('').__ne__, words))          #makes a list with the words of the text
#---------------------------------------------------------------
print("10 Most popular words:")
words1 = set(words)
words1 = list(words1)
n=[]
for item in words1:
    s = 0
    for i in range (len(words)):
        if words[i]==item:
            s += 1
    n.append(s)  
#print(words1)
#print(n)    
#print(len(words))
#print(len(words1))
copy_n=n
maxl=[]
for i in range (len(copy_n)):
    maximum = max(copy_n)
    copy_n.remove(maximum) 
    maxl.append(maximum)                #finds the frequency of each individual word
copy_maxl=maxl
maxl = set(maxl)
maxl = list(maxl)                       #creates a set->list with all the frequencies
#print(maxl)
k = len(maxl)
#print(k)
if k<10:
    for item in reversed(maxl):
        flag=False
        i=0
        while i<len(words1) and flag==False:
            if len(words1[i])==item:
                print(words1[i])
                words1.pop(i)
                flag=True
            i+=1  
    
    for item in reversed(maxl):
        flag=False
        i=0
        while i<len(words1) and flag==False:
            if len(words1[i])==item:
                k+=1
                print(words1[i])
                words1.pop(i)
                flag=True
                if k==10:
                    break  
            i+=1 
        if k==10:
            break  
else:
    j=0
    for item in reversed(maxl):
        j+=1
        flag=False
        i=0
        while i<len(words1) and flag==False:
            if len(words1[i])==item:
                print(words1[i])
                words1.pop(i)
                flag=True
            i+=1   
        if j==10:
            break                               #Finds most popoular words
#--------------------------------------------------------------------------
print("3 Most popular 2 first letters:")
Let2=[]
i=0
for item in words1:
   Let2.append(item[:2])
#print(Let2)
Let2_Copy=Let2
Let2=set(Let2)
Let2=list(Let2)
Let2_F=[]
for item in Let2:
    s = 0
    for i in range (len(Let2_Copy)):
        if Let2_Copy[i]==item:
            s += 1
    Let2_F.append(s) 
for i in range (3):
    maxL2=max(Let2_F)
    pos = Let2_F.index(maxL2)
    print(Let2[pos])
    Let2.pop(pos)
    Let2_F.pop(pos)
#-----------------------------------------------------------------------
print("3 Most popular 3 first letters:")
Let3=[]
i=0
for item in words1:
   Let3.append(item[:3])
#print(Let3)
Let3_Copy=Let3
Let3=set(Let3)
Let3=list(Let3)
Let3_F=[]
for item in Let3:
    s = 0
    for i in range (len(Let3_Copy)):
        if Let3_Copy[i]==item:
            s += 1
    Let3_F.append(s) 
for i in range (3):
    maxL3=max(Let3_F)
    pos = Let3_F.index(maxL3)
    print(Let3[pos])
    Let3.pop(pos)
    Let3_F.pop(pos)
#------------------------------------------------------------------------