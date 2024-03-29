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
            result_strand.append("Ala")

    elif dna_strand[i]=="g" or dna_strand[i]=="R":
            result_strand.append("Arg")

    elif dna_strand[i]=="u" or dna_strand[i]=="N":
            result_strand.append("Asn")
    
    elif dna_strand[i]=="c" or dna_strand[i]=="D":
            result_strand.append("Asp")

    elif dna_strand[i]=="c" or dna_strand[i]=="C":
            result_strand.append("Cys")

    elif dna_strand[i]=="c" or dna_strand[i]=="Q":
            result_strand.append("Gln")

    elif dna_strand[i]=="c" or dna_strand[i]=="E":
            result_strand.append("Glu")

    elif dna_strand[i]=="c" or dna_strand[i]=="G":
            result_strand.append("Gly")

    elif dna_strand[i]=="c" or dna_strand[i]=="H":
            result_strand.append("His")

    elif dna_strand[i]=="c" or dna_strand[i]=="I":
            result_strand.append("Ile")

    elif dna_strand[i]=="a" or dna_strand[i]=="L":
            result_strand.append("Leu")
    
    elif dna_strand[i]=="g" or dna_strand[i]=="K":
            result_strand.append("Lys")
   
    elif dna_strand[i]=="u" or dna_strand[i]=="M":
            result_strand.append("Met")

    elif dna_strand[i]=="c" or dna_strand[i]=="F":
            result_strand.append("Phe")

    elif dna_strand[i]=="c" or dna_strand[i]=="P":
            result_strand.append("Pro")

    elif dna_strand[i]=="c" or dna_strand[i]=="S":
            result_strand.append("Ser")

    elif dna_strand[i]=="c" or dna_strand[i]=="T":
            result_strand.append("Thr")

    elif dna_strand[i]=="c" or dna_strand[i]=="W":
            result_strand.append("Trp")

    elif dna_strand[i]=="c" or dna_strand[i]=="Y":
            result_strand.append("Tyr")

    elif dna_strand[i]=="c" or dna_strand[i]=="V":
            result_strand.append("Val")

        i=i+1

if error==False:
    better_strand="".join(result_strand)
    print("")
    print("Result: " + better_strand)
