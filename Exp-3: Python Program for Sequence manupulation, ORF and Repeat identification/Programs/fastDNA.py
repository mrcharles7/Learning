# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 16:16:18 2019

@author: Charles
"""
print ("Pogramme started") #Just an intimation

##################Getting user defined values

###Get the ORF length
print("Enter the desired ORF length:")
user_orf_len=raw_input()
user_orf_len=int(user_orf_len) #used for ORF prediction

###Get the repeat the length
print("Enter the repeat length:")
r_len=raw_input()
r_len=int(r_len) #used for passing to repeat identification

################BLOCK-1:Creations of dictionary################################
#Create a dictionary headers as keys and values as sequence
diction = {}
fast = open("dna2.fasta","r")
for line in fast.readlines():
    line = line.strip('\n')
    if ">" == line[0]:
        header = line
        diction[header] = "" #declaring and empty value with header as key
    else:
        diction[header] += line
#    return diction
fast.close() 
#Dictionary created sucessfully
#File will be closed and further operations are only in the dictionary
#In this way the program is not memeory efficient !!! 

################BLOCK-2:Number or records######################################
#printing number of sequnces
Generalinfo = open("Generalinfo.txt","w")
print ('\n Number of sequences are :', len(diction))
Generalinfo.write ('\n Number of sequences are :'+ str(len(diction)) )
Generalinfo.close()


################BLOCK-3:Check the sequnce lengths##############################
#To check the longest and shortest sequence in the multifastafile
lengthfile = open("seqlength.txt", "w") #File for result details to be written
length = {} # Decleration: empty Dictionary to store the length of the sequences
for akey in diction: #run througn the created dictionary
    length[akey]=len(diction[akey]) #measeure length of all elements
len_asending = sorted(list(length.values())) #Sort length dictionary
print ("Maximum length of the sequence is :",len_asending[-1]) #print the highest
lengthfile.write("Maximum length of the sequence is :" + str(len_asending[-1])+"\n") #print the length 

#take the longest length and match with the values of the original dictionary and print the key
#(identifier of fsta seq)
big_seq = len_asending[-1]
for akey in diction:
    if (len(diction[akey])) == big_seq:
        print ("Maximum length belongs to/ the header is",akey)
        lengthfile.write("Maximum length belongs to/ the header is" + akey+"\n")
print ("Minimum length of the sequence is :",len_asending[0])
lengthfile.write("Minimum length of the sequence is :" + str(len_asending[0])+"\n")
#take the shortest length and match with the values of the original dictionary and print the key
#(identifier of fsta seq)
small_seq = len_asending[0]
for akey in diction:
    if (len(diction[akey])) == small_seq:
        print ("Small length belongs to/ the header is",akey)
        lengthfile.write("Small length belongs to/ the header is" + akey+"\n")
lengthfile.close()

################BLOCK-4:ORF prediction form the sequences######################
orffile = open("orfdetails.txt", "w") #open file for writing the results
for akey in diction: # loop through the dictionary 
    #f=0
    print ("For the sequence with identifier ", akey)
    orffile.write ("\n For the sequence with identifier "+ str(akey)+ "\n")
    dna=(diction[akey]) #store the sequence to variable 'dna'
    #print("forward strand is ")
    #print(dna)
    for f in range(3): #Generating 3 forward reading frames
        fr = f+1
        print("ORF details are as follows for forward frame", fr)
        orffile.write("\n ORF details are as follows for forward frame"+ str(fr)+ "\n")
        #dna=(diction[akey])
        dna=dna[f:] #Call orfs function to predict the orf for any given sequence
        #orfs(dna)
        orffile.write(str(orfs(dna,user_orf_len))) #Call orfs function to predict the orf for any given sequenc
        f=f+1
    print ("Reverse of the sequence and calculating ORF")
    orffile.write ("\n Reverse of the sequence and calculating ORF"+"\n")
    #rf=0
    rev_dna=(diction[akey]) #
    rev_dna=rev_dna[::-1]#Generate the reverse of the sequence
    for rf in range(3):#Generating 3  reading frames
        rfr = rf+1
        print("ORF details are as follows for Reverse frame",rfr)
        orffile.write("\n ORF details are as follows for Reverse frame"+str(rfr)+"\n")
        #dna=(diction[akey])
        rev_dna=rev_dna[rf:]
        #orfs(rev_dna)
        orffile.write(str(orfs(rev_dna,user_orf_len))) #Call orfs function to predict the orf for any given sequence
        rf=rf+1
orffile.close() #close file

################BLOCK-5:Repeat identifications form the sequences##############
repeatfile = open("repeatdetails.txt", "w") #Opeining a new file for repeats
for akey in diction: #Loopint through the directory
    reading_frame=0 #The question asked for only one forward frame
    #This will create all possible repeats of the desired length
    print ("For the sequence with identifier ", akey)
    repeatfile.write("\n\nFor the sequence with identifier " + str(akey))
    nuc=(diction[akey]) #assing nuc as it holds the sequence
    reading_frame=0
    if reading_frame == 0:
        actual_reading_frame = reading_frame+1
        print("Sequence repeat details for forward frame", actual_reading_frame)
        repeatfile.write("\n\nSequence repeat details for forward frame"+ str(actual_reading_frame))
        #dna=(diction[akey])
        nuc=nuc[reading_frame:]
        repeat(nuc,r_len) #Calling the repeat identifier function
        #repeatfile.write(str(repeat(nuc,r_len)))
repeatfile.close()

##########################----EOF----##########################################