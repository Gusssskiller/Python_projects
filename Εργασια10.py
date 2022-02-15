f = open('text.txt')
data = str(f.read())
data = data.replace('\n','') #Makes text into one continuous string
#-------------------------------------------------------------------------
a_byte_array = bytearray(data, "utf8")
byte_list = []
for byte in a_byte_array:
    binary_representation = bin(byte)
    byte_list.append(binary_representation[2:])             #creates a list that contains lists of each bin number
#print(byte_list) 
#---------------------------------------------------------------------------
new = []
for item in byte_list:
    list1=list(item)
    while len(list1)<7:
        list1.insert(0,'0') #fills in gaps of non len==7 items
    #print(list1)
#------------------------------------------------------------------------------
for item in byte_list:
    i=0
    list1=item
    for bit in list1:
        if i==1 or i==0 or i==6 or i==5:
            new.append(bit)
        i+=1        #Makes a new list that contains onle the two first and two last bits of each item
#print(new)
#------------------------------------------------------------------------------
str1=""
for item in new:
    str1+= item
#print (str1)
length=len(str1)    #creates a continuous string of all the elements in "new" list
#-------------------------------------------------------------------------------
list2 = []
for i in range (0,length,17):
    list2.append(str1[i:i+16])
#print(list2)
while len(list2[len(list2)-1])<16:
    temp = '0' + list2[len(list2)-1]
    list2[len(list2)-1] = temp  #creates a new list that contains 16bit numbers, made from str1(splits the str1 every 16 chars)
#print(list2)
#----------------------------------------------------------------------------------------
temp= []
decimals = []
for item in list2:
    temp = list(item)
    i=0
    dec = 0
    for bit in temp:
        bit = int(bit)
        dec += (2^i)* bit
        i+=1
    decimals.append(dec)    #converts each bin number into its decimal and appends it into a new list(decimals)
#print(decimals)
#------------------------------------------------------------------------------------------------
Even_n=0
Div3=0
Div5=0
Div7=0
total=float(len(decimals))     #starting the vars of each question
#--------------------------------------------------------------------------------------------------
for item in decimals:
    if item%2==0:
        Even_n+=1
    if item%3==0:
        Div3+=1
    if item%5==0:
        Div5+=1
    if item%7==0:
        Div7+=1     #finding which numbers fit the criteria
#print(Even_n)
#print(Div3)
#print(Div5)
#print(Div7)
#print(total)
q1=float(Even_n)/total*100
q2=float(Div3)/total*100
q3=float(Div5)/total*100
q4=float(Div7)/total*100
#print(q1)
print("The percentage of even numbers is: ", q1,  "%.")
print("The percentage of numbers that are divided by 3 is: ", q2,  '%.')
print("The percentage of numbers that are divided by 5 is: ", q3,  "%.")
print("The percentage of numbers that are divided by 7 is: ", q4,  "%.")    #printing the results
#--------------------------------------------------------------------------------------------------------
