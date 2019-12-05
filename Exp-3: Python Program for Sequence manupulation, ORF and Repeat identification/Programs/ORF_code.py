# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 19:24:47 2019

@author: Charles
"""

dna="CAGGGCGAAGTGAGAAUGGAUGGCAUGAGCAAUGATCGTCCACGCGCAGCGCGGCACCGCGGGCCTCTGCCGTGCGCTGCTTGGCCAUGATGGCCTCCAGCGCACCGATCGGATCAAAGCCGCTGAAGCCTTCGCGCATCAGGCGGCCATAGTTGGCGCCAGTGACCGTACCAACCGCCTTGATGCGGCGCTCGGTCATCGCTGCATTGATCGAGTAGCCACCGCCGCCGCAAATGCCCAGCACGCCAATGCGTTCTTCATCCACATAGGGGAGCGTTACGAGGTAGTCGCAGACCACGCGGAAATCCTCGACGCGCAGTGTCGGGTCTTCGGTAAAACGTGGTTCGCCGCCGCTGGCACCCTGGAAGCTGGCGTCGAAGGCGATGACGACGAAACCTTCCTTGGCCAGCGCCTCGCCATACACGTTCCCCGATGTTTGCTCCTTGCAGCTGCCGATCGGATGCGCGCTGATGATGGCGGGATATTTCTTGCCTTCGTCGAAGTTCGGCGGGAAGTGGATGTCGGCTGCGATATCCCAATACACATTCTTGATCTTGACGCTTTTCATGACAGCTCC"
start_codon = "AUG"
stop_codon = ["TGA","TAG","TAA"]

def orfs(dna):
    
    start_positions=[]
    stop_positions=[]
    for x in range(0,len(dna),3):
        
        codon=dna[x:x+3] 
        if codon == start_codon:
            add_spos=[x]
            start_positions=start_positions + add_spos
            add_spos=[]
        elif codon in stop_codon:
            add_fpos=[x+3]
            stop_positions=stop_positions + add_fpos
            add_fpos=[]
    
    ORFs=[]  
    for i in range(len(start_positions)):
        for j in range(len(stop_positions)):
            if i < j or i-j==9:
                #print(dna[(start_positions[i]):(stop_positions[j])])
                ORF = [(dna[(start_positions[i]):(stop_positions[j])])]
                ORFs = ORFs + ORF
    
    if (len(ORFs) > 1):
        print(len(ORFs)) 
        sorted(ORFs)
        long_ORF=len(ORFs[-1])
        short_ORF=len(ORFs[0])
        print ("longest ORF length is",long_ORF)
        print ("Shortest ORF length is",short_ORF)
    else:
        start_positions=[]
        stop_positions=[]
        print ("No ORF found")
    return ORFs


orfs (dna)