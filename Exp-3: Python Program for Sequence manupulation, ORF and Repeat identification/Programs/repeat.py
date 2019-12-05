# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 09:06:39 2019

@author: Charles
"""
#part of fastDNA.py program
#This program is a function to identify reppeats in the given DNA sequence

##########################----STARTS HERE----##################################
#nuc="CAGGGCGAAGTGAGAAUGGAUGGCAUGAGCAAUGATCx" #these variables declared for testing
#r_len=3 #repet length, these variables declared for testing
repeatfile = open("repeatdetails.txt", "w") #OPening the file which already created by  main 

def repeat(nuc, r_len):#declaring the functions
    repeats=[] #Empty list to store the repeats
    #print (len(dna))
    for i in range(0, len(nuc)): #search throuh the elements for the stretch of the sequence
        new_repeat = [(nuc[i:i+r_len])] # generate all possible repeats)
        repeats = repeats + new_repeat #The list with all repeats
        #i=i+1
    print repeats #printing the list, Can be disabled
    #print (len(repeats))
    
#this block counts the number of repeats     
    repeat_dictionary={}
    for j in repeats: #for every element is list
        count = 0
        for elem in range(len(repeats)): # for every element in list
            if repeats[elem]==j and len(j)==r_len: #if the elememts matches
                #print("match")
                count = count+1 #add 1 to the count 
                repeat_dictionary[j]=count # and store as value 
    #print repeat_dictionary
    #So the dictionary contains keys as particular block of the sequence and values as number of time appeared    

########This block sort the diationary based on the number of occurance and print the last element of the dictionary    
    milti_r_dict={}
    for akey in repeat_dictionary: #for every key in the dictionary
        if repeat_dictionary[akey]!=1: #if the number of repeats is more than one 
            milti_r_dict[akey]=(repeat_dictionary[akey]) #add to the new directory, New directory will contains only repeats occur more than once
    if len(milti_r_dict)==0: #If the new dictionary is empty, report!
        print ("\nNo repeats found")
        repeatfile.write("\nNo repeats found")
    else: #or if the new dicationary contains elements    
        #sorted (milti_r_dict)
        #sorted(milti_r_dict.iteritems(), key = lambda x : x[1])
        milti_r_dict = sorted(milti_r_dict.iteritems(), lambda x, y : cmp(x[1], y[1])) #sort the dictionary based on the elements
        #print milti_r_dict
        repeatfile.write(str(milti_r_dict)) #write the sorted new directory in to the file
        repeatfile.write("\n\n")

repeat(nuc, r_len)    
    
#########Older version
"""
def repeat(dna, r_len):
    repeats=[]
    #print (len(dna))
    for i in range(0, len(nuc)):
        new_repeat = [(nuc[i:i+r_len])] # generate possible repeats)
        repeats = repeats + new_repeat
    #print repeats
    #print (len(repeats))
    
    
    repeat_dictionary={}
    for j in repeats:
        count = 0
        for elem in range(len(repeats)):
            if repeats[elem]==j and len(j)==r_len:
                #print("match")
                count = count+1
                repeat_dictionary[j]=count
    #print repeat_dictionary
    
    milti_r_dict={}
    for akey in repeat_dictionary:
        if repeat_dictionary[akey]!=1:
            milti_r_dict[akey]=(repeat_dictionary[akey])
    if len(milti_r_dict)==0:
        print ("No repeats found")
    else:
        print milti_r_dict
    
repeat(nuc, r_len)    
"""
##########################----EOF----##########################################
