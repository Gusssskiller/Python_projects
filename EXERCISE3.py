
#Σας δίνεται ένα αρχείο κειμένου το οποίο έχει μόνο ASCII χαρακτήρες. Αρχικά, κάντε την 
#κατάλληλη επεξεργασία ώστε να σας μείνει κείμενο με μόνο γράμματα και τον κενό 
#χαρακτήρα (space). Χωρείστε αυτό το κείμενο σε λέξεις σύμφωνα με το κενό και 
#ξεκινείστε να αφαιρείτε ζευγάρια λέξεων αν το άθροισμα των γραμμάτων τους είναι 20.
#Βγάλτε τα στατιστικά για το μήκος των λέξεων που έμειναν, πχ. 10 λέξεις του ενός
#γράμματος, 12 λέξεις των 2 γραμμάτων, 3 λέξεις των 3 γραμμάτων κτλ.
#--------------------------------------------------------------------------------------------------------
file = open('text.txt')
data = str(file.read())                             #Βάζω και διαβάζω αρχείο
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
data = data.replace("'",' ')                        #βγάζω ανεπιθύμητους χαρακτήρες
words = data.split(" ")                             #χωρίζω λέξεις από κενά σε λίστα
words = list(filter(('').__ne__, words))            #Βγάζω το στοιχεία που είναι κενά
#print(words)
#print(len(words))
#----------------------------------------------------------------------------------------------
for i in range (0,len(words)-3):
    #print(i)
    if len(words[i])+len(words[i+1])==20:
        item=words[i]
        item1=words[i+1]
        words.remove(item1)
        words.remove(item)                          #αφαιρώ ζευγάρια ανα 2 που το μήκος τους είναι 20 χαρακτήρες 
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
    print(stats[i], " words with ", lengths[i], " letters.\n")          #Τυπώνω τα στατιστικά
#---------------------------------------------------------------------------------------------------------