#standard_input="YOLOAUGAUGacuagucgagguccgaucgugagucgaugagucgauCGAUGCuaGCGUUAGCUAGCUGAUCGAUCGAGACUGAUAAFFGG"
standard_input="UAAAUG"
import sys

#Function
def del_early(string, index):
    return string[index:]

def mRNA_list_creation(mid):
    return [mid[i:i+3] for i in range(0, len(mid), 3)]

mRNAv1=input("Insert your mRNA strand (After splicing and whatnot):")

mRNA=mRNAv1.upper()

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

final_listv1=mRNA_list[:ending_index+1]


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



for i in range(len(final_listv1)):
    if final_listv1[i] in phe:
        final_listv1[i]="Phe"
   
    elif final_listv1[i] in leu:
        final_listv1[i]="Leu"
   
    elif final_listv1[i] in ile:
        final_listv1[i]="Ile"
   
    elif final_listv1[i] in met:
        final_listv1[i]="Met"
   
    elif final_listv1[i] in val:
        final_listv1[i]="Val"
   
    elif final_listv1[i] in ser:
        final_listv1[i]="Ser"
   
    elif final_listv1[i] in pro:
        final_listv1[i]="Pro"
   
    elif final_listv1[i] in thr:
        final_listv1[i]="Thr"
   
    elif final_listv1[i] in ala:
        final_listv1[i]="Ala"
   
    elif final_listv1[i] in tyr:
        final_listv1[i]="Tyr"
   
    elif final_listv1[i] in stop:
        final_listv1[i]="Stop"
   
    elif final_listv1[i] in his:
        final_listv1[i]="His"
   
    elif final_listv1[i] in gln:
        final_listv1[i]="Gln"
   
    elif final_listv1[i] in asn:
        final_listv1[i]="Asn"
   
    elif final_listv1[i] in lys:
        final_listv1[i]="Lys"
   
    elif final_listv1[i] in asp:
        final_listv1[i]="Asp"
    
    elif final_listv1[i] in glu:
        final_listv1[i]="Glu"
   
    elif final_listv1[i] in cys:
        final_listv1[i]="Cys"
   
    elif final_listv1[i] in arg:
        final_listv1[i]="Arg"
   
    elif final_listv1[i] in gly:
        final_listv1[i]="Gly"

if len(final_listv1)==0:
    print("There is no primary structure.")
    sys.exit()

reversed_final_list=list(reversed(final_listv1))

first_index=reversed_final_list.index('Met')

too_much_variables=reversed_final_list[:first_index + 1]

actual_final_list=list(reversed(too_much_variables))

stop_index=actual_final_list.index('Stop')

primary_structure=actual_final_list[:stop_index]

#debugging prints
print("-".join(primary_structure))