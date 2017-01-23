#author: Anurag Kulshrestha
#Assignment-1
#Programming Skills
#IIRS-ITC - MSc GFM
#Date: 4-01-2017
#This program takes any RNA sequence, cuts it into parts that start with a START codon and end with a STOP codon, and translates the codons into amino acids.

import random

rna_string = 'CUUCGGAUGAAGCUGUGGGCAAGUUGGGAUGAAUCGUGAUGGGUC'

#number of nucleotides
#num_nucleo=len(rna_string)


def num_codons(string):
    num_nucleo=len(string)
    if(num_nucleo%3==0):
        return num_nucleo/3.0
    else:
        print('The RNA sequence is incomplete. Complete the following sequence')
        incomp_seq=rna_string[(num_nucleo/3)*3:]
        #return incomp_seq
        return num_nucleo/3

def nth_codon(n, string):
    return string[(n-1)*3:n*3]

def print_codons(string):
    i=1
    codons=num_codons(string)
    while(i<=codons):
        print(nth_codon(i, string)+'\n')
        i=i+1
        
def str_to_list(string):
    i, codon_list=1, []
    codons=num_codons(string)
    while(i<=codons):
        codon_list.append(nth_codon(i, string))
        i=i+1
    return codon_list

def start_idx(string):
    codons=str_to_list(string)
    index=codons.index('AUG')
    return index*3

def stop_idx(string):
    codons=str_to_list(string)
    end_codons=['UAG','UGA','UAA']
    for i in codons:
        if i in end_codons:
            index=codons.index(i)
            break
    return index*3

def is_start_first(string):
    codons=str_to_list(string)
    if (start_idx(string)<stop_idx(string)):
        return True
    else:
        return False

def stop_after_start(string):
    codons=str_to_list(string)
    #codons,l=str_to_list(),[]
    if(is_start_first(string)):
        stop=stop_idx(string)
        start=0
    else:
        start=start_idx(string)
        #l=codons[start/3:]
        stop=stop_idx(''.join(codons[start/3:]))+len(codons[:start/3])*3 #dividing the list into 3 on either side of start_idx. 
    return stop

def rna_seq(string):
    #codons=str_to_list()
    start=start_idx(string)
    stop=stop_after_start(string)
    return string[start:stop+3]

def codon_count(codon):
    return str_to_list().count(codon)

def rand_rna_string(n):
    RNA=['A','G', 'C', 'U']
    result=''
    while(n>0):
        result=result+random.choice(RNA)
        n=n-1
    return result


#print(start_idx(str_to_list()))
#print(stop_idx(str_to_list()))
#print stop_after_start()
#print (is_start_first())
#print(rna_seq())
#print(codon_count('UGG'))
#print(rand_rna_string(100))

if __name__=='__main__':
    rna_string_1 = rand_rna_string(1002)
    #print(num_codons(rna_string_1))
    #print(nth_codon(15, rna_string_1))
    #print_codons(rna_string_1)
    #print(str_to_list(rna_string_1))
    print(start_idx(rna_string_1))
    print(stop_after_start(rna_string_1))
    print(rna_seq(rna_string_1))