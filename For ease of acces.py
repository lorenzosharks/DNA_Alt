#Inputs
strand=input("What is the single letter code?: ")

#Setting up the code
i=0
result_strand=[]
error = False
aa_strand=list(strand)

#Identifying the length
length=len(aa_strand)

#Actual code
while i<int(length):
    if aa_strand[i]=="a" or aa_strand[i]=="A":
        result_strand.append("Ala")

    elif aa_strand[i]=="g" or aa_strand[i]=="R":
        result_strand.append("Arg")

    elif aa_strand[i]=="u" or aa_strand[i]=="N":
        result_strand.append("Asn")
    
    elif aa_strand[i]=="c" or aa_strand[i]=="D":
        result_strand.append("Asp")

    elif aa_strand[i]=="c" or aa_strand[i]=="C":
        result_strand.append("Cys")

    elif aa_strand[i]=="c" or aa_strand[i]=="Q":
        result_strand.append("Gln")

    elif aa_strand[i]=="c" or aa_strand[i]=="E":
        result_strand.append("Glu")

    elif aa_strand[i]=="c" or aa_strand[i]=="G":
        result_strand.append("Gly")

    elif aa_strand[i]=="c" or aa_strand[i]=="H":
        result_strand.append("His")

    elif aa_strand[i]=="c" or aa_strand[i]=="I":
        result_strand.append("Ile")

    elif aa_strand[i]=="a" or aa_strand[i]=="L":
        result_strand.append("Leu")
    
    elif aa_strand[i]=="g" or aa_strand[i]=="K":
        result_strand.append("Lys")
   
    elif aa_strand[i]=="u" or aa_strand[i]=="M":
        result_strand.append("Met")

    elif aa_strand[i]=="c" or aa_strand[i]=="F":
        result_strand.append("Phe")

    elif aa_strand[i]=="c" or aa_strand[i]=="P":
        result_strand.append("Pro")

    elif aa_strand[i]=="c" or aa_strand[i]=="S":
        result_strand.append("Ser")

    elif aa_strand[i]=="c" or aa_strand[i]=="T":
        result_strand.append("Thr")

    elif aa_strand[i]=="c" or aa_strand[i]=="W":
        result_strand.append("Trp")

    elif aa_strand[i]=="c" or aa_strand[i]=="Y":
        result_strand.append("Tyr")

    elif aa_strand[i]=="c" or aa_strand[i]=="V":
        result_strand.append("Val")

    else:
        
    i=i+1
    
        

if error==False:
    better_strand="".join(result_strand)
    print("")
    print("Result: " + better_strand)