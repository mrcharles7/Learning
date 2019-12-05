# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 19:24:47 2019

@author: Charles
"""

#dna="CTCGCGTTGCAGGCCGGCGTGTCGCGCAACGACGTGTGGGGCCTGACGGGCAGGGAGGATCTCGGCGGCGCCAACTATGCGGTCTTTCGGCTCGAAAGCCAGTTCCAGACCTCCGACGGCGCGCTGACCGTGCCCGGCTCCGCATTCAGTTCGCAAGCCTACGTCGGGCTCGGCGGCGACTGGGGGACCGTGACGCTCGGGCGCCAGTTCGATTTCGTCGGCGATCTGATGCCGGCTTTCGCGATCGGCGCGAACACGCCGGCCGGCCTGCTCGCGTGGGGCTTGCCGGCGAATGCGTCGGCGGGCGGTGCGCTCGACAACCGCGTGTGGGGCGTCCAGGTGAACAATGCGGTGAAGTACGTGAGCCCGACGTTCGGCGGATTGTCGTTCGGCGGCCTGTGGGGCTTCGGCAACGTGCCCGGCACGGTCGCGCGCAGCAGCGTGCAAAGCGCGATGCTGTCCTACACGCAAGGCGCGTTCAGCGCCGCGCTCGCTTATTTCGGCCAGCACGATGTAACTGCCGGTGGCAATCTGCGCAATTTCTCGGGCGGTGCAGGCTACAACGTCGGGCAGTTCCGCGTCTTCGGCATGGTGTCGGACGTGCGGATCAGCGCCGCCGCGCCGCTGCGGGCCACGACCTATGACGGCGGCTTGACCTATGCGGTCACGCCGGCGTTGCAGCTCGGCGGCGGCTTCCAGTACCAGCAGCGCGGCGGCGACATCGGCTCGGCCAACCAGGTCACGTTGAGCGCCGACTATTCGCTGTCGAAGCGTACCGGCCTTTACGTGGTATTCGCACGCGGGCACGACAGTGCGTATGGCGCGCAGGTCGAGGCGGCGCTCGGCGGGGCGGCGTCCGGCTCGACGCAGACCGCGGTCCGGCTCGGGCTGCGGCATCAGTTCTGACGATGCGCGAGAAACACGGGCTGCCGCGTACGCCGCGCGCGAGCCCGTGTTTTTCCGCCGGATTCAGAACCGATGCATCATCCCGACGCGCAACGCCAGCTGGTTGCGGCCCGACGACTGCCCGGCCGTGCCGAGCACGTGCGCGTAGTCGAAATCGGTGCCGGTATGGCCGGTTGCATGCTGGTACGCGCCCTGGATGTACGTCGAGGTTCGCTTGCTCAGATCGTAGTCGAGCATCATCGACACCTGGTGCCAGTTCGGCGACGCATCGCCCGCCGCCGTCGCGACATGCGCATGCGTGTAGATATAGGCGGCGCCGAGCCAGAGGTCCGGCCGGAAGAAATACTGGCCGTTGACCTCGAAGTTGTCGAATTTCCACGCGTTCTGCGAGCCTGCCGCCGGCTGGTTCGCGAAGTACAGATTCGACTCGGGGTTGGTCACGTCGACGTGCGAATACGCGGCGGACAGCGTCAGCTTGTCGCTGAACTTGTACGATGCGCCCGCATCGATGTTCTGCTGCGCGCGGCCGCTGAAGACCGTATCGTCGCTCGACAACGCACCGCCCGCGGTCGCGCCGCCGTTGTTGGCCTTCAGGTACGCGACGGCGGCGGAGAACGCGCCCGCCTGGTACTGCACGGCGGCGCTATAGACGCGGTTCCGCGCGAAGCCCCCCGCCTGGTTCGCGAGCCCGTAGAGCACTTCGCCCTTGAAGCCGGCGTAGGAGGGCGACACGTACTTGACGCTGTTCTGGATGCGGTAGTCCCAATCGGCGTTGTCGTTGTCGTACGGGTGCGCGCCGAAGTCGCCGAGCCAGTTGCCGGTGGCGGTGAAGGTACTCCACATGTCGAGCGTGGGGTCGTACTGGCGGCCGAACGTGAGCGTGCCGAACCGGTCGGAATCGAGGCCGACGTAGGCTTGCCTGCCGAACATCCGCGACGTCACGCCGAGCGCGCCGGTGCTCGCGTTGAAGCCGTTCTCGAGCTGGAACAGCGCTCTGATCCCGCCGCCGAGATCCTCGGTGCCTTTCAGCCCCCAGTTGCTGCCGACGGTATCGCCGCTGACCATCTGGTAAGCCTTGCTGCCGCCCGCGTTGCTCGTGAAATTGACGCCTTCGTCGATCAGGCCGTACAGCGTCACGGTGCTTTGCGCATGGGCCGTCAGGCCGAATCCCATGGCGCTCGCGGCCGATACGGCCGCCATCATCTTCTTCATCGTCGATCTCCAGGTGTGGGCAGCCCACGCGGCGCGGTGCGGTTTCCGACGGCATACGTCAGCACCGGACGCGTGCAGCGAGTCCGTTTGTCGTTAGTAAAACGAAATATGAATTACGAAGAAAAGAGGCCCGCCGCGATCGGGCGGACCGGATGACGAACCGCGCCGGGCGCGCGGTTCCGCGTGGCGGCGGCGTTACAGCATCCGTCGCAGCACGTCGTTTTCCGGGTTGCGGTCGAAGAACCGGTGTTTCAGCGCGCCAAGCACATGCAGCACGATGAGCGCGAGCAACGTATAGGCGAGCGTTTTGTGCAGCCACTGAAACGCCTCGAACCAATGGTCGTTCTTCGGCAGCAGCTCGGGTACGCGGAAAAAGAAGAACGGCACGCCGTCGCTCTGCGTATACGTGCTGGACATCGAATAGCCCATCAGCGGCACGATGATCGCGAGCGCATACAGCAGGTAATGGCCGATCTTCGCGAGCGTGCGATCGAGCGTCGGCAGCGTGGAGGGCAGCGGCGGCAACGGCTTCATCGCGCGAATCGCCAGTTGCGTGACGACCACCAGCAGCGTGAGCACGCCGAACTCCTTGTGCGTCGGGTAGTACCAGTCGAACTTGGCCGGCAGGTTGTCGTCGAGCCGGACCATCGTCCAGCCGGTCCACAGCTGCGCGCCGATCAGGATCGCCCTGACCCAGTGCAGCAACCGAAGCGCGAGCGGGTATTTCTCCGCGGGGAATGCAATGGCCTGGTTGTCCATTTGACTTGTCTTCCTTTGAAACGACATTGCGACAGGCGGGATGCCGATCGTCGACTTCGGCGTCCCGCGGCGATCTACGTCGAACCGAGGCCGGATCGCGATACGCACGGACCTTCGACGAAAAGCCCGTGCGTCGGGCTGTTTCGCGCGGTCAGGCGATCGCGCGCGAATCCGCGCAGCACTCCTGCAACGCCTCGCGCAGTGTCACGGCCATGAAGTCGGCTTCGCCAGGCTGCAGCGTGAGCGGCGGCGAGATCACCACCTTGTTCGCGATCGCCCGCACCAGCACGCCGCGCCGACGCGCGGCATCGGCCACGCGGGCGGCGAACCCCTGGCCCGGATCGAGCGGCGTGCGGCTGGCCTTGTCGGTCACCAGATCGAGCGCCAGCATCAGCCCCTTGCCGCGGACGTCGCCGACCGTCTCGAAGTCGGCCTTCAGCGGCAGCAATTGCTCGAGCAGGCGCTGTCCGACCCGCGCCGCGTTGCCCGGCAGATCCTCGGCCTCGACGATGTCGAGCACCGCGAGCGACGCGGCGCACGCGAGCGGATGGCCGCTGTACGTATAGCCGTGCATGACCACGTGCGAGAAGCCCGCGCCATGTTCGATCGCGTCGGCGATCCGCCCGTTGTACAGCGTCGCGCCGAGCGGCACGTAGCCGGCGGAGATGCCCTTGGCGACGCACAGGATGTCGGCGGCGACGCCCCAGCCGCGGCTGCCGAGCAGGCTGCCGGTGCGGCCGAAGCCGGTGACCACCTCGTCGGCGATCAGCAGGATGCCGTTGCGGTCGCACACGGCCCGCACGCGCGCCCAGTAATCGGCCGGCGGGACGATCAGGCCGCCGGCGCCCTGCACCGGTTCGGCGACGAATGCGGCAATGGTCTGCGGGCCGTGGAACGCGATCGTTTCCTCGAGCTGCCGGATGCAGTGCTCGACGAGCTGGTGCGGATCGTCGCAATTCCACGGATTGCGATAGAGCCACGGCGTGTCGAGCAGCACGCAGCCGGGCAGCAGCGGGCCATGATTGTAATGGTAGACGCCGTTGCCGCCGATCGACGTGCCGCCCATGTGCACGCCGTGATAGCCGTTGCGCAGCGACAGGAATTTCGTGCGCGACGGCTCGCCCGCGGCGACCCAGTACTGGCGCGCCATCTTGAGCGCGGTCTCGATCGCGTCGGAGCCGCCGCTGCCGAACATCACCCGCTGCATGTCTTCCTGCGCGAACATCGCGCACAGGCGGTCGGCCAGATCGTAGACGCGCGGATGGGCGACGCCGTCGAAGGTCTGGTAGTACGACAGCTCGTCCATCTGCCGCGCGATCGCGCTTTTCACTTCCGGCCGGTTGTGGCCGACGTTGACGTTCCACAGTCCGCCGACGCCGTCGAGCATGCGGTGGCCGTCGACGTCGTACACGTAGTTGCCGTCGCCGCGCTCGATGATCACGGTGGGAGTCGTATGCCCGGCGGCCGCCGAGCTCATCGGGTGCCAGAATCGTTTTTGACGCTTTTGATAGTCCATGGTGTCTCTCGTCTCTCTTACGAAGTGCTTGAACAGGGGGCGGCGCGGTGTGCGCCGCCGGATCACAGGGCTGCGGTGATGATCTTTTCCTCGAGGTACGAATCGAGGGCGGCCTTCGACAGGTCGCGCCCGATCCCGCTTTGCTTGGTGCCGCCCCACGGCAGGCGTGCGTCGATCGGGCTCCACGCATTGATCGCGACCGCGCCGATGTCGAGCCGCTCGGCGACGCGGTGCGCGGTGCC"
start_codon = "ATG"
stop_codon = ["TGA","TAG","TAA"]
orffile = open("orfdetails.txt", "w")
#user_orf_len=100

def orfs(dna, user_orf_len): #defining the function, takes the sequnce as argument

################Block -1: Generate a list with all possible start and stop positions#################
    start_positions=[]  #list for start codon positions
    stop_positions=[] #list for stop codon positions
    for x in range(0,len(dna),3): #Declarin the triplets
        codon=dna[x:x+3] #Parsing triplet
        if codon == start_codon: #if the trplet matches with start codon
            add_spos=[x]
            start_positions=start_positions + add_spos #add to the start codon list
            add_spos=[]
        elif codon in stop_codon: #if the codon matches with stop codon
            add_fpos=[x+3]
            stop_positions=stop_positions + add_fpos #add to the stop positions list
            add_fpos=[]



################Block -2: Predict the ORFs using the list created with start/stop positions################
#Includes all ORF conditions

#####Predicts properly:verified
    ORFs=[]    #Declare a list to store ORFs
    for j in range(len(stop_positions)): #for every stop position
        for i in range(len(start_positions)): #for every start position
           if stop_positions[j]>start_positions[i] and stop_positions[j]-start_positions[i]>user_orf_len: #stop codon position should belarger than start position, #ORF length is more then 9(given in the isntruction)
               if stop_positions[0] > start_positions[-1]: #check for the first stop codon is larget than all elements of srart codon. Print all, 
                   ORF = [(dna[(start_positions[i]):(stop_positions[j])])] #add to ORF list
                   ORFs = ORFs + ORF
                   print('starting position-', start_positions[i],'  End position-',stop_positions[j],'  Length-',stop_positions[j]-start_positions[i])
                   orffile.write('\nstarting position-'+ str(start_positions[i])+'  End position-'+str(stop_positions[j])+'  Length-'+str(stop_positions[j]-start_positions[i]))
                   
               elif start_positions[i]>stop_positions[j-1]: # Or else some start posiions wil appear inbetween some stop codons, checking for the possibility
                   ORF = [(dna[(start_positions[i]):(stop_positions[j])])]
                   ORFs = ORFs + ORF #if satisfies add to the ORF list
                   print('starting position-', start_positions[i],'  End position-',stop_positions[j],'  Length-',stop_positions[j]-start_positions[i])
                   orffile.write('\nstarting position-'+ str(start_positions[i])+'  End position-'+str(stop_positions[j])+'  Length-'+str(stop_positions[j]-start_positions[i]))
    #print(ORFs) #ORFs will contail all the possible ORFs of the instructed length
    #the lenght may be changed to desired user input    


####Printing the details of the predicted ORFs    
    if (len(ORFs) >= 1): 
        print("Number of ORFs",len(ORFs))  #aprint number of ORFs
        orffile.write("\n"+"Number of ORFs" + str (len(ORFs)))
        orf_length_list=[] #create a list to store lengths of the sequnces
        for seq in ORFs: #for every predicted ORF
            orf_len=[(len(seq))] #calculate length
            orf_length_list= orf_length_list + orf_len  #Add the number to the list
        #print orf_length_list
        orf_length_list = sorted(orf_length_list) #Sort the list by numbers
        #print orf_length_list
        long_ORF=orf_length_list[-1] #last element of the list: largest
        short_ORF=orf_length_list[0] #first element of the list: smallest
        print ("longest ORF length is",long_ORF) #print longest
        orffile.write ("\n"+"longest ORF length is" + str(long_ORF))
        print ("Shortest ORF length is",short_ORF) #print smallest
        orffile.write("\n"+" Shortest ORF length is"+str(short_ORF))
        #print(ORFs)
    else:
        print ("No ORF found")
        orffile.write("\n"+"No ORF found\n"+"\n"+"\n")
#function ends 

orfs (dna, user_orf_len) #call function

##########Older version Doesn't calculate clearly
#this older version doesn't bougther about the inbetween stop codons
#generates all possible combinations with start and stop codons positions
"""
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

    #print(start_positions)
    #print(stop_positions)
    
    ORFs=[]  
    for i in start_positions:
        for j in stop_positions:
            if i < j and j-i>=9:
                #print(i,j)
                #print(dna[i:j])
                ORF = [(dna[i:j])]
                print('starting position-', i,'  End position-',j,'  Length-',j-i)
                ORFs = ORFs + ORF
    #print(ORFs)     

    
    if (len(ORFs) > 1):
        print("Number of ORFs",len(ORFs)) 
        sorted(ORFs)
        #print (ORFs)
        long_ORF=len(ORFs[-1])
        short_ORF=len(ORFs[0])
        print ("longest ORF length is",long_ORF)
        print ("Shortest ORF length is",short_ORF)
    else:
        start_positions=[]
        stop_positions=[]
        print ("No ORF found")
   

orfs (dna)
"""
##########################----EOF----##########################################