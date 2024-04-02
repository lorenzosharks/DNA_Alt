#Function
def del_early(string, index):
    return string[index:]

def mRNA_list_creation(mid):
    return [mid[i:i+3] for i in range(0, len(mid), 3)]

def first_combination(combinations, strings_list):
    for combination in combinations:
        for i, string in enumerate(strings_list):
            index = string.find(combination)
            if index != -1:
                return string, i, index
    return None, -1, -1

mRNA=input("Insert your mRNA strand (After splicing and whatnot):")

#Finding the first start codon
mRNA_index=mRNA.find("AUG")

#Splicing the string
mRNA_mid=del_early(mRNA, mRNA_index)

#Creating a list
mRNA_list=mRNA_list_creation(mRNA_mid)

ending_codon=["UGA", "UAG", "UAA"]

ending_index=first_combination(ending_codon, mRNA_list)

print(ending_index)