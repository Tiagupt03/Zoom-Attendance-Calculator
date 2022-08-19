#(A) Maximum function of our own
def max(l):
    m=-100000     #Smallest number according to the question
    for i in l:        #Iterative approach
        if(m<int(i)):       
            m=int(i)
    return m     #Fruitful Function 

#(B) Minimum function of our own
def min(l):
    m=100000     #largest number according to the question
    for i in l:       #iterative approach
        if(int(i)<m):
            m=int(i)
    return m    #Fruitful Function 

#(C) Histogram
def histogram(l,no_of_bins=3):
    r=[]
    d={}
    x=max(l)
    y=min(l)
    bin_size=(x-y)/no_of_bins
    start=y
    end=y+bin_size
    while(end<=x):
        r.append((start,end))      #Using a tuple so that it is hashable and thus can be used as key in the dictionary
        start+=bin_size
        end=start+bin_size
    l.sort()       #Sorting the list
    ct=0
    j=0
    for i in l:
        if(r[j][0]<=i<r[j][1]):
            ct+=1
        else:
            d['<'+str(r[j][1])]=ct
            ct=1
            j+=1
        if(j==len(r)):
            break
    return d
