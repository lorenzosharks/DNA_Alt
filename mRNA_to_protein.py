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

ending_codon=["UGA", "UAG", "UAA"]

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

print(ending_index)
print(mRNA_list[ending_index])