#The only function in this entire code and it doesn't even matter to the actual part.
def selection():
    
    validAnswer = False
    
    while validAnswer == False:
        option=input('Do you want it in lowercase? Answer "y" for yes and "n" for no: ')
        if option == "y" or option == "n":
            validAnswer = True
        else:
            print("Please enter a valid answer.")
    return option

print("This gives the DNA strand given one half of the RNA.")
print("Capitals doesn't matter. However, the results is in capitals")
print("However, there is a option to change it. Default is in capitals.")
print("")



#Inputs
selection_option = selection()
strand=input("What is half of the strand: ")

#Setting up the code
i=0
result_strand=[]
error = False
dna_strand=list(strand)

#Identifying the length
length=len(dna_strand)

#Actual code
while i<int(length):
    if dna_strand[i]=="a" or dna_strand[i]=="A":
        if selection_option=="n":
            result_strand.append("T")
        if selection_option=="y":
            result_strand.append("t")
    
    elif dna_strand[i]=="g" or dna_strand[i]=="G":
        if selection_option=="n":
            result_strand.append("C")
        if selection_option=="y":
            result_strand.append("c")
    
    elif dna_strand[i]=="u" or dna_strand[i]=="U":
        if selection_option=="n":
            result_strand.append("A")
        if selection_option=="y":
            result_strand.append("a")
    
    elif dna_strand[i]=="c" or dna_strand[i]=="C":
        if selection_option=="n":
            result_strand.append("G")
        if selection_option=="y":
            result_strand.append("g")
    
    else:
        error = True
        break
    i=i+1

if error==False:
    better_strand="".join(result_strand)
    print("")
    print("Result: " + better_strand)
