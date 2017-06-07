"""
Created on Wed Apr 26 11:02:39 2017

@author: Thomas
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 20:51:26 2017

@author: Thomas
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 19:29:58 2017

@author: Thomas
"""
class ranking(object):

    def __init(self, pageNumber, pageRanking):
        self.pageNumber = pageNumber
        self.pageRanking = pageRanking
    @classmethod
    def construct(self):
        self.pageNumber = -1.000
        self.pageRanking = -1.000
    def getPageNumber(self):
        return self.pageNumber
    def getPageRank(self):
        return self.pageRanking
    def printPage(self):
        print "Page Rank Value: %f \nPage Number: %d \n" % (self.pageRanking, self.pageNumber)
    def setParameters(self, pageNumber, pageRanking):
        self.pageNumber = float(pageNumber)
        self.pageRanking = float(pageRanking)
    def copy(self):
        return self
    

#pre process the adjacency matrix
import numpy as np
print "Welcome to the page rank algorithm\n"
print "In this we will create a random adjacency matrix and \nfigure out the page rank!\n"
print "Please select a d parameter value between 0 and 1"
flagBoundedParameter = False

while(flagBoundedParameter == False):
    d = input("What value of d? d = ")
    if(d > 0 and d < 1):
        flagBoundedParameter = True
    else:
        print "Please pick a value between d > 0 or d < 1\n"

#d = 0.85
flagIntegerAdjSize = False

while(flagIntegerAdjSize == False):
    value = input("How many objects?")
    try:
        number = int(value)
        if(number > 0):
            flagIntegerAdjSize = True    
        else:
            print("You must put a positive integer value greater than 0")
        
    except ValueError:
        print("You must put a positive value integer")

# Your matrix, or a generated matrix?
randomFlag = False
print "Would you like to define the matrix connections?\n Or a random generated matrix?"
#value = 0
choice = 0
#Check if one is detected.
oneDetected = False
while(choice != 1 and choice != 2):
    print "Choice 1: Type 1 for you to define the matrix connections?"
    print "Choice 2: Type 2 for you to have an auto generated matrix"
    choice = raw_input("Type 1 or 2: ")
    choice = int(choice)
    if(choice !=1 or choice !=2):
        print "1 and 2 are the only acceptable inputs"
# Get values. 
if(choice == 1):
    myMatrix = np.zeros(shape=(value,value))
    for row in range(0,value):
        for column in range(0,value):
            theRefFlag = True
            while(theRefFlag):
                print "Is object %d referencing object %d" % (row, column)
                connChoice = raw_input("y for connected, n for disconnected: ")
                if(connChoice == "y" or connChoice == "Y"):
                    print "Connecting..."
                    myMatrix[row,column] = 1
                    theRefFlag = False
                elif(connChoice =="n" or connChoice == "N"):
                    print "No connection established..."
                    myMatrix[row,column] = 0
                    theRefFlag = False
                else:
                    print "Incorrect choice try again, only y or n"
                    theRefFlag = True
    outbound_links = myMatrix.sum(axis = 0) *1.0
else:
    print "Auto generating values..."
    # Auto generate the values.
    while(oneDetected == False):
        oneDetected = True
        myMatrix = np.random.randint(2, size = (value, value))*1.0
        print myMatrix
        outbound_links = myMatrix.sum(axis = 0) *1.0
        for index in range(0,value):
            #print index
            #print "outbound_links[index]"
            #print outbound_links[index]
            if(outbound_links[index] == 0):                   
                oneDetected = False
#Matrix created.                 
#print outbound_links

# set the page rank equal to the number of outbound links.
# page rank = outbound links, p_j = c_j where c_j = outbound links
sum_p_j = outbound_links
print sum_p_j
print "\n"
print "\n myMatrix / p_j \n"
#Compute the term L_ij/p_j. This is my Matrix
myMatrix = myMatrix / sum_p_j[None,:]
print myMatrix
#Make flag for loop
flag = True
#Start it
runNumber = 1
while flag:
    print "Beginning run #", runNumber
    print "sum_p_j"
    print sum_p_j
    #p_j was needed for the product.
    #pj = myMatrix.sum(axis = 0)*1.0
    sum_product =   np.matmul(sum_p_j,np.transpose(myMatrix))
    # By doing this I've computed the sum product
    # Sum Product = sum(i = 1 to N of (L_ij/c_j)*p_j) Where...
    # L_ij is an element in the adjacency matrix at ith row jth column
    # c_j is the total number of outbound links
    # p_j = the current page rank 
    print "Sum product"
    print sum_product
    p_Not = 1 - d
    # 
    computed_page_rank = d*sum_product + p_Not
    print "d*sum_product"
    print "The total page rank"
    print computed_page_rank
    print "STATS"
    print "runNumber:", runNumber
    print "sum_p_j"
    print sum_p_j
    print "computed page rank"
    print computed_page_rank
    if((runNumber > 1) and (np.array_equal(sum_p_j, computed_page_rank))):
        print "Ending page rank."
        flag = False
    else:
        sum_p_j = computed_page_rank
    runNumber += 1

index = 0

rankList = []
for x in computed_page_rank:
    myRanking = ranking()
    y = 0.0
    print "X is %d" % x
    y = x*1.0
    myRanking.setParameters(index,y)
    rankList.append(myRanking)
    index+=1
    print myRanking.printPage()

print "\n\t\tFinal results\n"

sortedlist = sorted(rankList, key=lambda ranking : ranking.pageRanking, reverse=True)
index = 0;

for z in sortedlist:
    print "Rank Number is %d" %(index +1)
    print z.printPage()
    index +=1
    
    
