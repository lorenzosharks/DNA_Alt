standard_input="YOLOAUGFFFUGAUAAFFGG"
import sys

#Function
def del_early(string, index):
    return string[index:]

def mRNA_list_creation(mid):
    return [mid[i:i+3] for i in range(0, len(mid), 3)]

mRNA=input("Insert your mRNA strand (After splicing and whatnot):")

#Finding the first start codon
mRNA_index=mRNA.find("AUG")

if mRNA_index == -1:
    print("This chain has no start point.")
    sys.exit()

#Splicing the string
mRNA_mid=del_early(mRNA, mRNA_index)

#Creating a list
mRNA_list=mRNA_list_creation(mRNA_mid)

#finding the ending codon
ending_index = -1

for i in range(len(mRNA_list)):
    y=mRNA_list[i]
    for x in range(3):
        if y=="UAA" or y=="UAG" or y=="UGA":
            ending_index=i
            break
    if ending_index !=-1:
        break

final_list=mRNA_list[:ending_index+1]


phe=['UUU','UUC']
leu=['UUA','UUG','CUU','CUC','CUA','CUG']
ile=['AUU','AUC','AUA']
met=['AUG']
val=['GUU','GUC','GUA','GUG']
ser=['UCU','UCC','UCA','UCG','AGU','AGC']
pro=['CCU','CCC','CCA','CCG']
thr=['ACU','ACC','ACA','ACG']
ala=['GCU','GCC','GCA','GCG']
tyr=['UAU','UAC']
stop=['UAA','UAG','UGA']
his=['CAU','CAC']
gln=['CAA','CAG']
asn=['AAU','AAC']
lys=['AAA','AAG']
asp=['GAU','GAC']
glu=['GAA','GAG']
cys=['UGU','UGC']
trp=['UGG']
arg=['AGA','AGG','CGU','CGC','CGA','CGG']
gly=['GGU','GGC','GGA','GGG']



for i in range(len(final_list)):
    print(i+1)
    if final_list[i] in phe:
        final_list[i]=="Phe"
   
    elif final_list[i] in leu:
        final_list[i]=="Leu"
   
    elif final_list[i] in ile:
        final_list[i]=="Ile"
   
    elif final_list[i] in met:
        final_list[i]=="Met"
   
    elif final_list[i] in val:
        final_list[i]=="Val"
   
    elif final_list[i] in ser:
        final_list[i]=="Ser"
   
    elif final_list[i] in pro:
        final_list[i]=="pro"
   
    elif final_list[i] in thr:
        final_list[i]=="Thr"
   
    elif final_list[i] in ala:
        final_list[i]=="Ala"
   
    elif final_list[i] in tyr:
        final_list[i]=="Tyr"
   
    elif final_list[i] in stop:
        final_list[i]=="Stop"
   
    elif final_list[i] in his:
        final_list[i]=="His"
   
    elif final_list[i] in gln:
        final_list[i]=="Gln"
   
    elif final_list[i] in asn:
        final_list[i]=="Asn"
   
    elif final_list[i] in lys:
        final_list[i]=="Lys"
   
    elif final_list[i] in asp:
        final_list[i]=="Asp"
    
    elif final_list[i] in glu:
        final_list[i]=="Glu"
   
    elif final_list[i] in cys:
        final_list[i]=="Cys"
   
    elif final_list[i] in arg:
        final_list[i]=="Arg"
   
    elif final_list[i] in gly:
        final_list[i]=="Gly"


print(final_list)