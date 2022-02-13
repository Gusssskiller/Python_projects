f = open('text.txt')
data = str(f.read())
data = data.replace('\n','')
#-------------------------------------------------------------------------
a_byte_array = bytearray(data, "utf8")
byte_list = []
for byte in a_byte_array:
    binary_representation = bin(byte)
    byte_list.append(binary_representation[2:])
#print(byte_list)
#---------------------------------------------------------------------------
L1=[]
L0=[]
for item in byte_list:
    list1=list(item)
    if len(list1)<7:
        list1.insert(0,'0')
    #print(list1)
    max0=0
    max1=0
    s0=0
    s1=0
    for bit in list1:
        if bit=='1':
            s1+=1
            s0=0
            if max1<s1:
                max1=s1
        else:
            s0+=1
            s1=0
            if max0<s0:
                max0=s0
    L1.append(max1)
    L0.append(max0)
#print(L1)
#print(L0)
M1=max(L1)
M0=max(L0)
print("Longest queue of 1s:", M1)
print("Longest queue of 0s:", M0)
