#I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
#Any code taken from other sources is referenced within my code solution.


#Student ID - W1871490
#IIT ID - 20212041

#Date - 06/12/2021


print("\nStaff Version with Histogram\n")
total=0
progress = 0
trailer = 0
exclude = 0
retriever = 0
creditsRange = range(0,121,20)

ProgressList = []
TrailerList = []
ExcludedList  = []
RetrieverList = []

while True:
    try:
        passCredit = int(input("Please enter your credit at pass  : "))
        if passCredit not in creditsRange  :
            print("Out of range")
            continue
        deferCredit = int(input("Please enter your credit at defer : "))
        if deferCredit not in creditsRange :    
            print("Out of range")
            continue
        failCredit = int(input("Please enter your credit at fail  : ")) 
        if failCredit not in creditsRange  :
            print("Out of range") 
            continue
        total = passCredit + deferCredit + failCredit
        if total != 120:
            print("Total incorrect")
            continue
    except ValueError:
        print("Integer Required")
        continue
    if passCredit == 120 :
        print("Progress")
        progress = progress+1
        ProgressList.append(str(passCredit)+","+str(deferCredit)+","+str(failCredit))
    elif passCredit == 100 :
        print("Progress (module trailer)")
        trailer = trailer + 1
        TrailerList.append(str(passCredit)+","+str(deferCredit)+","+str(failCredit))
    elif failCredit == 80 or failCredit == 100 or failCredit == 120 :
        print("Exclude")
        exclude = exclude + 1
        ExcludedList.append(str(passCredit)+","+str(deferCredit)+","+str(failCredit))
    else:
        print("Do not progress – module retriever")
        retriever = retriever + 1
    print("\nWould you like to enter another set of data?")
    inputChoice = input("Enter 'y' for yes or 'q' to quit and view results : ")
    totalInputCount = progress + trailer + exclude + retriever
    outputNames =["Progress " , " Progress (module trailer) " ,"Do not Progress–module retriever", "Excluded "]
    
    if inputChoice == "y" :
        total = total + 1
        continue
    elif inputChoice == "q" :
        total=0
        print("\nHorizontal Histogramn/")
        print("Progress",progress,"  : ",end = "")
        for i in range(progress):
            print("*",end = "")
        print("\nTrailer",trailer,"   : ",end = "")
        for i in range (trailer):
            print("*",end = "")
        print("\nRetriever",retriever,":",end = "")
        for i in range(retriever):
            print("*",end = "")   
        print("\nExcluded",exclude,"  : ",end = "")
        for i in range(exclude):
            print("*",end = "")
        total=progress + trailer + exclude + retriever
        print("\n")
        print(total," Outcomes in total ")
        break
    else:
        print("y or q required")
        break

    

#PART 2 - VERTICAL HISTOGRAM

    
category  = [[],[],[],[]]
print(*outputNames)
for x in range(progress) :
    category [0].append('  *')
for x in range(trailer) :
    category [1].append('*')
for i in range(retriever) :
    category [2].append('*')
for x in range(exclude):
     category [3].append('*')
for i in range(totalInputCount):
    for x in category:
        try:
            print(x[i], end="\t\t\t")
        except:
            print(" ",end="\t\t\t")
    print()


    

#PART 3 - LIST/TUPLE/DIRECTORY

    
    
for p in range(len(ProgressList)):
    print("Progress - ", ProgressList[p])

for p in range(len(TrailerList)):
    print("Progress(Module trailer) - ",TrailerList[p])

for p in range(len(RetrieverList)):
    print("Module retriever - ", RetrieverList[p])    
        
for p in range(len(ExcludedList)):
    print("Excluded - ", ExcludedList[p])    






#PART 4 - TEXT FILE
    
#CREATING THE TEXT FILE , INSERTING DATA

    
    
textFile = open("marks.txt", "w")
for i in ProgressList:
    textFile.write("Progress - "+i+"\n")
for i in TrailerList:
    textFile.write("Progress(Module trailer) - "+i+"\n")
for i in RetrieverList:
    textFile.write("Module retriever - "+i+"\n")
for i in ExcludedList:
    textFile.write("Exclude - "+i+"\n")
textFile.close()



#Retrieving data from text file



textFile = open("marks.txt","r")
print("\nFrom text file\n")
print(textFile.read())
textFile.close()

    
    
            
    
