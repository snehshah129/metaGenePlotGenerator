# Sneh Shah
# COM 491 Independent Study
# Single Gene Plot for Display Purposes & Computational Efficiency

import csv
import pandas as pd
from Gene import *

headerNames = ['Chromosome','Source','Type','Start','End','Score','Strand','Frame','GeneLabel','GeneID','TranscriptLabel','TranscriptID']
annotation = pd.read_csv('SacCer3.gtf',sep ='\s+',names=headerNames)


samHeaderNames = ['QNAME','FLAG','RNAME','POS','MAPQ','CIGAR','RNEXT','PNEXT','TLEN','SEQ','SEQ2','QUAL']
sample = pd.read_csv('Lab4S3.sam',sep = '\t',names = samHeaderNames)

#RNAME = Chromosome
#POS = Start



def generatePlot(gene):

    geneArray = gene.getFixedArray()

    with open('singleGenePlot.csv', mode='w') as singleGenePlot_file:
        singleGenePlot_writer = csv.writer(singleGenePlot_file)

        singleGenePlot_writer.writerow([gene.getName()])

        
        for i in range(len(geneArray)):
            singleGenePlot_writer.writerow([i,geneArray[i]])

    

i = 0
while annotation.loc[i,'Type'] != 'CDS'and annotation.loc[i,'Chromosome'] != 'chrM' :
    i += 1

gene = Gene(annotation.loc[i,'GeneID'],annotation.loc[i,'Chromosome'],annotation.loc[i,'Type'],annotation.loc[i,'Start'],annotation.loc[i,'End'],annotation.loc[i,'Strand'])


readLength = 51

for j in range(len(sample)):
        if gene.getChromosome() == sample.loc[j,'RNAME']:
        
            start = sample.loc[j,'POS']
            end = start + readLength

            if start >= gene.getStart() and start <= gene.getEnd() and \
               end  >= gene.getStart() and end <= gene.getEnd():

                if gene.getStrand() == '+':
                    for k in range(start,end,1):
                        gene.incrementArray(k-gene.getStart())
                elif gene.getStrand() == '-':
                    for k in range(end,start,-1):
                        gene.incrementArray(k-gene.getStart())

gene.createFixedArray()


generatePlot(gene)



    
