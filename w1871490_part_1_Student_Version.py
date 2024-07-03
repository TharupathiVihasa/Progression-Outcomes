#STUDENT VERSION

creditsRange = range(0,121,20)
print("\nStudent Version\n")
count = 0
while count != 1:
    while True:
        try:
            passCredit = int(input("Please enter your credit at pass  : "))
            if passCredit not in creditsRange  :
                print("Out of range")
                break
            deferCredit = int(input("Please enter your credit at defer : "))
            if deferCredit not in creditsRange :    
                print("Out of range")
                break
            failCredit = int(input("Please enter your credit at fail  : ")) 
            if failCredit not in creditsRange  :
                print("Out of range") 
                break
        except ValueError:
            print("Integer Required")
            continue
            
        total = passCredit + deferCredit + failCredit
        if total != 120:
            print("Total incorrect")
        else:
            if passCredit == 120 :
                print("Progress")
            elif passCredit == 100 :
                print("Progress (module trailer)")
            elif failCredit == 80 or failCredit == 100 or failCredit == 120 :
                print("Exclude")
            else:
                print("Do not progress – module retriever")
            count = count+1
            break
                    
