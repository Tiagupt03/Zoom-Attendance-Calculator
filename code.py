import os
#(A)
#(a)
def all_csv():
    x=[]    #Initiating the file for csv files
    path=os.getcwd()     #Current directory path 
    l=os.listdir(path)
    for i in l:
        if(i[-4::]==".csv"):    #Checking for csv extension
            x.append(i)
#(b)
    d={}
    for i in x:
        f=open(i,"r")
        l=f.readlines()   #Returns lines of file in form of a list so we can read file line-by-line
        for j in l:
            if(j!=l[0]):
                y=j.split(",")    #Making a list by seperating commas sonce it is a csv file
                name=y[0]
                duration=int(y[1])   #To remove the \n
                if(name not in d):    #For uniqueness of name
                    d[name]=[duration]
                else:
                    d[name].append(duration)
        f.close()
#(c) returning the student dictionary
        return d
  
#(B)
def attendance(d):
    f=open("cs101-students.txt","w")
    l=list(d.keys())   #List of names of students
    l.sort()     #Alphabetical order sorting
    for i in l:
        f.write(i)
        f.write("\n")   #For getting a line gap
    f.close()
    
#(C)
def attendance_with_duration(d):
    f=open("cs101-students-attendance.txt","w")
    for i in d:
        f.write(str([i,len(d[i]),d[i]]))
        f.write("\n")   #For getting a line gap
    f.close()

#(D)
d=all_csv()   #Calling the function to get the dictionary we made in the first part
attendance(d)    #Calling the function to get the second file saved and ready
attendance_with_duration(d)    #Calling the function to get the first file saved and ready

from tiya_math import histogram   #Importing the function from my module
l=[]  #List for all durations
for i in d:
    l+=d[i]   #Concatinating all the durations to the list
    
print(histogram(l))       #Using the function
