# Sneh Shah
# Meta Gene Plot Generator
# COM 491 Independent Study

import pandas as pd

import csv
from Gene import *

headerNames = ['Chromosome','Source','Type','Start','End','Score','Strand','Frame','GeneLabel','GeneID','TranscriptLabel','TranscriptID']
annotation = pd.read_csv('SacCer3.gtf',sep ='\s+',names=headerNames)


samHeaderNames = ['QNAME','FLAG','RNAME','POS','MAPQ','CIGAR','RNEXT','PNEXT','TLEN','SEQ','SEQ2','QUAL']
sample = pd.read_csv('Lab4S3.sam',sep = '\t',names = samHeaderNames)

#RNAME = Chromosome
#POS = Start

print('I read the data files')

def generatePlots(dataset,iteration):

    if len(dataset) >= 10 and iteration <= 5:

        thresholdList = []
        for i in range(len(dataset)):
            thresholdList.append(dataset[i].getAverageExpression())

        threshold = statistics.mean(thresholdList)
        usedList = []
        notUsedList = []
        for i in range(len(dataset)):
            if dataset[i].getAverageExpression() >= threshold:
                usedList.append(dataset[i])
                dataset[i].setUsed()                    
            else:
                notUsedList.append(dataset[i])
                
        metaGenesList = []
        for i in range(len(usedList)):
            metaGenesList.append([usedList[i].getName(),usedList[i].getAverageExpression()])
            
        with open('completeCHRIMetaGenePlot'+str(iteration)+'.csv', mode='w') as metaGenePlot_file:
            metaGenePlot_writer = csv.writer(metaGenePlot_file)

            metaGenePlot_writer.writerow(['GeneID','Average Expression Level'])
            
            for gene in metaGenesList:
                metaGenePlot_writer.writerow(gene)
                
        iteration += 1
        generatePlots(notUsedList,iteration)
        
    else:

        with open('completeCHRINotUsedGenes.csv', mode='w') as notUsedGenes_file:
            notUsedGenes_writer = csv.writer(notUsedGenes_file)

            notUsedGenes_writer.writerow(['GeneID','Average Expression Level'])

            for i in range(len(dataset)):
                notUsedGenes_writer.writerow([dataset[i].getName(),dataset[i].getAverageExpression()])
                    
    



geneList = []
chrNum = 'chrI'


for i in range(len(annotation)):
    if annotation.loc[i,'Type'] == 'CDS' and annotation.loc[i,'Chromosome'] == chrNum :
        geneList.append(Gene(annotation.loc[i,'GeneID'],annotation.loc[i,'Chromosome'],annotation.loc[i,'Type'],annotation.loc[i,'Start'],annotation.loc[i,'End'],annotation.loc[i,'Strand']))
     
        
print('Number of CDS Genes on Chromosome '+chrNum+': ',len(geneList))

readLength = 51

for i in range(len(geneList)):
    for j in range(len(sample)):
        if geneList[i].getChromosome() == sample.loc[j,'RNAME']:
        
            start = sample.loc[j,'POS']
            end = start + readLength

            if start >= geneList[i].getStart() and start <= geneList[i].getEnd() and \
               end  >= geneList[i].getStart() and end <= geneList[i].getEnd():

                if geneList[i].getStrand() == '+':
                    for k in range(start,end,1):
                        geneList[i].incrementArray(k-geneList[i].getStart())
                elif geneList[i].getStrand() == '-':
                    for k in range(end,start,-1):
                        geneList[i].incrementArray(k-geneList[i].getStart())
    print('Finished counts for Gene',str(i))

for i in range(len(geneList)):
    geneList[i].createFixedArray()
    print('Creating fixed array for gene',str(i))

generatePlots(geneList,0)



        


 


            
        
    

